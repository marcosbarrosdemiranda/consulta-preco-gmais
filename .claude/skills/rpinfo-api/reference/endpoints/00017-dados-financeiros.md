# Tag 00017 — Dados financeiros

32 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| POST | `/v1.0/boleto` | Gerar boleto |  |
| GET | `/v1.0/boleto/{recibo}` | Consultar recibo de geracao do boleto |  |
| GET | `/v1.0/contabil/movimentos` | Retorna movimentos contábeis |  |
| GET | `/v1.0/financeiro/cliente/{cnpj_cpf}/saldocontas` | Consultar saldo do cliente considerando as contas informadas |  |
| POST | `/v1.0/financeiro/desvincularPendencia` | Desvincular Pendência Financeira |  |
| GET | `/v1.0/financeiro/finalizadoras` | Cadastro de finalizadoras |  |
| GET | `/v1.0/financeiro/movFinalizadoras/dataInicial/{dataInicial}/dataFinal/{dataFinal}/lastID/{lastId}` | MovFinalizadorasDet |  |
| GET | `/v1.0/financeiro/pendenciasFinanceiras/baixadas/lastID/{lastID}` | Consultar pendências baixadas |  |
| POST | `/v1.0/financeiro/pendenciasFinanceiras/reparcelarPendFin` | Realiza o reparcelamento de pendências financeiras |  |
| GET | `/v1.0/financeiro/planocontabil` | Consultar plano contábil |  |
| GET | `/v1.0/financeiro/saldocontas` | Consultar saldo de contas |  |
| POST | `/v1.0/financeiro/vincularPendencia` | Vincular Pendência Financeira |  |
| GET | `/v1.0/gerencial/movimentos` | Retorna movimentos gerenciais |  |
| GET | `/v1.0/localpagamento` | Cadastro de locais de pagamento |  |
| GET | `/v1.0/movimentos/cnpj/{cnpj}/contabil` | Consultar movimentos contábeis de uma unidade |  |
| GET | `/v1.0/movimentos/cnpj/{cnpj}/gerencial` | Consultar movimentos gerenciais de uma unidade |  |
| GET | `/v1.0/movimentos/gerencial/minrelease` | Retornar último release |  |
| GET | `/v1.0/movimentos/gerencial_rat` | Consultar movimentos gerenciais de rateio de uma unidade |  |
| POST | `/v1.0/ocorrencias-movimentacao-financeira` | Registrar ocorrência de movimentação financeira |  |
| GET | `/v1.1/despesasservicos` | Consultar Despesas de Serviços |  |
| GET | `/v1.1/financeiro/centrodecustos` | Consultar centro de custos |  |
| GET | `/v1.1/financeiro/cliente/{CPF_CNPJ}/saldolimitecheque` | Consultar limite no cheque |  |
| GET | `/v1.1/financeiro/cliente/{CPF_CNPJ}/saldolimitecredito` | Consultar limite de crédito do cliente |  |
| GET | `/v1.1/financeiro/cliente/{CPF_CNPJ}/saldolimitecredito/cartao` | Consultar limite de crédito de cartão do cliente |  |
| GET | `/v1.1/financeiro/movFormaVendaPDV/lastID/{lastId}` | movFormaVendaPDV |  |
| GET | `/v1.1/financeiro/pendenciasFinanceiras/{lastId}` | Pendências financeiras |  |
| GET | `/v1.1/financeiro/planocontas` | Consultar plano de contas |  |
| GET | `/v1.2/financeiro/funcionario/{CPF}/saldolimitecredito` | Consultar limite de crédito do funcionário |  |
| GET | `/v1.2/formaspagamento` | Cadastro de formas de pagamento |  |
| GET | `/v1.6/financeiro/pendenciasFinanceiras/dataInicial/{dataInicial}/dataFinal/{dataFinal}` | Pendências financeiras |  |
| GET | `/v1.6/financeiro/pendenciasFinanceiras/transacao/{transacao}` | Pendências financeiras |  |
| POST | `/v2.0/financeiro/pendenciasFinanceiras/baixarPendenciaFin` | Realiza a baixa de pendências financeiras |  |

