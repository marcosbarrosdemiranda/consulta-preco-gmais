# Tag 00029 — Pesquisa de Preços

7 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/flexapp/movpesquisapreco` | Obter dados de pesquisa de preços |  |
| GET | `/v1.0/flexapp/produtounidade/quantreceber` | Consultar quantidade do produto pendente em pedidos de compras |  |
| GET | `/v1.1/flexapp/concorrente` | Recuperar cadastro de concorrentes |  |
| GET | `/v1.2/flexapp/movpesquisa` | Obter dados de pesquisa de preços |  |
| GET | `/v1.2/flexapp/prodpesquisa` | Recuperar produtos para pesquisa de preço |  |
| POST | `/v1.3/flexapp/movpesquisa` | Inserir pesquisa de preços |  |
| GET | `/v1.3/flexapp/movpesquisa` | Obter dados de pesquisa de preços |  |

## Detalhes

### GET `/v1.0/flexapp/movpesquisapreco`

**Resumo:** Obter dados de pesquisa de preços

Obter dados de pesquisa de preços no período informado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `dataInicial` | query | sim | string | Data inicial no padrão dd-mm-yyyy |
| `dataFinal` | query | sim | string | Data final no padrão dd-mm-yyyy |
| `codigo` | query | não | number | Código do produto |
| `unidade` | query | não | string | Unidade |
| `lastId` | query | não | string | Código do último registro retornado, para paginação(se não aplicar este parametro, automaticamente a paginação vem com limit=100) |

**Respostas:**

- `200` Dados processados com sucesso — **RespostaMovPesquisaPreco_V_1_0** = object { response }

---

### GET `/v1.0/flexapp/produtounidade/quantreceber`

**Resumo:** Consultar quantidade do produto pendente em pedidos de compras

Consultar a quantidade do produto em pedidos de compras pendentes

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` | query | sim | string | CNPJ da unidade |
| `codigo` | query | sim | string | Código do produto a ser consultado |

**Respostas:**

- `200`  — **ResponseGetQuantPendPedVenda** = object { response }

---

### GET `/v1.1/flexapp/concorrente`

**Resumo:** Recuperar cadastro de concorrentes

Cadastro de concorrentes

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaGetConcorrentesV1_1** = object { response }

---

### GET `/v1.2/flexapp/movpesquisa`

**Resumo:** Obter dados de pesquisa de preços

Obter dados de pesquisa preços feitas no concorrente

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `dataInicial` | query | sim | string | dataInicial no padrão dd-mm-yyyy |
| `dataFinal` | query | sim | string | dataFinal no padrão dd-mm-yyyy |
| `unidade` | query | não | string | código interno da unidade |
| `ean` | query | não | string | código de barras (EAN) |

**Respostas:**

- `200` Dados processados com sucesso — **RespostaMovPesquisa_V_1_2** = object { response }

---

### GET `/v1.2/flexapp/prodpesquisa`

**Resumo:** Recuperar produtos para pesquisa de preço

Produtos para pesquisa de preço

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaProdPesquisa** = object { response }

---

### POST `/v1.3/flexapp/movpesquisa`

**Resumo:** Inserir pesquisa de preços

Inserir pesquisa de preços feita no concorrente

**Request body** (application/json, obrigatório: True):

- **PesquisaDePrecoV_1_2** = object { itens }

**Respostas:**

- `200` Dados processados com sucesso — **RespostaPesquisaDePreco** = object { response }

---

### GET `/v1.3/flexapp/movpesquisa`

**Resumo:** Obter dados de pesquisa de preços

Obter dados de pesquisa preços feitas no concorrente

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `dataInicial` | query | sim | string | dataInicial no padrão dd-mm-yyyy |
| `dataFinal` | query | sim | string | dataFinal no padrão dd-mm-yyyy |
| `unidade` | query | não | string | código interno da unidade |
| `ean` | query | não | string | código de barras (EAN) |

**Respostas:**

- `200` Dados processados com sucesso — **RespostaMovPesquisa_V_1_2** = object { response }

---
