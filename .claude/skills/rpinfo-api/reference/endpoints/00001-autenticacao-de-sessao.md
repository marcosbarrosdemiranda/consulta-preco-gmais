# Tag 00001 — Autenticação de sessão

2 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.1/logout` | Efetuar logout |  |
| POST | `/v1.2/auth` | Autenticar sessão |  |

## Detalhes

### GET `/v1.1/logout`

**Resumo:** Efetuar logout

Limpar o cache e invalidar o token

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Logout efetuado — **RespostaPadrao_SemMessage** = object { response }

---

### POST `/v1.2/auth`

**Resumo:** Autenticar sessão

Autenticar sessão com usuário e senha

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `origem` | query | não | string | Nome do aplicativo mapeado pelo ERP ('RPONEMOBILE' e 'RPCOLLECT') |
| `versao` | query | não | string | Versão do aplicativo (Ex 5.05.24) |

**Request body** (application/json, obrigatório: True):

- **AutenticarSessao** = object { usuario, senha }

**Respostas:**

- `200` Sessão autenticada — **RespostaAutenticacao_V_1_1** = object { response }

---