## Detalhes

### POST `/v1.0/boleto`

**Resumo:** Gerar boleto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PostGeracaoBoleto_V_1_0** = object { operacao, origemVersao, origemApp, origemIdent }

**Respostas:**

- `200` Boleto gerado com sucesso — **Retorno_PostGeracaoBoleto_V_1_0** = object { response }

---

### GET `/v1.0/boleto/{recibo}`

**Resumo:** Consultar recibo de geracao do boleto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `recibo` | path | sim | number | número do recibo |

**Respostas:**

- `200` Dados carregados com sucesso — **Retorno_GeracaoBoleto_V_1_0** = object { response }

---

### GET `/v1.0/contabil/movimentos`

**Resumo:** Retorna movimentos contábeis

Retorna múltiplos movimentos contábeis conforme os filtros fornecidos

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |
| `dataInicial` | query | não | string | Data inicial do filtro (formato dd-MM-yyyy) |
| `dataFinal` | query | não | string | Data final do filtro (formato dd-MM-yyyy) |
| `unidades` | query | não | string | Códigos das unidades separados por vírgula |
| `contas` | query | não | string | Códigos das contas separados por vírgula |
| `debitoCredito` | query | não | string | Filtro por débito ou crédito (valores possíveis: D ou C) |
| `status` | query | não | string | Status do movimento (default: N) |
| `lastId` | query | não | integer | ID do último item processado (para paginação) |
| `release` | query | não | integer | Número da release ou versão do sistema |
| `limit` | query | não | integer | Quantidade máxima de registros a retornar |

**Respostas:**

- `200` Content — { response: object { status, appVersion, messages, content } }

---

### GET `/v1.0/financeiro/cliente/{cnpj_cpf}/saldocontas`

**Resumo:** Consultar saldo do cliente considerando as contas informadas

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj_cpf` | path | sim | number | CPF/CNPJ do cliente a ser consultado |
| `contas` | query | sim | string | contas a serem consideradas na composição do saldo, as contas devem ser fornecidas com o separador ; - Exemplo (211101;111801) |

**Respostas:**

- `200` Limite de crédito retornado — **ConsultarSaldoContasResponse** = object { response }

---

### POST `/v1.0/financeiro/desvincularPendencia`

**Resumo:** Desvincular Pendência Financeira

Realiza a desvinculação de pendências financeiras

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Auth Token |

**Request body** (application/json, obrigatório: False):

- { operacaoPFPagar: string ex: "0011939818411"; operacoesPFReceber: array de string }

**Respostas:**

- `200` Desvincular Pendência Financeira — { response: object { status, messages, content } }

---

### GET `/v1.0/financeiro/finalizadoras`

**Resumo:** Cadastro de finalizadoras

Retorna dados da tabela Finalizadoras.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200`  — **RespostaFinalizadoras_V_1_0** = object { response }

---

### GET `/v1.0/financeiro/movFinalizadoras/dataInicial/{dataInicial}/dataFinal/{dataFinal}/lastID/{lastId}`

**Resumo:** MovFinalizadorasDet

Retorna dados da tabela MovFinalizadorasDet.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `dataInicial` | path | sim | string | Data inicial do período (Formato dd-mm-yyyy) |
| `dataFinal` | path | sim | string | Data final do período (Formato dd-mm-yyyy) |
| `cnpj` | query | sim | string | cnpj da Unidade que deve ser considerada no filtro |
| `lastId` |  | não |  |  |

**Respostas:**

- `200`  — **RespostaMovFinalizadoras_V_1_0** = object { response }

---

### GET `/v1.0/financeiro/pendenciasFinanceiras/baixadas/lastID/{lastID}`

**Resumo:** Consultar pendências baixadas

