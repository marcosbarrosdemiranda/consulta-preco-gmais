# Tag 00011 — Dados referentes a Venda

19 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/pedidos/{CPF_CNPJ}/flex` | Consultar lista de pedidos do cliente no sistema ERP |  |
| GET | `/v1.0/pedidos/{CPF_CNPJ}/flex/{status}` | Consultar lista de pedidos do cliente no sistema ERP |  |
| DELETE | `/v1.0/pedidos/{codigo}` | Excluir Pedido |  |
| PUT | `/v1.0/pedidos/{codigo}/atualizarStatus` | Atualizar status do pedido |  |
| DELETE | `/v1.0/pedidos/{codigo}/item/{codigoItem}` | Excluir Item do Pedido |  |
| GET | `/v1.0/supervisores/{lastID}` | Listar Supervisores |  |
| GET | `/v1.1/pedidos/listaitens/{lastId}` | Consultar itens de pedidos |  |
| GET | `/v1.1/vendedores/{lastID}` | Listar Vendedores |  |
| GET | `/v1.3/pedidos/listapedidos/{lastId}` | Consultar pedidos de venda |  |
| GET | `/v1.4/pedidos/pedidocliente/{codigo}/origem/{origem}` | Consultar processamento do pedido de venda pelo número de pedido do cliente |  |
| GET | `/v1.4/pedidos/{codigo}` | Consultar processamento do pedido de venda |  |
| GET | `/v1.8/pedidos/flex/{codigo}/status` | Consultar status pedido de venda |  |
| GET | `/v1.8/pedidos/listar/status/datamodificacao/{datahora}/lastid/{lastId}` | Consultar status pedido de venda |  |
| GET | `/v1.8/pedidos/status` | Consultar status pedido de venda |  |
| GET | `/v1.8/pedidos/{codigo}/status` | Consultar status pedido de venda |  |
| PUT | `/v2.1/pedidos/{codigo}` | Editar Pedido de Venda |  |
| POST | `/v2.1/pedidos/{codigo}/item` | Inserir novo item ao pedido |  |
| PUT | `/v2.1/pedidos/{codigo}/item/{codigoItem}` | Editar Item do Pedido |  |
| POST | `/v3.3/pedidos` | Inserir Pedido de Venda |  |

## Detalhes

### GET `/v1.0/pedidos/{CPF_CNPJ}/flex`

**Resumo:** Consultar lista de pedidos do cliente no sistema ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF_CNPJ` | path | sim | string | CPF/CNPJ do cliente a ser consultado nos pedidos |
| `codDcto` | query | não | number | Código do documento a ser considerado na resposta do endpoint |

**Respostas:**

- `200` Lista de pedidos — **PedidosClienteFlexResponse** = object { response }

---

### GET `/v1.0/pedidos/{CPF_CNPJ}/flex/{status}`

