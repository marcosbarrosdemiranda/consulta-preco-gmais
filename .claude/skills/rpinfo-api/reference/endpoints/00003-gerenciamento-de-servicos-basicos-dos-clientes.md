# Tag 00003 — Gerenciamento de serviços básicos dos clientes

8 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| PUT | `/v1.0/clientes/{codigo}/camposextras` | Cadastrar campos extras do cliente |  |
| GET | `/v1.6/clientes/cnpj_cpf/{CPF_CNPJ}` | Obter dados do cliente |  |
| GET | `/v1.6/clientes/email/{email}` | Obter dados do cliente |  |
| PUT | `/v1.8/clientes/{codigo}` | Editar Cliente |  |
| GET | `/v1.9/clientes/lastid/{lastId}` | Obter cadastro de clientes |  |
| POST | `/v2.0/clientes` | Inserir novo cliente |  |
| GET | `/v2.0/clientes/{codigo}` | Obter dados do cliente |  |
| GET | `/v4.0/precocliente/lastid/{lastid}` | Obter preços por cliente |  |

## Detalhes

### PUT `/v1.0/clientes/{codigo}/camposextras`

**Resumo:** Cadastrar campos extras do cliente

Cadastrar ou alterar os campos extras do cliente

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do cliente |

**Request body** (application/json, obrigatório: True):

- **CamposExtrasCliente** = object { Extra1, Extra2, Extra3, Extra4, Extra5, Extra6, Extra7, Extra8, Extra9 }

**Respostas:**

- `200` Dados do cliente — **RespostaPadrao** = object { response }

---

### GET `/v1.6/clientes/cnpj_cpf/{CPF_CNPJ}`

**Resumo:** Obter dados do cliente

Obter dados do cliente pelo CPF/CNPJ

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF_CNPJ` | path | sim | string | CPF/CNPJ do cliente |
| `outrosextras` | query | não | boolean | True para processar os Campos Extras do cliente e retornar o atributo 'camposExtras' |

**Respostas:**

- `200` Dados do cliente — **ResponseCadClientes_v1.6** = object { response }

---

### GET `/v1.6/clientes/email/{email}`

**Resumo:** Obter dados do cliente

Obter dados do cliente pelo email

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `email` | path | sim | string | Email do cliente |

**Respostas:**

- `200` Dados do cliente — **ResponseCadClientes_v1.6** = object { response }

---

### PUT `/v1.8/clientes/{codigo}`

**Resumo:** Editar Cliente

Editar dados de determinado cliente

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do cliente |

**Request body** (application/json, obrigatório: True):

- **Cliente_v1_8** = object { nome, sexo, tipo, tipoCliente, fone, celular, foneComercial, classe, enderecoResidencial, enderecoComercial, dataNascimento, cpf, cnpj, rg, ie, orgaoExpRG, ufExpRG, estadoCivil, profissao, escolaridade, email, contaContabil, contaGerencial, contribuinte, unidadeCadastro, observacao, vendedor, ramoAtividade }

**Respostas:**

- `200` Cliente Alterado — **EnviarDadosNovoClienteResponse** = object { response }

---

### GET `/v1.9/clientes/lastid/{lastId}`

**Resumo:** Obter cadastro de clientes

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastid` | path | sim | number | Código do último cliente consultado. Envie "0" caso queira consultar todos os clientes (mesmo passando 0 os dados retornam paginados) |
| `dtHrManut` | query | não | string | Data e hora de modificação do cadastro dos clientes a ser considerada. Formato 'YYYY-MM-DD hh:mm:ss' |
| `nome` | query | não | string | Nome do cliente. |
| `razaoSocial` | query | não | string | Razão social do cliente. |
| `outrosextras` |  | não |  |  |

**Respostas:**

- `200` Dados do cliente — **ResponseCadClientesLastId_v1.9** = object { response }

---

### POST `/v2.0/clientes`

**Resumo:** Inserir novo cliente

Inserir novo cliente na base de dados

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **Cliente_v2_0** = `Cliente_v1_9` (ver reference/schemas.md) & object { razaoSocial }

**Respostas:**

- `200` Cliente adicionado — **EnviarDadosNovoClienteResponseV2** = object { response }

---

### GET `/v2.0/clientes/{codigo}`

**Resumo:** Obter dados do cliente

Obter dados do cliente pelo código

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do cliente |

**Respostas:**

- `200` Dados do cliente — **ResponseCadClientes_v2.0** = object { response }

---

### GET `/v4.0/precocliente/lastid/{lastid}`

**Resumo:** Obter preços por cliente

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastid` | path | sim | string | lastid é último código lido na página anterior, caso seja a primeira página enviar 0 |

**Respostas:**

- `200` Obter preços de clientes — **PrecosClienteV1_0** = object { response }
- `404` Nenhum registro encontrado — **Error404** = object { appVersion, content }

---
