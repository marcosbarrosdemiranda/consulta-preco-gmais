import os
import time
import sqlite3
import logging
import threading
import requests
from datetime import datetime
from fastapi import FastAPI, HTTPException, BackgroundTasks, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("consulta-preco-server")

app = FastAPI(title="Consulta Preço Gmais - Servidor Local Multi-Loja + Painel Admin", version="3.2.0")

RP_HOST = os.getenv("RP_HOST", "http://servicosflex.rpinfo.com.br:9000")
RP_USER = os.getenv("RP_USER", "100049")
RP_PASS = os.getenv("RP_PASS", "gr142536")
RP_CNPJ = os.getenv("RP_CNPJ", "00000000000000,11111111000100")
SYNC_INTERVAL_MINUTES = int(os.getenv("SYNC_INTERVAL_MINUTES", "10"))
SERVER_PORT = int(os.getenv("PORT", "48291"))

DATA_DIR = "/app/data" if os.path.exists("/app") else "data"
os.makedirs(DATA_DIR, exist_ok=True)
DB_PATH = os.path.join(DATA_DIR, "produtos.db")

sync_status = {
    "is_syncing": False,
    "last_sync": None,
    "total_produtos": 0,
    "unidades_sincronizadas": [],
    "ultimo_erro": None
}

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

    conn.commit()

    # Seed products if empty
    cursor.execute("SELECT COUNT(*) FROM produtos")
    if cursor.fetchone()[0] == 0:
        logger.info("Banco vazio detectado. Inserindo produtos de exemplo (seed)...")
        sample_products = [
            (100099, "33168717000104", "7894900010015", "Refrigerante Coca Cola 350ml", 4.99, 5.49, "UN", "https://via.placeholder.com/400?text=Coca-Cola+350ml", 1),
            (100100, "33168717000104", "7891000123456", "Cerveja Skol 350ml Lata", 4.49, 4.99, "UN", "https://via.placeholder.com/400?text=Cerveja+Skol", 1),
            (100101, "33168717000104", "7896004710123", "Leite Integral Parmalat 1L", 6.89, 7.29, "UN", "https://via.placeholder.com/400?text=Leite+Parmalat", 1),
            (100099, "07647329000198", "7894900010015", "Refrigerante Coca Cola 350ml (Jardim)", 4.79, 5.29, "UN", "https://via.placeholder.com/400?text=Coca-Cola+350ml+Jardim", 1),
            (100100, "07647329000198", "7891000123456", "Cerveja Skol 350ml Lata (Jardim)", 4.29, 4.79, "UN", "https://via.placeholder.com/400?text=Cerveja+Skol", 1)
        ]
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for p in sample_products:
            cursor.execute("""
                INSERT OR REPLACE INTO produtos (codigo, cnpj, codigo_barras, descricao, preco, preco_anterior, unidade, imagem_url, ativo, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (*p, now_str))
        conn.commit()
        logger.info("Produtos de exemplo inseridos com sucesso.")

    conn.close()
    logger.info(f"Banco SQLite inicializado em {DB_PATH}.")

init_db()

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
    cnpjs = [c.strip() for c in RP_CNPJ.split(",") if c.strip()]
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
                    resp = requests.get(url, headers=headers, timeout=10)
                except Exception:
                    break
                if resp.status_code == 401:
                    token = get_rp_token()
                    if token:
                        headers["token"] = token
                        resp = requests.get(url, headers=headers, timeout=10)
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
                    codigo = item.get("codigo", item.get("id"))
                    if not codigo:
                        continue
                    codigo_barras = item.get("codigoBarras", item.get("codBarras", ""))
                    if not codigo_barras and "codigosBarras" in item and item["codigosBarras"]:
                        codigo_barras = item["codigosBarras"][0].get("codigoBarras", "")
                    descricao = item.get("descricao", item.get("nome", "PRODUTO"))
                    preco = float(item.get("preco", item.get("precoVenda", item.get("valor", 0.0))))
                    preco_anterior = item.get("precoAnterior", None)
                    unidade = item.get("unidadeMedida", item.get("unidade", "UN"))
                    imagem_url = item.get("imagemUrl", f"https://via.placeholder.com/400?text={codigo_barras or codigo}")
                    ativo = 1 if item.get("ativo", True) else 0

                    cursor.execute("""
                        INSERT OR REPLACE INTO produtos (codigo, cnpj, codigo_barras, descricao, preco, preco_anterior, unidade, imagem_url, ativo, updated_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (codigo, cnpj, str(codigo_barras), descricao, preco, preco_anterior, unidade, imagem_url, ativo, now_str))
                    total_unidade += 1
                conn.commit()
                last_item = batch[-1]
                next_id = last_item.get("codigo", last_item.get("id"))
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
    store_cnpj = data.get("store_cnpj", RP_CNPJ.split(",")[0])
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

@app.get("/api/product/{barcode}")
def get_product(barcode: str, cnpj: str = None, device_id: str = "unknown"):
    target_cnpj = cnpj if cnpj else [c.strip() for c in RP_CNPJ.split(",") if c.strip()][0]
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
            "imagemUrl": row["imagem_url"],
            "ativo": bool(row["ativo"])
        }
        log_device_event(device_id, target_cnpj, barcode, "CONSULTA", "SUCESSO", f"Produto: {row['descricao']} - R$ {row['preco']}")
        return {"status": "ok", "source": "cache_local", "product": product_data}

    log_device_event(device_id, target_cnpj, barcode, "CONSULTA", "NAO_ENCONTRADO", f"EAN não localizado: {barcode}")
    return {"status": "not_found", "message": f"Produto não encontrado para a unidade {target_cnpj}."}

# --- Painel Administrativo API ---

@app.get("/api/admin/stores")
def admin_stores():
    token = get_rp_token()
    if token:
        try:
            resp = requests.get(f"{RP_HOST}/v1.6/unidades", headers={"token": token}, timeout=5)
            if resp.status_code == 200:
                data = resp.json()
                content = data.get("response", {}).get("content", data.get("unidades", []))
                if content:
                    stores = []
                    for u in content:
                        cnpj = str(u.get("cnpj", ""))
                        nome = u.get("nome", u.get("nomeReduzido", f"Loja {cnpj}"))
                        if cnpj:
                            stores.append({"cnpj": cnpj, "nome": nome})
                    if stores:
                        return stores
        except Exception:
            pass
    cnpjs = [c.strip() for c in RP_CNPJ.split(",") if c.strip()]
    stores = [{"cnpj": c, "nome": f"Loja / CNPJ {c}"} for c in cnpjs]
    return stores

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
