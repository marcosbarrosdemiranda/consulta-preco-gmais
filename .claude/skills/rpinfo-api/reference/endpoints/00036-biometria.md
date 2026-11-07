# Tag 00036 — Biometria

2 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| POST | `/v1.0/biometria` | Cadastrar biometria de entidades |  |
| GET | `/v1.0/biometrias/lastid/{lastid}` | Listar todas as biometrias |  |

## Detalhes

### POST `/v1.0/biometria`

**Resumo:** Cadastrar biometria de entidades

Cadastrar ou edita biometria de entidades pelo código, categoriaEntidade, dedo e equipamento

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: False):

- **biometriasReqBodyArray** = array de `biometriasReqBody` (ver reference/schemas.md)

**Respostas:**

- `200` Biometria gravada com sucesso — **biometriasRes** = object { response }

---

### GET `/v1.0/biometrias/lastid/{lastid}`

**Resumo:** Listar todas as biometrias

Lista todas as biometrias disponíveis

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastid` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `categoria` | query | não | string | Categoria a ser considerada (C - Cliente, F - Fornecedor, I - Funcionário, U - Unidades, V - Vinculado, P - Promotor). Para selecionar mais de uma categoria utilize ";" como separador |
| `entidade` | query | não | number | Código da entidade a ser considerado |
| `dispositivo` | query | não | string | Equipamento utilizado no scan das biometrias |
| `dataHora` | query | não | string | Data e Hora da manutenção da biometria (dd-mm-yyyy hh:MM:ss) |
| `limit` | query | não | string | Limite de biometrias retornadas por consulta/página |

**Respostas:**

- `200` Biometrias carregadas com sucesso — **RespostaListarBiometrias_V_1_0** = object { response }

---
