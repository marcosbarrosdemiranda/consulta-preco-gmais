import os
import time
import sqlite3
import logging
import threading
import base64
import gzip
import requests
from datetime import datetime
from fastapi import FastAPI, HTTPException, BackgroundTasks, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("consulta-preco-server")

app = FastAPI(title="Consulta Preço Gmais - Servidor Local Multi-Loja + Painel Admin", version="3.6.0")

RP_HOST = os.getenv("RP_HOST", "http://servicosflex.rpinfo.com.br:9000")
RP_USER = os.getenv("RP_USER", "100049")
RP_PASS = os.getenv("RP_PASS", "gr142536")
RP_CNPJ = os.getenv("RP_CNPJ", "33168717000104,33168717000449,33168717000368,33168717000791")
SYNC_INTERVAL_MINUTES = int(os.getenv("SYNC_INTERVAL_MINUTES", "10"))
SERVER_PORT = int(os.getenv("PORT", "48291"))

DATA_DIR = "/app/data" if os.path.exists("/app") else "data"
os.makedirs(DATA_DIR, exist_ok=True)
DB_PATH = os.path.join(DATA_DIR, "produtos.db")

ALLOWED_CNPJS = ["33168717000104", "33168717000449", "33168717000368", "33168717000791"]

sync_status = {
    "is_syncing": False,
    "last_sync": None,
    "total_produtos": 0,
    "unidades_sincronizadas": [],
    "ultimo_erro": None
}

def get_rp_token():
    url = f"{RP_HOST}/v1.1/auth"
    payload = {"usuario": RP_USER, "senha": RP_PASS}
    headers = {"Content-Type": "application/json"}
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=15)
        data = resp.json()
        response_obj = data.get("response", data)
        if response_obj.get("status") == "ok" or "token" in response_obj:
            return response_obj.get("token")
    except Exception as e:
        logger.error(f"Exceção ao autenticar: {e}")
    return None

def get_sales_units():
    token = get_rp_token()
    sales_stores = []
    if token:
        try:
            resp = requests.get(f"{RP_HOST}/v1.6/unidades", headers={"token": token}, timeout=5)
            if resp.status_code == 200:
                data = resp.json()
                content = data.get("response", {}).get("content", data.get("unidades", []))
                for u in content:
                    cnpj = str(u.get("cnpj", u.get("CNPJ", "")))
                    nome = u.get("nome", u.get("Nome", u.get("nomeReduzido", f"Loja {cnpj}")))
                    if cnpj in ALLOWED_CNPJS:
                        sales_stores.append({"cnpj": cnpj, "nome": nome, "codigo": u.get("codigo", u.get("Codigo", ""))})
        except Exception:
            pass
    if not sales_stores:
        sales_stores = [
            {"cnpj": "33168717000104", "nome": "Loja 001 - Matriz", "codigo": "1"},
            {"cnpj": "33168717000449", "nome": "Loja 003 - Filial", "codigo": "3"},
            {"cnpj": "33168717000368", "nome": "Loja 010 - Filial", "codigo": "10"},
            {"cnpj": "33168717000791", "nome": "Loja 030 - Filial", "codigo": "30"}
        ]
    return sales_stores

