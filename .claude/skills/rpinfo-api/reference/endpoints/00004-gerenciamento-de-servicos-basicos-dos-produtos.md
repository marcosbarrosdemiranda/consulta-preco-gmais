# Tag 00004 — Gerenciamento de serviços básicos dos produtos

68 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/pontosexposicao/listarpontos/unidade/{cpf_cnpj}/data/{data}` | Lista as Agendas dos pontos de exposição |  |
| GET | `/v1.0/pontosexposicao/listarpontos/unidade/{cpf_cnpj}/lastid/{lastId}` | Lista os pontos de exposição |  |
| GET | `/v1.0/produn/listaprodutos/{lastID}/unidade/{CNPJ}` | Lista de produtos unidade |  |
| GET | `/v1.0/produn/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado` | Lista de produtos unidade |  |
| GET | `/v1.0/produto/classes` | Listar classes de produtos |  |
| GET | `/v1.0/produto/filtros/curvasABC` | Opções de curva ABC para o filtro de produtos |  |
| GET | `/v1.0/produto/filtros/opcoesAtivos` | Opção de ativos para escopo produto |  |
| GET | `/v1.0/produto/marcas` | Listar marcas de produtos |  |
| GET | `/v1.0/produto/setores` | Listar setores de produtos |  |
| GET | `/v1.0/produto/setoresdeposito` | Listar setores de depósito dos produtos |  |
| GET | `/v1.0/produto/tipos` | Listar tipos de produtos |  |
| GET | `/v1.0/produto/{codigo}` | Consultar cadastro de um produto |  |
| GET | `/v1.0/produtos/alterados/dthrmanutencao/{dthrmanutencao}` | Obter produtos alterados na data informada |  |
| GET | `/v1.0/produtosFornecedores/lastRelease/{lastRelease}` | Produtos e fornecedores |  |
| GET | `/v1.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/estoque/datahoraalteracao/{datahora}` | Obter dados do produto |  |
| GET | `/v1.0/produtounidade/ofertas` | Ofertas de produtos por unidade |  |
| GET | `/v1.0/produtounidade/unidade/{cnpj}/estoquediario` | Consultar estoque de produto |  |
| GET | `/v1.0/produtounidade/unidade/{cnpj}/produto/{codigo}/snapshotbyday` | Consultar estoque de produto de forma diária |  |
| GET | `/v1.0/produtounidade/unidade/{cpnj}/estoquedisponivel` | Consulta o Estoque Disponível dos produtos enviados para a unidade informada |  |
| GET | `/v1.0/produtounidade/{codigoproduto}/unidade/{CNPJ}/imagens` | Consultar imagens de um produto |  |
| PUT | `/v1.0/produtounidade/{codigo}/unidade/{CNPJ}/marcado` | Alterar o campo marcado do produto |  |
| GET | `/v1.0/produtounidade/{codigo}/unidade/{CNPJ}/precoUnidadeMedida` | Preço da Unidade de Medida |  |
| PUT | `/v1.0/produtounidade/{codigo}/unidade/{cnpjOrCodigo}` | Atualiza produto unidade |  |
| GET | `/v1.0/produtounidade/{codigo}/unidade/{unidade}/custos` | Cálculo de custos do produto/unidade |  |
| GET | `/v1.0/tabemb` | Obter cadastro de embalagens |  |
| GET | `/v1.1/grupos` | Consultar o cadastro de grupos de produtos |  |
| POST | `/v1.1/grupos` | Inserir o cadastro de grupos de produtos |  |
| PUT | `/v1.1/grupos/{codigo}` | Alterar o cadastro de grupos de produtos |  |
| DELETE | `/v1.1/grupos/{codigo}` | Deletar o cadastro de grupos de produtos |  |
| POST | `/v1.1/metasprod` | Inserir novas Metas de Produtos |  |
| PUT | `/v1.1/metasprod` | Alterar Meta de Produto cadastrada |  |
| GET | `/v1.1/metasprod/cnpj/{cnpj}` | Consultar Metas de Produtos de uma unidade |  |
| GET | `/v1.1/precadastro` | Obter dados de pré cadastro do produto |  |
| POST | `/v1.1/precadastro` | Inserir dados de pré cadastro do produto |  |
| GET | `/v1.1/precadastro/{sequencia}` | Obter dados de pré cadastro do produto |  |
| GET | `/v1.1/produto/codigobarrasalterados/ativos/unidade/{unidade}/lastid/{lastID}` | Obter dados de códigos de barras alternativos dos produtos ativos |  |
| GET | `/v1.1/produto/codigobarrasalterados/lastid/{lastID}` | Obter dados de códigos de barras alternativos |  |
| GET | `/v1.1/produto/excluidos/lastid/{lastid}/dataexclusao/{dataexclusao}` | Obter dados dos produtos excluidos |  |
| PUT | `/v1.1/produto/{codigo}` | Editar cadastro de um produto |  |
| GET | `/v1.1/produto/{codigo}/codigobarrasalterados` | Obter dados de códigos de barras alternativos |  |
| GET | `/v1.1/produto/{codigo}/detalhado` | Consultar cadastro de um produto |  |
| GET | `/v1.1/produto/{prodCodigo}/fornecedor/{fornCodigo}` | Obter dados dos códigos do fornecedor vinculados a um produto |  |
| GET | `/v1.2/produto/listaprodutos/{lastId}` | Consultar cadastro de um produto |  |
| GET | `/v1.2/produto/listaprodutos/{lastId}/detalhado` | Consultar cadastro de um produto |  |
| GET | `/v1.3/produtos/lastid/{lastId}/fornecedor/{codigo}` | Obter dados dos produtos vinculados ao fornecedor |  |
| GET | `/v1.3/usuariosexternos/{codigo}` | Obter dados do usuario externo |  |
| GET | `/v1.4/cestabasica/listarcestas/lastid/{lastId}` | Consultar o cadastro de cestas básicas |  |
| GET | `/v2.8/produtounidade/listaprodutos/{codigo}/unidade/{CNPJ}` | Obter dados do produto |  |
| GET | `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/departamento/{departamento}` | Obter dados do produto |  |
| GET | `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/grupo/{grupo}` | Obter dados do produto |  |
| GET | `/v2.8/produtounidade/{codBarras}/unidade/{CNPJ}/estoquecodigobarras` | Obter dados do produto |  |
| GET | `/v2.8/produtounidade/{codigoBarras}/unidade/{CNPJ}/consultarcodigobarras` | Obter estoque do produto |  |
| GET | `/v2.8/produtounidade/{codigo}/unidade/{CNPJ}` | Obter estoque do produto |  |
| GET | `/v2.8/produtounidade/{codigo}/unidade/{CNPJ}/estoque` | Obter estoque do produto |  |
| GET | `/v3.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/grupo/{grupo}` | Obter dados dos produtos |  |
| GET | `/v3.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/marcados` | Obter dados dos produtos |  |
| GET | `/v3.2/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado` | Obter dados dos produtos |  |
| GET | `/v3.2/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos` | Lista de produtos ativos detalhado |  |
| GET | `/v3.2/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos/dataHoraManutencao/{dataHoraManutencao}` | Lista de produtos ativos detalhado |  |
| GET | `/v3.2/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/departamento/{departamento}` | Obter dados dos produtos |  |
| GET | `/v3.2/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/grupo/{grupo}` | Obter dados dos produtos |  |
| GET | `/v3.2/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/semcalcularestoque` | Obter dados dos produtos |  |
| GET | `/v3.2/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/setor/{setor}` | Obter dados dos produtos |  |
| GET | `/v3.2/produtounidade/listaprodutos/{lastId}/unidade/{CNPJ}/detalhado/dataHoraManutencao/{dataHoraManutencao}` |  |  |
| GET | `/v3.2/produtounidade/{codigoBarras}/unidade/{CNPJ}/detalhado/consultarcodigobarras` | Obter dados do produto |  |
| GET | `/v3.2/produtounidade/{codigo}/unidade/{CNPJ}/detalhado` | Obter dados do produto |  |
| GET | `/v3.2/produtounidade/{codigo}/unidade/{CNPJ}/detalhado/estoque` | Obter dados do produto |  |
| GET | `/v3.3/produtounidade/listaprodutos/{lastRelease}/unidade/{CNPJ}/detalhado/customrelease` |  |  |

## Detalhes

### GET `/v1.0/pontosexposicao/listarpontos/unidade/{cpf_cnpj}/data/{data}`

**Resumo:** Lista as Agendas dos pontos de exposição

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cpf_cnpj` | path | sim | string | CPF ou CNPJ vinculado a unidade desejada |
| `data` | path | sim | string | Data a ser considerada formato(dd-MM-yyyy) |

