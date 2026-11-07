# Tag 00035 — Negociações de compra

4 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/nlq/{recibo}` |  |  |
| POST | `/v1.0/reenviarMensageriaKafka` | Reenvia as negociações para a mensageria ao Kafka |  |
| GET | `/v1.1/negociacoes` | Consultar negociações disponíveis |  |
| POST | `/v1.1/nlq` | Inserir NLQ |  |

## Detalhes

### GET `/v1.0/nlq/{recibo}`

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `recibo` | path | sim | string | recibo para consulta de processamento |

**Respostas:**

- `200`  — **Retorno_ConsultaReciboNLQ_V_1_0** = object { response }

---

### POST `/v1.0/reenviarMensageriaKafka`

**Resumo:** Reenvia as negociações para a mensageria ao Kafka

Reenvia as negociações para a mensageria, informar a "transação" da negociação ou o período de lançamento da negociação, sendo "DataLctoInicial" e "DataLctoFinal" (máximo 30 dias de intervalo)

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `transacao` | query | sim | string | código da transação |
| `dataLctoInicial` | query | sim | string | Data de lançamento inicial da negociação |
| `dataLctoFinal` | query | sim | string | Data de lançamento final da negociação |

**Respostas:**

- `200` Requisição processada com sucesso — **Retorno_reenviarMensageriaKafka_V_1_0** = object { response }

---

### GET `/v1.1/negociacoes`

**Resumo:** Consultar negociações disponíveis

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `unidade` | query | sim | string | código da unidade |
| `datainicial` | query | sim | string | Data Inicial para filtro (dd-mm-yyyy) |
| `datafinal` | query | sim | string | Data Final para filtro (dd-mm-yyyy) |
| `fornecedor` | query | sim | string | Data Inicial para filtro |

**Respostas:**

- `200` Dados carregados com sucesso — **Retorno_ConsultaNegociacoes_V_1_1** = object { response }

---

### POST `/v1.1/nlq`

**Resumo:** Inserir NLQ

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: False):

- **NlqInsert_V_1_1** = object { origemApp, origemVersao, origemIdentificador, CodDcto, usuario, ListProduto }

**Respostas:**

- `200` Dados carregados com sucesso — **Retorno_PostNLQ_V_1_1** = object { response }

---
