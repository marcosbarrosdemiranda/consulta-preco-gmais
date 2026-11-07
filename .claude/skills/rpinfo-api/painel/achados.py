#!/usr/bin/env python3
"""
Monta um RASCUNHO de texto no estilo de `reference/pegadinhas.md` a partir de um registro
do histórico de testes. Só gera o texto — nunca escreve sozinho no arquivo da skill; o
usuário revisa, edita e cola manualmente em `pegadinhas.md` se achar que vale a pena.
"""
import json


def montar_rascunho(registro):
    status = "confirmado ao vivo" if registro["ok"] else "FALHOU ao vivo"
    data = registro["criado_em"][:10]
    titulo = f"{registro['categoria']} — {registro['subtipo']}"
    detalhes_json = json.dumps(registro["detalhes"], indent=2, ensure_ascii=False)

    linhas = [
        f"## N. {titulo} ({status}, {data})",
        "",
        "**Achado:** <preencher — descrever em 1-2 frases o que esse teste confirmou ou",
        "quebrou, e por quê isso importa pra quem usar a skill depois>",
        "",
        f"Rodado pelo painel local (`painel/`), registro #{registro['id']} do histórico",
        "(`painel/historico.db`). Resultado bruto do teste:",
        "",
        "```json",
        detalhes_json,
        "```",
        "",
        "_Rascunho gerado automaticamente — revisar antes de colar em `pegadinhas.md`;",
        "confirmar que não sobrou nenhuma credencial/token no bloco acima antes de commitar._",
    ]
    return "\n".join(linhas)
