# Tag 00008 — Serviços de movimento referentes ao produtos

14 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| POST | `/v1.0/movimentopdv` | Inserir movimentação de PDV |  |
| DELETE | `/v1.0/movimentopdv/unidade/{cnpj}/pdv/{pdv}/cupom/{cupom}` | Deletar movimentação de PDV |  |
| GET | `/v1.0/movimentoprodutos/listartransferencias/lastid/{lastID}/datainicial/{datainicial}` | Listar transferências de produtos |  |
| GET | `/v1.0/movimentoprodutos/medias` | Buscar medias de venda e compra |  |
| GET | `/v1.0/movimentoprodutos/sugestaodia/unidade/{cnpj}/produto/{codigo}` | Buscar a sugestão de espaço do dia para o produto |  |
| GET | `/v1.0/movimentoprodutos/ultimaentrada` | buscar ultima entrada de um produto |  |
| GET | `/v1.0/movimentoprodutos/ultimavenda` | Buscar a última venda do produto |  |
| GET | `/v1.0/movimentoprodutos/vendas` | Buscar a última venda do produto |  |
| GET | `/v1.2/movimentoprodutos/semrecebimento/lastid/{lastid}` | Busca de Movimentos de Produtos Sem RCM |  |
| GET | `/v1.3/agendas/datainicio/{dataInicio}/datafim/{dataFim}/unidade/{cnpj}/lastid/{lastId}` | Buscar agenda de ofertas |  |
| GET | `/v1.3/agendas/periodoFinal/unidade/{cnpj}/lastid/{lastId}` | Buscar agenda de ofertas |  |
| GET | `/v1.3/agendas/periodoInicio/unidade/{cnpj}/lastid/{lastId}` | Buscar agenda de ofertas |  |
| GET | `/v1.3/movimentoprodutos/listarmovimentosevp/lastid/{lastID}` | Listar movimentos de produtos vendidos no PDV |  |
| GET | `/v2.0/movimentoprodutos/listarmovimentos/lastid/{lastId}` | Listar movimentos de produtos |  |

## Detalhes

### POST `/v1.0/movimentopdv`

**Resumo:** Inserir movimentação de PDV

Inserir uma nova movimentação de PDV

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **InsertMovPdvV1** = object { data, pdv, cupom, codigoUnidade, valor, tipo, categoriaEntidade, codigosPendencias, cnpjCpf, dataVencimento, cmc7 }

**Respostas:**

- `200` Dados processados com sucesso — **RespostaPadrao_SemMessage** = object { response }

---

### DELETE `/v1.0/movimentopdv/unidade/{cnpj}/pdv/{pdv}/cupom/{cupom}`

**Resumo:** Deletar movimentação de PDV

Deletar uma movimentação de PDV

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` |  | não |  |  |
| `pdv` | path | sim | string | Número do PDV a ser definido como filtro |
| `cupom` | path | sim | number | Número do cupom a ser deletado |

**Respostas:**

- `200` Dados processados com sucesso — **RespostaPadrao_SemMessage** = object { response }

---

### GET `/v1.0/movimentoprodutos/listartransferencias/lastid/{lastID}/datainicial/{datainicial}`

**Resumo:** Listar transferências de produtos

Listar transferências de produtos por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `datainicial` | path | sim | string | Data em que inicia-se a leitura das transferências, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `transfPend` | query | não | string | Indicativo para filtrar transferêcias pendentes, caso queira recuperar apenas pendentes, deve-se informar S ou N para transferências já concluídas |

**Respostas:**

- `200` Transferências retornadas — **TransfProdResponse** = object { response }

---

### GET `/v1.0/movimentoprodutos/medias`

**Resumo:** Buscar medias de venda e compra

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `unidade` | query | sim | number | Código da unidade a ser considerada |
| `produto` | query | sim | number | Código do produto a ser considerado |

**Respostas:**

- `200`  — **MediasResponse_V_1_0** = object { response }

---

### GET `/v1.0/movimentoprodutos/sugestaodia/unidade/{cnpj}/produto/{codigo}`

**Resumo:** Buscar a sugestão de espaço do dia para o produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` | path | sim | string | CNPJ da unidade a consultar |
| `codigo` | path | sim | string | Código do produto |

**Respostas:**

