# Tag 00019 — Programação de Preços

3 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/programacaoprecos` | Listar programações de preços |  |
| GET | `/v1.0/programacaoprecos/listarprogramacoes/datainicio/{dataInicio}/datafim/{dataFim}/unidade/{cnpj}` | Obter programação de preço |  |
| POST | `/v1.1/programacaoprecos` | Inserir uma ou várias novas Programações de Preços |  |

## Detalhes

### GET `/v1.0/programacaoprecos`

**Resumo:** Listar programações de preços

Consulta as programações de preços cadastradas, com suporte à paginação por release.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação. |
| `release` | query | sim | number | Código do último release consultado. Envie "0" para iniciar a consulta desde o primeiro registro. Os resultados são retornados de forma paginada. |
| `limit` | query | não | number | Quantidade máxima de registros retornados por página. |

**Respostas:**

- `200` Dados carregados com sucesso. — **ResponseProgramacaoPrecosReleaseV_1_0** = object { response }

---

### GET `/v1.0/programacaoprecos/listarprogramacoes/datainicio/{dataInicio}/datafim/{dataFim}/unidade/{cnpj}`

**Resumo:** Obter programação de preço

Consulta dados referentes a programação de preço.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `dataInicio` | path | sim | string | Data de ínicio da programação.  (Formato 'dd-mm-yyyy') |
| `dataFim` | path | sim | string | Data final da programação.  (Formato 'dd-mm-yyyy') |
| `cnpj` | path | sim | string | CNPJ da unidade a consultar |

**Respostas:**

- `200` Dados carregados — **ConsultaProgramaPreco** = object { response }

---

### POST `/v1.1/programacaoprecos`

**Resumo:** Inserir uma ou várias novas Programações de Preços

Inserir uma ou várias novas Programações de Preços.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **InserirProgramacoesPrecos** = object { programacoes }

**Respostas:**

- `200` Resposta de cada objeto de programação diferenciado pelo id enviado, Sucessos e erros serão diferenciados pelo atributo 'status' (Ok ou Erro) — **InserirProgramasPrecosResponseV1_1** = object { response }

---
