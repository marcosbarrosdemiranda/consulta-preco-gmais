# Tag 00046 — Historicos

1 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/historicos` | Recuperar dados do historico |  |

## Detalhes

### GET `/v1.0/historicos`

**Resumo:** Recuperar dados do historico

Recuperar dados por ID do historico

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | query | não | number | Codigo opcional para recuperar historicos cadastrados |

**Respostas:**

- `200`  — **ResponseHistoricov1** = object { response }

---
