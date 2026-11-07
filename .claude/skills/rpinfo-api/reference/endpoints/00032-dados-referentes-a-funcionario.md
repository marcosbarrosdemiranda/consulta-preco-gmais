# Tag 00032 — Dados referentes a Funcionário

5 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| POST | `/v1.0/funcionario` | Cadastrar novo funcionário |  |
| PUT | `/v1.0/funcionario/{id}` | Editar cadastro de funcionário |  |
| GET | `/v1.1/funcionario` | Consulta de funcionários |  |
| GET | `/v1.2/funcionario/codcpf/{codcpf}` | Consultar cadastro de funcionário |  |
| GET | `/v1.2/funcionario/lastid/{lastid}` | Consultar cadastro de funcionários |  |

## Detalhes

### POST `/v1.0/funcionario`

**Resumo:** Cadastrar novo funcionário

Cadastrar novo funcionário.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: False):

- **funcionarioInsert** = object { codigo, nome, unidade, nascimento, endereco, enderecoNumero, enderecoComplemento, bairro, codigoMunicipio, cep, nomeMae, nomePai, telefone, estadoCivil, sexo, cor, deficiente, rg, rgUf, rgExpedicao, rgData, cpf, pis, documentoMilitar, tipoDocumentoMilitar, eleitor, zonaEleitoral, secaoEleitoral, carteiraProfissional, serieCarteiraProfissional, ufCarteiraProfissional, admissao, demissao, salarioBase, codigoFgts, valeTransporte, banco, agencia, digitoAgencia, contaCorrente, digitoConta, titularConta, nroCartaoMagnetico, tipo, situacao, senha, limiteConvenio, codigoPDV, acumuladoChequeDiario, acumuladoChequeDiario01, acumuladoChequeDiario02, acumuladoChequeDiario03, acumuladoChequeDiario04, acumuladoChequeDiario05, acumuladoChequeDiario06, acumuladoValorDiario, ultimaOperacaoPdv, limiteCheque, foneEmergencia, celular, codigoUsuario, comissao, funcao, unidadeFechamentoPDV, observacao, email, limiteDiario, centroCusto, escolaridade, horarioEntrada, horarioSaida, tipos }

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaPostFuncionarioV1** = object { response }

---

### PUT `/v1.0/funcionario/{id}`

**Resumo:** Editar cadastro de funcionário

Editar cadastro de funcionário.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `id` | path | sim | string | Código do funcionário a ser editado. |

**Request body** (application/json, obrigatório: False):

- **funcionarioInsert** = object { codigo, nome, unidade, nascimento, endereco, enderecoNumero, enderecoComplemento, bairro, codigoMunicipio, cep, nomeMae, nomePai, telefone, estadoCivil, sexo, cor, deficiente, rg, rgUf, rgExpedicao, rgData, cpf, pis, documentoMilitar, tipoDocumentoMilitar, eleitor, zonaEleitoral, secaoEleitoral, carteiraProfissional, serieCarteiraProfissional, ufCarteiraProfissional, admissao, demissao, salarioBase, codigoFgts, valeTransporte, banco, agencia, digitoAgencia, contaCorrente, digitoConta, titularConta, nroCartaoMagnetico, tipo, situacao, senha, limiteConvenio, codigoPDV, acumuladoChequeDiario, acumuladoChequeDiario01, acumuladoChequeDiario02, acumuladoChequeDiario03, acumuladoChequeDiario04, acumuladoChequeDiario05, acumuladoChequeDiario06, acumuladoValorDiario, ultimaOperacaoPdv, limiteCheque, foneEmergencia, celular, codigoUsuario, comissao, funcao, unidadeFechamentoPDV, observacao, email, limiteDiario, centroCusto, escolaridade, horarioEntrada, horarioSaida, tipos }

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaPadrao_SemMessageV2** = object { response }

---

### GET `/v1.1/funcionario`

**Resumo:** Consulta de funcionários

consultar funcionários por cpf ou codigo do funcionario, ou por lastId. é obrigatório passar um dos parametros abaixo para o funcionamento do endpoint.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cpf` | query | não | string | CPF do funcionário. |
| `codigo` | query | não | number | Código do funcionário |
| `lastid` | query | não | number | Código do último funcionário |
| `limit` | query | não | number | ao usar o parametro lastId, é obrigatório usar o parametro limit e definir seu valor. (ex: lastId=10&&limit=3) |

**Respostas:**

- `200`  — **RespostaListaDeFuncionarios** = object { response }

---

### GET `/v1.2/funcionario/codcpf/{codcpf}`

**Resumo:** Consultar cadastro de funcionário

Consultar cadastro de funcionário por meio do código ou CPF.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codcpf` | path | sim | string | Código ou CPF do funcionário. |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaFuncionario** = object { response }

---

### GET `/v1.2/funcionario/lastid/{lastid}`

**Resumo:** Consultar cadastro de funcionários

Consultar cadastro de funcionários por meio de paginação.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastid` | path | sim | string | Código do último funcionário ou 0. |
| `nome` | query | não | string | Nome do funcionário. |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaPostFuncionarioV1_2** = object { response }

---