Retorna as pendências baixadas (tabela pendFin) de forma paginada.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de Autenticação |
| `lastID` | path | sim | string | último ID consultado |
| `contas` | query | não | string | Contas a considerar. Separadas por ';' |
| `locaisPgto` | query | não | string | Locais de pagamento a considerar. Separados por ';' |
| `portadores` | query | não | string | Portadores a considerar. Separados por ';' |
| `especies` | query | não | string | Especies a considerar. Separados por ';' |
| `dataInicial` | query | não | string | Data inicial da data de baixa. Formato 'dd/mm/aaaa' |
| `dataFinal` | query | não | string | Data final da data de baixa. Formato 'dd/mm/aaaa' |
| `limit` | query | não | string | limite da busca |

**Respostas:**

- `200` Consultar centro de custos — **getPendenciasFinanceirasBaixadasResponse** = object { response }

---

### POST `/v1.0/financeiro/pendenciasFinanceiras/reparcelarPendFin`

**Resumo:** Realiza o reparcelamento de pendências financeiras

Este método realiza o **reparcelamento** de uma ou mais pendências financeiras existentes,
gerando novas parcelas com base nos parâmetros informados no payload.

> **Observação:** É obrigatório enviar o header `token` com o valor obtido via `/v1.1/auth`.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação (Bearer Token) |

**Request body** (application/json, obrigatório: True):

- **PayloadReparcelamentoPendFinReq** = object { dctoCodigo, dataMovimento, pfin_operacao, unidadeMovimento, observacao, especieCodigo, numeroDocumento, parcelas }

**Respostas:**

- `200` Reparcelamento processado com sucesso — **ResponseContentMovDctosTransacaoPendFin** = object { appVersion, pages, content }

---

### GET `/v1.0/financeiro/planocontabil`

**Resumo:** Consultar plano contábil

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Consultar plano de contas contábil — **ConsultarPlanoContabilResponse** = object { response }

---

### GET `/v1.0/financeiro/saldocontas`

**Resumo:** Consultar saldo de contas

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `unidade` | query | sim | string | unidade de movimento |
| `contas` | query | sim | string | contas gerenciais separadas por ; |
| `data` | query | sim | string | data de movimento |

**Respostas:**

- `200` Consultar saldo de contas — **RespostaSaldoContas_V_1_0** = object { response }

---

### POST `/v1.0/financeiro/vincularPendencia`

**Resumo:** Vincular Pendência Financeira

Realiza a vinculação de pendências financeiras

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Auth Token |

**Request body** (application/json, obrigatório: False):

- { operacaoPFPagar: string ex: "0011939818411"; operacoesPFReceber: array de string }

**Respostas:**

- `200` Vincular Pendência Financeira — { response: object { status, messages, content } }

---

### GET `/v1.0/gerencial/movimentos`

**Resumo:** Retorna movimentos gerenciais

Retorna múltiplos movimentos gerenciais conforme os filtros fornecidos

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |
| `dataInicial` | query | não | string | Data inicial do filtro (formato dd-MM-yyyy) |
| `dataFinal` | query | não | string | Data final do filtro (formato dd-MM-yyyy) |
| `unidades` | query | não | string | Códigos das unidades separados por vírgula |
| `contas` | query | não | string | Códigos das contas separados por vírgula |
| `debitoCredito` | query | não | string | Filtro por débito ou crédito (valores possíveis: D ou C) |
| `status` | query | não | string | Status do movimento (default: N) |
| `lastId` | query | não | integer | ID do último item processado (para paginação) |
| `release` | query | não | integer | Número da release ou versão do sistema |
| `limit` | query | não | integer | Quantidade máxima de registros a retornar |

**Respostas:**

- `200` Content — { response: object { status, appVersion, messages, content } }

---

### GET `/v1.0/localpagamento`

**Resumo:** Cadastro de locais de pagamento

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | query | sim | number | lastId = último código retornado no atributo codigo, se for a primeira página informar 0 |
| `limit` | query | não | number | limit = número de itens retornados por página |

