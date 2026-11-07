# Tag 00031 — Industrialização

10 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| POST | `/v1.2/industcomp` | Cadastrar produto industrializado |  |
| PUT | `/v1.2/industcomp/{codigo}/unidade/{CNPJ}` | Editar um produto industrializado |  |
| DELETE | `/v1.2/industcomp/{codigo}/unidade/{CNPJ}` | Deletar um produto industrializado |  |
| POST | `/v1.2/industdecomp` | Cadastrar produto da 'receita' de um industrializado |  |
| DELETE | `/v1.2/industdecomp/codigo1/{codigo1}/codigo2/{codigo2}/unidade/{CNPJ}` | Deletar um produto 'receita' |  |
| GET | `/v1.2/industdecomp/codigo1/{codigo1}/codigo2/{codigo2}/unidade/{CNPJ}` | Consultar cadastro de um produto pertencente a um industrializado |  |
| GET | `/v1.2/industdecomp/{codigo1}/unidade/{CNPJ}` | Consultar cadastro dos produtos 'receita' de um produto industrializado |  |
| PUT | `/v1.2/industdecomp/{codigo1}/unidade/{CNPJ}` | Editar o cadastro de um produto 'receita' |  |
| GET | `/v1.3/industcomp/lastId/{lastId}` | Consultar cadastro dos produtos industrializados |  |
| GET | `/v1.3/industcomp/{codigo}/unidade/{CNPJ}` | Consultar cadastro de produto industrializado |  |

## Detalhes

### POST `/v1.2/industcomp`

**Resumo:** Cadastrar produto industrializado

Efetuar o cadastro de produto industrializado, podendo efeturar o cadastro também dos itens de 'receita'

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: False):

- **RequestCadastroProdutosIndustrializados_V1_2** = object { codigo, descricao, tipo, unidade, rendimento, pesoTotal, precoTotal, dataCusto, comportamento, fase, tempoProducao, observacao, quantidadeMinimaProduzir, quantidadeProduzir, quantidadeMultiplaProduzir, baseProducao, tempoAntecedencia, tempoProducaoHomensHora, prioridadeProducao, tempoPreparo, estoqueSeguranca, baixaEstoqueMateriaPrima, fatorProducao, AgrupamentoUnidadesValidas, departamento, itens }

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaPadrao_SemMessageV3** = object { response }

---

### PUT `/v1.2/industcomp/{codigo}/unidade/{CNPJ}`

**Resumo:** Editar um produto industrializado

Efetuar a edição de produto industrializado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do a produto a ser editado. |
| `CNPJ` | path | sim | string | CNPJ da unidade do produto a ser editado. |

**Request body** (application/json, obrigatório: False):

- **IndustrializadoEdicao_V1_2** = object { descricao, tipo, unidade, rendimento, pesoTotal, precoTotal, dataCusto, comportamento, fase, tempoProducao, observacao, quantidadeMinimaProduzir, quantidadeProduzir, quantidadeMultiplaProduzir, baseProducao, tempoAntecedencia, tempoProducaoHomensHora, prioridadeProducao, tempoPreparo, estoqueSeguranca, baixaEstoqueMateriaPrima, fatorProducao, AgrupamentoUnidadesValidas, departamento }

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaPadrao_SemMessageV3** = object { response }

---

### DELETE `/v1.2/industcomp/{codigo}/unidade/{CNPJ}`

**Resumo:** Deletar um produto industrializado

Efetuar a exclusão do cadastro de industrialização

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do produto industrializado a ser deletado. |
| `CNPJ` | path | sim | string | CNPJ da unidade do produto industrializado a ser deletado. |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaIndustrializadoDeletado** = object { response }

---

### POST `/v1.2/industdecomp`

**Resumo:** Cadastrar produto da 'receita' de um industrializado

Cadastrar produto que faz parte da 'receita' de um industrializado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: False):

