# Tag 00016 — Dados referentes a Fornecedores

13 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| POST | `/v1.0/fornecedor` | Inserir dados do fornecedor |  |
| GET | `/v1.0/fornecedor/listaFornecedores/release/{releaseNumber}` | Busca de fornecedores por Release |  |
| GET | `/v1.0/fornecedor/pedidosbaixados/lastid/{lastId}/unidade/{cnpjUnid}/datainicial/{dataInicial}/datafinal/{dataFinal}` | Pedidos baixados |  |
| PUT | `/v1.0/fornecedor/{codigo}` | Alterar dados do fornecedor |  |
| GET | `/v1.0/tabforn/lastRelease/{lastRelease}` | Ler dados de produtos do fornecedor |  |
| GET | `/v1.0/tiposforn/listatiposforn/{lastId}` | Tipos de Fornecedores |  |
| PUT | `/v1.1/fornecedor/situacao` | Alterar situação do fornecedor |  |
| GET | `/v1.1/fornecedor/{codigo}/regranegocio` | Cadastro dos Fornecedores |  |
| GET | `/v1.4/fornecedor/listaFornecedores/lastid/{lastId}/datahoramanutencao/{datahoramanutencao}` | Cadastro dos Fornecedores |  |
| GET | `/v1.4/fornecedor/listaFornecedores/lastid/{lastId}/tipos/{tipos}` | Fornecedores filtrados pelo tipo |  |
| GET | `/v1.5/fornecedor` | Fornecedor filtrado pelo código, cpf ou lastid |  |
| GET | `/v1.5/fornecedor/cnpj_cpf/{cnpj_cpf}` | Fornecedor filtrado pelo CPF ou CNPJ |  |
| GET | `/v1.5/fornecedor/listaFornecedores/lastid/{lastId}` | Cadastro dos Fornecedores |  |

## Detalhes

### POST `/v1.0/fornecedor`

**Resumo:** Inserir dados do fornecedor

Inserir dados de cadastro do fornecedor

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **InsertFornecedorV1_0** = object { cnpjcpf, razaoSocial, nome, email, situacao, status, inscricaoestadual, contribuinte, dtHrManutencao, dataCad, usua_Codigo, enderecoResidencial, fone }

**Respostas:**

- `200` Fornecedor salvo com sucesso — **InsertFornecedorV1_0** = object { cnpjcpf, razaoSocial, nome, email, situacao, status, inscricaoestadual, contribuinte, dtHrManutencao, dataCad, usua_Codigo, enderecoResidencial, fone }

---

### GET `/v1.0/fornecedor/listaFornecedores/release/{releaseNumber}`

**Resumo:** Busca de fornecedores por Release

busca todos os fornecedores acima do numero de release informado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `releaseNumber` | path | sim | string | Número do release a ser consultado |

**Respostas:**

- `200`  — **FornecReleaseListV1_0** = object { response }

---

### GET `/v1.0/fornecedor/pedidosbaixados/lastid/{lastId}/unidade/{cnpjUnid}/datainicial/{dataInicial}/datafinal/{dataFinal}`

**Resumo:** Pedidos baixados

Busca os pedidos baixados de uma unidade dentro de um período

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Código do último fornecedor consultado. Envie "0" caso queira consultar todos os pedidos baixados (mesmo passando 0 os dados retornam paginados) |
| `cnpjUnid` | path | sim | string | CNPJ da unidade a consultar |
| `dataInicial` | path | sim | string | Data em que inicia-se a leitura dos pedidos baixados, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `dataFinal` | path | sim | string | Data em que finaliza-se a leitura dos pedidos baixados, considera-se até o dia atual (Formato "dd-mm-yyyy") |

**Respostas:**

- `200` Dados caregados — **ListaFornecTipoV1_4** = object { status, messages, fornecedores }

---

### PUT `/v1.0/fornecedor/{codigo}`

**Resumo:** Alterar dados do fornecedor

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | boolean | Código de identificação do fornecedor |

**Request body** (application/json, obrigatório: True):

- **UpdateFornecedorV1_0** = object { obsPedidos }

**Respostas:**

- `200` Situação fornecedor alterada com sucesso — **ResponseUpdateFornecedorV1_0** = object { response }

---

### GET `/v1.0/tabforn/lastRelease/{lastRelease}`