**Respostas:**

- `200` Dados carregados com sucesso — **Response_PontosExposicao_ListarPontos_Unidade_Data_V_1_0** = object { response }

---

### GET `/v1.0/pontosexposicao/listarpontos/unidade/{cpf_cnpj}/lastid/{lastId}`

**Resumo:** Lista os pontos de exposição

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cpf_cnpj` | path | sim | string | CPF ou CNPJ vinculado a unidade desejada |
| `lastId` | path | sim | string | Código do último dado consultado. Envie "0" caso queira consultar todos os dados (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados com sucesso — **Response_PontosExposicao_ListarPontos_Unidade_LastId_V_1_0** = object { response }

---

### GET `/v1.0/produn/listaprodutos/{lastID}/unidade/{CNPJ}`

**Resumo:** Lista de produtos unidade

Busca da lista de produtos unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | string | Código do último produto consultado. Envie "0" caso queira consultar todos os produtos  (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `exportarEstoqueDisp` | query | não | boolean | Se informado e marcado como 'true', será retornado o estoque no atributo 'Estoque' |
| `fieldName` | query | não | string | Nome do campo de release customizado |
| `departamentos` | query | não | string | Departamentos a serem considerados no filtro |
| `setor` | query | não | string | Setor a ser considerado no filtro |
| `grupo` | query | não | string | Filtro pelo grupo do produto |
| `dataHoraManutencao` | query | não | string | Data e hora de alteração cadastro padrão dd-MM-yyyy HH:mm:ss |
| `ativos` | query | não | boolean | Se informado e marcado como 'true', será retornado os produtos unidade ativos |
| `considerarCancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |
| `classe` | query | não | string | Se informado será retornado a classe do produto |
| `codPreco` | query | não | integer | Se informado será filtrado pelo código do preço |

**Respostas:**

- `200` Requisição processada com sucesso — **ResponseProdUn_V_1_0** = object { response }

---

### GET `/v1.0/produn/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado`

**Resumo:** Lista de produtos unidade