def sync_products_from_erp():
    global sync_status
    if sync_status["is_syncing"]:
        return

    sync_status["is_syncing"] = True
    sync_status["ultimo_erro"] = None
    token = get_rp_token()
    if not token:
        sync_status["is_syncing"] = False
        sync_status["ultimo_erro"] = "Falha ao autenticar na RP Info"
        return

    headers = {"token": token, "Content-Type": "application/json"}
    sales_units = get_sales_units()
    cnpjs = [s["cnpj"] for s in sales_units if s.get("cnpj")]
    total_geral = 0
    unidades_sucesso = []

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        for cnpj in cnpjs:
            last_id = 0
            total_unidade = 0
            while True:
                url = f"{RP_HOST}/v3.2/produtounidade/listaprodutos/{last_id}/unidade/{cnpj}/detalhado/ativos"
                try:
                    resp = requests.get(url, headers=headers, timeout=15)
                except Exception:
                    break
                if resp.status_code == 401:
                    token = get_rp_token()
                    if token:
                        headers["token"] = token
                        resp = requests.get(url, headers=headers, timeout=15)
                    else:
                        break
                if resp.status_code != 200:
                    break
                data = resp.json()
                batch = data if isinstance(data, list) else data.get("produtos", data.get("content", data.get("response", {}).get("produtos", [])))
                if not batch:
                    break
                now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                for item in batch:
                    codigo = item.get("Codigo", item.get("codigo", item.get("id", item.get("ID"))))
                    if not codigo:
                        continue
                    codigo_barras = item.get("CodigoBarras", item.get("codigoBarras", item.get("codBarras", "")))
                    if not codigo_barras and "codigosBarras" in item and item["codigosBarras"]:
                        codigo_barras = item["codigosBarras"][0].get("codigoBarras", item["codigosBarras"][0].get("CodigoBarras", ""))

                    descricao = item.get("Descricao", item.get("descricao", item.get("nome", item.get("Nome", "PRODUTO"))))

                    preco = float(item.get("PrecoPDV", item.get("precoPDV", item.get("Preco", item.get("preco", item.get("precoVenda", item.get("valor", item.get("PrecoVenda", 0.0))))))))
                    if preco == 0.0:
                        preco = float(item.get("PrecoNormal", item.get("precoNormal", item.get("PrecoLista", 0.0))))

                    preco_anterior = item.get("PrVendaAnt", item.get("prVendaAnt", item.get("PrecoAnterior", item.get("precoAnterior", None))))
                    if preco_anterior is not None:
                        try:
                            preco_anterior = float(preco_anterior)
                        except:
                            preco_anterior = None

                    unidade = item.get("UnidadeMedida", item.get("unidadeMedida", item.get("unidade", item.get("Unidade", "UN"))))
                    imagem_url = f"/api/product-image/{codigo}/{cnpj}"

                    ativo_val = item.get("Ativo", item.get("ativo", True))
                    ativo = 1 if (ativo_val is True or ativo_val == 1 or str(ativo_val).lower() == 'true') else 0

                    cursor.execute("""
                        INSERT OR REPLACE INTO produtos (codigo, cnpj, codigo_barras, descricao, preco, preco_anterior, unidade, imagem_url, ativo, updated_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (codigo, cnpj, str(codigo_barras), descricao, preco, preco_anterior, unidade, imagem_url, ativo, now_str))
                    total_unidade += 1
                conn.commit()
                last_item = batch[-1]
                next_id = last_item.get("Codigo", last_item.get("codigo", last_item.get("id", last_item.get("ID"))))
                if next_id == last_id:
                    break
                last_id = next_id
                time.sleep(0.05)
            total_geral += total_unidade
            unidades_sucesso.append({"cnpj": cnpj, "produtos": total_unidade})

        sync_status["last_sync"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        sync_status["total_produtos"] = total_geral or cursor.execute("SELECT COUNT(*) FROM produtos").fetchone()[0]
        sync_status["unidades_sincronizadas"] = unidades_sucesso
    except Exception as e:
        sync_status["ultimo_erro"] = str(e)
    finally:
        conn.close()
        sync_status["is_syncing"] = False

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            codigo INTEGER,
            cnpj TEXT,
            codigo_barras TEXT,
            descricao TEXT,
            preco REAL,
            preco_anterior REAL,
            unidade TEXT,
            imagem_url TEXT,
            ativo INTEGER,
            updated_at TEXT,
            PRIMARY KEY (codigo, cnpj)
        )
    """)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_barras_cnpj ON produtos(codigo_barras, cnpj)")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS devices (
            device_id TEXT PRIMARY KEY,
            store_cnpj TEXT,
            ip_address TEXT,
            app_version TEXT,
            status TEXT,
            last_seen TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS device_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT,
            store_cnpj TEXT,
            barcode TEXT,
            action_type TEXT,
            result_status TEXT,
            message TEXT,
            created_at TEXT
        )
    """)

    # Remove unauthorized CNPJs from database
    cursor.execute("DELETE FROM produtos WHERE cnpj NOT IN ('33168717000104', '33168717000449', '33168717000368', '33168717000791')")
    conn.commit()
    conn.close()
    logger.info(f"Banco SQLite inicializado em {DB_PATH}.")

# Initialize DB and start sync thread
init_db()
threading.Thread(target=sync_products_from_erp, daemon=True).start()

def log_device_event(device_id: str, store_cnpj: str, barcode: str, action_type: str, result_status: str, message: str):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""
            INSERT INTO device_logs (device_id, store_cnpj, barcode, action_type, result_status, message, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (device_id, store_cnpj, barcode, action_type, result_status, message, now))
        conn.commit()
        conn.close()
    except Exception as e:
        logger.error(f"Erro ao registrar log: {e}")

def background_scheduler():
    global SYNC_INTERVAL_MINUTES
    while True:
        try:
            sync_products_from_erp()
        except Exception:
            pass
        time.sleep(max(SYNC_INTERVAL_MINUTES, 1) * 60)

threading.Thread(target=background_scheduler, daemon=True).start()

@app.get("/api/health")
def health_check():
    return {"status": "ok", "port": SERVER_PORT, "sync_status": sync_status}

@app.post("/api/sync/trigger")
def trigger_sync(background_tasks: BackgroundTasks):
    if sync_status["is_syncing"]:
        return {"status": "running", "message": "Sincronização em andamento."}
    background_tasks.add_task(sync_products_from_erp)
    return {"status": "started", "message": "Sincronização iniciada."}

@app.post("/api/device/heartbeat")
def device_heartbeat(data: dict):
    device_id = data.get("device_id", "unknown")
    store_cnpj = data.get("store_cnpj", ALLOWED_CNPJS[0])
    ip_address = data.get("ip_address", "0.0.0.0")
    app_version = data.get("app_version", "1.0.0")
    status = data.get("status", "online")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO devices (device_id, store_cnpj, ip_address, app_version, status, last_seen)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (device_id, store_cnpj, ip_address, app_version, status, now))
    conn.commit()
    conn.close()
    return {"status": "ok"}

@app.get("/api/product-image/{codigo}/{cnpj}")
def get_product_image(codigo: int, cnpj: str):
    token = get_rp_token()
    if not token:
        return Response(status_code=404)
    headers = {"token": token, "Content-Type": "application/json"}
    try:
        url = f"{RP_HOST}/v1.0/produtounidade/{codigo}/unidade/{cnpj}/imagens"
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            prod = data.get("response", {}).get("Produto", {})
            imagens = prod.get("imagens", [])
            if imagens and "imagem" in imagens[0]:
                img_b64 = imagens[0]["imagem"]
                img_type = imagens[0].get("tipo", "PNG").lower()
                b = base64.b64decode(img_b64)
                try:
                    raw = gzip.decompress(b)
                except:
                    raw = b
                media_type = f"image/{img_type}" if img_type in ["png", "jpeg", "jpg"] else "image/png"
                return Response(content=raw, media_type=media_type)
    except Exception as e:
        logger.error(f"Erro ao buscar imagem do produto {codigo}: {e}")
    return Response(status_code=404)

@app.get("/api/product/{barcode}")
def get_product(barcode: str, cnpj: str = None, device_id: str = "unknown"):
    target_cnpj = cnpj if cnpj else ALLOWED_CNPJS[0]
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM produtos
        WHERE (cnpj = ? OR cnpj = '00000000000000') AND (codigo_barras = ? OR codigo = ? OR codigo_barras LIKE ?)
        LIMIT 1
    """, (target_cnpj, barcode, barcode, f"%{barcode}%"))
    row = cursor.fetchone()
    conn.close()
    if row:
        product_data = {
            "codigo": row["codigo"],
            "cnpj": row["cnpj"],
            "codigoBarras": row["codigo_barras"],
            "descricao": row["descricao"],
            "preco": row["preco"],
            "precoAnterior": row["preco_anterior"],
            "unidadeMedida": row["unidade"],
            "imagemUrl": f"/api/product-image/{row['codigo']}/{row['cnpj']}",
            "ativo": bool(row["ativo"])
        }
        log_device_event(device_id, target_cnpj, barcode, "CONSULTA", "SUCESSO", f"Produto: {row['descricao']} - R$ {row['preco']}")
        return {"status": "ok", "source": "cache_local", "product": product_data}

    log_device_event(device_id, target_cnpj, barcode, "CONSULTA", "NAO_ENCONTRADO", f"EAN não localizado: {barcode}")
    return {"status": "not_found", "message": f"Produto não encontrado para a unidade {target_cnpj}."}

