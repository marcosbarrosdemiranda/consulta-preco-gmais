#!/usr/bin/env python3
"""
Painel local de testes — API REST da RP Info (e, opcionalmente, Postgres direto).

Ferramenta OPCIONAL que acompanha a skill: serve pra visualizar, num navegador, se as vias de
acesso à API (e ao banco, se configurado) estão OK, sem precisar ler log/JSON cru. Não é
necessária pra skill funcionar — é só um atalho visual pra quem quiser. Funciona com QUALQUER
instalação da RP Info, não só a que gerou este exemplo: todo endereço/credencial vem do `.env`
(ver `.env.example`).

Abas:
  - "Conexão API-Banco": autenticação na API (`POST /v1.2/auth`) + (opcional) conexão direta
    ao Postgres, se `RPINFO_DB_*` estiver configurado no `.env`. Testes independentes — ver
    prioridade de acesso no `SKILL.md`/`CLAUDE.md` do projeto que instalar isto: API sempre
    primeiro, banco direto é última instância.
  - "Endpoint de Negócio": round-trip completo (autentica, pega token, chama um endpoint de
    negócio real de leitura, `GET /v1.6/unidades`) — confirma que o token funciona ponta a ponta.
  - "Ofertas por Loja": lista as lojas ao vivo (`/v1.6/unidades`) e busca as ofertas de preço
    vigentes de uma loja (`GET /v1.0/produtounidade/ofertas`, paginado por lastId).
  - "Histórico": todos os testes já rodados (guardados em `historico.db`, local e nunca
    versionado), com botão pra gerar um rascunho de achado pra `reference/pegadinhas.md`.

SOMENTE LEITURA em tudo — nenhum teste aqui escreve dado nenhum (nem no banco, nem via
endpoint de negócio da API).

Credenciais vêm só do `.env` (nunca hardcoded aqui, nunca devolvidas inteiras ao navegador).
Uma única tentativa por clique, com os parâmetros exatos do `.env` — nunca adivinha variação.

Uso:
    cp .env.example .env   # preencher com os dados do SEU ambiente
    pip install -r requirements.txt
    python app.py
    (abre em http://127.0.0.1:5000 — só local, não expõe na rede)
"""
import os
import sys
import time
from pathlib import Path

import requests
from dotenv import load_dotenv
from flask import Flask, abort, jsonify, render_template, request

import achados
import historico

AQUI = Path(__file__).resolve().parent
load_dotenv(AQUI / ".env")

# Reaproveita a autenticação já testada/corrigida da skill (response.content, expiresIn em
# segundos etc. — ver reference/pegadinhas.md item 9) em vez de duplicar a lógica aqui.
# `painel/` fica dentro da própria skill, então `scripts/` é sempre o irmão logo acima.
sys.path.insert(0, str(AQUI.parent / "scripts"))
import rp_auth  # noqa: E402

# Lista fechada de bancos permitidos — configurável via RPINFO_DB_BANCOS (ex.: "erp,vdadet,wrpdv"),
# porque cada instalação da RP Info tem seus próprios nomes de banco. Vazio = aba de banco
# direto fica desabilitada (só a API é testada), o que é o padrão seguro pra uma instalação nova.
BANCOS_PERMITIDOS = [b.strip() for b in os.environ.get("RPINFO_DB_BANCOS", "").split(",") if b.strip()]

app = Flask(__name__)

try:
    import psycopg2
except ImportError:
    psycopg2 = None  # banco direto é opcional; sem psycopg2 instalado, essa aba só fica desabilitada