**Respostas:**

- `200` Dados carregados com sucesso — **Retorno_LocalPagamento_V_1_0** = object { response }

---

### GET `/v1.0/movimentos/cnpj/{cnpj}/contabil`

**Resumo:** Consultar movimentos contábeis de uma unidade

Consultar movimentos contábeis de uma unidade dentro de um período (Período máximo de 5 dias)

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` |  | não |  |  |
| `datainicial` | query | sim | string | Data inicial do período a ser consultado (Formato dd-MM-yyyy) |
| `datafinal` | query | sim | string | Data final do período a ser consultado (Formato dd-MM-yyyy) |
| `conta` | query | não | integer | Código reduzido da conta para filtro |
| `credDeb` | query | não | string | Tipo do lançamento ('C' - à crédito, 'D' - à débito) |

**Respostas:**

- `200`  — **ConsultarMovimentosContabeisResponse** = object { response }

---

### GET `/v1.0/movimentos/cnpj/{cnpj}/gerencial`

**Resumo:** Consultar movimentos gerenciais de uma unidade

Consultar movimentos gerenciais de uma unidade dentro de um período (Período máximo de 5 dias)

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` |  | não |  |  |
| `datainicial` | query | sim | string | Data inicial do período a ser consultado (Formato dd-MM-yyyy) |
| `datafinal` | query | sim | string | Data final do período a ser consultado (Formato dd-MM-yyyy) |
| `conta` | query | não | integer | Código reduzido da conta para filtro |
| `credDeb` | query | não | string | Tipo do lançamento ('C' - à crédito, 'D' - à débito) |

**Respostas:**

- `200`  — **ConsultarMovimentosGerenciaisResponse** = object { response }

---

### GET `/v1.0/movimentos/gerencial/minrelease`

**Resumo:** Retornar último release

Retornar último release com base em uma data de movimento ou baixa

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `data` | query | sim | string | Data a ser considerada. |

**Respostas:**

- `200` Content — { content: number ex: 111 }

---

### GET `/v1.0/movimentos/gerencial_rat`

**Resumo:** Consultar movimentos gerenciais de rateio de uma unidade

Consultar movimentos gerenciais de rateio de uma unidade dentro de um período (Período máximo de 15 dias)

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` | query | não | string | CNPJ da unidade a ser consultada |
| `datainicial` | query | não | string | Data inicial do período a ser consultado (Formato dd-MM-yyyy) |
| `datafinal` | query | não | string | Data final do período a ser consultado (Formato dd-MM-yyyy) |
| `conta` | query | não | integer | Código reduzido da conta para filtro |
| `credDeb` | query | não | string | Tipo do lançamento ('C' - à crédito, 'D' - à débito) |
| `transacao` | query | não | string | Consulta por número de transação |
| `release` | query | não | number | Número do último release lido, deve-se informar 0 quando for início de leitura |
| `limit` | query | não | number | Número de itens retornados na página |

**Respostas:**

- `200`  — **ConsultarMovimentosGerenciaisRatResponse** = object { response }

---

### POST `/v1.0/ocorrencias-movimentacao-financeira`

**Resumo:** Registrar ocorrência de movimentação financeira

Registrar ocorrência de movimentação financeira associado a uma transação

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Auth Token |

**Request body** (application/json, obrigatório: False):

- { transacao: string ex: "00210137274"; texto: string ex: "Problema detectado na transação"; origemSistema: string ex: "Flex"; origemVersao: string ex: 1.0; origemId: string ex: 5214 }

**Respostas:**

- `200` responsta de sucesso — **RegistrarOcorrenciaMovFinResponse** = object { response }

---

### GET `/v1.1/despesasservicos`

**Resumo:** Consultar Despesas de Serviços

Consultar todas as Despesas de Serviços

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Lista de despesas de serviços — **depesasServicosV1** = object { response }

---

### GET `/v1.1/financeiro/centrodecustos`

**Resumo:** Consultar centro de custos

Retorna todos os centros de custo com departamento

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de Autenticação |
| `unidade` | query | não | string | Filtra os centros de custos por Unidade/Loja |

**Respostas:**

- `200` Consultar centro de custos — **financeiro_centrodecustos_V_1_1** = object { response }

---

### GET `/v1.1/financeiro/cliente/{CPF_CNPJ}/saldolimitecheque`

**Resumo:** Consultar limite no cheque

Consultar limite de crédito do cliente no cheque

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF_CNPJ` | path | sim | number | CPF/CNPJ do cliente a ser consultado |
| `cnpjunidade` | query | sim | number | Cnpj ou código da unidade |