# --- Painel Administrativo API ---

@app.get("/api/admin/stores")
def admin_stores():
    return get_sales_units()

@app.get("/api/admin/stats")
def admin_stats():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM produtos")
    total_produtos = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM devices")
    total_devices = cursor.fetchone()[0]
    cursor.execute("SELECT cnpj, COUNT(*) FROM produtos GROUP BY cnpj")
    por_loja = [{"cnpj": row[0], "produtos": row[1]} for row in cursor.fetchall()]
    conn.close()
    return {
        "sync_status": sync_status,
        "total_produtos": total_produtos,
        "total_devices": total_devices,
        "produtos_por_loja": por_loja,
        "sync_interval_minutes": SYNC_INTERVAL_MINUTES
    }

@app.get("/api/admin/devices")
def admin_devices():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM devices ORDER BY last_seen DESC")
    devices = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return devices

@app.get("/api/admin/logs")
def admin_logs(limit: int = 50):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM device_logs ORDER BY id DESC LIMIT ?", (limit,))
    logs = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return logs

@app.get("/api/admin/products/search")
def admin_search_products(q: str = "", cnpj: str = None):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    if cnpj and cnpj != "all":
        if not q.strip():
            cursor.execute("SELECT * FROM produtos WHERE cnpj = ? LIMIT 100", (cnpj,))
        else:
            cursor.execute("""
                SELECT * FROM produtos
                WHERE cnpj = ? AND (descricao LIKE ? OR codigo_barras LIKE ? OR codigo = ?)
                LIMIT 100
            """, (cnpj, f"%{q}%", f"%{q}%", q))
    else:
        if not q.strip():
            cursor.execute("SELECT * FROM produtos LIMIT 100")
        else:
            cursor.execute("""
                SELECT * FROM produtos
                WHERE (descricao LIKE ? OR codigo_barras LIKE ? OR codigo = ?)
                LIMIT 100
            """, (f"%{q}%", f"%{q}%", q))

    products = [dict(row) for row in cursor.fetchall()]
    for p in products:
        p["imagem_url"] = f"/api/product-image/{p['codigo']}/{p['cnpj']}"

    conn.close()
    return {"count": len(products), "products": products}

@app.post("/api/admin/config")
def admin_update_config(data: dict):
    global SYNC_INTERVAL_MINUTES
    if "sync_interval_minutes" in data:
        SYNC_INTERVAL_MINUTES = int(data["sync_interval_minutes"])
    return {"status": "ok", "sync_interval_minutes": SYNC_INTERVAL_MINUTES}

@app.get("/", response_class=HTMLResponse)
def kiosk_home():
    for p in [os.path.join("server", "static", "index.html"), os.path.join("static", "index.html")]:
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                return HTMLResponse(content=f.read(), headers={"Cache-Control": "no-store, no-cache, must-revalidate, max-age=0"})
    return "index.html não encontrado"

@app.get("/admin", response_class=HTMLResponse)
def admin_panel():
    for admin_path in [os.path.join("server", "static", "admin.html"), os.path.join("static", "admin.html")]:
        if os.path.exists(admin_path):
            with open(admin_path, "r", encoding="utf-8") as f:
                return HTMLResponse(content=f.read(), headers={"Cache-Control": "no-store, no-cache, must-revalidate, max-age=0"})
    return "Painel admin.html não encontrado"

if os.path.exists("server/static"):
    app.mount("/static", StaticFiles(directory="server/static"), name="static")
elif os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")
