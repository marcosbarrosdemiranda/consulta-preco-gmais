import os
import time
import sqlite3
import logging
import threading
import requests
from datetime import datetime
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("consulta-preco-server")

app = FastAPI(title="Consulta Preço Gmais - Servidor Local (Multi-Loja RP Info)", version="2.1.0")

RP_HOST = os.getenv("RP_HOST", "http://servicosflex.rpinfo.com.br:9000")
RP_USER = os.getenv("RP_USER", "100049")
RP_PASS = os.getenv("RP_PASS", "gr142536")
RP_CNPJ = os.getenv("RP_CNPJ", "00000000000000")
SYNC_INTERVAL_MINUTES = int(os.getenv("SYNC_INTERVAL_MINUTES", "10"))

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
    """Inicializa o banco de dados SQLite local com suporte a multi-loja (por CNPJ/Unidade)."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Verifica se a tabela antiga existe sem a coluna cnpj
    cursor.execute("PRAGMA table_info(produtos)")
    columns = [col[1] for col in cursor.fetchall()]

    if columns and "cnpj" not in columns:
        logger.warning("Migrando banco de dados antigo para o formato multi-loja (adicionando CNPJ)...")
        cursor.execute("DROP TABLE IF EXISTS produtos")

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
    conn.commit()
    conn.close()
    logger.info(f"Banco de dados SQLite multi-loja inicializado com sucesso em {DB_PATH}.")

init_db()

def get_rp_token():
    """Obtém ou renova o token de autenticação da API RP Info."""
    url = f"{RP_HOST}/v1.1/auth"
    payload = {"usuario": RP_USER, "senha": RP_PASS}
    headers = {"Content-Type": "application/json"}

    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=15)
        data = resp.json()
        response_obj = data.get("response", data)
        if response_obj.get("status") == "ok" or "token" in response_obj:
            return response_obj.get("token")
        else:
            logger.error(f"Erro na autenticação RP Info: {data}")
            return None
    except Exception as e:
        logger.error(f"Exceção ao autenticar na RP Info: {e}")
        return None

def sync_products_from_erp():
    """Tarefa em background: Sincroniza produtos ativos e preços específicos de cada unidade/loja (CNPJ)."""
    global sync_status
    if sync_status["is_syncing"]:
        logger.info("Sincronização já está em andamento. Ignorando...")
        return

    sync_status["is_syncing"] = True
    sync_status["ultimo_erro"] = None
    logger.info("=== Iniciando sincronização multi-loja de produtos e preços ativos com ERP RP Info ===")

    token = get_rp_token()
    if not token:
        sync_status["is_syncing"] = False
        sync_status["ultimo_erro"] = "Falha ao obter token de autenticação na RP Info"
        logger.error(sync_status["ultimo_erro"])
        return

    headers = {"token": token, "Content-Type": "application/json"}
    cnpjs = [c.strip() for c in RP_CNPJ.split(",") if c.strip()]
    total_geral = 0
    unidades_sucesso = []

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        for cnpj in cnpjs:
            logger.info(f"--- Sincronizando unidade / CNPJ: {cnpj} ---")
            last_id = 0
            total_unidade = 0

            while True:
                url = f"{RP_HOST}/v3.2/produtounidade/listaprodutos/{last_id}/unidade/{cnpj}/detalhado/ativos"

                resp = requests.get(url, headers=headers, timeout=30)
                if resp.status_code == 401:
                    token = get_rp_token()
                    if token:
                        headers["token"] = token
                        resp = requests.get(url, headers=headers, timeout=30)
                    else:
                        break

                if resp.status_code != 200:
                    logger.error(f"Erro HTTP {resp.status_code} para unidade {cnpj}: {resp.text}")
                    break

                data = resp.json()

                batch = []
                if isinstance(data, list):
                    batch = data
                elif isinstance(data, dict):
                    content = data.get("produtos", data.get("content", data.get("response", {}).get("produtos", data.get("response", {}).get("content", []))))
                    batch = content if isinstance(content, list) else []

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

                    descricao = item.get("descricao", item.get("nome", "PRODUTO SEM DESCRIÇÃO"))
                    preco = float(item.get("preco", item.get("precoVenda", item.get("valor", item.get("preco2", 0.0)))))
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
            logger.info(f"Unidade {cnpj} sincronizada: {total_unidade} produtos ativos.")

        sync_status["last_sync"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        sync_status["total_produtos"] = total_geral
        sync_status["unidades_sincronizadas"] = unidades_sucesso
        logger.info(f"=== Sincronização multi-loja concluída com sucesso! Total geral: {total_geral} produtos ===")

    except Exception as e:
        logger.exception("Erro crítico durante a sincronização multi-loja")
        sync_status["ultimo_erro"] = str(e)
    finally:
        conn.close()
        sync_status["is_syncing"] = False

def background_scheduler():
    """Loop em background que executa a sincronização periodicamente."""
    while True:
        try:
            sync_products_from_erp()
        except Exception as e:
            logger.error(f"Erro no agendador de sincronização: {e}")

        time.sleep(SYNC_INTERVAL_MINUTES * 60)

threading.Thread(target=background_scheduler, daemon=True).start()

@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "service": "consulta-preco-gmais-server-multiloja",
        "rp_host": RP_HOST,
        "cnpjs_configurados": [c.strip() for c in RP_CNPJ.split(",") if c.strip()],
        "sync_status": sync_status
    }

@app.post("/api/sync/trigger")
def trigger_sync(background_tasks: BackgroundTasks):
    """Força sincronização manual imediata."""
    if sync_status["is_syncing"]:
        return {"status": "running", "message": "Sincronização já está em andamento."}

    background_tasks.add_task(sync_products_from_erp)
    return {"status": "started", "message": "Sincronização multi-loja iniciada em segundo plano."}

@app.get("/api/product/{barcode}")
def get_product(barcode: str, cnpj: str = None):
    """Consulta ultrarrápida no SQLite local filtrando pelo código de barras e pela unidade (CNPJ)."""
    target_cnpj = cnpj if cnpj else [c.strip() for c in RP_CNPJ.split(",") if c.strip()][0]

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM produtos
        WHERE cnpj = ? AND (codigo_barras = ? OR codigo = ? OR codigo_barras LIKE ?)
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
        return {"status": "ok", "source": "cache_local", "product": product_data}

    logger.warning(f"Produto {barcode} não encontrado no cache local para a unidade {target_cnpj}.")
    return {"status": "not_found", "message": f"Produto não encontrado para a unidade {target_cnpj}."}

if os.path.exists("server/static"):
    app.mount("/", StaticFiles(directory="server/static", html=True), name="static")
else:
    @app.get("/")
    def root():
        return {"message": "Servidor rodando. Frontend em server/static/"}