- `200` Transferências retornadas — **SugestDiaResponse** = object { response }

---

### GET `/v1.0/movimentoprodutos/ultimaentrada`

**Resumo:** buscar ultima entrada de um produto

Busca último registro de EAQ, para o produto consultado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `produto` | query | sim | number | codigo do produto |

**Respostas:**

- `200`  — **ResponseUltimaEntradaEAQ_V_1_0** = object { response }

---

### GET `/v1.0/movimentoprodutos/ultimavenda`

**Resumo:** Buscar a última venda do produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `produto` | query | sim | number | Código do produto a ser considerado no filtro |
| `unidade` | query | sim | number | Unidade/Loja que deseja considerar no filtro |

**Respostas:**

- `200`  — **UltimaVendaDResponse_V_1_0** = object { response }

---

### GET `/v1.0/movimentoprodutos/vendas`

**Resumo:** Buscar a última venda do produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `produto` | query | sim | number | Código do produto a ser considerado no filtro |
| `unidade` | query | sim | number | Unidade/Loja que deseja considerar no filtro |
| `dataI` | query | sim | string | Data inicial que deseja considerar no filtro |
| `dataF` | query | sim | string | Data final que deseja considerar no filtro |

**Respostas:**

- `200`  — **VendasResponse_V_1_0** = object { response }

---

### GET `/v1.2/movimentoprodutos/semrecebimento/lastid/{lastid}`

**Resumo:** Busca de Movimentos de Produtos Sem RCM

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastid` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `documentos` | query | sim | string | Tipo do documento da movimentação. Docs Permitidos: PBX;EAQ;EOE;EET;EDV;ETE;EBR;EEC;EES;EOS;EST;EDC;ETS;EBC;ECI;ETM;ESC;EFE;ESE;EPE;ESS;EVD;ETA;EVA |
| `codDocumento` | query | sim | string | codigo de documento que tem dentro do tipo de documento |
| `cnpj` | query | sim | string | CNPJ da unidade a consultar |
| `catEntidade` | query | sim | string | Categoria da entidade a consultar. Valores válidos: F;U;C;N; (Fornecedor;Unidade;Cliente;Nenhuma) |
| `codEntidade` | query | sim | string | Código da entidade a consultar |
| `dataInicial` | query | sim | string | Data em que inicia-se a consulta por movimentos, considera-se até o dia indicado em dataFinal (Formato "dd-mm-yyyy") |
| `dataFinal` | query | sim | string | Data em que finaliza-se a consulta por movimentos (Formato "dd-mm-yyyy") |
| `validarDestino` | query | sim | boolean | Flag para validar ou não o destino |

**Respostas:**

- `200` Dados processados com sucesso — **MovProdRCMResponseV12** = object { response }

---

### GET `/v1.3/agendas/datainicio/{dataInicio}/datafim/{dataFim}/unidade/{cnpj}/lastid/{lastId}`

**Resumo:** Buscar agenda de ofertas

Buscar agendas de ofertas da unidade dentro do período informado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `dataInicio` | path | sim | string | Data inicial da agenda, (Formato "dd-mm-yyyy") |
| `dataFim` | path | sim | string | Data final da agenda, (Formato "dd-mm-yyyy") |
| `cnpj` |  | não |  |  |
| `lastId` |  | não |  |  |

**Respostas:**

- `200` Agendas retornadas — **GetAgendasOfertasV1_2** = object { response }

---

### GET `/v1.3/agendas/periodoFinal/unidade/{cnpj}/lastid/{lastId}`

**Resumo:** Buscar agenda de ofertas

Buscar agendas de ofertas da unidade dentro do período informado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` |  | não |  |  |
| `lastId` |  | não |  |  |
| `datainicio` | query | não | string | Data inicial da agenda, (Formato "dd-mm-yyyy") |
| `datafim` | query | não | string | Data final da agenda, (Formato "dd-mm-yyyy") |

**Respostas:**

- `200` Agendas retornadas — **GetAgendasOfertasV1_2** = object { response }

---

### GET `/v1.3/agendas/periodoInicio/unidade/{cnpj}/lastid/{lastId}`

**Resumo:** Buscar agenda de ofertas