def testar_api():
    """Uma única tentativa de POST /v1.2/auth, com os parâmetros exatos do .env."""
    host = os.environ.get("RPINFO_API_BASE_URL")
    usuario = os.environ.get("RPINFO_API_USUARIO")
    senha = os.environ.get("RPINFO_API_SENHA")

    faltando = [k for k, v in {
        "RPINFO_API_BASE_URL": host, "RPINFO_API_USUARIO": usuario, "RPINFO_API_SENHA": senha,
    }.items() if not v]
    if faltando:
        return {"ok": False, "erro": f"Variável(is) de ambiente faltando no .env: {', '.join(faltando)}"}

    try:
        resultado = rp_auth.authenticate(host, usuario, senha)
    except Exception as exc:
        return {"ok": False, "erro": str(exc)}

    token = resultado.get("token", "")
    token_mascarado = f"{token[:8]}...{token[-4:]}" if len(token) > 12 else "***"
    restante_seg = rp_auth._seconds_until_expiry(dict(resultado, saved_at=time.time()))
    return {
        "ok": True,
        "host": host,
        "usuario": usuario,
        "token_mascarado": token_mascarado,
        "expira_em": resultado.get("expires", ""),
        "expira_em_min": round(restante_seg / 60) if restante_seg else None,
    }


def testar_conexao(dbname):
    """Uma única tentativa, somente leitura, com os parâmetros exatos do .env. Nunca adivinha nada."""
    if psycopg2 is None:
        return {"ok": False, "erro": "psycopg2 não instalado — instale via requirements.txt pra usar esta aba."}

    host = os.environ.get("RPINFO_DB_HOST")
    port = os.environ.get("RPINFO_DB_PORT")
    user = os.environ.get("RPINFO_DB_USER")
    password = os.environ.get("RPINFO_DB_PASSWORD")

    faltando = [k for k, v in {
        "RPINFO_DB_HOST": host, "RPINFO_DB_PORT": port,
        "RPINFO_DB_USER": user, "RPINFO_DB_PASSWORD": password,
    }.items() if not v]
    if faltando:
        return {"ok": False, "erro": f"Variável(is) de ambiente faltando no .env: {', '.join(faltando)}"}

    conn = None
    try:
        conn = psycopg2.connect(
            host=host, port=port, user=user, password=password,
            dbname=dbname, connect_timeout=10, sslmode="disable",
        )
        conn.set_session(readonly=True, autocommit=True)
        cur = conn.cursor()
        cur.execute("SELECT version();")
        versao = cur.fetchone()[0]
        cur.execute("SELECT current_database();")
        banco_atual = cur.fetchone()[0]
        return {
            "ok": True,
            "banco": banco_atual,
            "host": host,
            "porta": port,
            "usuario": user,
            "versao_postgres": versao,
        }
    except Exception as exc:
        return {"ok": False, "erro": str(exc)}
    finally:
        if conn is not None:
            conn.close()


def testar_endpoint_negocio():
    """Round-trip completo: autentica, pega o token e chama GET /v1.6/unidades (endpoint
    de negócio real, somente leitura, já confirmado ao vivo — ver reference/pegadinhas.md
    item 9). Não escreve nada, só confirma que o token funciona ponta a ponta."""
    host = os.environ.get("RPINFO_API_BASE_URL")
    usuario = os.environ.get("RPINFO_API_USUARIO")
    senha = os.environ.get("RPINFO_API_SENHA")

    faltando = [k for k, v in {
        "RPINFO_API_BASE_URL": host, "RPINFO_API_USUARIO": usuario, "RPINFO_API_SENHA": senha,
    }.items() if not v]
    if faltando:
        return {"ok": False, "erro": f"Variável(is) de ambiente faltando no .env: {', '.join(faltando)}"}

    try:
        auth = rp_auth.authenticate(host, usuario, senha)
    except Exception as exc:
        return {"ok": False, "erro": f"Falha na autenticação: {exc}"}

    token = auth.get("token", "")
    if not token:
        return {"ok": False, "erro": "Autenticação OK, mas o token veio vazio."}

    endpoint = "/v1.6/unidades"
    url = f"{host}{endpoint}"
    try:
        resp = requests.get(
            url, headers={"token": token, "Content-Type": "application/json"}, timeout=15
        )
        resp.raise_for_status()
        body = resp.json()
    except Exception as exc:
        return {"ok": False, "erro": f"Falha ao chamar GET {endpoint}: {exc}"}

    # response.content aqui é uma LISTA de unidades (confirmado ao vivo), não um dict como
    # em /v1.2/auth — nunca cair no "messages" (array só com a msg de confirmação) por engano.
    response = body.get("response", {}) if isinstance(body, dict) else {}
    content = response.get("content")
    if isinstance(content, list):
        lista = content
    elif isinstance(content, dict):
        lista = next((v for v in content.values() if isinstance(v, list)), [])
    else:
        # fallback p/ formato tipo auth (dado solto na raiz de response) - nunca "messages".
        lista = next((v for k, v in response.items() if k != "messages" and isinstance(v, list)), [])

    return {
        "ok": True,
        "endpoint": f"GET {endpoint}",
        "host": host,
        "quantidade": len(lista),
        "amostra": lista[:3],
    }