**Respostas:**

- `200` Limite de crédito no cheque retornado — **ConsultarLimCredResponse** = object { response }

---

### GET `/v1.1/financeiro/cliente/{CPF_CNPJ}/saldolimitecredito`

**Resumo:** Consultar limite de crédito do cliente

Consultar limite de crédito do cliente no estabelecimento

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF_CNPJ` | path | sim | number | CPF/CNPJ do cliente a ser consultado |
| `cnpjunidade` | query | sim | number | CNPJ ou código da unidade/loja |

**Respostas:**

- `200` Limite de crédito retornado — **ConsultarLimCredResponse** = object { response }

---

### GET `/v1.1/financeiro/cliente/{CPF_CNPJ}/saldolimitecredito/cartao`

**Resumo:** Consultar limite de crédito de cartão do cliente

Consultar limite de crédito de cartão do cliente no estabelecimento

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF_CNPJ` | path | sim | number | CPF/CNPJ do cliente a ser consultado |
| `cnpjunidade` | query | sim | string | cnpjunidade é o cnpj da unidade a ser considerada. |

**Respostas:**

- `200` Limite de crédito do cartão retornado — **ConsultarLimCredResponse** = object { response }

---

### GET `/v1.1/financeiro/movFormaVendaPDV/lastID/{lastId}`

**Resumo:** movFormaVendaPDV

Retorna dados da tabela movFormaVdaPDV.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` | query | sim | string | cnpj da Unidade que deve ser considerada no filtro |
| `pdv` | query | não | string | código do pdv a ser considerado no filtro |
| `lastId` |  | não |  |  |
| `dataInicio` | query | sim | string | Data inicial da agenda, (Formato "dd-mm-yyyy") |
| `dataFim` | query | sim | string | Data final da agenda, (Formato "dd-mm-yyyy") |

**Respostas:**

- `200`  — **RespostaMovFormaVdaPDV_V_1_1** = object { response }

---

### GET `/v1.1/financeiro/pendenciasFinanceiras/{lastId}`

**Resumo:** Pendências financeiras

Retorna as pendências financeiras.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação. |
| `lastId` | path | sim | string | Código da última pendência recebida. Envie '0' para iniciar a consulta. Os registros são retornados em ordem crescente de codigo; para obter a próxima página, envie o codigo do último registro recebido, até que a página retorne menos registros que o limit. |
| `limit` | query | não | string | Limite de resgistros retornados por página. |
| `status` | query | não | string | Status da pendência à ser considerado (P ou B). |
| `dataInicial` | query | sim | string | Data inicial do período (Formato dd-mm-yyyy). |
| `dataFinal` | query | sim | string | Data final do período (Formato dd-mm-yyyy). |
| `unidade` | query | não | string | Código ou CNPJ da Unidade à ser considerada no filtro. |
| `catEntidade` | query | não | string | Categoria da entidade à ser considerada no filtro. |
| `codEntidade` | query | não | string | Código da entidade à ser considerada no filtro. |
| `codDocumento` | query | não | string | Código do documento à ser considerado no filtro. |
| `origemFDE` | query | não | string | Origem do FDE gerado via serviço, essa origem é fornecida pelo gerador do FDE no ato do envio para o endPoint de FDE |
| `fdeViaApi` | query | não | boolean | fdeViaApi=true serve para indicar se deseja buscar todos os FDEs gerados via API independente de sua origem |

**Respostas:**

- `200` Requisição processada com sucesso — **ResponsePendenciasFinanceiras_V_1_1** = object { response }

---

### GET `/v1.1/financeiro/planocontas`

**Resumo:** Consultar plano de contas

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Consultar plano de contas Gerencial — **ConsultarPlanoContasResponse** = object { response }

---

### GET `/v1.2/financeiro/funcionario/{CPF}/saldolimitecredito`

**Resumo:** Consultar limite de crédito do funcionário

Consultar limite de crédito do funcionário no estabelecimento

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF` | path | sim | number | CPF do funcionário a ser consultado |
| `cnpjunidade` | query | sim | number | Cnpj ou código da unidade |

