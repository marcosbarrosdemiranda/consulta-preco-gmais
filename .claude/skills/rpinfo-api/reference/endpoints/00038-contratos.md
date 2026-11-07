# Tag 00038 — Contratos

3 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| PUT | `/v1.0/contratos/registrarAceite` | Registra o Aceite da regra do contrato |  |
| GET | `/v1.0/contratos/regras` | Obter lista de regras dos contratos |  |
| GET | `/v1.0/contratos/variaveis` | Obter lista de variáveis de contratos |  |

## Detalhes

### PUT `/v1.0/contratos/registrarAceite`

**Resumo:** Registra o Aceite da regra do contrato

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |

**Request body** (application/json, obrigatório: True):

- **Request_Contratos_BaixarRegra_V_1_0** = object { id, dataHora, nomeResponsavel }

**Respostas:**

- `200` Regra do contrato atualizada. — **Response_Contratos_BaixarRegra_V_1_0** = object { content }

---

### GET `/v1.0/contratos/regras`

**Resumo:** Obter lista de regras dos contratos

Consulta dados referente as regras dos contratos.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |
| `datainicial` | query | sim | string | Data inicial do período. Formato (DD-MM-YYYY) |
| `datafinal` | query | sim | string | Data final do período. Formato (DD-MM-YYYY) |

**Respostas:**

- `200` Requisição processada com sucesso — **Response_Contratos_Regras_V_1_0** = object { response }

---

### GET `/v1.0/contratos/variaveis`

**Resumo:** Obter lista de variáveis de contratos

Consulta dados referente aos contratos.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Dados carregados com sucesso — **Retorno_Contratos_Variaveis_V_1_0** = object { response }

---
