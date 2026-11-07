# Tag 00013 — Dados referentes a Etiquetas de preço

2 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| POST | `/v1.1/produtounidade/unidade/{CNPJ}/atualizaretiquetaprecos` | Atualizar etiqueta de preços |  |
| GET | `/v1.2/produtounidade/{lastID}/unidade/{CNPJ}/etiquetaspendentes/{campoConsiderar}` | Consultar etiquetas pendentes |  |

## Detalhes

### POST `/v1.1/produtounidade/unidade/{CNPJ}/atualizaretiquetaprecos`

**Resumo:** Atualizar etiqueta de preços

Atualizar etiqueta de preços da unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CNPJ` | path | sim | string | CNPJ da unidade |

**Request body** (application/json, obrigatório: True):

- **AtualizarEtiquetasPost_V_1_1** = object { etiquetas }

**Respostas:**

- `200` Etiquetas atualizadas — **RespostaPadrao** = object { response }

---

### GET `/v1.2/produtounidade/{lastID}/unidade/{CNPJ}/etiquetaspendentes/{campoConsiderar}`

**Resumo:** Consultar etiquetas pendentes

Consultar etiquetas pendentes da unidade

O retorno será paginado, com número de itens definido em configuração do serviço.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do produto que retornou da lista. Para solicitar a primeira página de informações, enviar :lastID igual a zero.  (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `campoConsiderar` | path | sim | string | Preço a ser considerado  Possíveis valores: PRECO_PDV, PRECO_VENDA |

**Respostas:**

- `200` Etiquetas pendentes retornadas — **EtiquetasPendentesResponse_V_1_2** = object { response }

---
