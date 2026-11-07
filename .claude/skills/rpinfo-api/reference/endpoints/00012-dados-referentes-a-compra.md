# Tag 00012 — Dados referentes a Compra

12 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| PUT | `/v1.0/pedidocompra/devolucao/codigo/{codigo}` | Listar itens de um pedido de compra para devolução |  |
| POST | `/v1.0/pedidocompra/inserir` | Inserir pedido de compra |  |
| GET | `/v1.0/pedidocompra/lastrelease/{lastrelease}` | Listar pedidos de compra |  |
| GET | `/v1.0/pedidocompra/minrelease` | Retornar último código |  |
| GET | `/v1.0/pedidocompra/transacao` | Listar pedidos de compra |  |
| GET | `/v1.1/lotercm/notassemrcm` | Listar notas fiscais sem recebimento |  |
| GET | `/v1.1/lotercm/pedidossemrcm` | Listar pedidos de compra sem Recebimento |  |
| GET | `/v2.3/pedidocompra/chave/{chaveNfe}` | Listar pedidos de compra |  |
| GET | `/v2.3/pedidocompra/listarpedidos/pedidossemrcm/lastid/{lastID}/fornecedor/{cnpj}/unidade/{cnpjUnid}/datainicial/{dataInicial}/datafinal/{dataFinal}/vinc/{vinc}` | Listar pedidos de compra sem Recebimento |  |
| GET | `/v2.4/pedidocompra` | obter dados do pedido de compra |  |
| GET | `/v2.4/pedidocompra/listarpedidos/lastid/{lastID}` | Listar pedidos de compra |  |
| GET | `/v2.4/pedidocompra/{codigo}` | obter dados do pedido de compra |  |

## Detalhes

### PUT `/v1.0/pedidocompra/devolucao/codigo/{codigo}`

**Resumo:** Listar itens de um pedido de compra para devolução

Marcar itens de um pedido de compra para devolução

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido de compra |

**Request body** (application/json, obrigatório: True):

- **PedidoCompraDevolucaoLV10** = object { itens }

**Respostas:**

- `200` Lista de itens marcados para devolução — **RespPedCompraDevolucaoLV10** = object { response }

---

### POST `/v1.0/pedidocompra/inserir`

**Resumo:** Inserir pedido de compra

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoCompra_Inserir_Req_V_1_0** = object { tipo, dctoCodigo, dataMvto, unidLcto, unidDest, usuaCodigo, fornCodigo, fpgtCodigo, espeCodigo, valor, tpFrete, percFrete, adicFinanc, despAcess, prazo, dtPrev, obs, tranCodigo, pedForn, formaDescarga, negTrocas, abatimentos, acrescimos, autorizacao, dataVencimento, itens }

**Respostas:**

- `200` Pedido de compra inserido — **PedidoCompra_Inserir_res_V_1_0** = object { response }

---

### GET `/v1.0/pedidocompra/lastrelease/{lastrelease}`

**Resumo:** Listar pedidos de compra

Listar pedidos de compra por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastrelease` | path | sim | number | Código do pedido de compra |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedidoCompra_LastRelease_V_1_0** = object { response }

---

### GET `/v1.0/pedidocompra/minrelease`

**Resumo:** Retornar último código

Retornar último código com base em uma data de movimento ou baixa

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `datamovimento` | query | sim | string | Data de movimento a ser considerada. |
| `databaixa` | query | sim | string | Data da baixa a ser considerada. |

**Respostas:**

- `200` Content — { content: number ex: 111 }

---

### GET `/v1.0/pedidocompra/transacao`

**Resumo:** Listar pedidos de compra

Listar pedidos de compra por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `tipo` | query | sim | string | Tipo de transação ("I - Transação de inclusão", "B - Transação de Baixa" ou "E - Transação de Entrada") |
| `transacao` | query | sim | string | Número da transação |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseV14** = object { response }

---

### GET `/v1.1/lotercm/notassemrcm`

**Resumo:** Listar notas fiscais sem recebimento

Listar notas fiscais sem recebimento por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `documento` | query | sim | number | Código do documento RCM |
| `unidade` | query | sim | string | Unidade/loja de destino do pedido de compra |
| `entidades` | query | sim | string | Entidade refere-se ao código da entidade que pode ser um ou vários fornecedores/unidades, os valores podem ser passados separados por vírgula |

**Respostas:**

- `200` Notas fiscais retornadas — **NotasSemRCMResponse_V_1_01** = object { response }

---

### GET `/v1.1/lotercm/pedidossemrcm`

**Resumo:** Listar pedidos de compra sem Recebimento

Listar pedidos de compra sem recebimento por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `documento` | query | sim | number | Código do documento RCM |
| `unidade` | query | sim | string | Unidade/loja de destino do pedido de compra |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraSemRCMResponse_V_1_00** = object { response }

---

### GET `/v2.3/pedidocompra/chave/{chaveNfe}`

**Resumo:** Listar pedidos de compra

Listar pedidos de compra por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `chaveNfe` | path | sim | number | Chave da Nota fiscal eletrônica do pedido de compra |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseV23** = object { response }

---

### GET `/v2.3/pedidocompra/listarpedidos/pedidossemrcm/lastid/{lastID}/fornecedor/{cnpj}/unidade/{cnpjUnid}/datainicial/{dataInicial}/datafinal/{dataFinal}/vinc/{vinc}`

**Resumo:** Listar pedidos de compra sem Recebimento

Listar pedidos de compra sem recebimento por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `cnpj` | path | sim | string | Cnpj do fornecedor do pedido |
| `cnpjUnid` | path | sim | string | Cnpj da unidade do pedido, se passado 999 retorna pedidos de todas as unidades |
| `dataInicial` | path | sim | string | Data em que inicia-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `dataFinal` | path | sim | string | Data em que finaliza-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `vinc` | path | sim | string | Indicar se a rota deve buscar os pedidos dos fornecedores vinculados (deve-se utilizar valores SIM ou NAO) |
| `apenasBaixados` | query | não | boolean | Retorna apenas os pedidos baixados (Valores válidos: True/False) |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseLV23** = object { response }

---

### GET `/v2.4/pedidocompra`

**Resumo:** obter dados do pedido de compra

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | query | não | number | Código do pedido de compra ( pcpc_codigo ) |
| `numPed` | query | não | number | Número do pedido de compra ( pcpc_numPed ) |
| `idNfe` | query | não | string | Chave da nota do pedido de compra ( pcpc_idNfe ) |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseV24** = object { response }

---

### GET `/v2.4/pedidocompra/listarpedidos/lastid/{lastID}`

**Resumo:** Listar pedidos de compra

Listar pedidos de compra por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `dataInicial` | query | não | string | Data em que inicia-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `dataFinal` | query | não | string | Data em que encerra-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `dataInicialBaixa` | query | não | string | Data em que inicia-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `dataFinalBaixa` | query | não | string | Data em que encerra-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `unidade` | query | não | string | Código da unidade de destino do pedido de compra |
| `status` | query | sim | string | Informar um dos seguintes valores, "P" para Pendentes, "B" para Baixados ou "C" para Cancelados |
| `fornecedor` | query | não | string | Código do fornecedor do pedido de compra |
| `vinculados` | query | não | boolean | Indica se deve considerar fornecedores vinculados ao fornecedor informado |
| `autorização` | query | não | string | Informar um dos seguintes valores, "P" para Pendentes, "A" para autorizados. |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseLV23** = object { response }

---

### GET `/v2.4/pedidocompra/{codigo}`

**Resumo:** obter dados do pedido de compra

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido de compra |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseV24** = object { response }

---