def obter_unidades():
    """Autentica e lista as lojas (GET /v1.6/unidades) — usado pra popular o seletor de loja
    da aba "Ofertas por Loja". Nunca lista fixa/hardcoded: sempre busca as lojas reais da
    instalação configurada no `.env`."""
    host = os.environ.get("RPINFO_API_BASE_URL")
    usuario = os.environ.get("RPINFO_API_USUARIO")
    senha = os.environ.get("RPINFO_API_SENHA")

    faltando = [k for k, v in {
        "RPINFO_API_BASE_URL": host, "RPINFO_API_USUARIO": usuario, "RPINFO_API_SENHA": senha,
    }.items() if not v]
    if faltando:
        return {"ok": False, "erro": f"Variável(is) de ambiente faltando no .env: {', '.join(faltando)}"}

    try:
        auth = rp_auth.authenticate(host, usuario, senha)
    except Exception as exc:
        return {"ok": False, "erro": f"Falha na autenticação: {exc}"}
    token = auth.get("token", "")
    if not token:
        return {"ok": False, "erro": "Autenticação OK, mas o token veio vazio."}

    try:
        resp = requests.get(
            f"{host}/v1.6/unidades",
            headers={"token": token, "Content-Type": "application/json"}, timeout=15,
        )
        resp.raise_for_status()
        body = resp.json()
    except Exception as exc:
        return {"ok": False, "erro": f"Falha ao chamar GET /v1.6/unidades: {exc}"}

    response = body.get("response", {}) if isinstance(body, dict) else {}
    content = response.get("content")
    lojas = content if isinstance(content, list) else []  # ver pegadinhas.md item 10
    return {
        "ok": True,
        "lojas": [{"codigo": u.get("codigo"), "nome": u.get("nome"), "cnpj": u.get("cnpj")} for u in lojas],
    }


def obter_ofertas(cnpj, departamento=None, setor=None):
    """Round-trip: autentica e pagina GET /v1.0/produtounidade/ofertas (tag 00004, atual, não
    depreciado) por `lastId` (= maior codigoProduto do lote anterior — confirmado ao vivo,
    mesmo padrão de paginação incremental do item 5 de pegadinhas.md), até vir lista vazia
    ou bater um teto de segurança. Somente leitura."""
    host = os.environ.get("RPINFO_API_BASE_URL")
    usuario = os.environ.get("RPINFO_API_USUARIO")
    senha = os.environ.get("RPINFO_API_SENHA")

    faltando = [k for k, v in {
        "RPINFO_API_BASE_URL": host, "RPINFO_API_USUARIO": usuario, "RPINFO_API_SENHA": senha,
    }.items() if not v]
    if faltando:
        return {"ok": False, "erro": f"Variável(is) de ambiente faltando no .env: {', '.join(faltando)}"}

    try:
        auth = rp_auth.authenticate(host, usuario, senha)
    except Exception as exc:
        return {"ok": False, "erro": f"Falha na autenticação: {exc}"}
    token = auth.get("token", "")
    if not token:
        return {"ok": False, "erro": "Autenticação OK, mas o token veio vazio."}

    url = f"{host}/v1.0/produtounidade/ofertas"
    params = {"unidade": cnpj, "limit": 1000}
    if departamento:
        params["departamento"] = departamento
    if setor:
        params["setor"] = setor

    ofertas = []
    MAX_PAGINAS = 10  # teto de segurança (10 x 1000 = até 10 mil ofertas por loja)
    for _ in range(MAX_PAGINAS):
        try:
            resp = requests.get(
                url, headers={"token": token, "Content-Type": "application/json"},
                params=params, timeout=20,
            )
            resp.raise_for_status()
            body = resp.json()
        except Exception as exc:
            return {"ok": False, "erro": f"Falha ao chamar GET {url}: {exc}"}

        response = body.get("response", {}) if isinstance(body, dict) else {}
        content = response.get("content")
        lote = content if isinstance(content, list) else []
        if not lote:
            break
        ofertas.extend(lote)
        params["lastId"] = max(p.get("codigoProduto", 0) for p in lote)
        time.sleep(0.2)  # mesma pausa já usada nos loops de paginação legados (pegadinhas.md item 5)
        if len(lote) < params["limit"]:
            break  # último lote veio incompleto = acabou

    return {"ok": True, "endpoint": f"GET /v1.0/produtounidade/ofertas?unidade={cnpj}", "quantidade": len(ofertas), "ofertas": ofertas}


