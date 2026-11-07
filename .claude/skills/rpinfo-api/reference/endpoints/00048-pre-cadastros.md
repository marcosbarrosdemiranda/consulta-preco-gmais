# Tag 00048 — Pré-Cadastros

3 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/precadastros/v1.0/consulta` | Consultar pre-cadastro(s) |  |
| POST | `/precadastros/v1.0/produto` | Pré-cadastrar um produto |  |
| POST | `/precadastros/v1.0/promotor` | Pré-cadastrar um promotor |  |

## Detalhes

### GET `/precadastros/v1.0/consulta`

**Resumo:** Consultar pre-cadastro(s)

Consultar um pré-cadastro pelo código ou vários por release

**Respostas:**

- `200` Sessão autenticada — **EfetivCadPromotorConsultaContentRes** = `ResponsePadrao` (ver reference/schemas.md) & object { content }

---

### POST `/precadastros/v1.0/produto`

**Resumo:** Pré-cadastrar um produto

Pré-cadastrar um produto para o modulo de efetivação de cadastros

**Request body** (application/json, obrigatório: True):

- **EfetivCadProduto** = object { descricao, complemento, grupCodigo, grupNome, dptoCodigo, tribCodigo, marca, classe, tipo, funcao, codestoque, fatorestoque, codpreco, codbarras, descrpdvs, peso, pesoliq, emb, qemb, pzrepos, pzentrega, diasseg, vslhCodigo, balanca, contrest, datacad, usucad, dataalt, usualt, extra1, extra2, extra3, extra4, extra5, extra6, extra7, extra8, extra9, altura, largura, profundidade, lastro, camadas, fatoremb, faquisicao, status, dataexcl, usuexcl, gardCodigo, descritivo, codcaixa, display, tptrocas, grpreco, descricaocliente, ativounidades, bloqueadounidades, codigoncm, classfiscal, fornCodigo, codigoex, pesomaximo, volumemaximo, temperatura, compCodigo, valminima, sensCodigo, varpeso, centralcodigo, centraldescricao, sazoCodigo, simiCodigo, codcompra, descricaoecomm, complementoecomm, marcaecomm, dthrmanutencao, dthrintegracao, carpCodigo, origemcad, ecommid, datarecupexcl, release }

**Respostas:**

- `200` Sessão autenticada — **EfetivCadProdutoRes** = object { codigo, cadTipo, cadCodigo, etapaAprov, status, release, eventos, produto }

---

### POST `/precadastros/v1.0/promotor`

**Resumo:** Pré-cadastrar um promotor

Pré-cadastrar um promotor para o modulo de efetivação de cadastros

**Request body** (application/json, obrigatório: True):

- **EfetivCadPromotor** = object { nome, obs, fone, email, dtvenccad, supervisornome, supervisorfone, supervisoremail, cpf, fonecel, supervisorfonecel, contatoalt, supervisorcontatoalt, ufexprg, rg, dtnasc, fornecedores }

**Respostas:**

- `200` Sessão autenticada — **EfetivCadPromotorRes** = `ResponsePadrao` (ver reference/schemas.md) & object { content }

---