**Resumo:** Ler dados de produtos do fornecedor

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastRelease` | path | sim | string | Último Release lido, caso queira consultar desde o início deve-se informar 0 |

**Respostas:**

- `200` Fornecedor salvo com sucesso — **ResponseTabFornV1_0** = object { response }

---

### GET `/v1.0/tiposforn/listatiposforn/{lastId}`

**Resumo:** Tipos de Fornecedores

Busca de Tipos de Fornecedores

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Código do último fornecedor consultado. Envie "0" caso queira consultar todos os fornecedores (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados com sucesso — **ListaTipo** = object { status, message, messages, tiposForn }

---

### PUT `/v1.1/fornecedor/situacao`

**Resumo:** Alterar situação do fornecedor

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` | query | sim | string | cnpj do fornecedor |
| `updateVinculados` | query | não | boolean | indica se atualiza os fornecedores vinculados |
| `updateCnpjRaiz` | query | não | boolean | indica se atualiza os fornecedores com mesmo CNPJ raiz |

**Request body** (application/json, obrigatório: True):

- **UpdateSituacaoFornecedorV1_1** = object { situacao, codigoBloqueio }

**Respostas:**

- `200` Situação fornecedor alterada com sucesso — **ResponseUpdateSituacaoFornecedorV1_0** = object { response }

---

### GET `/v1.1/fornecedor/{codigo}/regranegocio`

**Resumo:** Cadastro dos Fornecedores

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do fornecedor a ser consultado. |
| `cnpjUnidade` | query | sim | string | Cnpj da unidade a ser considerada na consulta. |

**Respostas:**

- `200` Dados carregados com sucesso — **RegraNegocioResponse** = object { response }

---

### GET `/v1.4/fornecedor/listaFornecedores/lastid/{lastId}/datahoramanutencao/{datahoramanutencao}`

**Resumo:** Cadastro dos Fornecedores

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Código do último fornecedor consultado. Envie "0" caso queira consultar todos os fornecedores (mesmo passando 0 os dados retornam paginados) |
| `datahoramanutencao` | path | sim | string | Data e hora a ser considerada para o filtro de manutenções realizadas após a data e hora informada formato "dd-MM-yyyy hh:mm:ss" |

**Respostas:**

- `200` Dados carregados com sucesso — **ListaFornecTipoV1_4** = object { status, messages, fornecedores }

---

### GET `/v1.4/fornecedor/listaFornecedores/lastid/{lastId}/tipos/{tipos}`

**Resumo:** Fornecedores filtrados pelo tipo

Busca de fornecedores, filtrando pelo tipo

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Código do último fornecedor consultado. Envie "0" caso queira consultar todos os fornecedores (mesmo passando 0 os dados retornam paginados) |
| `tipos` | path | sim | string | Tipo do fornecedor |

**Respostas:**

- `200` Dados carregados com sucesso — **ListaFornecTipoV1_4** = object { status, messages, fornecedores }

---

### GET `/v1.5/fornecedor`

**Resumo:** Fornecedor filtrado pelo código, cpf ou lastid

Busca de fornecedor, filtrando pelo código

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | query | não | number | código interno do fornecedor |
| `cpf` | query | não | number | cpf interno do fornecedor |
| `lastid` | query | não | number | lastid para retornar os fornecedores(se enviar 0 retorna todos ja com paginação). |

**Respostas:**

- `200` Dados carregados com sucesso — **FornecedorResponseV1_5** = object { response }

---

### GET `/v1.5/fornecedor/cnpj_cpf/{cnpj_cpf}`

**Resumo:** Fornecedor filtrado pelo CPF ou CNPJ

Busca de fornecedor, filtrando pelo CPF ou CNPJ

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj_cpf` | path | sim | string | cnpj do fornecedor |

**Respostas:**

- `200` Dados carregados com sucesso — **responseFornecedor_V_1_5** = object { response }

---

### GET `/v1.5/fornecedor/listaFornecedores/lastid/{lastId}`

**Resumo:** Cadastro dos Fornecedores

Retorna os fornecedores com todos os status

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Código do último fornecedor consultado. Envie "0" caso queira consultar todos os fornecedores (mesmo passando 0 os dados retornam paginados). |
| `nomeRazaoSocial` | query | não | string | Nome ou Razão Social a ser considerada |
| `status` | query | não | string | Filtra por status do fornecedor |
| `limit` | query | não | number | Número de dados retornados na consulta |

**Respostas:**

- `200` Dados carregados com sucesso — **ListaFornecTipoV1_4** = object { status, messages, fornecedores }

---
