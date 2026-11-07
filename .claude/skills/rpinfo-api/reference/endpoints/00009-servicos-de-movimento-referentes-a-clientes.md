# Tag 00009 — Serviços de movimento referentes a clientes

14 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| POST | `/v1.0/clientes/alterarsenha` | Atualizar senha do cliente |  |
| POST | `/v1.0/clientes/{CPF_CNPJ}/baixarpontos/unidade/{unidade}` | Baixar pontos do cliente |  |
| POST | `/v1.0/clientes/{CPF_CNPJ}/cancelarbaixa/unidade/{unidade}` | Cancelar baixa da unidade |  |
| GET | `/v1.0/clientes/{CPF_CNPJ}/extratopontos/datainicial/{datainicial}/datafinal/{datafinal}` | Consultar pontos |  |
| POST | `/v1.0/clientes/{CPF_CNPJ}/gerarpontos/unidade/{CNPJ}` | Gerar pontos |  |
| GET | `/v1.0/clientes/{CPF_CNPJ}/saldopontos` | Obter dados de extrato de pontos do cliente |  |
| GET | `/v1.0/clientes/{CPF_CNPJ}/vendas/datainicial/{dataini}/datafinal/{datafim}` | Consultar vendas |  |
| POST | `/v1.0/descontos/incluir` | Inserção de registros na TabDescontos |  |
| GET | `/v1.0/descontos/listar/lastid/{lastId}` | Listar dados de Descontos |  |
| GET | `/v1.0/extrato/cliente/{CNPJ_CPF}/{dataInicial}/{dataFinal}/{CNPJ}` | Obter extrato do cliente |  |
| POST | `/v1.0/packvirtual` | Inserir PackVirtual |  |
| GET | `/v1.0/packvirtual/listar/lastid/{lastId}` | Listar dados de PackVirtual |  |
| GET | `/v1.0/veiculos/cliente/{codigo}` | Consultar placas de veículos de um cliente |  |
| GET | `/v1.0/veiculos/placa/{placa}` | Consultar cliente por placa de veículo |  |

## Detalhes

### POST `/v1.0/clientes/alterarsenha`

**Resumo:** Atualizar senha do cliente

Atualizar senha do cliente pelo CPNJ/CPF

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **AlterarSenhaClientePost** = object { cliente, senha }

**Respostas:**

- `200` Senha alterada com sucesso — **RespostaPadrao** = object { response }

---

### POST `/v1.0/clientes/{CPF_CNPJ}/baixarpontos/unidade/{unidade}`

**Resumo:** Baixar pontos do cliente

Baixar pontos do cliente pelo CPF/CNPJ e unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF_CNPJ` | path | sim | string | CPF/CNPJ do cliente |
| `unidade` | path | sim | string | Unidade do cliente |

**Request body** (application/json, obrigatório: True):

- **BaixarPontosCliente** = object { Valor, Pdv, Cupom }

**Respostas:**

- `200` Extrato de pontos — **RespostaBaixaCancelada** = object { response }

---

### POST `/v1.0/clientes/{CPF_CNPJ}/cancelarbaixa/unidade/{unidade}`

**Resumo:** Cancelar baixa da unidade

Cancelar baixa

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF_CNPJ` | path | sim | string | CNPJ/CPF do cliente |
| `unidade` | path | sim | string | Unidade a ser cancelado a baixa |

**Request body** (application/json, obrigatório: True):

- **CalcelarBaixa** = object { Transacao }

**Respostas:**

- `200` Baixa cancelada — **RespostaBaixaCancelada** = object { response }

---

### GET `/v1.0/clientes/{CPF_CNPJ}/extratopontos/datainicial/{datainicial}/datafinal/{datafinal}`

**Resumo:** Consultar pontos

Consultar pontos do cliente pelo CPNJ/CPF

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF_CNPJ` | path | sim | string | CNPJ/CPF do cliente |
| `datainicial` | path | sim | string | Data inicial do período (Formato dd-mm-yyyy) |
| `datafinal` | path | sim | string | Data final do período (Formato dd-mm-yyyy) |

**Respostas:**

- `200` Pontos do cliente recuperados — **ConsultarExtratoPontosResponse** = object { response }

---

### POST `/v1.0/clientes/{CPF_CNPJ}/gerarpontos/unidade/{CNPJ}`

**Resumo:** Gerar pontos

Gerar pontos para o cliente

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF_CNPJ` | path | sim | string | CNPJ/CPF do cliente |
| `CNPJ` | path | sim | string | CNPJ da unidade que serão gerados os pontos |

**Request body** (application/json, obrigatório: True):

- **PontosPost** = object { Pontos }

**Respostas:**

- `200` Pontos do cliente gerados — **RespostaPadrao** = object { response }

---

### GET `/v1.0/clientes/{CPF_CNPJ}/saldopontos`

**Resumo:** Obter dados de extrato de pontos do cliente

