# Tag 00015 — Consulta Xml da NFe

4 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/xmlNfe/chave/{chave}/produtos` | Obter produtos do Xml da NFe |  |
| GET | `/v1.1/xmlNfe/chave/{chave}` | Obter Xml da NFe |  |
| GET | `/v1.2/xmlNfe/unidade/{cnpj_cpf}/dataEmissao/{dataEmissao}` | Obter Xml da NFe |  |
| POST | `/v4.0/xmlNfe` | Gravar Xml da NFe |  |

## Detalhes

### GET `/v1.0/xmlNfe/chave/{chave}/produtos`

**Resumo:** Obter produtos do Xml da NFe

Método para obter os produtos do xml da chave informada

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `chave` | path | sim | string | Chave da Xml |

**Respostas:**

- `200` Xml carregado com sucesso — **RespostaXmlChaveProdutosV10** = object { response }

---

### GET `/v1.1/xmlNfe/chave/{chave}`

**Resumo:** Obter Xml da NFe

Método para obter o xml da chave informada

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `chave` | path | sim | string | Chave da Xml |

**Respostas:**

- `200` Xml carregado com sucesso — **RespostaXmlChaveV11** = object { response }

---

### GET `/v1.2/xmlNfe/unidade/{cnpj_cpf}/dataEmissao/{dataEmissao}`

**Resumo:** Obter Xml da NFe

Método para consultar as chaves de notas emitidas na data e unidade informada

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj_cpf` | path | sim | string | CNPJ/CPF da unidade |
| `dataEmissao` | path | sim | string | Data de Emissão da NFe (Formato 'dd-mm-yyyy') |

**Respostas:**

- `200` Xml da NFe carregado com sucesso — **RespostaXmlDataUnidV11** = object { response }

---

### POST `/v4.0/xmlNfe`

**Resumo:** Gravar Xml da NFe

Grava o xml de uma NF-e na tabela XmlNfe do ERP, com a mesma regra que o ERP aplica na importação de um arquivo xml.
Os dados de cabeçalho — emitente, destinatário, data de emissão, número, série, modelo, natureza da operação e totais — são lidos do próprio xml; o cliente não os informa.
Quando já existe um registro com texto para a chave nada é gravado e o campo "operacao" retorna JA_EXISTENTE; quando existe um registro sem texto, ele é complementado e "operacao" retorna ATUALIZADO.
Disponível somente na versão 4.0: por ser um método novo, a resposta já vem sem o envelope "response" e com o status HTTP real.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **Request_XmlNfe_Gravar_V_4_0** = object { conteudo, chave, unidade, transacao }

**Respostas:**

- `200` Xml gravado com sucesso — **Response_XmlNfe_Gravar_V_4_0** = object { chave, unidade, operacao, entSai, catEntidade, codEntidade }
- `400` Conteúdo ausente, xml sem protocolo de autorização ou chave divergente da informada — **Error400** = object { appVersion, content }

---
