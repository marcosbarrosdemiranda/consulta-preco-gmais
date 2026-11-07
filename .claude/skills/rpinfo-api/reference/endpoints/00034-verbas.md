# Tag 00034 — Verbas

5 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/verbas/verbas_contratos/lastid/{lastId}` | Recuperar verbas de contratos |  |
| GET | `/v1.0/verbas/verbas_fornecedores` | Recuperar verbas de fornecedores |  |
| GET | `/v1.0/verbas/verbas_fornecedores_pagto` | Recuperar verbas de fornecedores |  |
| GET | `/v1.0/verbas/verbas_produtos` |  |  |
| GET | `/v1.0/verbas/verbas_produtos_pagto` |  |  |

## Detalhes

### GET `/v1.0/verbas/verbas_contratos/lastid/{lastId}`

**Resumo:** Recuperar verbas de contratos

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` |  | não |  |  |
| `dataInicial` | query | não | string | Data Inicial a ser considerada |
| `dataFinal` | query | não | string | Data Final a ser considerada |
| `tipoData` | query | não | string | Tipo da Data a ser considerada. (M = Movimento, B = Baixa) |
| `unidade` | query | não | string | Código ou CNPJ a ser considerado |

**Respostas:**

- `200` Dados carregados com sucesso — **RetornoVerbas_Contratos_V_1_0** = object { response }

---

### GET `/v1.0/verbas/verbas_fornecedores`

**Resumo:** Recuperar verbas de fornecedores

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codVerba` | query | sim | string | Código da verba |
| `contas` | query | sim | string | Contas a serem consideradas, separadas por , |
| `cnpj` | query | sim | string | Cnpj da unidade |
| `dataInicial` | query | sim | string | Data Inicial a ser considerada |
| `dataFinal` | query | sim | string | Data Final a ser considerada |

**Respostas:**

- `200`  — **RetornoVerbas_fornecedores_V_1_0** = object { response }

---

### GET `/v1.0/verbas/verbas_fornecedores_pagto`

**Resumo:** Recuperar verbas de fornecedores

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codVerba` | query | sim | string | Código da verba |
| `contas` | query | sim | string | Contas a serem consideradas, separadas por , |
| `cnpj` | query | sim | string | Cnpj da unidade |
| `dataInicial` | query | sim | string | Data Inicial a ser considerada |
| `dataFinal` | query | sim | string | Data Final a ser considerada |

**Respostas:**

- `200`  — **RetornoVerbas_fornecedores_pagto_V_1_0** = object { verbas }

---

### GET `/v1.0/verbas/verbas_produtos`

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` | query | sim | string | Cnpj da unidade |
| `dataInicial` | query | sim | string | Data Inicial a ser considerada |
| `dataFinal` | query | sim | string | Data Final a ser considerada |

**Respostas:**

- `200`  — **RetornoVerbas_Produtos_V_1_0** = object { response }

---

### GET `/v1.0/verbas/verbas_produtos_pagto`

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` | query | sim | string | Cnpj da unidade |
| `dataInicial` | query | sim | string | Data Inicial a ser considerada |
| `dataFinal` | query | sim | string | Data Final a ser considerada |

**Respostas:**

- `200`  — **RetornoVerbas_produtos_pagto_V_1_0** = object { response }

---
