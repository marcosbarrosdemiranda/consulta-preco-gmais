# Tag 00023 — Documentos

12 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| PUT | `/v1.0/documento/cancelar` | Cancelar transação |  |
| GET | `/v1.0/documento/config/{codigo}` | Obter os dados da configuração de um documento |  |
| GET | `/v1.0/documento/consultarrecibo/{recibo}` | Cancelar transação |  |
| GET | `/v1.0/documentos/ativo_usuario` | Consulta de documentos ativos para o usuário logado |  |
| GET | `/v1.0/documentos/config/pes` | Buscar configurações de documentos do tipo PES |  |
| GET | `/v1.0/documentos/digitalizacoes/{transacao}` | Consultar digitalizações de documentos por transação |  |
| GET | `/v1.0/documentos/relatorio/{transacao}` | Gerar relatório de documentos por transação |  |
| GET | `/v1.0/documentos/{lastId}` | Consulta de documentos |  |
| GET | `/v1.0/movdctos/status` | Consultar status do MovDctos pela transação |  |
| POST | `/v1.1/auditoria/documentos` | Marcar como realizada a auditoria de documento |  |
| PUT | `/v1.1/auditoria/documentos/desmarcar` | Desmarcar como realizada a auditoria de documento |  |
| GET | `/v4.0/documentos/config/ccv/{codigo}` | Obter a configuração de comissão de vendedores (documento CCV) |  |

## Detalhes

### PUT `/v1.0/documento/cancelar`

**Resumo:** Cancelar transação

Cancelar transação no sistema ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: False):

- **CancelarTransacao_V_1_0** = object { transacao, motivo, origemApp, origemVersao, origemIdentificador }

**Respostas:**

- `200` Dados carregados com sucesso — **CancelamentoTransacaoResponse_V_1_0** = object { response }
- `400` Dados inconsistentes — **ResponseError_V_1_0** = object { error }
- `404` Transação não encontrada — **ResponseError_V_1_0** = object { error }

---

### GET `/v1.0/documento/config/{codigo}`

**Resumo:** Obter os dados da configuração de um documento

Obter os dados da configuração de um documento a partir do código informado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string |  |

**Respostas:**

- `200` Dados carregados com sucesso — **ObterConfigDocumentoResponse** = object { response }

---

### GET `/v1.0/documento/consultarrecibo/{recibo}`

**Resumo:** Cancelar transação

Cancelar transação no sistema ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `recibo` | path | sim | number | recibo da requisição de cancelamento |

**Respostas:**

- `200` Dados carregados com sucesso — **ConsultaCancelamentoTransacaoResponse_V_1_0** = object { response }

---

### GET `/v1.0/documentos/ativo_usuario`

**Resumo:** Consulta de documentos ativos para o usuário logado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `tipo` | query | sim | string | Tipo do documento a ser filtrado |

**Respostas:**

- `200` Dados carregados com sucesso — **ConsultaDocumentosAtivosUsuario_V_1_0** = object { response }

---

### GET `/v1.0/documentos/config/pes`

**Resumo:** Buscar configurações de documentos do tipo PES

Obter os dados da configuração de um ou mais documentos do tipo PES.

Se nenhuma espécie válida inicial e final, como também espécie de produto inicial e final não for informada, 
o endpoint vai carregar todas as espécies apenas no atributo 'especiesValidas' e o atributo 'especiesProdutos' 
retornará null e as espécies válidas para o produto devem ser as contidas no atributo 'especiesValidas'.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |
| `codigo` | query | não | string | Filtro por código do documento |
| `ativoUsuario` | query | não | boolean | Filtra por documentos ativos para o usuário ERP vinculado |

**Respostas:**

- `200` Requisição processada com sucesso — **ResponseDocumentosConfigPES** = object { response }

---

### GET `/v1.0/documentos/digitalizacoes/{transacao}`

**Resumo:** Consultar digitalizações de documentos por transação

Consultar digitalizações de documentos por transação. Versão: 3.2.6.179

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `transacao` | path | sim | string | Transação gerado pelo ERP |

**Respostas:**

- `200`  — **ResponseDigitalizacaoDocumentosV_1_0** = object { response }

---

### GET `/v1.0/documentos/relatorio/{transacao}`

**Resumo:** Gerar relatório de documentos por transação

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |
| `transacao` | path | sim | string | Transação para gerar relatório |

**Respostas:**

- `200` Requisição processada com sucesso — **Response_Documentos_Relatorio_Transacao_V_1_0** = object { response }

---

### GET `/v1.0/documentos/{lastId}`

**Resumo:** Consulta de documentos

Consulta de documentos, com as respectivas configurações, permitindo paginação através do parâmetro `lastId`.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` |  | não |  |  |
| `limit` | query | não | integer | Quantidade máxima de registros a serem retornados |
| `codigos` | query | não | string | Lista de códigos de documentos a serem filtrados, separados por "," |
| `tipos` | query | sim | string | Lista de tipos de documento a serem filtrados, separados por "," |

**Respostas:**

- `200` Dados carregados com sucesso — **ConsultaDocumentos_V_1_0** = object { response }

---

### GET `/v1.0/movdctos/status`

**Resumo:** Consultar status do MovDctos pela transação

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `transacoes` | query | sim | string | Códigos das transações (Separados por ';') |

**Respostas:**

- `200`  — **ResponseDigitalizacaoDocumentosV_1_0** = object { response }

---

### POST `/v1.1/auditoria/documentos`

**Resumo:** Marcar como realizada a auditoria de documento

Marcar como realizada a auditoria de documento - Apenas para uso do cliente CSD

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: False):

- **RequestMarcaAuditoriaDocV_1_1** = `RequestMarcaAuditoriaDocV_1_0` (ver reference/schemas.md) & object { origemApp, origemVersao, origemIdent, pendenciasAutorizar }

**Respostas:**

- `200`  — **ResponseMarcaAuditoriaDocV_1_0** = object { response }

---

### PUT `/v1.1/auditoria/documentos/desmarcar`

**Resumo:** Desmarcar como realizada a auditoria de documento

Desmarcar como realizada a auditoria de documento - Apenas para uso do cliente CSD

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `transacao` | query | sim | string | Transação do movimento a ser desmardado |
| `operacao` | query | sim | string | Operação do movimento a ser desmardado |

**Respostas:**

- `200`  — **ResponseMarcaAuditoriaDocV_1_0** = object { response }

---

### GET `/v4.0/documentos/config/ccv/{codigo}`

**Resumo:** Obter a configuração de comissão de vendedores (documento CCV)

Retorna as políticas de comissão, as regras de cada política, as definições (condições) de cada regra e as tabelas de pontos configuradas em um documento do tipo CCV.
Os atributos "regras" e "pontos" refletem as abas Regras e Pontos da tela Configuração Comissão Vendedores do ERP; os nomes de atributo e os códigos são os mesmos usados pelo ERP.
Quando a configuração ainda não foi gravada no ERP, "regras" retorna {"Conjuntos":[]} e "pontos" retorna {"Tabelas":[]}.
Disponível somente na versão 4.0: por ser um método novo, a resposta vem sem o envelope "response", com os dados em "content" e com o status HTTP real.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do documento CCV |

**Respostas:**

- `200` Configuração carregada com sucesso — **Response_DocumentoConfigCCV_V_4_0** = object { appVersion, content }
- `404` Documento não encontrado ou não é do tipo CCV — **Error404** = object { appVersion, content }

---
