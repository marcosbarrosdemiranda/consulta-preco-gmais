# Tag 00041 — Patrimonial

9 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| POST | `/v1.0/patrimonial/auditar` | Auditoria patrimonial |  |
| GET | `/v1.0/patrimonial/bens/classificacao` | Retorna o cadastro de bens patrimoniais |  |
| PUT | `/v1.0/patrimonial/bens/{codigo}` | Alterar um Bem |  |
| POST | `/v1.0/patrimonio/bem/imagens` | Adicionar uma Imagem de um Bem |  |
| PUT | `/v1.0/patrimonio/bem/imagens/{codigo}` | Alterar Imagem de um Bem |  |
| GET | `/v1.0/patrimonio/bem/imagens/{codigo}` | Buscar Imagem do bem |  |
| DELETE | `/v1.0/patrimonio/bem/imagens/{codigo}` | Deleta a Imagem do bem |  |
| GET | `/v1.0/patrimonio/bem/{codigo}/imagens` | Obter codigos digitalizações de um Bem |  |
| GET | `/v1.1/patrimonial/bens` | Retorna o cadastro de bens patrimoniais |  |

## Detalhes

### POST `/v1.0/patrimonial/auditar`

**Resumo:** Auditoria patrimonial

Realiza auditoria patrimonial por data e unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |

**Request body** (application/json, obrigatório: True):

- **v1_0_patrimonial_auditar_requestBody** = object { data, unidade, auditorias }

**Respostas:**

- `200` Requisição processada com sucesso — **v1_0_patrimonial_auditar_response** = object { response }

---

### GET `/v1.0/patrimonial/bens/classificacao`

**Resumo:** Retorna o cadastro de bens patrimoniais

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Requisição processada com sucesso — { response: object { status, appVersion, messages, content } }

---

### PUT `/v1.0/patrimonial/bens/{codigo}`

**Resumo:** Alterar um Bem

Alterar dados referente a um Bem pelo seu código

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | integer | Código do Bem |

**Request body** (application/json, obrigatório: True):

- **bens_update_req_V_1_0** = object { descricao, complemento, funcao, gbenCodigo, numeroserie, plaqueta, codigoncm, ccstRateio, marca, identutil, vctogarantia, corretor, vlsegurado, franquia, vigsegi, vigsegf, apoliceseg, codresponsavel, peso, observacao }

**Respostas:**

- `200` Requisição processada com sucesso — **bens_update_res_V_1_0** = object { response }

---

### POST `/v1.0/patrimonio/bem/imagens`

**Resumo:** Adicionar uma Imagem de um Bem

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: False):

- **imageBens_req_V1_0** = object { codigoBem, fileName, descricao, codigoGrupo, data }

**Respostas:**

- `200` Requisição processada com sucesso — **imageBensPOST_res_V1_0** = object { response }

---

### PUT `/v1.0/patrimonio/bem/imagens/{codigo}`

**Resumo:** Alterar Imagem de um Bem

Alterar dados referente a um Bem pelo seu código

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | integer | Código da Imagem |

**Request body** (application/json, obrigatório: True):

- **imageBens_req_V1_0** = object { codigoBem, fileName, descricao, codigoGrupo, data }

**Respostas:**

- `200` Requisição processada com sucesso — **imageBensPUT_res_V1_0** = object { response }

---

### GET `/v1.0/patrimonio/bem/imagens/{codigo}`

**Resumo:** Buscar Imagem do bem

Busca a imagem do bem pelo codigo da imagem

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | integer | Código da Imagem |

**Respostas:**

- `200`  — 

---

### DELETE `/v1.0/patrimonio/bem/imagens/{codigo}`

**Resumo:** Deleta a Imagem do bem

Deleta a imagem do bem pelo codigo da imagem

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | integer | Código da Imagem |

**Respostas:**

- `200` Requisição processada com sucesso — **imageBensDEL_res_V1_0** = object { response }

---

### GET `/v1.0/patrimonio/bem/{codigo}/imagens`

**Resumo:** Obter codigos digitalizações de um Bem

Retorna os códigos das digitalizações vinculadas a um Bem pelo seu código.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |
| `codigo` | path | sim | integer | Código do Bem |

**Respostas:**

- `200` Requisição processada com sucesso — **imageBensGET_res_V1_0** = object { response }

---

### GET `/v1.1/patrimonial/bens`

**Resumo:** Retorna o cadastro de bens patrimoniais

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | query | não | string | Código do bem |
| `plaqueta` | query | não | string | Número da plaqueta |
| `identificador` | query | não | string | Identificador que pode corresponder o código ou a plaqueta |
| `unidade` | query | não | string | Unidade em que o bem está localizado |
| `lastId` | query | não | number | ID retornado na última requisição para utilizar na paginação (Keyset/Seek Pagination) |
| `limit` | query | não | number | Limite máximo de bens retornados na requisição (Default: Limite configurado) |
| `consulta` | query | não | string | Colocar como true para aplicar os filtros de dos campos habilitados para RP One Mobile |

**Respostas:**

- `200` Requisição processada com sucesso — **bens_V_1_1** = object { response }

---
