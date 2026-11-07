# Tag 00010 — Serviços de movimento referentes ao estoque

15 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/pendest/codigospendencias` | Obter o cadastro de códigos de pendências de estoque |  |
| GET | `/v1.0/pendest/codigospendencias/codigo/{codigo}` | Obter o cadastro de um código de pendência de estoque |  |
| POST | `/v1.0/pendest/esm/inserir` | Incluir separação de pendências de estoque |  |
| GET | `/v1.0/pendest/recibo/{recibo}` | Incluir pendências de estoque |  |
| GET | `/v1.0/produtounidade/auditoriaestoque/recibo/{recibo}` | Consultar processamento da auditoria de estoque |  |
| PUT | `/v1.0/recmerc/update/{transacao}` | Substituir notas dos recebimentos de mercadoria |  |
| GET | `/v1.0/recmerc/{lastId}` | Obter recebimentos de mercadoria |  |
| GET | `/v1.0/recmerc/{lastId}/vencimento-validade` | Relação de produtos com validade a vencer |  |
| GET | `/v1.1/produtounidade/auditoriaestoque/{lastID}/datainicial/{dataInicial}/datafinal/{dataFinal}` | Obter auditorias de estoque |  |
| GET | `/v1.1/produtounidade/unidade/{CNPJ}/departamento/{departamento}/snapshotestoque` | Obter snapshot do estoque |  |
| GET | `/v1.1/produtounidade/{codigoProduto}/unidade/{CNPJ}/snapshotestoque` | Obter snapshot do estoque |  |
| POST | `/v1.1/recmerc/inserir` | Incluir recebimentos de mercadoria |  |
| GET | `/v1.2/pendest/pendenciaestoque/lastid/{lastID}` | Obter pendências de estoque |  |
| POST | `/v1.3/produtounidade/auditoriaestoque` | Incluir auditoria de estoque |  |
| POST | `/v1.6/pendest/incluir` | Incluir pendências de estoque |  |

## Detalhes

### GET `/v1.0/pendest/codigospendencias`

**Resumo:** Obter o cadastro de códigos de pendências de estoque

Obter o cadastro de códigos de pendências de estoque do ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Dados carregados com sucesso — **ObterCodsPendResponse** = object { response }

---

### GET `/v1.0/pendest/codigospendencias/codigo/{codigo}`

**Resumo:** Obter o cadastro de um código de pendência de estoque

Obter o cadastro de um código de pendência de estoque do ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código da pendência de estoque a obter os dados de cadastro |

**Respostas:**

- `200` Dados carregados com sucesso — **ObterCodPendResponse** = object { response }

---

### POST `/v1.0/pendest/esm/inserir`

**Resumo:** Incluir separação de pendências de estoque

**Request body** (application/json, obrigatório: True):

- **IncluirESMPost** = object { unidadeOrigem, unidadeDestino, codigoDocumento, codigoPendencia, dataMovimento, pendencias }

**Respostas:**

- `200` Separaça de pendências incluida — **RespRecMercInserirV11** = object { response }

---

### GET `/v1.0/pendest/recibo/{recibo}`

**Resumo:** Incluir pendências de estoque

Incluir pendências de estoque no sistema

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de Autenticação |
| `recibo` | path | sim | string | Número do recibo para verificar o processamento das pendências de estoque |

**Respostas:**

- `200` Processamento concluído. Retorna o número da transação. — { response: object { status, messages, content } }

---

### GET `/v1.0/produtounidade/auditoriaestoque/recibo/{recibo}`

**Resumo:** Consultar processamento da auditoria de estoque

Consultar processamento da auditoria de estoque no sistema
    para o atributo `statusProcessamento` os valores possíveis são: 
        `PENDENTE` ( para este status o atributo criticas não será retornado )
        `EM_PROCESSAMENTO`
        `PROCESSADO`
        `PROCESSADO_COM_CRITICAS`
        `ERRO`

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `recibo` | path | sim | number | número do recibo a ser consultado |

**Respostas:**

- `200` Consulta de processamento de auditoria de estoque — **RespostaGetAuditoriaEstoque_V_1_3** = object { response }

---

### PUT `/v1.0/recmerc/update/{transacao}`

**Resumo:** Substituir notas dos recebimentos de mercadoria

Substituir notas dos recebimentos de mercadoria para a unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `transacao` | path | sim | string | numero da transação do recebimento de mercadoria |

**Request body** (application/json, obrigatório: True):

- **IncluirRecPost** = object { unidade, codigoDcto, numero, serie, dataMovimento, categoriaEntidade, codigoEntidade, produtos }

**Respostas:**

- `200` Recebimento incluido — **RespRecMercInserirV11** = object { response }

---

### GET `/v1.0/recmerc/{lastId}`

**Resumo:** Obter recebimentos de mercadoria

Obter dados do recebimentos de mercadoria

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Último código do registro recebido na página anterior atributo (codigo), caso seja a primeira página informar 0 |
| `dataInicial` | query | sim | string | Data Inicial do período (Formato "dd-mm-yyyy") |
| `dataFinal` | query | sim | string | Data Final do período (Formato "dd-mm-yyyy") |
| `status` | query | não | string | Status do recebimento |
| `hasValidade` | query | não | boolean | Verifica se o recebimento tem data de validade (true, false) |
| `validadeInicial` | query | não | string | Data de Validade Inicial do período ("dd-mm-yyyy"). Funciona apenas com o 'hasValidade=true' |
| `validadeFinal` | query | não | string | Data de Validade Final do período ("dd-mm-yyyy"). Funciona apenas com o "hasValidade=true" |
| `unidade` | query | não | string | Unidade do recebimento |
| `produto` | query | não | string | Produto do recebimento |

**Respostas:**

- `200` JSON dos recebimentos retornados — **RecMerc_V_1_0** = object { response }

---

### GET `/v1.0/recmerc/{lastId}/vencimento-validade`

**Resumo:** Relação de produtos com validade a vencer

Lista os recebimentos de mercadoria (RecMerc) pendentes (status 'N') cuja data de validade
cai dentro do período informado, calculando saídas ocorridas desde o recebimento, estoque
(soma seletiva conforme os códigos de estoque informados), estoque disponível, percentual de
shelf life decorrido e vendas dos últimos 3 meses / mês atual.

Produtos do tipo "kit" (função do produto contém 'ID') têm seus componentes expandidos como
linhas adicionais (via IndustD), uma por grupo produto+unidade, apenas para componentes com
estoque disponível maior que zero.

Migração do relatório do ERP "Relação Dos Produtos Com Validade Vencendo No Período"
(TFunRelEst.VctoValidade).

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Último código do registro (recm_codigo) recebido na página anterior, caso seja a primeira página informar 0 |
| `dataInicial` | query | sim | string | Data Inicial do período de validade (Formato "dd-mm-yyyy"). Também é usada como limite inferior padrão para o cálculo de saídas (substituída pela data do recebimento quando esta for anterior) |
| `dataFinal` | query | sim | string | Data Final do período de validade (Formato "dd-mm-yyyy"). Também é o limite superior do cálculo de saídas |
| `unidades` | query | sim | string | Unidade(s) a considerar, separadas por ";" (ex. "001;002") |
| `codigosEstoque` | query | sim | string | Código(s) de estoque a somar (1 a 5, referentes a prun_estoque1..5 de produn), separados por ";" (ex. "1;2") |
| `codigoProduto` | query | sim | integer | Código do produto a considerar |
| `limit` | query | não | integer | Quantidade máxima de registros por página |

**Respostas:**

- `200` JSON dos produtos com validade a vencer — **RecMercVencimentoValidade_V_1_0** = object { response }

---

### GET `/v1.1/produtounidade/auditoriaestoque/{lastID}/datainicial/{dataInicial}/datafinal/{dataFinal}`

**Resumo:** Obter auditorias de estoque

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | string | Código do último comprador consultado. Envie "0" caso queira consultar todos os compradores (mesmo passando 0 os dados retornam paginados) |
| `dataInicial` | path | sim | string | Data inicial do período (Formato dd-mm-yyyy) |
| `dataFinal` | path | sim | string | Data final do período (Formato dd-mm-yyyy) |
| `unidades` | query | sim | string | Código das unidades separadas por ;   Exemplo unidades=001;002;003 |
| `departamento` | query | não | string | Departamento a ser considerado no filtro |

**Respostas:**

- `200`  — **RespostaGetAuditoriaEstoque** = object { response }

---

### GET `/v1.1/produtounidade/unidade/{CNPJ}/departamento/{departamento}/snapshotestoque`

**Resumo:** Obter snapshot do estoque

Obter snapshot do estoque no período

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `departamento` | path | sim | string | Código do departamento dos produtos a consultar |
| `calcularRCM` | query | sim | string | Define se irá considerar recebimentos de mercadorias sem que haja entrada registrada da mesma, a qual será acrescida ao estoque disponível.  Pode receber os valores "SIM" e "NAO". |
| `considerarVendaOnline` | query | sim | string | Define se irá considerar venda online de mercadorias, a qual será deduzida do estoque disponível  Pode receber os valores "SIM" e "NAO". |
| `dataInicial` | query | sim | string | Data Inicial do período (Formato "dd-mm-yyyy") |
| `dataFinal` | query | sim | string | Data Final do período (Formato "dd-mm-yyyy") |
| `lastId` | query | sim | string | último código de produto recebido na página anterior, caso seja a primeira página informar 0 |

**Respostas:**

- `200` Snapshot do estoque retornado — **SnapShotProdutoResponse** = object { response }

---

### GET `/v1.1/produtounidade/{codigoProduto}/unidade/{CNPJ}/snapshotestoque`

**Resumo:** Obter snapshot do estoque

Obter snapshot do estoque do produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigoProduto` | path | sim | string | Código do produto a consultar |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `calcularRCM` | query | sim | string | Define se irá considerar recebimentos de mercadorias sem que haja entrada registrada da mesma, a qual será acrescida ao estoque disponível.  Pode receber os valores "SIM" e "NAO". |
| `considerarVendaOnline` | query | sim | string | Define se irá considerar venda online de mercadorias, a qual será deduzida do estoque disponível  Pode receber os valores "SIM" e "NAO". |
| `dataInicial` | query | sim | string | Data Inicial do período (Formato "dd-mm-yyyy") |
| `dataFinal` | query | sim | string | Data Final do período (Formato "dd-mm-yyyy") |