- **ProdutoDeIndustrializadoCadastro** = object { codigoIndustrializado, codigoItem, unidade, quantComercializacao, quantReceita, pesoItem, precoItem, fase }

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaPadrao_SemMessageV3** = object { response }

---

### DELETE `/v1.2/industdecomp/codigo1/{codigo1}/codigo2/{codigo2}/unidade/{CNPJ}`

**Resumo:** Deletar um produto 'receita'

Efetuar a exclusão do cadastro de um produto da 'receita' pertencente de um industrializado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo1` | path | sim | string | Código do produto industrializado. |
| `codigo2` | path | sim | string | Código do item |
| `CNPJ` | path | sim | string | CNPJ da unidade do item a ser deletado. |
| `fase` | query | não | string | Fase do produto a ser deletado (Se não informado, o valor padrão para fase será = '0'). |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaProdutoDeletado** = object { response }

---

### GET `/v1.2/industdecomp/codigo1/{codigo1}/codigo2/{codigo2}/unidade/{CNPJ}`

**Resumo:** Consultar cadastro de um produto pertencente a um industrializado

Consultar cadastro de um produto pertencente a 'receita' de um produto industrializado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo1` | path | sim | string | Código do produto industrializado. |
| `codigo2` | path | sim | string | Código do produto 'receita' |
| `CNPJ` | path | sim | string | CNPJ da unidade do produto a ser consultado. |
| `fase` | query | não | string | Fase do produto a ser consultado. |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaConsultaProdutoReceitaIndustrializadoV_1_2** = object { response }

---

### GET `/v1.2/industdecomp/{codigo1}/unidade/{CNPJ}`

**Resumo:** Consultar cadastro dos produtos 'receita' de um produto industrializado

Consultar cadastro dos produtos da 'receita' de um produto industrializado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo1` | path | sim | string | Código do produto industrializado |
| `CNPJ` | path | sim | string | CNPJ da unidade do produto a ser consultado. |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaConsultaTodosProdutosReceitaIndustrializadoV_1_2** = object { response }

---

### PUT `/v1.2/industdecomp/{codigo1}/unidade/{CNPJ}`

**Resumo:** Editar o cadastro de um produto 'receita'

Editar o cadastro de um produto da 'receita' pertencente a um produto industrializado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo1` | path | sim | string | Código do produto industrializado a qual o produto a ser editado pertence. |
| `CNPJ` | path | sim | string | CNPJ da unidade do produto a ser editado. |
| `fase` | query | não | string | Fase do produto a ser editado. Se não informado, a edição é aplicada ao item em todas as fases. |

**Request body** (application/json, obrigatório: False):

- **ProdutoDeIndustrializadoEdicao_V1_2** = object { cod2, unidade, quantComercializacao, quantReceita, pesoItem, precoItem, fase }

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaPadrao_SemMessageV3** = object { response }

---

### GET `/v1.3/industcomp/lastId/{lastId}`

**Resumo:** Consultar cadastro dos produtos industrializados

Consultar o cadastro dos produtos industrializados

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Código do último produto consultado. Envie "0" caso queira consultar todos os produtos (mesmo passando 0 os dados retornam paginados) |
| `unidade` | query | não | string | CNPJ da unidade do produto a ser consultado. |
| `loadCodBarras` | query | não | string | Se informado e marcado como true, será retornado os códigos de barras associados nas tabelas Produtos e CbAlt |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaConsultaProdutosIndustrializados_V1_3** = object { response }

---

### GET `/v1.3/industcomp/{codigo}/unidade/{CNPJ}`

**Resumo:** Consultar cadastro de produto industrializado

Consultar o cadastro de produto industrializado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do a produto consultado. |
| `CNPJ` | path | sim | string | CNPJ da unidade do produto a ser consultado. |
| `loadCodBarras` | query | não | boolean | Se informado |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaConsultaProdutoIndustrializados_V1_3** = object { response }

---