**Resumo:** Consultar lista de pedidos do cliente no sistema ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF_CNPJ` | path | sim | string | CPF/CNPJ do cliente a ser consultado nos pedidos |
| `status` | path | sim | string | Status dos pedidos de venda a listar |
| `codDcto` | query | não | number | Código do documento a ser considerado na resposta do endpoint |

**Respostas:**

- `200` Lista de pedidos — **PedidosClienteFlexResponse** = object { response }

---

### DELETE `/v1.0/pedidos/{codigo}`

**Resumo:** Excluir Pedido

Excluir pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do pedido de venda |

**Respostas:**

- `200` Pedido excluído com sucesso — **RespostaPadrao** = object { response }

---

### PUT `/v1.0/pedidos/{codigo}/atualizarStatus`

**Resumo:** Atualizar status do pedido

Atualizar status operacional do pedido venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do pedido de venda |

**Request body** (application/json, obrigatório: True):

- **DadoEnvioStatus** = object { status }

**Respostas:**

- `200` Item alterado com sucesso — **RespostaPadrao** = object { response }

---

### DELETE `/v1.0/pedidos/{codigo}/item/{codigoItem}`

**Resumo:** Excluir Item do Pedido

Excluir item do pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do pedido de venda |
| `codigoItem` | path | sim | number | Código do produto |

**Respostas:**

- `200` Item excluido com sucesso — **RespostaExclusaoItem_SemMessage** = object { response }

---

### GET `/v1.0/supervisores/{lastID}`

**Resumo:** Listar Supervisores

Retorna lista de Supervisores

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Na consulta deve-se informar sempre o último ID que foi lido, quando for o inicio da consulta informa-se 0. (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Lista retornada — **ListarSupervisoresResponse** = object { response }

---

### GET `/v1.1/pedidos/listaitens/{lastId}`

**Resumo:** Consultar itens de pedidos

Consultar itens de pedidos, podendo filtrar pelo código de carregamento dos itens

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `carregamento` | query | não | string | Código do carregamento a ser filtrado |

**Respostas:**

- `200`  — **ListaItensPedidosComFiltrosResponse** = object { response }

---

### GET `/v1.1/vendedores/{lastID}`

**Resumo:** Listar Vendedores

Retorna lista de vendedores

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Na consulta deve-se informar sempre o último ID que foi lido, quando for o inicio da consulta informa-se 0. (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Lista retornada — **RespostaListaDeVendedores** = object { response }

---

### GET `/v1.3/pedidos/listapedidos/{lastId}`

**Resumo:** Consultar pedidos de venda

Consultar todos os pedidos de vendas, podendo ser filtrados por data de Inclusão, status, código de Carregamento, código de Rota e código do Pedido do Cliente.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `loadItens` | query | não | boolean | Se informado com valor 'true', será carregado os itens de cada pedido |
| `status` | query | não | string | Filtra os pedidos pelo status, podendo ser B, P ou A |
| `carregamento` | query | não | string | Código do carregamento a ser filtrado |
| `dataInclusao` | query | não | string | Data a ser comparada com a data de movimento do pedido |
| `rota` | query | não | string | Código da rota a ser filtrada |
| `codPedCliente` | query | não | string | Número do pedido do cliente a ser filtrado |
| `codigo` | query | não | string | Filtra pelo código do pedido de venda. |

**Respostas:**

- `200`  — **Response_Pedidos_ListaPedidos_V_1_3** = object { response }

---

### GET `/v1.4/pedidos/pedidocliente/{codigo}/origem/{origem}`

**Resumo:** Consultar processamento do pedido de venda pelo número de pedido do cliente

Consultar processamento da inserção do pedido de venda pelo número de pedido do cliente

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido |
| `origem` | path | sim | string | Identificador de origem do pedido, relacionado ao campo 'Origem' na gravação do pedido |

**Respostas:**

- `200` Status do pedido — **StatusProcessamentoPedidoResponsev3** = object { response }

---

### GET `/v1.4/pedidos/{codigo}`

**Resumo:** Consultar processamento do pedido de venda

Consultar processamento da inserção do pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido |

**Respostas:**

- `200` Status do pedido — **StatusProcessamentoPedidoResponsev4** = object { response }

---

### GET `/v1.8/pedidos/flex/{codigo}/status`

**Resumo:** Consultar status pedido de venda

Consultar o status de um pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido de venda |

**Respostas:**

- `200` Status do pedido retornado — **ConsultarStatusAltPVDResponseV18** = object { response }

---

### GET `/v1.8/pedidos/listar/status/datamodificacao/{datahora}/lastid/{lastId}`

**Resumo:** Consultar status pedido de venda

Consultar o status de um pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `datahora` | path | sim | string | Data e hora da modificação do status do pedido. A data e hora deve estar no formato "dd-MM-yyyy hh:mm:ss" |
| `lastId` | path | sim | string | Código do último pedido de venda consultado. Envie "0" caso queira consultar todos os fornecedores (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Status do pedido retornado — **ConsultarStatusDataModPedidoV18** = object { response }

---

### GET `/v1.8/pedidos/status`

**Resumo:** Consultar status pedido de venda

Consultar o status de um pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `pdv` | query | sim | string | Código do pdv |
| `cupom` | query | sim | string | Cupom |
| `unidade` | query | sim | string | Código da unidade |
| `data` | query | sim | string | Data de movimento formato (dd-MM-yyyy) |

**Respostas:**

- `200` Status do pedido retornado — **ConsultarStatusAltPVDResponseV18** = object { response }

---

### GET `/v1.8/pedidos/{codigo}/status`

**Resumo:** Consultar status pedido de venda

Consultar o status de um pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido de venda |

**Respostas:**

- `200` Status do pedido retornado — **ConsultarStatusAltPVDResponseV18** = object { response }

---

### PUT `/v2.1/pedidos/{codigo}`

**Resumo:** Editar Pedido de Venda

Editar dados do pedido de venda.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do pedido de venda |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV21** = object { unidade, data, codigoCliente, formaPagamento, numeroPedidoCliente, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, email, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, turnoEntrega, dataPrevista, valorFrete, despesaAcessoria, transportador, camposExtras, itens }

**Respostas:**

- `200` Pedido Alterado — **RespostaPadrao_SemMessage** = object { response }

---

### POST `/v2.1/pedidos/{codigo}/item`

**Resumo:** Inserir novo item ao pedido

Inserir um novo item ao pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do pedido de venda |

**Request body** (application/json, obrigatório: True):

- **ItemPedidoV21** = object { codigoProduto, qtdUnitaria, qtdEmbalagem, valorProduto, percDesconto, valorProdFlex }

**Respostas:**

- `200` Item adicionado — **RespostaPadrao_SemMessage** = object { response }

---

### PUT `/v2.1/pedidos/{codigo}/item/{codigoItem}`

**Resumo:** Editar Item do Pedido

Editar item do pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do pedido de venda |
| `codigoItem` | path | sim | number | Código do produto |

**Request body** (application/json, obrigatório: True):

- **ItemPedidoV21** = object { codigoProduto, qtdUnitaria, qtdEmbalagem, valorProduto, percDesconto, valorProdFlex }

**Respostas:**

- `200` Item alterado com sucesso — **RespostaPadrao_SemMessage** = object { response }

---

### POST `/v3.3/pedidos`

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV33** = `PedidoVendaV32` (ver reference/schemas.md) & object { camposExtras, itens, financeiro }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponseSemMessage** = object { response }

---