Buscar agendas de ofertas da unidade dentro do período informado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` |  | não |  |  |
| `lastId` |  | não |  |  |
| `datainicio` | query | não | string | Data inicial da agenda, (Formato "dd-mm-yyyy") |
| `datafim` | query | não | string | Data final da agenda, (Formato "dd-mm-yyyy") |

**Respostas:**

- `200` Agendas retornadas — **GetAgendasOfertasV1_2** = object { response }

---

### GET `/v1.3/movimentoprodutos/listarmovimentosevp/lastid/{lastID}`

**Resumo:** Listar movimentos de produtos vendidos no PDV

Listar movimentos de produtos vendidos no PDV por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `datainicial` | query | sim | string | Data em que inicia-se a leitura dos movimentos, (Formato "dd-mm-yyyy") |
| `datafinal` | query | sim | string | Data em que finaliza-se a leitura dos movimentos (Formato "dd-mm-yyyy") |
| `documentos` | query | sim | string | Valores para filtro, deve-se enviar os códigos dos documentos que devem ser considerados no filtro |
| `marca` | query | não | string | Filtro pela marca do produto |
| `grupo` | query | não | string | Filtro pelo grupo do produto |
| `unidade` | query | não | string | Filtro pela unidade do produto |

**Respostas:**

- `200` Movimentos retornados — **VdaDetResponse** = object { response }

---

### GET `/v2.0/movimentoprodutos/listarmovimentos/lastid/{lastId}`

**Resumo:** Listar movimentos de produtos

Listar movimentos de produtos por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` |  | não |  |  |
| `datainicial` | query | não | string | Data em que inicia-se a leitura dos movimentos, considera-se até o dia atual (Formato "dd-mm-yyyy"). Obrigatório caso um número de transação não seja informado |
| `datafinal` | query | não | string | Data em que finaliza-se a leitura dos movimentos (Formato "dd-mm-yyyy") |
| `tipoconsulta` | query | não | string | Tipo da consulta, tipos válidos (CODIGO_DCTO, TIPO_DCTO) |
| `valores` | query | não | string | Valores para filtro devem ser enviados com ; (ponto e virgula) como separador, enviar tipos de documento quando informar (tipoconsulta = TIPO_DCTO) e quando enviar (tipoconsulta = CODIGO_DCTO) deve-se enviar os códigos dos documentos que devem ser considerados no filtro |
| `departamentos` | query | não | string | Departamentos a serem considerados no filtro |
| `produto` | query | não | number | Código do produto a ser considerado no filtro |
| `fornecedorPadrao` | query | não | number | Código do fornecedor padrão do produto a ser considerado no filtro |
| `codEntidade` | query | não | number | Código da entidade a ser considerada no filtro |
| `catEntidade` | query | não | number | Categoria da entidade a ser considerada no filtro Possíveis valores: SEM_ENTIDADE, UNIDADE, CLIENTE, FORNECEDOR, FUNCIONARIO |
| `unidade` | query | não | string | Unidade/Loja que deseja considerar no filtro |
| `transacao` | query | não | string | Número da transação a ser considerada no filtro. Obrigatório caso a dataInicial não seja informadaz |

**Respostas:**

- `200`  — **MovimentosMovProdD_V_2_0** = array de object { id, chavePrimaria, transacao, operacao, tipoMovimento, tipo, status, chaveNfe, data, hora, codigoEntidade, categoriaEntidade, unidade, numero, serie, codBenef, codEstoque, fatorEstoque, codigoProduto, sequencial, quantidadeUnitaria, quantidadeEmbalagem, embCom, embTrib, subTribEnt, ipiDevol, valorBcBruto, valor, icms, icmsSimplesFed, icmsCritica, valorIcmsInf, valorIcms, valorFCP, aliqFCP, cstIPI, percReducaoBC, percentualIPI, percentualDesconto, outrosAcrescimos, valorSubTrib, bcSubTribInf, alSubTribinf, despesasAdicionais, percentualISS, simbologiaICMS, valorPIS, valorCofins, bcPisCofins, aliqPis, aliqCofins, cstPis, cstCofins, cfop, cst, bcIpi, percReducaoBcSt, valorUnitario, ctCompra, ctMedio, ctTransf, ctEmpresa, ctFiscal, prCompra, tipoDcto, dataEmissao, qtdeTrib, qtdeCom, comissaoValor, comissaoBase, comissaoPerc, nextra, cextra, xml }

---
