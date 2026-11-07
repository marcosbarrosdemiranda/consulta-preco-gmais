#!/usr/bin/env python3
"""
Histórico local (SQLite) de todos os testes rodados pelo painel.

`historico.db` fica aqui mesmo (nunca versionado — é dado de execução local, não segredo, mas
também não precisa ir pro repositório). Guarda só o que cada teste já devolve (os testes já
mascaram token/senha antes de retornar — ver `app.py`).
"""
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "historico.db"


def _conectar():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS historico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            criado_em TEXT NOT NULL,
            categoria TEXT NOT NULL,
            subtipo TEXT NOT NULL,
            ok INTEGER NOT NULL,
            detalhes TEXT NOT NULL
        )
        """
    )
    return conn


def salvar(categoria, subtipo, resultado):
    """Grava um registro. `resultado` é o dict que o teste já retorna (sem credencial em
    texto puro — isso é responsabilidade de cada função de teste em app.py)."""
    conn = _conectar()
    try:
        conn.execute(
            "INSERT INTO historico (criado_em, categoria, subtipo, ok, detalhes) VALUES (?, ?, ?, ?, ?)",
            (
                datetime.now(timezone.utc).isoformat(),
                categoria,
                subtipo,
                1 if resultado.get("ok") else 0,
                json.dumps(resultado, ensure_ascii=False),
            ),
        )
        conn.commit()
    finally:
        conn.close()


def listar(limite=50):
    conn = _conectar()
    try:
        cur = conn.execute(
            "SELECT id, criado_em, categoria, subtipo, ok, detalhes FROM historico ORDER BY id DESC LIMIT ?",
            (limite,),
        )
        linhas = cur.fetchall()
    finally:
        conn.close()
    return [_linha_para_dict(r) for r in linhas]


def buscar(id_):
    conn = _conectar()
    try:
        cur = conn.execute(
            "SELECT id, criado_em, categoria, subtipo, ok, detalhes FROM historico WHERE id = ?",
            (id_,),
        )
        linha = cur.fetchone()
    finally:
        conn.close()
    return _linha_para_dict(linha) if linha else None


def _linha_para_dict(linha):
    return {
        "id": linha[0],
        "criado_em": linha[1],
        "categoria": linha[2],
        "subtipo": linha[3],
        "ok": bool(linha[4]),
        "detalhes": json.loads(linha[5]),
    }