@app.route("/")
def index():
    return render_template("index.html", bancos=BANCOS_PERMITIDOS)


@app.route("/api/testar-api", methods=["POST"])
def api_testar_api():
    resultado = testar_api()
    historico.salvar("Teste de Conexão API-Banco", "api", resultado)
    return jsonify(resultado)


@app.route("/api/testar-banco", methods=["POST"])
def api_testar_banco():
    dados = request.get_json(silent=True) or {}
    banco = dados.get("banco")
    if not BANCOS_PERMITIDOS:
        return jsonify({"ok": False, "erro": "Nenhum banco configurado — defina RPINFO_DB_BANCOS no .env pra habilitar esta aba."}), 400
    if banco not in BANCOS_PERMITIDOS:
        return jsonify({"ok": False, "erro": f"Banco inválido. Use um de: {', '.join(BANCOS_PERMITIDOS)}"}), 400
    resultado = testar_conexao(banco)
    historico.salvar("Teste de Conexão API-Banco", f"banco:{banco}", resultado)
    return jsonify(resultado)


@app.route("/api/testar-endpoint-negocio", methods=["POST"])
def api_testar_endpoint_negocio():
    resultado = testar_endpoint_negocio()
    historico.salvar("Teste de Endpoint de Negócio", "unidades", resultado)
    return jsonify(resultado)


@app.route("/api/unidades")
def api_unidades():
    resultado = obter_unidades()
    return jsonify(resultado)


@app.route("/api/ofertas", methods=["POST"])
def api_ofertas():
    dados = request.get_json(silent=True) or {}
    codigo = dados.get("codigo")
    cnpj = dados.get("cnpj")
    if not codigo or not cnpj:
        return jsonify({"ok": False, "erro": "Escolha uma loja da lista (código + CNPJ obrigatórios)."}), 400

    resultado = obter_ofertas(cnpj, departamento=dados.get("departamento"), setor=dados.get("setor"))

    # Histórico guarda só um resumo (amostra de 5) — a lista completa de ofertas pode ter
    # centenas de itens por loja e não precisa inflar o historico.db; a tela mostra tudo.
    resumo = dict(resultado)
    if resultado.get("ok"):
        resumo = {
            "ok": True, "endpoint": resultado["endpoint"], "quantidade": resultado["quantidade"],
            "amostra": resultado["ofertas"][:5],
        }
    historico.salvar("Teste de Ofertas por Loja", f"loja:{codigo}", resumo)
    return jsonify(resultado)


@app.route("/api/historico")
def api_historico():
    return jsonify(historico.listar())


@app.route("/api/gerar-achado/<int:id_>", methods=["POST"])
def api_gerar_achado(id_):
    registro = historico.buscar(id_)
    if not registro:
        abort(404)
    return jsonify({"ok": True, "texto": achados.montar_rascunho(registro)})


if __name__ == "__main__":
    # host 127.0.0.1 = só esta máquina, não expõe na rede local.
    app.run(host="127.0.0.1", port=5000, debug=False)
