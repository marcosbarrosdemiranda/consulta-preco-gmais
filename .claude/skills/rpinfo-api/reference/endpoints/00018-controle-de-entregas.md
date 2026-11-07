# Tag 00018 — Controle de Entregas

7 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| PUT | `/v1.0/controleentregas` | Controle de entrega |  |
| PUT | `/v1.0/controleentregas/editar` | Editar entrega existente |  |
| GET | `/v1.0/controleentregas/pendentes` | Consultar entregas pendentes |  |
| PUT | `/v1.1/controleentregas/baixa` | Baixar entrega |  |
| GET | `/v1.1/controleentregas/lastid/{lastId}` | Consultar entregas com suporte a lastId |  |
| GET | `/v1.1/controleentregas/{transacao}` | Obter Controle de entrega |  |
| POST | `/v1.3/controleentregas` | Controle de entrega |  |

## Detalhes

### PUT `/v1.0/controleentregas`

**Resumo:** Controle de entrega

Alterar status do controle de entrega

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **AlterarStatusControleEntrega** = object { transacao, status, statusOperacional }

**Respostas:**

- `200` Status do Controle de entrega atualizado com sucesso — **RespostaUpdateStatusControleEntrega** = object { response }

---

### PUT `/v1.0/controleentregas/editar`

**Resumo:** Editar entrega existente

Permite editar os dados de uma entrega já inserida no ERP. Campos como transação, cliente e data de venda não podem ser alterados.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |

**Request body** (application/json, obrigatório: True):

- **EditarEntrega** = object { transacao, bairro, cidade, observacao1, fone, valor, kmFim, veiculo }

**Respostas:**

- `200` Entrega atualizada com sucesso — **EditarEntregasV_1_0** = object { response }

---

### GET `/v1.0/controleentregas/pendentes`

**Resumo:** Consultar entregas pendentes

Consulta todas as entregas pendentes

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |

**Respostas:**

- `200` Requisição processada com sucesso — **ResponseControleEntregasPendentes** = object { response }

---

### PUT `/v1.1/controleentregas/baixa`

**Resumo:** Baixar entrega

Realiza a baixa da entrega com atualização de status, data, hora e entregador

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |

**Request body** (application/json, obrigatório: True):

- **ResquestBaixaEntregaV1_1** = object { transacao, Entregador, quilometragem, observacao, dataHora }

**Respostas:**

- `200` Entrega baixada com sucesso — **BaixaEntregasV1_1** = object { response }

---

### GET `/v1.1/controleentregas/lastid/{lastId}`

**Resumo:** Consultar entregas com suporte a lastId

Consulta todas ou parte das entregas gravadas no ERP usando paginação por lastId

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |
| `lastId` | path | sim | integer | Último ID conhecido. Use 0 para retornar todas as entregas. |
| `status` | query | não | integer | Filtro por status da entrega. Use "P" para entregas pendentes, "N" para entregas normais, Use "B" para entregas baixadas e "C" para entregas canceladas. |

**Respostas:**

- `200` Entregas carregadas com sucesso — **ListaEntregasV_1_0** = object { response }

---

### GET `/v1.1/controleentregas/{transacao}`

**Resumo:** Obter Controle de entrega

Consulta dados referentes ao Controle de entrega.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `transacao` | path | sim | string | Transação do Controle de entrega. |

**Respostas:**

- `200` Dados carregados — **ConsultaControleEntregaV1_1** = object { response }

---

### POST `/v1.3/controleentregas`

**Resumo:** Controle de entrega

Gravar controle de entrega

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **ControleEntregaV13** = object { transacao, status, statusOperacional, data, dataVenda, codEntregador, unidade, cliente, bairro, cidade, endereco, complemento, nome, fone, valor, pdv, volumes, cupom, observacao1, observacao2, hora, referencia, numeroCaixas, dataBaixa, enderecoNumero, enderecoCep, veiculo, kmInicio, kmFim, idNfe, horaVenda, codigoAgenda, valorCupom }

**Respostas:**

- `200` Controle de entrega gravado com sucesso — **ControleEntregaResponseSemMessage** = object { response }

---