**Respostas:**

- `200` Limite de crédito retornado — **ConsultarLimCredResponse** = object { response }

---

### GET `/v1.2/formaspagamento`

**Resumo:** Cadastro de formas de pagamento

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | query | não | string | codigo da forma de pagamento a ser filtrada |

**Respostas:**

- `200` Dados carregados com sucesso — **listaFormasPagamentoResponse_V_1_2** = object { response }

---

### GET `/v1.6/financeiro/pendenciasFinanceiras/dataInicial/{dataInicial}/dataFinal/{dataFinal}`

**Resumo:** Pendências financeiras

Pendências financeiras filtrados por data e cnpj da unidade.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `dataInicial` | path | sim | string | Data inicial do período (Formato dd-mm-yyyy) |
| `dataFinal` | path | sim | string | Data final do período (Formato dd-mm-yyyy) |
| `cnpj` | query | não | string | cnpj da Unidade que deve ser considerada no filtro |
| `codigo` | query | não | string | Código da entidade que pode ser considerada no filtro |
| `categoria` | query | não | string | Categoria da entidade que pode ser considerada no filtro |
| `origemFDE` | query | não | string | Origem do FDE gerado via serviço, essa origem é fornecida pelo gerador do FDE no ato do envio para o endPoint de FDE |
| `fdeViaApi` | query | não | boolean | fdeViaApi=true serve para indicar se deseja buscar todos os FDEs gerados via API independente de sua origem |

**Respostas:**

- `200` Dados carregados com sucesso — **listaPendenciasFinanceirasFornecedorResponse_V_1_6** = object { response }

---

### GET `/v1.6/financeiro/pendenciasFinanceiras/transacao/{transacao}`

**Resumo:** Pendências financeiras

Pendências financeiras filtrados por transação e cnpj da unidade.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `transacao` | path | sim | string | Numero da transação da pendência financeira |
| `cnpj` | query | sim | string | cnpj da Unidade que deve ser considerada no filtro |
| `codigo` | query | não | string | Código da entidade que pode ser considerada no filtro |
| `categoria` | query | não | string | Categoria da entidade que pode ser considerada no filtro |

**Respostas:**

- `200` Dados carregados com sucesso — **listaPendenciasFinanceirasFornecedorResponse_V_1_6** = object { response }

---

### POST `/v2.0/financeiro/pendenciasFinanceiras/baixarPendenciaFin`

**Resumo:** Realiza a baixa de pendências financeiras

Realiza a baixa de pendências financeiras criando uma transação de baixa do movimento, transação de baixa e contabilização dos movimentos

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PayloadBaixaPendFinReq** = object { dctoCodigo, dataMovimento, dataContabil, unidadeMovimento, unidadeAcessorios, contaBaixa, codigoHistorico, complementoHistorico, observacao, especieCodigo, numeroDocumento, pendencias, dadosBancarios }

**Respostas:**

- `200` Baixa de pendência financeira realizada com sucesso — **ResponseContentMovDctosTransacaoPendFin** = object { appVersion, pages, content }

---
