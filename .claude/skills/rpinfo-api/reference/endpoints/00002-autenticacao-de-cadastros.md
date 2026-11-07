# Tag 00002 — Autenticação de cadastros

3 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| POST | `/v1.0/auth/cliente` | Autenticar cliente |  |
| POST | `/v1.0/auth/funcionario` | Autenticar funcionário |  |
| POST | `/v1.0/auth/usuario` | Autenticar usuário |  |

## Detalhes

### POST `/v1.0/auth/cliente`

**Resumo:** Autenticar cliente

Autenticar dados do cliente

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **AutenticarClientePost** = object { cliente, senha }

**Respostas:**

- `200` Cliente autenticado — **RespostaPadrao** = object { response }

---

### POST `/v1.0/auth/funcionario`

**Resumo:** Autenticar funcionário

Autenticar funcionário pelo CPF

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **AutenticarFuncionarioPost** = object { funcionario, senha }

**Respostas:**

- `200` Funcionário autenticado — **RespostaPadrao** = object { response }

---

### POST `/v1.0/auth/usuario`

**Resumo:** Autenticar usuário

Autenticar usuário do ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **AutenticarPost** = `AutenticarSessao` (ver reference/schemas.md)

**Respostas:**

- `200` Usuário autenticado — **RespostaPadrao** = object { response }

---
