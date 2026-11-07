#!/usr/bin/env python3
"""
RP Info API — módulo de autenticação, pronto para uso.

Usa o endpoint ATUAL e não-depreciado (POST /v1.2/auth) — ver reference/pegadinhas.md
sobre por que não usar mais /v1.1/auth.

Uso:
    python rp_auth.py --host http://192.168.1.4:9000 --usuario 100049 --senha ********
    python rp_auth.py --show     # mostra o token salvo (sem reautenticar)
    python rp_auth.py --check    # verifica se o token salvo ainda é válido

As credenciais NUNCA devem ser hardcoded neste arquivo (ele é copiado entre máquinas/usuários
ao instalar a skill). Preferir passar via variáveis de ambiente ou argumentos de linha de comando:

    set RPINFO_API_BASE_URL=http://192.168.1.4:9000
    set RPINFO_API_USUARIO=100049
    set RPINFO_API_SENHA=********
    python rp_auth.py

O token obtido é salvo em `rp_token.json`, no diretório atual — não versionar esse arquivo
(já coberto por padrões comuns de .gitignore: `rp_token.json`).
"""

import argparse
import json
import os
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

TOKEN_FILE = "rp_token.json"
# Exemplo oficial da documentação da RP Info — NÃO é uma credencial real, é só o default
# documentado publicamente para facilitar o primeiro teste contra o ambiente de homologação.
DEFAULT_HOST = "http://servicosflex.rpinfo.com.br:9000"
DEFAULT_USER = "100000"
DEFAULT_PASS = "123456"


def authenticate(host, usuario, senha):
    url = f"{host}/v1.2/auth"
    payload = json.dumps({"usuario": usuario, "senha": senha}).encode("utf-8")
    req = urllib.request.Request(
        url, data=payload, headers={"Content-Type": "application/json"}, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code}: {e.read().decode('utf-8', errors='replace')}") from e

    response = body.get("response", {})
    if response.get("status") != "ok":
        raise RuntimeError(f"Autenticação recusada: {json.dumps(body, ensure_ascii=False)}")

    # PEGADINHA (confirmada contra servidor real em 2026-10-14): o spec documenta o token
    # direto em `response.token`, mas pelo menos nesta versão do ERP (appVersion 5.0.7.022)
    # ele vem aninhado em `response.content.token`. Tratar os dois formatos.
    # Ver reference/pegadinhas.md item 9.
    content = response.get("content") if isinstance(response.get("content"), dict) else response

    return {
        "token": content.get("token", ""),
        "expires": content.get("tokenExpiration", ""),
        "expires_in": content.get("expiresIn", 0),  # unidade varia (ver _seconds_until_expiry)
        "host": host,
    }


def _seconds_until_expiry(token_data):
    """Calcula segundos restantes até a expiração, preferindo a data absoluta
    (`tokenExpiration`) a `expiresIn`, porque a unidade de `expiresIn` já variou entre
    minutos (spec v1.1) e segundos (observado ao vivo em 2026-10-14) — ver pegadinhas.md item 9.
    """
    expires = token_data.get("expires", "")
    for fmt in ("%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z", "%d/%m/%Y %H:%M:%S"):
        try:
            value = expires.replace("Z", "+0000") if fmt.endswith("%z") else expires
            dt = datetime.strptime(value, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return (dt - datetime.now(timezone.utc)).total_seconds()
        except (ValueError, AttributeError):
            continue
    # Fallback: não deu pra parsear a data absoluta — tenta expiresIn como segundos
    # (observado ao vivo) e, se o resultado parecer baixo demais, tenta como minutos.
    expires_in = token_data.get("expires_in", 0) or 0
    elapsed = time.time() - token_data.get("saved_at", 0)
    remaining_as_seconds = expires_in - elapsed
    if remaining_as_seconds > 0:
        return remaining_as_seconds
    return expires_in * 60 - elapsed


def save_token(data, path=TOKEN_FILE):
    data = dict(data, saved_at=time.time())
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return path


def load_token(path=TOKEN_FILE):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def is_token_valid(token_data):
    if not token_data or not token_data.get("token"):
        return False
    remaining = _seconds_until_expiry(token_data)
    return remaining > 0


def main():
    parser = argparse.ArgumentParser(description="RP Info API — autenticação (v1.2)")
    parser.add_argument("--host", default=os.environ.get("RPINFO_API_BASE_URL", DEFAULT_HOST))
    parser.add_argument("--usuario", default=os.environ.get("RPINFO_API_USUARIO", DEFAULT_USER))
    parser.add_argument("--senha", default=os.environ.get("RPINFO_API_SENHA", DEFAULT_PASS))
    parser.add_argument("--show", action="store_true", help="Mostra o token salvo, sem reautenticar")
    parser.add_argument("--check", action="store_true", help="Verifica se o token salvo ainda é válido")
    args = parser.parse_args()

    if args.show:
        data = load_token()
        print(json.dumps(data, indent=2, ensure_ascii=False) if data else "Nenhum token salvo.")
        return

    if args.check:
        data = load_token()
        if data and is_token_valid(data):
            print(f"Token válido. Expira em: {data.get('expires', 'desconhecido')} (host: {data.get('host')})")
        else:
            print("Token ausente ou expirado — rode sem --check/--show para reautenticar.")
        return

    print(f"Autenticando em {args.host} ...")
    result = authenticate(args.host, args.usuario, args.senha)
    path = save_token(result)
    token = result["token"]
    masked = f"{token[:8]}...{token[-4:]}" if len(token) > 12 else "***"
    remaining = _seconds_until_expiry(dict(result, saved_at=time.time()))
    print(f"Token obtido: {masked}")
    print(f"Expira em: {result['expires']} (faltam ~{remaining / 60:.0f} min)")
    print(f"Salvo em: {path}")


if __name__ == "__main__":
    main()
