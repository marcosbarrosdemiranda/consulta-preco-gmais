import os
import time
import logging
import requests
from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("consulta-preco-server")

app = FastAPI(title="Consulta Preço Gmais - Servidor Local", version="1.0.0")

RP_HOST = os.getenv("RP_HOST", "http://servicosflex.rpinfo.com.br:9000")
RP_USER = os.getenv("RP_USER", "100049")
RP_PASS = os.getenv("RP_PASS", "gr142536")
RP_CNPJ = os.getenv("RP_CNPJ", "00000000000000")

# Token cache storage
token_cache = {
    "token": None,
    "expires_at": 0
}

def get_rp_token():
    """Obtém ou renova o token de autenticação da API RP Info."""
    current_time = time.time()
    if token_cache["token"] and current_time < token_cache["expires_at"]:
        return token_cache["token"]

    url = f"{RP_HOST}/v1.1/auth"
    payload = {
        "usuario": RP_USER,
        "senha": RP_PASS
    }
    headers = {"Content-Type": "application/json"}

    try:
        logger.info(f"Autenticando na API RP Info em {RP_HOST}...")
        resp = requests.post(url, json=payload, headers=headers, timeout=15)
        data = resp.json()

        # Trata formato de resposta da API RP Info
        response_obj = data.get("response", data)
        if response_obj.get("status") == "ok" or "token" in response_obj:
            token = response_obj.get("token")
            expires_in = response_obj.get("expiresIn", 3600)
            # Define margem de segurança de 5 minutos antes de expirar
            token_cache["token"] = token
            token_cache["expires_at"] = current_time + max(expires_in - 300, 60)
            logger.info("Autenticação realizada com sucesso na RP Info.")
            return token
        else:
            logger.error(f"Erro na autenticação RP Info: {data}")
            raise HTTPException(status_code=502, detail="Falha ao autenticar na retaguarda RP Info")
    except Exception as e:
        logger.exception("Exceção ao conectar com RP Info para autenticação")
        raise HTTPException(status_code=503, detail=f"Servidor RP Info indisponível: {str(e)}")

@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "consulta-preco-gmais", "cnpj": RP_CNPJ}

@app.get("/api/product/{barcode}")
def get_product(barcode: str, cnpj: str = RP_CNPJ):
    """Consulta produto por código de barras na API RP Info."""
    token = get_rp_token()
    headers = {
        "token": token,
        "Content-Type": "application/json"
    }

    # Tentativa 1: Endpoint específico de consulta por código de barras
    url = f"{RP_HOST}/v2.8/produtounidade/{barcode}/unidade/{cnpj}/consultarcodigobarras"

    try:
        logger.info(f"Consultando código de barras {barcode} para CNPJ {cnpj}")
        resp = requests.get(url, headers=headers, timeout=10)

        if resp.status_code == 401:
            # Token expirado, limpa cache e tenta novamente
            token_cache["token"] = None
            headers["token"] = get_rp_token()
            resp = requests.get(url, headers=headers, timeout=10)

        if resp.status_code == 404:
            return {"status": "not_found", "message": "Produto não encontrado"}

        data = resp.json()

        # Normalização de resposta (trata array direto, objeto ou response aninhado)
        product_item = None
        if isinstance(data, list) and len(data) > 0:
            product_item = data[0]
        elif isinstance(data, dict):
            if "response" in data and isinstance(data["response"], dict):
                content = data["response"].get("content", data["response"].get("produto", data["response"]))
                product_item = content[0] if isinstance(content, list) and content else content
            elif "produto" in data:
                product_item = data["produto"]
            elif "content" in data:
                content = data["content"]
                product_item = content[0] if isinstance(content, list) and content else content
            else:
                product_item = data

        if not product_item or not product_item.get("descricao") and not product_item.get("codigo"):
            return {"status": "not_found", "message": "Produto não encontrado"}

        # Mapeia para o formato padronizado do totem
        formatted_product = {
            "codigo": product_item.get("codigo", product_item.get("id", 0)),
            "codigoBarras": barcode,
            "descricao": product_item.get("descricao", product_item.get("nome", "PRODUTO SEM DESCRIÇÃO")),
            "preco": float(product_item.get("preco", product_item.get("precoVenda", product_item.get("valor", 0.0)))),
            "precoAnterior": product_item.get("precoAnterior", None),
            "unidadeMedida": product_item.get("unidadeMedida", product_item.get("unidade", "UN")),
            "imagemUrl": product_item.get("imagemUrl", f"https://via.placeholder.com/400?text={barcode}"),
            "estoque": float(product_item.get("estoque", 0.0))
        }

        return {"status": "ok", "product": formatted_product}

    except Exception as e:
        logger.exception(f"Erro ao consultar produto {barcode}")
        # Retorna mock estruturado para testes caso a retaguarda esteja inacessível em ambiente de homologação
        return {
            "status": "error",
            "message": str(e),
            "product": {
                "codigo": 99999,
                "codigoBarras": barcode,
                "descricao": f"PRODUTO TESTE (BARCODE: {barcode})",
                "preco": 12.99,
                "unidadeMedida": "UN",
                "imagemUrl": "https://via.placeholder.com/400?text=Produto+Exemplo"
            }
        }

# Monta arquivos estáticos do frontend Kiosk
if os.path.exists("server/static"):
    app.mount("/", StaticFiles(directory="server/static", html=True), name="static")
else:
    @app.get("/")
    def root():
        return {"message": "Servidor rodando. Coloque os arquivos do frontend em server/static/"}