Busca da lista de produtos unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | string | Código do último produto consultado. Envie "0" caso queira consultar todos os produtos  (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `exportarEstoqueDisp` | query | não | boolean | Se informado e marcado como 'true', será retornado o estoque no atributo 'Estoque' |
| `loadCbalt` | query | não | boolean | Se informado e marcado como 'true', será retornado os códigos de barras alternativos |
| `loadTributacao` | query | não | boolean | Se informado e marcado como 'true', será retornada a tributacao do produto no atributo 'tributacao', se não encontrar tributação retornará como null |
| `fieldName` | query | não | string | Nome do campo de release customizado |
| `departamentos` | query | não | string | Departamentos a serem considerados no filtro |
| `setor` | query | não | string | Setor a ser considerado no filtro |
| `grupo` | query | não | string | Filtro pelo grupo do produto |
| `dataHoraManutencao` | query | não | string | Data e hora de alteração cadastro padrão dd-MM-yyyy HH:mm:ss |
| `ativos` | query | não | boolean | Se informado e marcado como 'true', será retornado os produtos unidade ativos |
| `outrosExtras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |
| `considerarCancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |
| `classe` | query | não | string | Se informado será retornado a classe do produto |
| `codPreco` | query | não | integer | Se informado será filtrado pelo código do preço |

**Respostas:**

- `200` Requisição processada com sucesso — **ResponseProdUnDetalhado_V_1_0** = object { response }

---

### GET `/v1.0/produto/classes`

**Resumo:** Listar classes de produtos

Retorna as classes de produtos maiores que zero, sem repetições e ordenadas.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |

**Respostas:**

- `200` OK — **response_v1.0_classes** = object { response }

---

### GET `/v1.0/produto/filtros/curvasABC`

**Resumo:** Opções de curva ABC para o filtro de produtos

Consulta as opções de curva ABC disponíveis para filtrar produtos

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |

**Respostas:**

- `200` OK — **response_v1.0_curvasABC** = object { response }

---

### GET `/v1.0/produto/filtros/opcoesAtivos`

**Resumo:** Opção de ativos para escopo produto

Consultar opção de Ativos para filtrar produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |

**Respostas:**

- `200` OK — **response_v1.0_ativos** = object { response }

---

### GET `/v1.0/produto/marcas`

**Resumo:** Listar marcas de produtos

Retorna as marcas distintas cadastradas nos produtos.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |

**Respostas:**

- `200` OK — **response_v1.0_marcas** = object { response }

---

### GET `/v1.0/produto/setores`

**Resumo:** Listar setores de produtos

Retorna os setores distintos cadastrados para os produtos.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |

**Respostas:**

- `200` OK — **response_v1.0_setores** = object { response }

---

### GET `/v1.0/produto/setoresdeposito`

**Resumo:** Listar setores de depósito dos produtos

Retorna os setores de depósito distintos cadastrados na tabela produto unidade.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |

**Respostas:**

- `200` OK — **response_v1.0_setoresdeposito** = object { response }

---

### GET `/v1.0/produto/tipos`

**Resumo:** Listar tipos de produtos

Retorna os tipos de produtos maiores que zero, sem repetições e ordenados.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |

**Respostas:**

- `200` OK — **response_v1.0_tipos** = object { response }

---

### GET `/v1.0/produto/{codigo}`

**Resumo:** Consultar cadastro de um produto

Consultar o cadastro geral de um produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Codigo do produto a ser consultado |

**Respostas:**

- `200` Dados carregados — **ConsultarCadastroProdutoResponse** = object { response }

---

### GET `/v1.0/produtos/alterados/dthrmanutencao/{dthrmanutencao}`

**Resumo:** Obter produtos alterados na data informada

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `dthrmanutencao` | path | sim | string | Data e hora de manutenção do produto |

**Respostas:**

- `200` Requisição processada com sucesso — **alterados_dthrmanutencao_V_1_0** = object { response }

---

### GET `/v1.0/produtosFornecedores/lastRelease/{lastRelease}`

**Resumo:** Produtos e fornecedores

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |
| `lastRelease` | path | sim | integer | Código do último produto-fornecedor consultado. Envie "0" caso queira consultar todos os produtos-fornecedores (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` OK — **response_v1.0_produtosFornecedores** = object { response }

---

### GET `/v1.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/estoque/datahoraalteracao/{datahora}`

**Resumo:** Obter dados do produto

Consulta de produtos com estoque alterado a partir da data e hora. informada.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação. |
| `lastID` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados). |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar. |
| `datahora` | path | sim | string | Data e hora da alteração do estoque. Utilizar no formato "dd-MM-yyyy HH:mm:ss." |
| `marca` | query | não | string | Marca do produto a ser filtrado. |
| `grupo` | query | não | string | Grupo do produto a ser filtrado. |
| `camposExtra` | query | não | string | Deve ser adicionado neste formato: &camposExtra=prod_extra12=9;prun_extra7=10;prun_extra23=15. Separado por ';'. Ele aceita campos extra da tabela Produtos e ProdUn. |
| `departamentos` | query | não | string | Departamentos dos produtos que deseja filtrar separados por ';' |
| `limit` | query | não | string | Limite de registros a serem retornados por requisição, Default 100 |

**Respostas:**

- `200` Dados carregados — **ConsultarEstoqueAlterado** = object { response }

---

### GET `/v1.0/produtounidade/ofertas`

**Resumo:** Ofertas de produtos por unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |
| `unidade` | query | sim | string |  |
| `departamento` | query | não | string |  |
| `setor` | query | não | string |  |
| `lastId` | query | não | integer |  |
| `limit` | query | não | integer |  |

**Respostas:**

- `200` OK — **response_v1.0_produtounidade_ofertas** = object { status, appVersion, messages, content }

---

### GET `/v1.0/produtounidade/unidade/{cnpj}/estoquediario`

**Resumo:** Consultar estoque de produto

Consultar estoque de produto utilizando filtros de departamento, grupo, marca, clase e/ou tipo

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` |  | não |  |  |
| `datainicial` | query | sim | string | Data inicial a ser consultada o estoque (Formato dd-MM-yyyy) |
| `datafinal` | query | sim | string | Data final a ser consultada o estoque (Formato dd-MM-yyyy) |
| `departamento` | query | sim | number | Código do departamento dos produtos a serem consultados |
| `grupo` | query | sim | number | Código do grupo dos produtos a serem consultados |
| `marca` | query | sim | string | Marca dos produtos a serem consultados |
| `classe` | query | sim | string | Classe dos produtos a serem consultados |
| `tipo` | query | sim | string | Tipo dos produtos a serem consultados |

**Respostas:**

- `200`  — **EstoqueByProdutoFilter** = object { response }

---

### GET `/v1.0/produtounidade/unidade/{cnpj}/produto/{codigo}/snapshotbyday`

**Resumo:** Consultar estoque de produto de forma diária

Consultar estoque de produto de forma diária entre datas inicial e final - Período máximo de 31 dias

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` |  | não |  |  |
| `cnpj` |  | não |  |  |
| `datainicial` | query | sim | string | Data inicial a ser consultada o estoque (Formato dd-MM-yyyy) |
| `datafinal` | query | sim | string | Data final a ser consultada o estoque (Formato dd-MM-yyyy) |
| `especies` | query | não | string | Espécie do movimento, não enviar para considerar todas |
| `estoques` | query | não | string | Estoques a considerar dos movimentos de entrada ou saida, não enviar para considerar todos |

**Respostas:**

- `200`  — **SnapshotDailyResponse** = object { response }

---

### GET `/v1.0/produtounidade/unidade/{cpnj}/estoquedisponivel`

**Resumo:** Consulta o Estoque Disponível dos produtos enviados para a unidade informada

Consulta o Estoque Disponível dos produtos enviados para a unidade informada de maneira paralelizada, sendo o (tempo/quant de produtos) menor quando consultado mais que 5 produtos

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cpnj` | path | sim | string | CNPJ da unidade a consultar |
| `codigos` | query | sim | number | lista de códigos de produtos a serem consultados separados por vírgula (,) |

**Respostas:**

- `200`  — **ConsultarEstoqueDisponivel** = object { response }

---

### GET `/v1.0/produtounidade/{codigoproduto}/unidade/{CNPJ}/imagens`

**Resumo:** Consultar imagens de um produto

Consultar imagens de um produto de uma determinada unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigoproduto` | path | sim | number | Codigo do produto a ser consultado |
| `CNPJ` | path | sim | string | CNPJ da unidade |

**Respostas:**

- `200` Dados carregados — **ConsultarImagensProdResponse** = object { response }

---

### PUT `/v1.0/produtounidade/{codigo}/unidade/{CNPJ}/marcado`

**Resumo:** Alterar o campo marcado do produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do produto |
| `CNPJ` | path | sim | string | CNPJ/CPF da unidade |

**Request body** (application/json, obrigatório: True):

- **ProdutoMarcadoPut_V1** = object { marcado }

**Respostas:**

- `200` Dados gravados com sucesso. — **RespostaPadrao** = object { response }

---

### GET `/v1.0/produtounidade/{codigo}/unidade/{CNPJ}/precoUnidadeMedida`

**Resumo:** Preço da Unidade de Medida

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do produto |
| `CNPJ` | path | sim | string | CNPJ/CPF da unidade |

**Respostas:**

- `200` processado com sucesso — **RespostaUnMedida** = object { response }

---

### PUT `/v1.0/produtounidade/{codigo}/unidade/{cnpjOrCodigo}`

**Resumo:** Atualiza produto unidade

Editar cadastro de um produto unidade - use 'eraseExtras' para setar os campos extras acima do extra9 para 'null'

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |
| `codigo` | path | sim | number | Código do produto |
| `cnpjOrCodigo` | path | sim | string | Código ou CNPJ da unidade |

**Request body** (application/json, obrigatório: False):

- **v1_0_produtounidade_codigo_unidade_cnpjOrCodigo_requestbody** = object { setor, setorDep, etq, ctz, tecla, espaco, pzRepos, pzEntrega, diasSeg, validade, valMinima, marcado, bloqueado, margem, margemMin, comissao, difCusto, difVenda, emb, qEmb, etqMag, tpAltPrVenda, difCusto1, difCusto2, difCusto3, difCusto4, difCusto5, difVenda1, difVenda2, difVenda3, difVenda4, difVenda5, fAquisicao, frentes, codigoSim, margem3, margem4, margem5, etiquetas, sensCodigo, estAbastMin, compCodigo, vmd, extra1, extra2, extra3, extra4, extra5, extra6, extra7, extra8, extra9, extra10, extra11, extra12, extra13, extra14, extra15, extra16, extra17, extra18, extra19, extra20, extra21, extra22, extra23, extra24, extra25, extra26, extra27, extra28, extra29, extra30, extra31, extra32, extra33, extra34, extra35, extra36, extra37, extra38, extra39, extra40, extra41, extra42, extra43, extra44, extra45, extra46, extra47, extra48, extra49, extra50, extra51, extra52, extra53, extra54, extra55, extra56, extra57, extra58, extra59, extra60, extra61, extra62, extra63, extra64, extra65, extra66, extra67, extra68, extra69, extra70, extra71, extra72, extra73, extra74, extra75, extra76, extra77, extra78, extra79, extra80, extra81, extra82, extra83, extra84, extra85, extra86, extra87, extra88, extra89, extra90, extra91, extra92, extra93, extra94, extra95, extra96, extra97, extra98, extra99, eraseExtras }

**Respostas:**

- `200`  — **v1_0_produtounidade_codigo_unidade_cnpjOrCodigo_response** = object { response }

---

### GET `/v1.0/produtounidade/{codigo}/unidade/{unidade}/custos`

**Resumo:** Cálculo de custos do produto/unidade

Calcula e retorna os custos, preços sugeridos, margens e impostos (ICMS/ICMS-ST, PIS/COFINS,
IPI, ISS, FCP, partilha de ICMS, restituição de quebra ST, etc.) de um produto/unidade,
delegando ao mesmo cálculo usado internamente pelo ERP (equivalente a
TGeral.CalculaCustosProdUn do Delphi).

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | integer | Código do produto |
| `unidade` | path | sim | string | Código da unidade |

**Respostas:**

- `200` JSON com os custos calculados do produto/unidade — **ProdUnCustos_V_1_0** = object { response }

---

### GET `/v1.0/tabemb`

**Resumo:** Obter cadastro de embalagens

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Dados de tipo de embalagens — **ResponseCadTabEmb_V_1_0** = object { response }

---

### GET `/v1.1/grupos`

**Resumo:** Consultar o cadastro de grupos de produtos

Consultar o cadastro de grupos de produtos do ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Cadastro de grupos recuperado — **ConsultarCadGruposResponse** = object { response }

---

### POST `/v1.1/grupos`

**Resumo:** Inserir o cadastro de grupos de produtos

Inserir o novo cadastro de grupos de produtos do ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **InserirGrupoV_1_00** = object { classificacao, descricao, prodServ, decimaisEst, recuo, periodos, codigoNCM, comissao, dpto_codigo, comportamento, classFiscal, tipoItem, dtEstMin, ctrlEstMin, percAbast, abatimento }

**Respostas:**

- `200` Grupo inserido — **InserirGrupoResponseV1_1** = object { response }

---

### PUT `/v1.1/grupos/{codigo}`

**Resumo:** Alterar o cadastro de grupos de produtos

Alterar o cadastro de grupos de produtos do ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | integer | codigo do cadastro do grupo de produtos a ser editado |

**Request body** (application/json, obrigatório: True):

- **InserirGrupoV_1_00** = object { classificacao, descricao, prodServ, decimaisEst, recuo, periodos, codigoNCM, comissao, dpto_codigo, comportamento, classFiscal, tipoItem, dtEstMin, ctrlEstMin, percAbast, abatimento }

**Respostas:**

- `200` Grupo alterado — **UpdateGrupoResponseV1_1** = object { response }

---

### DELETE `/v1.1/grupos/{codigo}`

**Resumo:** Deletar o cadastro de grupos de produtos

Deletar o cadastro de grupos de produtos do ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | integer | codigo do cadastro do grupo de produtos a ser deletado |

**Respostas:**

- `200` Grupo deletado — **DeleteGrupoResponseV1_1** = object { response }

---

### POST `/v1.1/metasprod`

**Resumo:** Inserir novas Metas de Produtos

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: False):

- **bodyMetasProd_V1_1** = object { metas }

**Respostas:**

- `200` Meta gravada com sucesso — **metasProdSucess** = object { response }

---

### PUT `/v1.1/metasprod`

**Resumo:** Alterar Meta de Produto cadastrada

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: False):

- **bodyMetasProd_V1_1** = object { metas }

**Respostas:**

- `200` Meta gravada com sucesso — **metasProdSucess** = object { response }

---

### GET `/v1.1/metasprod/cnpj/{cnpj}`

**Resumo:** Consultar Metas de Produtos de uma unidade

Consultar metas de produtos de uma unidade, podendo ser filtrado por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` | path | sim | string | Cnpj da unidade |
| `data` | query | não | string | Data inicio a ser considerada, sendo retornado datas iguais ou maiores que a informada |
| `tipo` | query | não | string | Filtro por tipo de metas: 'Dia' - Diária; 'Mes' - Mensal |
| `agrupamento` | query | não | string | Filtro por agrupamento de metas: 'Grupos', 'Deptos' (Departamentos), 'Produtos', 'Unidades' |

**Respostas:**

- `200` Dados carregados com sucesso — **getMetasProd_V1_1** = object { response }

---

### GET `/v1.1/precadastro`

**Resumo:** Obter dados de pré cadastro do produto

Obter dados de pré cadastro de produtos

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` PreCadastro de produto recuperado com sucesso — **ConsultarPreCadastrosV_1_1** = object { response }

---

### POST `/v1.1/precadastro`

**Resumo:** Inserir dados de pré cadastro do produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **ProdutoPreCadastroV1_1** = object { unid_codigo, status, descricao, complemento, marca, codBarras, descrPdvs, emb, qemb, prod_Codigo, dtCadastro, horaCadastro, dtLiberacao, horaLiberacao, codNcm, obs, balanca, peso, pesoLiq, prodFuncao, cest, codCaixa, lastro, camadas, forn_Codigo, validade, altura, largura, profundidade, codProdFor, tiposTroca, grupo, departamento, formaAquisicao }

**Respostas:**

- `200` PreCadastro de produto recuperado com sucesso — **InsertPreCadastroV_1_0** = object { response }

---

### GET `/v1.1/precadastro/{sequencia}`

**Resumo:** Obter dados de pré cadastro do produto

Obter dados de pré cadastro do produto incluído pelo endPoint de inclusão de pré Cadastro

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `sequencia` | path | sim | number | Sequencia de indentificação do pré cadastro |

**Respostas:**

- `200` PreCadastro de produto recuperado com sucesso — **ConsultarPreCadastroV_1_1** = object { response }

---

### GET `/v1.1/produto/codigobarrasalterados/ativos/unidade/{unidade}/lastid/{lastID}`

**Resumo:** Obter dados de códigos de barras alternativos dos produtos ativos

Obter dados de códigos de barras alternativos para os produtos ativos

Este serviço irá retornar os itens páginados conforme configuração no servidor

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `unidade` | path | sim | string | Unidade do cliente |
| `lastID` | path | sim | number | Codigo do ultimo produto que retornou na lista. Para a primeira página de registros enviar esse valor igual a zero. (mesmo passando 0 os dados retornam paginados) |
| `loadPrecoUnidadeMedida` | query | não | boolean | Se informado e marcado como 'true', será retornado o Preço de Venda baseado na Unidade de Medida do Produto |

**Respostas:**

- `200` Dados carregados — **ConsultarCodBarrasAlternativoListaResponseV11** = object { response }

---

### GET `/v1.1/produto/codigobarrasalterados/lastid/{lastID}`

**Resumo:** Obter dados de códigos de barras alternativos

Obter dados de códigos de barras alternativos para o produto

Este serviço irá retornar os itens páginados conforme configuração no servidor

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Codigo do ultimo produto que retornou na lista. Para a primeira página de registros enviar esse valor igual a zero. (mesmo passando 0 os dados retornam paginados) |
| `dataAlteracao` | query | não | string | Data de alteração ( dd-MM-yyyy ) a ser considerada para alterações posteiores ou iguais a data informada |
| `loadPrecoUnidadeMedida` | query | não | boolean | Se informado e marcado como 'true', será retornado o Preço de Venda baseado na Unidade de Medida do Produto |

**Respostas:**

- `200` Dados carregados — **ConsultarCodBarrasAlternativoListaResponseV11** = object { response }

---

### GET `/v1.1/produto/excluidos/lastid/{lastid}/dataexclusao/{dataexclusao}`

**Resumo:** Obter dados dos produtos excluidos

Recuperar produtos excluidos com data de exclusão acima da data informada (prod_status ='C')

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastid` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `dataexclusao` | path | sim | string | Data a ser consultada. Formato data: (DD-MM-AAAA) |

**Respostas:**

- `200` Dados carregados com sucesso — **ConsultarProdutoExcluidosV10** = object { response }

---

### PUT `/v1.1/produto/{codigo}`

**Resumo:** Editar cadastro de um produto

Editar cadastro de um produto - use 'eraseExtras' para setar os campos extras acima do extra9 para 'null'

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | código do produto |

**Request body** (application/json, obrigatório: False):

- **EditProdutoV_1_1** = `EditProdutoV_1_0` (ver reference/schemas.md) & `CamposExtras_10_ao_99` (ver reference/schemas.md)

**Respostas:**

- `200`  — **RespostaEditProdutoV_1_0** = object { response }

---

### GET `/v1.1/produto/{codigo}/codigobarrasalterados`

**Resumo:** Obter dados de códigos de barras alternativos

Obter dados de códigos de barras alternativos para o produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Codigo do produto |
| `loadPrecoUnidadeMedida` | query | não | boolean | Se informado e marcado como 'true', será retornado o Preço de Venda baseado na Unidade de Medida do Produto |

**Respostas:**

- `200` Dados carregados — **ConsultarCodBarrasAlternativoProdResponseV11** = object { response }

---

### GET `/v1.1/produto/{codigo}/detalhado`

**Resumo:** Consultar cadastro de um produto

Consultar o cadastro detalhado de um produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Codigo do produto a ser consultado |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |

**Respostas:**

- `200` Dados carregados — **ConsultarCadastroProdutoDetalhadoResponseV2** = object { response }

---

### GET `/v1.1/produto/{prodCodigo}/fornecedor/{fornCodigo}`

**Resumo:** Obter dados dos códigos do fornecedor vinculados a um produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |
| `prodCodigo` | path | sim | string | Código interno do produto a ser consultado |
| `fornCodigo` | path | sim | string | Código interno do fornecedor a ser consultado |

**Respostas:**

- `200`  — **ProdutoFornecedorResponse_V_1_1** = object { response }

---

### GET `/v1.2/produto/listaprodutos/{lastId}`

**Resumo:** Consultar cadastro de um produto

Consultar o cadastro geral de um produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | number | Codigo do ultimo produto que retornou na lista. Para a primeira página de registros enviar esse valor igual a zero. (mesmo passando 0 os dados retornam paginados) |
| `codPreco` | query | não | string | Filtra os produtos por código de preço |
| `departamentos` | query | não | boolean | Filtra os produtos por departamentos vinculados ao usuario externo. |

**Respostas:**

- `200` Dados carregados — **ConsultarCadastroProdutosResponse** = object { response }

---

### GET `/v1.2/produto/listaprodutos/{lastId}/detalhado`

**Resumo:** Consultar cadastro de um produto

Consultar o cadastro detalhado de um produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | number | Codigo do ultimo produto que retornou na lista. Para a primeira página de registros enviar esse valor igual a zero. (mesmo passando 0 os dados retornam paginados) |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |
| `departamentos` | query | não | string | Departamentos dos produtos que deseja filtrar separados por ';' |
| `limit` | query | não | string | Limite de registros a serem retornados por requisição, Default 100 |

**Respostas:**

- `200` Dados carregados — **ConsultarCadastroProdutosDetalhadoResponseV2** = object { response }

---

### GET `/v1.3/produtos/lastid/{lastId}/fornecedor/{codigo}`

**Resumo:** Obter dados dos produtos vinculados ao fornecedor

Obter dados dos produtos vinculados ao fornecedor informado, sendo resultado paginado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Código do último produto consultado. Envie '0' caso queira consultar todos os produtos (mesmo passando 0 os dados retornam paginados) |
| `codigo` | path | sim | string | Código interno do fornecedor a ser consultado |
| `dhmanutencaoinicial` | query | não | string | Data Inicial do período (Formato "dd-mm-yyyy") |
| `dhmanutencaofinal` | query | não | string | Data Final do período (Formato "dd-mm-yyyy") |

**Respostas:**

- `200`  — **ProdutosFornecedorRes_V_1_3** = object { response }

---

### GET `/v1.3/usuariosexternos/{codigo}`

**Resumo:** Obter dados do usuario externo

Obter dados do usuario externo do sistema ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Codigo do usuario externo |

**Respostas:**

- `200` Dados do usuário retornado — **ConsultarDadosUsuarioExternoResponse_V_1_3** = object { response }

---

### GET `/v1.4/cestabasica/listarcestas/lastid/{lastId}`

**Resumo:** Consultar o cadastro de cestas básicas

Consultar o cadastro de cestas básicas do ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Último código de cesta lido, quando for a primeira leitura informar "0"  (mesmo passando 0 os dados retornam paginados) |
| `codigo` | query | não | string | retorna a cesta basica de acordo com o codigo especificado. |
| `unidade` | query | não | number | retorna a cesta basica de acordo com a unidade especificado. |
| `limit` | query | não | number | retorna a cesta basica de acordo com o limit especificado. |

**Respostas:**

- `200` Cadastro de cestas básicas recuperado — **ConsultarCestasBasicasResponseV2** = object { response }

---

### GET `/v2.8/produtounidade/listaprodutos/{codigo}/unidade/{CNPJ}`

**Resumo:** Obter dados do produto

Consulta dados de um determinado produto de um grupo

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Codigo do produto a ser consultado |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `considerarcancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco2` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |
| `departamentos` | query | não | string | Departamentos dos produtos que deseja filtrar separados por ';' |
| `limit` | query | não | string | Limite de registros a serem retornados por requisição, Default 100 |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoV28** = object { response }

---

### GET `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/departamento/{departamento}`

**Resumo:** Obter dados do produto

Consulta dados de um determinado produto de um departamento

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto que retornou da lista. Para solicitar a primeira página de informações, enviar :lastID igual a zero.  (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `departamento` | path | sim | string | Código do departamento a consultar |
| `considerarcancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco2` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoV28** = object { response }

---

### GET `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/grupo/{grupo}`

**Resumo:** Obter dados do produto

Consulta dados de um determinado produto de um grupo

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto que retornou da lista. Para solicitar a primeira página de informações, enviar :lastID igual a zero. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `grupo` | path | sim | string | Código do grupo a consultar |
| `considerarcancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco2` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoV28** = object { response }

---

### GET `/v2.8/produtounidade/{codBarras}/unidade/{CNPJ}/estoquecodigobarras`

**Resumo:** Obter dados do produto

Obter dados do produto pelo código de barras

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codBarras` | path | sim | string | Codigo de barras do produto |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `considerarcancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco2` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |

**Respostas:**

- `200` Dados carregados — **ConsultarEstProdutoResponseV28** = object { response }

---

### GET `/v2.8/produtounidade/{codigoBarras}/unidade/{CNPJ}/consultarcodigobarras`

**Resumo:** Obter estoque do produto

Obter estoque do produto para a unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigoBarras` | path | sim | string | Codigo de barras do produto |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `considerarcancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco2` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoResponseV28** = object { response }

---

### GET `/v2.8/produtounidade/{codigo}/unidade/{CNPJ}`

**Resumo:** Obter estoque do produto

Obter estoque do produto para a unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do produto |
| `CNPJ` | path | sim | string | CNPJ da unidade que deseja consultar estoque |
| `considerarcancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco2` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |

**Respostas:**

- `200` Dados carregados — **ProdutoComEstoqueV28** = object { Codigo, SKU, CodigoBarras, CodigoNCM, Descricao, DescricaoCliente, Complemento, Marca, Status, Preco, Estoque, Grupo, Oferta, DataOferta, PrecoNormal, CodigoUnidade, CodigoDepartamento, Departamento, Ativo, CodigoTributario, Estoque1, Estoque2, Estoque3, Estoque4, Estoque5, PrecoLista, PrecoPDV, PrecoPDV2, PrecoPDV3, PrecoPDV4, PrecoPDV5, PrecoEtiqueta, PrecoCartaz, PrecoVenda2, PrecoVenda3, PrecoVenda4, PrecoVenda5, FatorPr3, FatorPr4, FatorPr5, CodEstoque, EstoqueMinimo, EstoqueMaximo, VendaMediaDiaria, Espaco, CodigoCaixa, CustoCompra, CustoEmpresa, CustoFiscal, CustoMedio, CustoTranferencia, SetorLoja, SetorDeposito, PrecoUnidadeMedida, DescricaoPDV, TipoEmbalagem, QuantidadeEmbalagem, DataHoraManutencao }

---

### GET `/v2.8/produtounidade/{codigo}/unidade/{CNPJ}/estoque`

**Resumo:** Obter estoque do produto

Obter estoque do produto para a unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do produto |
| `CNPJ` | path | sim | string | CNPJ da unidade que deseja consultar estoque |
| `considerarcancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco2` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |

**Respostas:**

- `200` Dados carregados — **ProdutoComEstoqueV28** = object { Codigo, SKU, CodigoBarras, CodigoNCM, Descricao, DescricaoCliente, Complemento, Marca, Status, Preco, Estoque, Grupo, Oferta, DataOferta, PrecoNormal, CodigoUnidade, CodigoDepartamento, Departamento, Ativo, CodigoTributario, Estoque1, Estoque2, Estoque3, Estoque4, Estoque5, PrecoLista, PrecoPDV, PrecoPDV2, PrecoPDV3, PrecoPDV4, PrecoPDV5, PrecoEtiqueta, PrecoCartaz, PrecoVenda2, PrecoVenda3, PrecoVenda4, PrecoVenda5, FatorPr3, FatorPr4, FatorPr5, CodEstoque, EstoqueMinimo, EstoqueMaximo, VendaMediaDiaria, Espaco, CodigoCaixa, CustoCompra, CustoEmpresa, CustoFiscal, CustoMedio, CustoTranferencia, SetorLoja, SetorDeposito, PrecoUnidadeMedida, DescricaoPDV, TipoEmbalagem, QuantidadeEmbalagem, DataHoraManutencao }

---

### GET `/v3.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/grupo/{grupo}`

**Resumo:** Obter dados dos produtos

Consulta dados detalhados dos produtos de um determinado grupo.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `grupo` | path | sim | string | Código do grupo |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |
| `loadtributacao` | query | não | boolean | Se informado e marcado como 'true', será retornada a tributacao do produto no atributo 'tributacao', se encontrar tributação retornará como null |
| `considerarcancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco2` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |
| `loadCodBarrasAlt` | query | não | boolean | Se informado e marcado como 'true', será retornado os códigos de barras alternativos de cada produto |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV31** = object { response }

---

### GET `/v3.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/marcados`

**Resumo:** Obter dados dos produtos

Consulta dados detalhados dos produtos que estão marcados.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |
| `loadtributacao` | query | não | boolean | Se informado e marcado como 'true', será retornada a tributacao do produto no atributo 'tributacao', se encontrar tributação retornará como null |
| `considerarcancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco2` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |
| `loadCodBarrasAlt` | query | não | boolean | Se informado e marcado como 'true', será retornado os códigos de barras alternativos de cada produto |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoComEstoqueV31** = object { response }

---

### GET `/v3.2/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado`

**Resumo:** Obter dados dos produtos

Consulta dados detalhados dos produtos com informação de estoque.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |
| `loadtributacao` | query | não | boolean | Se informado e marcado como 'true', será retornada a tributacao do produto no atributo 'tributacao', se nãoencontrar tributação retornará como null |
| `considerarcancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco2` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |
| `codPreco` | query | não | string | Filtra os produtos por código de preço |
| `loadCodBarrasAlt` | query | não | boolean | Se informado e marcado como 'true', será retornado os códigos de barras alternativos de cada produto |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV32** = object { response }

---

### GET `/v3.2/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos`

**Resumo:** Lista de produtos ativos detalhado

Busca da lista de produtos ativos detalhado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | não | string | token de autenticação |
| `lastID` | path | sim | string | Código do último produto consultado. Envie "0" caso queira consultar todos os produtos  (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |
| `loadtributacao` | query | não | boolean | Se informado e marcado como 'true', será retornada a tributacao do produto no atributo 'tributacao', se encontrar tributação retornará como null |
| `considerarcancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco2` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |
| `loadCodBarrasAlt` | query | não | boolean | Se informado e marcado como 'true', será retornado os códigos de barras alternativos de cada produto |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV31** = object { response }

---

### GET `/v3.2/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos/dataHoraManutencao/{dataHoraManutencao}`

**Resumo:** Lista de produtos ativos detalhado

Busca da lista de produtos ativos detalhado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | não | string | token de autenticação |
| `lastID` | path | sim | string | Código do último produto consultado. Envie "0" caso queira consultar todos os produtos  (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `dataHoraManutencao` | path | sim | string | Data e hora de alteração cadastro padrão dd-MM-yyyy HH:mm:ss |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |
| `loadtributacao` | query | não | boolean | Se informado e marcado como 'true', será retornada a tributacao do produto no atributo 'tributacao', se encontrar tributação retornará como null |
| `loadCodBarrasAlt` | query | não | boolean | Se informado e marcado como 'true', será retornado os códigos de barras alternativos de cada produto |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV32** = object { response }

---

### GET `/v3.2/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/departamento/{departamento}`

**Resumo:** Obter dados dos produtos

Consulta dados detalhados dos produtos de um determinado departamento.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `departamento` | path | sim | string | Código do departamento |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |
| `loadtributacao` | query | não | boolean | Se informado e marcado como 'true', será retornada a tributacao do produto no atributo 'tributacao', se encontrar tributação retornará como null |
| `considerarcancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco2` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |
| `loadCodBarrasAlt` | query | não | boolean | Se informado e marcado como 'true', será retornado os códigos de barras alternativos de cada produto |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV32** = object { response }

---

### GET `/v3.2/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/grupo/{grupo}`

**Resumo:** Obter dados dos produtos

Consulta dados detalhados dos produtos de um determinado grupo.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `grupo` | path | sim | string | Código do grupo |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |
| `loadtributacao` | query | não | boolean | Se informado e marcado como 'true', será retornada a tributacao do produto no atributo 'tributacao', se encontrar tributação retornará como null |
| `considerarcancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco2` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |
| `loadCodBarrasAlt` | query | não | boolean | Se informado e marcado como 'true', será retornado os códigos de barras alternativos de cada produto |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV32** = object { response }

---

### GET `/v3.2/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/semcalcularestoque`

**Resumo:** Obter dados dos produtos

Consulta dados detalhados dos produtos sem calcular estoque.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |
| `loadtributacao` | query | não | boolean | Se informado e marcado como 'true', será retornada a tributacao do produto no atributo 'tributacao', se encontrar tributação retornará como null |
| `considerarcancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco2` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |
| `loadCodBarrasAlt` | query | não | boolean | Se informado e marcado como 'true', será retornado os códigos de barras alternativos de cada produto |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV32** = object { response }

---

### GET `/v3.2/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/setor/{setor}`

**Resumo:** Obter dados dos produtos

Consulta dados detalhados dos produtos de um determinado setor.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `setor` | path | sim | string | Código do setor |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |
| `loadtributacao` | query | não | boolean | Se informado e marcado como 'true', será retornada a tributacao do produto no atributo 'tributacao', se encontrar tributação retornará como null |
| `considerarcancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco2` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |
| `loadCodBarrasAlt` | query | não | boolean | Se informado e marcado como 'true', será retornado os códigos de barras alternativos de cada produto |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV32** = object { response }

---

### GET `/v3.2/produtounidade/listaprodutos/{lastId}/unidade/{CNPJ}/detalhado/dataHoraManutencao/{dataHoraManutencao}`

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` |  | não |  |  |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `dataHoraManutencao` | path | sim | string | Data e hora de alteração (dd-MM-yyyy HH:mm:ss) |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |
| `loadtributacao` | query | não | boolean | Se informado e marcado como 'true', será retornada a tributacao do produto no atributo 'tributacao', se encontrar tributação retornará como null |
| `considerarcancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco2` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |
| `loadCodBarrasAlt` | query | não | boolean | Se informado e marcado como 'true', será retornado os códigos de barras alternativos de cada produto |
| `departamentos` | query | não | string | Departamentos dos produtos que deseja filtrar separados por ';' |
| `limit` | query | não | string | Limite de registros a serem retornados por requisição, Default 100 |

**Respostas:**

- `200`  — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV32** = object { response }

---

### GET `/v3.2/produtounidade/{codigoBarras}/unidade/{CNPJ}/detalhado/consultarcodigobarras`

**Resumo:** Obter dados do produto

Consulta dados detalhados de um determinado produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigoBarras` | path | sim | number | Código de barras do produto |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |
| `loadtributacao` | query | não | boolean | Se informado e marcado como 'true', será retornada a tributacao do produto no atributo 'tributacao', se encontrar tributação retornará como null |
| `considerarcancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco2` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |
| `loadCodBarrasAlt` | query | não | boolean | Se informado e marcado como 'true', será retornado os códigos de barras alternativos de cada produto |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoDetalhadoV32** = object { response }

---

### GET `/v3.2/produtounidade/{codigo}/unidade/{CNPJ}/detalhado`

**Resumo:** Obter dados do produto

Consulta dados detalhados de um determinado produto.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do produto |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |
| `loadtributacao` | query | não | boolean | Se informado e marcado como 'true', será retornada a tributacao do produto no atributo 'tributacao', se encontrar tributação retornará como null |
| `considerarcancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco2` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |
| `loadCodBarrasAlt` | query | não | boolean | Se informado e marcado como 'true', será retornado os códigos de barras alternativos de cada produto |

**Respostas:**

- `200`  — **ConsultarProdutoDetalhadoV32** = object { response }

---

### GET `/v3.2/produtounidade/{codigo}/unidade/{CNPJ}/detalhado/estoque`

**Resumo:** Obter dados do produto

Consulta dados detalhados do produto.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do produto |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |
| `loadtributacao` | query | não | boolean | Se informado e marcado como 'true', será retornada a tributacao do produto no atributo 'tributacao', se encontrar tributação retornará como null |
| `considerarcancelados` | query | não | boolean | Se informado e marcado como 'true', serão retornados produtos cancelados/excluídos |
| `somentePreco2` | query | não | boolean | Se informado e marcado como 'true', serão retornados apenas produtos que tenham preço 2 cadastro |
| `loadCodBarrasAlt` | query | não | boolean | Se informado e marcado como 'true', será retornado os códigos de barras alternativos de cada produto |

**Respostas:**

- `200`  — **ConsultarProdutoEstoqueDetalhadoComEstoqueV32** = object { response }

---

### GET `/v3.3/produtounidade/listaprodutos/{lastRelease}/unidade/{CNPJ}/detalhado/customrelease`

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `limit` | query | sim | string | Total de registros por página |
| `fieldName` | query | sim | number | Nome do campo de release customizado |
| `lastRelease` | path | sim | number | Código do último release consultado. Envie "0" caso queira consultar desde o primeiro release (mesmo passando 0 os dados retornam paginados) |
| `loadCodBarrasAlt` | query | não | boolean | Se informado e marcado como 'true', será retornado os códigos de barras alternativos de cada produto |
| `loadtributacao` | query | não | boolean | Se informado e marcado como 'true', será retornado as informações de tributação de cada produto |
| `estoquedisponivel` | query | não | boolean | Se informado e marcado como 'true', será retornado as informações de estoque disponível de cada produto |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado as informações dos campos extras customizados de cada produto |
| `departamentos` | query | não | string | Filtra os produtos pelos departamentos informados. Aceita múltiplos códigos separados por ';' |

**Respostas:**

- `200`  — **ConsultarProdutoEstoqueDetalhadoCustomReleaseV32** = object { response }

---
