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

app = FastAPI(title="Consulta Preço Gmais - Servidor Local (RP Info Sync)", version="2.0.0")

RP_HOST = os.getenv("RP_HOST", "http://192.168.1.4:9000")
RP_USER = os.getenv("RP_USER", "100049")
RP_PASS = os.getenv("RP_PASS", "gr142536")
RP_CNPJ = os.getenv("RP_CNPJ", "00000000000000")
SYNC_INTERVAL_MINUTES = int(os.getenv("SYNC_INTERVAL_MINUTES", "10"))

# Diretório e arquivo de banco de dados SQLite local
DATA_DIR = "/app/data" if os.path.exists("/app") else "data"
os.makedirs(DATA_DIR, exist_ok=True)
DB_PATH = os.path.join(DATA_DIR, "produtos.db")

# Estado global da sincronização
sync_status = {
    "is_syncing": False,
    "last_sync": None,
    "total_produtos": 0,
    "ultimo_erro": None
}

def init_db():
    """Inicializa o banco de dados SQLite local para cache de produtos ativos."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            codigo INTEGER PRIMARY KEY,
            codigo_barras TEXT,
            descricao TEXT,
            preco REAL,
            preco_anterior REAL,
            unidade TEXT,
            imagem_url TEXT,
            ativo INTEGER,
            updated_at TEXT
        )
    """)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_barras ON produtos(codigo_barras)")
    conn.commit()
    conn.close()
    logger.info(f"Banco de dados SQLite local inicializado em {DB_PATH}.")

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
    """Tarefa em background: Sincroniza produtos ativos da API RP Info para o SQLite local."""
    global sync_status
    if sync_status["is_syncing"]:
        logger.info("Sincronização já está em andamento. Ignorando...")
        return

    sync_status["is_syncing"] = True
    sync_status["ultimo_erro"] = None
    logger.info("=== Iniciando sincronização periódica de produtos ativos com ERP RP Info ===")

    token = get_rp_token()
    if not token:
        sync_status["is_syncing"] = False
        sync_status["ultimo_erro"] = "Falha ao obter token de autenticação na RP Info"
        logger.error(sync_status["ultimo_erro"])
        return

    headers = {"token": token, "Content-Type": "application/json"}
    last_id = 0
    total_sincronizados = 0

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        while True:
            # Endpoint oficial v3.2 para produtos ativos detalhados
            url = f"{RP_HOST}/v3.2/produtounidade/listaprodutos/{last_id}/unidade/{RP_CNPJ}/detalhado/ativos"
            logger.info(f"Buscando lote de produtos ativos a partir do lastID={last_id}...")

            resp = requests.get(url, headers=headers, timeout=30)
            if resp.status_code == 401:
                token = get_rp_token()
                if token:
                    headers["token"] = token
                    resp = requests.get(url, headers=headers, timeout=30)
                else:
                    break

            if resp.status_code != 200:
                logger.error(f"Erro HTTP {resp.status_code} ao buscar produtos: {resp.text}")
                break

            data = resp.json()

            batch = []
            if isinstance(data, list):
                batch = data
            elif isinstance(data, dict):
                content = data.get("produtos", data.get("content", data.get("response", {}).get("produtos", data.get("response", {}).get("content", []))))
                batch = content if isinstance(content, list) else []

            if not batch:
                logger.info("Fim da listagem de produtos ou lote vazio.")
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
                    INSERT OR REPLACE INTO produtos (codigo, codigo_barras, descricao, preco, preco_anterior, unidade, imagem_url, ativo, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (codigo, str(codigo_barras), descricao, preco, preco_anterior, unidade, imagem_url, ativo, now_str))

                total_sincronizados += 1

            conn.commit()

            last_item = batch[-1]
            next_id = last_item.get("codigo", last_item.get("id"))
            if next_id == last_id:
                break
            last_id = next_id

            time.sleep(0.1)

        sync_status["last_sync"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        sync_status["total_produtos"] = total_sincronizados
        logger.info(f"=== Sincronização concluída com sucesso! Total de produtos ativos salvos: {total_sincronizados} ===")

    except Exception as e:
        logger.exception("Erro crítico durante a sincronização de produtos")
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

# Inicia a thread de sincronização em background
threading.Thread(target=background_scheduler, daemon=True).start()

@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "service": "consulta-preco-gmais-server",
        "rp_host": RP_HOST,
        "cnpj": RP_CNPJ,
        "sync_status": sync_status
    }

@app.post("/api/sync/trigger")
def trigger_sync(background_tasks: BackgroundTasks):
    """Força sincronização manual imediata."""
    if sync_status["is_syncing"]:
        return {"status": "running", "message": "Sincronização já está em andamento."}

    background_tasks.add_task(sync_products_from_erp)
    return {"status": "started", "message": "Sincronização iniciada em segundo plano."}

@app.get("/api/product/{barcode}")
def get_product(barcode: str):
    """Consulta ultrarrápida no SQLite local."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM produtos
        WHERE codigo_barras = ? OR codigo = ? OR codigo_barras LIKE ?
        LIMIT 1
    """, (barcode, barcode, f"%{barcode}%"))

    row = cursor.fetchone()
    conn.close()

    if row:
        product_data = {
            "codigo": row["codigo"],
            "codigoBarras": row["codigo_barras"],
            "descricao": row["descricao"],
            "preco": row["preco"],
            "precoAnterior": row["preco_anterior"],
            "unidadeMedida": row["unidade"],
            "imagemUrl": row["imagem_url"],
            "ativo": bool(row["ativo"])
        }
        return {"status": "ok", "source": "cache_local", "product": product_data}

    logger.warning(f"Produto {barcode} não encontrado no cache local.")
    return {"status": "not_found", "message": "Produto não encontrado no cache local."}

# Servir frontend estático
if os.path.exists("server/static"):
    app.mount("/", StaticFiles(directory="server/static", html=True), name="static")
else:
    @app.get("/")
    def root():
        return {"message": "Servidor rodando. Frontend em server/static/"}