Obter dados de extrato de pontos do cliente pelo CPF/CNPJ

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF_CNPJ` | path | sim | string | CPF/CNPJ do cliente |

**Respostas:**

- `200` Extrato de pontos — **ResponsePontosCliente** = object { response }

---

### GET `/v1.0/clientes/{CPF_CNPJ}/vendas/datainicial/{dataini}/datafinal/{datafim}`

**Resumo:** Consultar vendas

Consultar vendas para um determinado cliente

O período de consulta não pode exceder 90 dias

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF_CNPJ` | path | sim | string | CPF/CNPJ do cliente |
| `dataini` | path | sim | string | Data inicial da consulta (Formato "dd-mm-yyyy") |
| `datafim` | path | sim | string | Data final da consulta (Formato "dd-mm-yyyy") |

**Respostas:**

- `200` Vendas retornadas — **ConsultarVendasClienteResponse** = object { response }

---

### POST `/v1.0/descontos/incluir`

**Resumo:** Inserção de registros na TabDescontos

Inserção de registros na TabDescontos.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **Request_Descontos_Incluir_V_1_0** = object { webService, codBarra, valorMin, valorMinCupom, percentual, unidades, dataInicial, dataFinal, descricao, preco, finValidas, finInvalidas, qtdMaxima, qtdMinima, valorMaxDesconto, fatorDiv, qtdFatorDiv, fatorDivSub, tipoCliente, tipoClienteCrm, tipoDesconto, utilPreco2, igrPrecoDif, prodOferta, grupos, marcas, rcrCodigo, valorDesconto, produtoSbt, qtdFatorDivSbt, produtoOfVId, codBarrasVld, gruposVld, codIntoOferta, codAgof, permedicao, titulo, linha1, linha2, linha3, rgFixa, qtdMaxImaVld, qtdMaxImaCli, horaInicial, horaFinal, itensPartVlrMin, gruposInvalidos, dataHoraManutencao }

**Respostas:**

- `200` Dados adicionados com sucesso — **Response_Descontos_Incluir_V_1_0** = object { content }

---

### GET `/v1.0/descontos/listar/lastid/{lastId}`

**Resumo:** Listar dados de Descontos

Listar dados de Descontos da tabela TabDescontos

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `unidade` | query | não | string | Código da(s) unidade(s) (Para mais de uma unidade utilize ';' como separador) |
| `datainicial` | query | sim | string | Data Final do período (Formato "dd-mm-yyyy") |
| `datafinal` | query | sim | string | Data Final do período (Formato "dd-mm-yyyy") |
| `lastId` | path | sim | string | Código do último desconto consultado. Envie "0" caso queira consultar todos os descontos (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados com sucesso — **Response_Descontos_Listar_V_1_0** = object { response }

---

### GET `/v1.0/extrato/cliente/{CNPJ_CPF}/{dataInicial}/{dataFinal}/{CNPJ}`

**Resumo:** Obter extrato do cliente

Obter dados do cliente em determinada data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CNPJ_CPF` | path | sim | string | CPF/CNPJ do cliente |
| `dataInicial` | path | sim | string | Data Inicial do período (Formato "dd-mm-yyyy") |
| `dataFinal` | path | sim | string | Data Final do período (Formato "dd-mm-yyyy") |
| `CNPJ` | path | sim | string | CNPJ da matriz, retornará pendências de todas as unidades da empresa |

**Respostas:**

- `200` Extrato do cliente — **ExtratoResponse** = object { response }

---

### POST `/v1.0/packvirtual`

**Resumo:** Inserir PackVirtual

Inserir dados de PackVirtual da tabela PackVirtual C e D

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: False):

- **Request_PackVirtual_V_1_0** = object { dataInicial, dataFinal, unidCodigo, prodCodigo, prvenda, quantidade, tipo, unidades, descritivo, desconto, alteracao, qtdLimite, produtos, tiposCli, valorUnitCli, codintOferta, tiposCliCrm, webService, tipoRegra, permaCresFc, finValidas, binsValidos, diasSemana, tiposCliZoombox, descricao, detalhes }

**Respostas:**

- `200` Pack virtual criado com sucesso! — **Response_PackVirtual_Post_V_1_0** = object { response }

---

### GET `/v1.0/packvirtual/listar/lastid/{lastId}`

**Resumo:** Listar dados de PackVirtual

Listar dados de PackVirtual da tabela PackVirtual C e D

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `unidade` | query | não | string | Código da(s) unidade(s) (Para mais de uma unidade utilize ';' como separador) |
| `datainicial` | query | sim | string | Data Final do período (Formato "dd-mm-yyyy") |
| `datafinal` | query | sim | string | Data Final do período (Formato "dd-mm-yyyy") |
| `lastId` | path | sim | string | Código do último desconto consultado. Envie "0" caso queira consultar todos os descontos (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados com sucesso — **Response_PackVirtual_Listar_V_1_0** = object { response }

---

### GET `/v1.0/veiculos/cliente/{codigo}`

**Resumo:** Consultar placas de veículos de um cliente

Consultar placas de veículos associado a um cliente

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Codigo do cliente |

**Respostas:**

- `200` Placas de veículos associados ao cliente — **ConsultarPlacasVeiculosClienteResponse** = object { response }

---

### GET `/v1.0/veiculos/placa/{placa}`

**Resumo:** Consultar cliente por placa de veículo

Consultar código de cliente associado a um veículo, pesquisando por placa

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `placa` | path | sim | string | Codigo do cliente |

**Respostas:**

- `200` Cliente associado à placa — **ConsultarClientePlacaVeiculoReponde** = object { response }

---
