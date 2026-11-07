# Tag 00042 — Tributação

5 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| POST | `/v1.0/tributacao` | Incluir Tributação |  |
| GET | `/v1.0/tributacao/hashes/inconsistentes` | Processa todos os hashes inconsistentes |  |
| GET | `/v1.0/tributacao/hashes/recibo/{recibo}` | Consulta recibo dos hashes inconsistentes |  |
| GET | `/v1.0/tributacao/release/{release}` | Buscar grade tributária a partir do release |  |
| GET | `/v1.0/tributacao/valtrib/lastexec` | Retorno da Data/hora de ultima execução |  |

## Detalhes

### POST `/v1.0/tributacao`

**Resumo:** Incluir Tributação

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **ReqInsertTributacao_V_1_0** = `Tributacao_V_1_0` (ver reference/schemas.md)

**Respostas:**

- `200` Tributação incluída — **ResponseInsertTributacao_V_1_0** = object { response }

---

### GET `/v1.0/tributacao/hashes/inconsistentes`

**Resumo:** Processa todos os hashes inconsistentes

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Requisição processada com sucesso — **ResponseTribHashesInconsistentes_V_1_0** = object { response }

---

### GET `/v1.0/tributacao/hashes/recibo/{recibo}`

**Resumo:** Consulta recibo dos hashes inconsistentes

Consulta o recibo gerado pelo endpoint de processar hashes inconsistentes e apresenta um array com todos os controles inconsistentes.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `recibo` | path | sim | string | Código do recibo que foi gerado no endpoint de processar hashes inconsistentes |

**Respostas:**

- `200` Requisição processada com sucesso — **ResponseTribHashesConsultaReciboOk_V_1_0** = object { response }
- `206` Requisição processada com sucesso — **ResponseTribHashesConsultaReciboPartial_V_1_0** = object { response }

---

### GET `/v1.0/tributacao/release/{release}`

**Resumo:** Buscar grade tributária a partir do release

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `release` | path | sim | number | Código do último release consultado. Envie "0" caso queira consultar todos os releases (mesmo passando 0 os dados retornam paginados) |
| `limit` | query | não | number | Número de dados retornados por página |

**Respostas:**

- `200` Requisição processada com sucesso — **ResponseTribRelease_V_1_0** = object { response }

---

### GET `/v1.0/tributacao/valtrib/lastexec`

**Resumo:** Retorno da Data/hora de ultima execução

Retorno da Data/hora de ultima execução da validação tributária

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Requisição processada com sucesso — **ResponseTribLastExec_V_1_0** = object { response }

---
