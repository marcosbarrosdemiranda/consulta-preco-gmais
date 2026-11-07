# Tag 00033 — Consulta de Cadastro de Carregamentos

2 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/carregamentos/lastid/{lastid}` | Consultar cadastro de carregamentos |  |
| GET | `/v1.0/carregamentos/{codigo}` | Consultar cadastro de um carregamento |  |

## Detalhes

### GET `/v1.0/carregamentos/lastid/{lastid}`

**Resumo:** Consultar cadastro de carregamentos

Consultar cadastro de carregamentos de forma paginada.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastid` | path | sim | string | Código do último carregamento ou 0. |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaCarregamentos** = object { response }

---

### GET `/v1.0/carregamentos/{codigo}`

**Resumo:** Consultar cadastro de um carregamento

Consultar cadastro de um carregamento.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do carregamento a ser pesquisado. |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaCarregamento** = object { response }

---