**Respostas:**

- `200` Snapshot do estoque retornado — **SnapShotProdutosResponse** = object { response }

---

### POST `/v1.1/recmerc/inserir`

**Resumo:** Incluir recebimentos de mercadoria

Incluir recebimentos de mercadoria para a unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **IncluirRecPost** = object { unidade, codigoDcto, numero, serie, dataMovimento, categoriaEntidade, codigoEntidade, produtos }

**Respostas:**

- `200` Recebimento incluido — **RespRecMercInserirV11** = object { response }

---

### GET `/v1.2/pendest/pendenciaestoque/lastid/{lastID}`

**Resumo:** Obter pendências de estoque

Obter pendências de estoque da empresa

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | string | Último id lido na paginação, enviar zero para consultar desde a o início do cadastro.  (mesmo passando 0 os dados retornam paginados) |
| `CategoriaEntidade` | query | não | string | Categoria da entidade, valores possíveis: SEM_ENTIDADE, UNIDADE, CLIENTE, FORNECEDOR, FUNCIONARIO |
| `CodigoEntidade` | query | não | string | Codigo da entidade |
| `UnidadeOrigem` | query | não | string | Unidade de origem |
| `UnidadeDestino` | query | não | string | Unidade de destino |
| `CodigoProduto` | query | não | string | Codigo do produto |
| `CodigoPendencia` | query | não | string | Codigo das pendencias, separadas por ',' |
| `TipoPendencia` | query | não | string | Tipo da pendencia |
| `DataInicial` | query | não | string | Data inicial a se considerar no periodo. (Formato "dd-MM-yyyy") |
| `DataFinal` | query | não | string | Data final a se considerar no periodo.. (Formato "dd-MM-yyyy") |
| `Status` | query | não | string | Status da pendencia, valores possíveis: BAIXADA, PENDENTE |
| `Transacao` | query | não | string | Transação da pendencia |

**Respostas:**

- `200` Dados retornados — **ObterPendResponse** = object { response }

---

### POST `/v1.3/produtounidade/auditoriaestoque`

**Resumo:** Incluir auditoria de estoque

Incluir auditoria de estoque no sistema

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **IncluirAuditoriaPostV1_3** = object { id, origem, dataHoraDispositivo, auditorias }

**Respostas:**

- `200` Auditoria de estoque adicionada — **RespostaPostAuditoriaEstoqueV1_3** = object { response }

---

### POST `/v1.6/pendest/incluir`

**Resumo:** Incluir pendências de estoque

Observação: a Grade de unidades com quantidades (`unidades`) dentro das pendências é exigida apenas quando o comportamento "QU" estiver habilitado no documento PES.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de Autenticação |

**Request body** (application/json, obrigatório: True):

- **V_1_6_pendest_incluir** = object { Inclusoes, Baixas }

**Respostas:**

- `200` Iniciado processamento das pendências de estoque. Retorna um recibo para verificar o status desse processamento. — { status: string(string) ex: "ok"; messages: `messages` (ver reference/schemas.md); content: number ex: 124 }

---
