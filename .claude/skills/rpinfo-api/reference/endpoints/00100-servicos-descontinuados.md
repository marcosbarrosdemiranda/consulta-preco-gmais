# Tag 00100 — Serviços descontinuados

359 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/agendas/datainicio/{dataInicio}/datafim/{dataFim}/unidade/{CNPJ}` | Buscar agenda de ofertas | ⚠️ SIM |
| GET | `/v1.0/agendas/periodoFinal/unidade/{cnpj}/lastid/{lastId}` | Buscar agenda de ofertas | ⚠️ SIM |
| GET | `/v1.0/agendas/periodoInicio/unidade/{cnpj}/lastid/{lastId}` | Buscar agenda de ofertas | ⚠️ SIM |
| POST | `/v1.0/auditoria/documentos` | Marcar como realizada a auditoria de documento | ⚠️ SIM |
| PUT | `/v1.0/auditoria/documentos/desmarcar` | Desmarcar como realizada a auditoria de documento | ⚠️ SIM |
| POST | `/v1.0/auth` | Autenticar sessão | ⚠️ SIM |
| GET | `/v1.0/bens` | Retorna um Bem | ⚠️ SIM |
| PUT | `/v1.0/bens/update/{codigo}` | Alterar um Bem | ⚠️ SIM |
| GET | `/v1.0/cestabasica/listarcestas/lastid/{lastId}` | Consultar o cadastro de cestas básicas | ⚠️ SIM |
| GET | `/v1.0/cidades/{lastId}` | Buscar cidades cadastradas | ⚠️ SIM |
| GET | `/v1.0/classecommerce` | Consultar dados de Classes Commerce | ⚠️ SIM |
| GET | `/v1.0/clientes/email/{email}` | Obter dados do cliente | ⚠️ SIM |
| GET | `/v1.0/clientes/{codigo}` | Obter dados do cliente | ⚠️ SIM |
| PUT | `/v1.0/clientes/{codigo}` | Editar Cliente | ⚠️ SIM |
| GET | `/v1.0/compradores/{lastID}` | Obter lista de compradores cadastrados | ⚠️ SIM |
| POST | `/v1.0/controleentregas` | Controle de entrega | ⚠️ SIM |
| GET | `/v1.0/controleentregas/{transacao}` | Obter Controle de entrega | ⚠️ SIM |
| GET | `/v1.0/estoques` | Obter classificação de estoques com seus identificadores | ⚠️ SIM |
| GET | `/v1.0/fde/lancamentos/{lastRelease}` | Obter os lançamentos do tipo FDE | ⚠️ SIM |
| GET | `/v1.0/financeiro/centrodecustos` | Consultar centro de custos | ⚠️ SIM |
| GET | `/v1.0/financeiro/cliente/{CPF_CNPJ}/saldolimitecheque` | Consultar limite no cheque | ⚠️ SIM |
| GET | `/v1.0/financeiro/cliente/{CPF_CNPJ}/saldolimitecredito` | Consultar limite de crédito do cliente | ⚠️ SIM |
| GET | `/v1.0/financeiro/cliente/{CPF_CNPJ}/saldolimitecredito/cartao` | Consultar limite de crédito de cartão do cliente | ⚠️ SIM |
| GET | `/v1.0/financeiro/funcionario/{CPF}/saldolimitecredito` | Consultar limite de crédito do funcionário | ⚠️ SIM |
| GET | `/v1.0/financeiro/movFinalizadoras/dataInicial/{dataInicial}/dataFinal/{dataFinal}` | MovFinalizadorasDet | ⚠️ SIM |
| GET | `/v1.0/financeiro/movFormaVendaPDV/lastID/{lastId}` | movFormaVendaPDV | ⚠️ SIM |
| GET | `/v1.0/financeiro/pendenciasFinanceiras/dataInicial/{dataInicial}/dataFinal/{dataFinal}` | Pendências financeiras | ⚠️ SIM |
| GET | `/v1.0/financeiro/pendenciasFinanceiras/{lastId}` | Pendências financeiras | ⚠️ SIM |
| GET | `/v1.0/financeiro/planocontas` | Consultar plano de contas | ⚠️ SIM |
| GET | `/v1.0/fiscal/getnfecupom/cupom/{cupom}/pdv/{pdv}` | Nota fiscal eletrônica emitida para um determinado cupom fiscal | ⚠️ SIM |
| GET | `/v1.0/flexapp/concorrente` | Recuperar cadastro de concorrentes | ⚠️ SIM |
| GET | `/v1.0/formaspagamento` | Cadastro de formas de pagamento | ⚠️ SIM |
| GET | `/v1.0/fornecedor/listaFornecedores/lastid/{lastId}` | Cadastro dos Fornecedores | ⚠️ SIM |
| GET | `/v1.0/fornecedor/pendenciasFinanceiras/dataInicial/{dataInicial}/dataFinal/{dataFinal}` | Pendências financeiras de fornecedores | ⚠️ SIM |
| PUT | `/v1.0/fornecedor/situacao` | Alterar situação do fornecedor | ⚠️ SIM |
| GET | `/v1.0/fornecedor/{codigo}/regranegocio` | Cadastro dos Fornecedores | ⚠️ SIM |
| GET | `/v1.0/funcionario/codcpf/{codcpf}` | Consultar cadastro de funcionário | ⚠️ SIM |
| GET | `/v1.0/funcionario/lastid/{lastid}` | Consultar cadastro de funcionários | ⚠️ SIM |
| GET | `/v1.0/grupos` | Consultar o cadastro de grupos de produtos | ⚠️ SIM |
| POST | `/v1.0/grupos` | Inserir o cadastro de grupos de produtos | ⚠️ SIM |
| PUT | `/v1.0/grupos/{codigo}` | Alterar o cadastro de grupos de produtos | ⚠️ SIM |
| DELETE | `/v1.0/grupos/{codigo}` | Deletar o cadastro de grupos de produtos | ⚠️ SIM |
| POST | `/v1.0/industcomp` | Cadastrar produto industrializado | ⚠️ SIM |
| GET | `/v1.0/industcomp/lastId/{lastId}` | Consultar cadastro dos produtos industrializados | ⚠️ SIM |
| GET | `/v1.0/industcomp/{codigo}` | Consultar cadastro de produto industrializado | ⚠️ SIM |
| PUT | `/v1.0/industcomp/{codigo}` | Editar um produto industrializado | ⚠️ SIM |
| DELETE | `/v1.0/industcomp/{codigo}` | Deletar um produto industrializado | ⚠️ SIM |
| POST | `/v1.0/industdecomp` | Cadastrar produto da 'receita' de um industrializado | ⚠️ SIM |
| DELETE | `/v1.0/industdecomp/codigo1/{codigo1}/codigo2/{codigo2}` | Deletar um produto 'receita' | ⚠️ SIM |
| GET | `/v1.0/industdecomp/codigo1/{codigo1}/codigo2/{codigo2}` | Consultar cadastro de um produto pertencente a um industrializado | ⚠️ SIM |
| GET | `/v1.0/industdecomp/{codigo1}` | Consultar cadastro dos produtos 'receita' de um produto industrializado | ⚠️ SIM |
| PUT | `/v1.0/industdecomp/{codigo1}` | Editar o cadastro de um produto 'receita' | ⚠️ SIM |
| GET | `/v1.0/logout` | Efetuar logout | ⚠️ SIM |
| POST | `/v1.0/metasprod` | Inserir novas Metas de Produtos | ⚠️ SIM |
| PUT | `/v1.0/metasprod` | Alterar Meta de Produto cadastrada | ⚠️ SIM |
| GET | `/v1.0/metasprod/cnpj/{cnpj}` | Consultar Metas de Produtos de uma unidade | ⚠️ SIM |
| GET | `/v1.0/movimentoprodutos/listarmovimentos/lastid/{lastID}` | Listar movimentos de produtos | ⚠️ SIM |
| GET | `/v1.0/movimentoprodutos/listarmovimentosevp/lastid/{lastID}` | Listar movimentos de produtos vendidos no PDV | ⚠️ SIM |
| GET | `/v1.0/movimentoprodutos/semrecebimento/documentos/{docs}/codDocumento/{codDocumento}/unidade/{cnpj}/catentidade/{catentidade}/codentidade/{codentidade}/datainicial/{dataini}/datafinal/{datafim}/validardestino/{validar}/lastid/{lastid}` | Busca de Movimentos de Produtos Sem RCM | ⚠️ SIM |
| GET | `/v1.0/movimentos/cnpj/{cnpj}/gerencial-rat` | Consultar movimentos gerenciais de rateio de uma unidade | ⚠️ SIM |
| GET | `/v1.0/negociacoes` | Consultar negociações disponíveis | ⚠️ SIM |
| POST | `/v1.0/nlq` | Inserir NLQ | ⚠️ SIM |
| GET | `/v1.0/patrimonial/bens` | Retorna o cadastro de bens patrimoniais | ⚠️ SIM |
| GET | `/v1.0/pedidocompra/listarpedidos/lastid/{lastID}/dataInicial/{datainicial}` | Listar pedidos de compra | ⚠️ SIM |
| POST | `/v1.0/pedidos` | Inserir pedido de venda | ⚠️ SIM |
| GET | `/v1.0/pedidos/listar/status/datamodificacao/{datahora}/lastid/{lastId}` | Consultar status pedido de venda | ⚠️ SIM |
| GET | `/v1.0/pedidos/pedidocliente/{codigo}` | Consultar processamento do pedido de venda pelo número de pedido do cliente | ⚠️ SIM |
| GET | `/v1.0/pedidos/{codigo}` | Consultar processamento do pedido de venda | ⚠️ SIM |
| PUT | `/v1.0/pedidos/{codigo}` | Editar Pedido de Venda | ⚠️ SIM |
| POST | `/v1.0/pedidos/{codigo}/item` | Inserir novo item ao pedido | ⚠️ SIM |
| PUT | `/v1.0/pedidos/{codigo}/item/{codigoItem}` | Editar Item do Pedido | ⚠️ SIM |
| GET | `/v1.0/pedidos/{codigo}/status` | Consultar status pedido de venda | ⚠️ SIM |
| POST | `/v1.0/pendest/incluir` | Incluir pendências de estoque | ⚠️ SIM |
| GET | `/v1.0/pendest/que/lastid/{lastID}` | Obter pendências de estoque | ⚠️ SIM |
| GET | `/v1.0/precadastro` | Obter dados de pré cadastro do produto | ⚠️ SIM |
| POST | `/v1.0/precadastro` | Inserir dados de pré cadastro do produto | ⚠️ SIM |
| GET | `/v1.0/precadastro/{sequencia}` | Obter dados de pré cadastro do produto | ⚠️ SIM |
| GET | `/v1.0/precocliente/lastid/{lastid}` | Obter preços por cliente | ⚠️ SIM |
| GET | `/v1.0/produto/codigobarrasalterados/ativos/unidade/{unidade}/lastid/{lastID}` | Obter dados de códigos de barras alternativos dos produtos ativos | ⚠️ SIM |
| GET | `/v1.0/produto/codigobarrasalterados/lastid/{lastID}` | Obter dados de códigos de barras alternativos | ⚠️ SIM |
| GET | `/v1.0/produto/excluidos/lastid/{lastid}/dataexclusao/{dataexclusao}` | Obter dados dos produtos excluidos | ⚠️ SIM |
| GET | `/v1.0/produto/listaprodutos/{lastId}` | Consultar cadastro de um produto | ⚠️ SIM |
| GET | `/v1.0/produto/listaprodutos/{lastId}/detalhado` | Consultar cadastro de um produto | ⚠️ SIM |
| PUT | `/v1.0/produto/{codigo}` | Editar cadastro de um produto | ⚠️ SIM |
| GET | `/v1.0/produto/{codigo}/codigobarrasalterados` | Obter dados de códigos de barras alternativos | ⚠️ SIM |
| GET | `/v1.0/produto/{codigo}/detalhado` | Consultar cadastro de um produto | ⚠️ SIM |
| GET | `/v1.0/produto/{prodCodigo}/fornecedor/{fornCodigo}` | Obter dados dos codigos do fornecedor vinculados a um produto | ⚠️ SIM |
| GET | `/v1.0/produtos/lastid/{lastId}/fornecedor/{codigo}` | Obter dados dos produtos vinculados ao fornecedor | ⚠️ SIM |
| POST | `/v1.0/produtounidade/auditoriaestoque` | Incluir auditoria de estoque | ⚠️ SIM |
| GET | `/v1.0/produtounidade/auditoriaestoque/{lastID}/datainicial/{dataInicial}/datafinal/{dataFinal}` | Obter auditorias de estoque | ⚠️ SIM |
| GET | `/v1.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}` | Obter cadastro de produtos | ⚠️ SIM |
| GET | `/v1.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/departamento/{departamento}` | Obter dados do produto | ⚠️ SIM |
| GET | `/v1.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v1.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/departamento/{departamento}` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v1.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/grupo/{grupo}` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v1.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/semcalcularestoque` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v1.0/produtounidade/listaprodutos/{lastId}/unidade/{CNPJ}/detalhado/dataalteracao/{dataAlteracao}` | Obter dados dos produtos | ⚠️ SIM |
| POST | `/v1.0/produtounidade/pendenciaestoque` | Incluir pendências de estoque | ⚠️ SIM |
| POST | `/v1.0/produtounidade/unidade/{CNPJ}/atualizaretiquetaprecos` | Atualizar etiqueta de preços | ⚠️ SIM |
| GET | `/v1.0/produtounidade/unidade/{CNPJ}/departamento/{departamento}/rcm/{calcularRCM}/vdonline/{considerarVendaOnline}/datainicial/{dataInicial}/datafinal/{dataFinal}/snapshotestoque` | Obter snapshot do estoque | ⚠️ SIM |
| GET | `/v1.0/produtounidade/{codBarras}/unidade/{CNPJ}/estoquecodigobarras` | Obter dados do produto | ⚠️ SIM |
| GET | `/v1.0/produtounidade/{codigoProduto}/unidade/{CNPJ}/rcm/{calcularRCM}/vdonline/{considerarVendaOnline}/datainicial/{dataInicial}/datafinal/{dataFinal}/snapshotestoque` | Obter snapshot do estoque | ⚠️ SIM |
| GET | `/v1.0/produtounidade/{codigo}/unidade/{CNPJ}/detalhado/estoque` | Obter dados do produto | ⚠️ SIM |
| GET | `/v1.0/produtounidade/{lastID}/unidade/{CNPJ}/etiquetaspendentes/{campoConsiderar}` | Consultar etiquetas pendentes | ⚠️ SIM |
| POST | `/v1.0/programacaoprecos` | Inserir uma nova Programação de Preço | ⚠️ SIM |
| POST | `/v1.0/recmerc/inserir` | Incluir recebimentos de mercadoria | ⚠️ SIM |
| GET | `/v1.0/subcontas/movimentos/release/{release}` | Consultar os movimentos de sub contas | ⚠️ SIM |
| GET | `/v1.0/usuarios/` | Obter cadastro de usuarios | ⚠️ SIM |
| GET | `/v1.0/usuarios/{codigo}` | Obter dados do usuario | ⚠️ SIM |
| GET | `/v1.0/vdonline/unidade/{cnpj}/pdv/{pdv}/datainicio/{datainicio}/datafim/{datafim}/lastid/{lastid}` | Buscar vendas online por PDV | ⚠️ SIM |
| GET | `/v1.0/vendedores/{lastID}` | Listar Vendedores | ⚠️ SIM |
| GET | `/v1.0/xmlNfe/chave/{chave}` | Obter Xml da NFe | ⚠️ SIM |
| GET | `/v1.0/xmlNfe/unidade/{cnpj_cpf}/dataEmissao/{dataEmissao}` | Obter Xml da NFe | ⚠️ SIM |
| GET | `/v1.1/agendas/datainicio/{dataInicio}/datafim/{dataFim}/unidade/{cnpj}/lastid/{lastId}` | Buscar agenda de ofertas | ⚠️ SIM |
| POST | `/v1.1/auth` | Autenticar sessão | ⚠️ SIM |
| POST | `/v1.1/clientes` | Inserir novo cliente | ⚠️ SIM |
| GET | `/v1.1/clientes/cnpj_cpf/{CPF_CNPJ}` | Obter dados do cliente | ⚠️ SIM |
| GET | `/v1.1/compradores/listar/{lastID}` | Obter lista de compradores cadastrados | ⚠️ SIM |
| GET | `/v1.1/compradores/{codigo}` | Obter lista de compradores cadastrados | ⚠️ SIM |
| POST | `/v1.1/controleentregas` | Controle de entrega | ⚠️ SIM |
| GET | `/v1.1/financeiro/funcionario/{CPF}/saldolimitecredito` | Consultar limite de crédito do funcionário | ⚠️ SIM |
| GET | `/v1.1/financeiro/pendenciasFinanceiras/dataInicial/{dataInicial}/dataFinal/{dataFinal}` | Pendências financeiras | ⚠️ SIM |
| GET | `/v1.1/fiscal/getnfecupom` | Nota fiscal eletrônica emitida para um determinado cupom fiscal | ⚠️ SIM |
| POST | `/v1.1/flexapp/movpesquisa` | Inserir pesquisa de preços | ⚠️ SIM |
| GET | `/v1.1/flexapp/movpesquisa` | Obter dados de pesquisa de preços | ⚠️ SIM |
| GET | `/v1.1/flexapp/prodpesquisa` | Recuperar produtos para pesquisa de preço | ⚠️ SIM |
| GET | `/v1.1/formaspagamento` | Cadastro de formas de pagamento | ⚠️ SIM |
| GET | `/v1.1/funcionario/codcpf/{codcpf}` | Consultar cadastro de funcionário | ⚠️ SIM |
| GET | `/v1.1/funcionario/lastid/{lastid}` | Consultar cadastro de funcionários | ⚠️ SIM |
| POST | `/v1.1/industcomp` | Cadastrar produto industrializado | ⚠️ SIM |
| GET | `/v1.1/industcomp/lastId/{lastId}` | Consultar cadastro dos produtos industrializados | ⚠️ SIM |
| GET | `/v1.1/industcomp/{codigo}/unidade/{CNPJ}` | Consultar cadastro de produto industrializado | ⚠️ SIM |
| PUT | `/v1.1/industcomp/{codigo}/unidade/{CNPJ}` | Editar um produto industrializado | ⚠️ SIM |
| DELETE | `/v1.1/industcomp/{codigo}/unidade/{CNPJ}` | Deletar um produto industrializado | ⚠️ SIM |
| POST | `/v1.1/industdecomp` | Cadastrar produto da 'receita' de um industrializado | ⚠️ SIM |
| DELETE | `/v1.1/industdecomp/codigo1/{codigo1}/codigo2/{codigo2}/unidade/{CNPJ}` | Deletar um produto 'receita' | ⚠️ SIM |
| GET | `/v1.1/industdecomp/codigo1/{codigo1}/codigo2/{codigo2}/unidade/{CNPJ}` | Consultar cadastro de um produto pertencente a um industrializado | ⚠️ SIM |
| GET | `/v1.1/industdecomp/{codigo1}/unidade/{CNPJ}` | Consultar cadastro dos produtos 'receita' de um produto industrializado | ⚠️ SIM |
| PUT | `/v1.1/industdecomp/{codigo1}/unidade/{CNPJ}` | Editar o cadastro de um produto 'receita' | ⚠️ SIM |
| GET | `/v1.1/movimentoprodutos/listarmovimentos/lastid/{lastID}` | Listar movimentos de produtos | ⚠️ SIM |
| GET | `/v1.1/pedidocompra/listarpedidos/lastid/{lastID}/dataInicial/{datainicial}` | Listar pedidos de compra | ⚠️ SIM |
| GET | `/v1.1/pedidocompra/listarpedidos/pedidossemrcm/lastid/{lastID}/fornecedor/{cnpj}/datainicial/{dataInicial}/datafinal/{dataFinal}` | Listar pedidos de compra sem Recebimento | ⚠️ SIM |
| POST | `/v1.1/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| GET | `/v1.1/pedidos/listapedidos/{lastId}` | Consultar pedidos de venda | ⚠️ SIM |
| GET | `/v1.1/pedidos/{codigo}` | Consultar processamento do pedido de venda | ⚠️ SIM |
| PUT | `/v1.1/pedidos/{codigo}` | Editar Pedido de Venda | ⚠️ SIM |
| POST | `/v1.1/pedidos/{codigo}/financeiro` | Enviar dados pedido de venda | ⚠️ SIM |
| POST | `/v1.1/pendest/pendenciaestoque` | Incluir pendências de estoque | ⚠️ SIM |
| GET | `/v1.1/pendest/que/lastid/{lastID}` | Obter pendências de estoque | ⚠️ SIM |
| GET | `/v1.1/produto/listaprodutos/{lastId}` | Consultar cadastro de um produto | ⚠️ SIM |
| GET | `/v1.1/produto/listaprodutos/{lastId}/detalhado` | Consultar cadastro de um produto | ⚠️ SIM |
| POST | `/v1.1/produtounidade/auditoriaestoque` | Incluir auditoria de estoque | ⚠️ SIM |
| GET | `/v1.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}` | Obter cadastro de produtos | ⚠️ SIM |
| GET | `/v1.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/departamento/{departamento}` | Obter dados do produto | ⚠️ SIM |
| GET | `/v1.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/semcalcularestoque` | Obter cadastro de produtos | ⚠️ SIM |
| GET | `/v1.1/produtounidade/{lastID}/unidade/{CNPJ}/etiquetaspendentes/{campoConsiderar}` | Consultar etiquetas pendentes | ⚠️ SIM |
| GET | `/v1.1/usuarios/` | Obter cadastro de usuarios | ⚠️ SIM |
| GET | `/v1.1/usuarios/{codigo}` | Obter dados do usuario | ⚠️ SIM |
| GET | `/v1.1/usuarios/{codigo}/detalhado` | Obter dados do usuario detalhado | ⚠️ SIM |
| GET | `/v1.1/usuariosexternos/{codigo}` | Obter dados do usuario externo | ⚠️ SIM |
| GET | `/v1.1/vdonline/unidade/{cnpj}/pdv/{pdv}/datainicio/{datainicio}/datafim/{datafim}/lastid/{lastid}` | Buscar vendas online por PDV | ⚠️ SIM |
| GET | `/v1.1/xmlNfe/unidade/{cnpj_cpf}/dataEmissao/{dataEmissao}` | Obter Xml da NFe | ⚠️ SIM |
| GET | `/v1.2/cestabasica/listarcestas/lastid/{lastId}` | Consultar o cadastro de cestas básicas | ⚠️ SIM |
| POST | `/v1.2/clientes` | Inserir novo cliente | ⚠️ SIM |
| POST | `/v1.2/controleentregas` | Controle de entrega | ⚠️ SIM |
| GET | `/v1.2/financeiro/pendenciasFinanceiras/dataInicial/{dataInicial}/dataFinal/{dataFinal}` | Pendências financeiras | ⚠️ SIM |
| GET | `/v1.2/financeiro/pendenciasFinanceiras/transacao/{transacao}` | Pendências financeiras | ⚠️ SIM |
| POST | `/v1.2/flexapp/movpesquisa` | Inserir pesquisa de preços | ⚠️ SIM |
| GET | `/v1.2/industcomp/lastId/{lastId}` | Consultar cadastro dos produtos industrializados | ⚠️ SIM |
| GET | `/v1.2/industcomp/{codigo}/unidade/{CNPJ}` | Consultar cadastro de produto industrializado | ⚠️ SIM |
| GET | `/v1.2/movimentoprodutos/listarmovimentos/lastid/{lastId}` | Listar movimentos de produtos | ⚠️ SIM |
| POST | `/v1.2/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| GET | `/v1.2/pedidos/listapedidos/{lastId}` | Consultar pedidos de venda | ⚠️ SIM |
| GET | `/v1.2/pedidos/{codigo}` | Consultar processamento do pedido de venda | ⚠️ SIM |
| PUT | `/v1.2/pedidos/{codigo}` | Editar Pedido de Venda | ⚠️ SIM |
| GET | `/v1.2/pedidos/{codigo}/status` | Consultar status pedido de venda | ⚠️ SIM |
| POST | `/v1.2/pendest/pendenciaestoque` | Incluir pendências de estoque | ⚠️ SIM |
| POST | `/v1.2/produtounidade/auditoriaestoque` | Incluir auditoria de estoque | ⚠️ SIM |
| GET | `/v1.2/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/departamento/{departamento}` | Obter dados do produto | ⚠️ SIM |
| GET | `/v1.2/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/grupo/{grupo}` | Obter dados do produto | ⚠️ SIM |
| GET | `/v1.2/usuariosexternos/{codigo}` | Obter dados do usuario externo | ⚠️ SIM |
| GET | `/v1.2/vdonline/unidade/{cnpj}/pdv/{pdv}/datainicio/{datainicio}/datafim/{datafim}/lastid/{lastid}` | Buscar vendas online por PDV | ⚠️ SIM |
| GET | `/v1.3/cestabasica/listarcestas/lastid/{lastId}` | Consultar o cadastro de cestas básicas | ⚠️ SIM |
| POST | `/v1.3/clientes` | Inserir novo cliente | ⚠️ SIM |
| GET | `/v1.3/clientes/cnpj_cpf/{CPF_CNPJ}` | Obter dados do cliente | ⚠️ SIM |
| GET | `/v1.3/clientes/email/{email}` | Obter dados do cliente | ⚠️ SIM |
| GET | `/v1.3/clientes/lastid/{lastID}` | Obter cadastro de clientes | ⚠️ SIM |
| GET | `/v1.3/clientes/{codigo}` | Obter dados do cliente | ⚠️ SIM |
| PUT | `/v1.3/clientes/{codigo}` | Editar Cliente | ⚠️ SIM |
| GET | `/v1.3/financeiro/pendenciasFinanceiras/dataInicial/{dataInicial}/dataFinal/{dataFinal}` | Pendências financeiras | ⚠️ SIM |
| GET | `/v1.3/financeiro/pendenciasFinanceiras/transacao/{transacao}` | Pendências financeiras | ⚠️ SIM |
| GET | `/v1.3/fornecedor/cnpj_cpf/{cnpj_cpf}` | Fornecedor filtrado pelo CPF ou CNPJ | ⚠️ SIM |
| GET | `/v1.3/fornecedor/listaFornecedores/lastid/{lastId}` | Cadastro dos Fornecedores | ⚠️ SIM |
| GET | `/v1.3/fornecedor/listaFornecedores/lastid/{lastId}/datahoramanutencao/{datahoramanutencao}` | Cadastro dos Fornecedores | ⚠️ SIM |
| GET | `/v1.3/fornecedor/listaFornecedores/lastid/{lastId}/tipos/{tipos}` | Fornecedores filtrados pelo tipo | ⚠️ SIM |
| GET | `/v1.3/fornecedor/pedidosbaixados/lastid/{lastId}/unidade/{cnpjUnid}/datainicial/{dataInicial}/datafinal/{dataFinal}` | Pedidos baixados | ⚠️ SIM |
| GET | `/v1.3/fornecedor/{codigo}` | Fornecedor filtrado pelo código | ⚠️ SIM |
| GET | `/v1.3/movimentoprodutos/listarmovimentos/lastid/{lastId}` | Listar movimentos de produtos | ⚠️ SIM |
| POST | `/v1.3/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| GET | `/v1.3/pedidos/{codigo}` | Consultar processamento do pedido de venda | ⚠️ SIM |
| GET | `/v1.3/pedidos/{codigo}/status` | Consultar status pedido de venda | ⚠️ SIM |
| POST | `/v1.3/pendest/incluir` | Incluir pendências de estoque | ⚠️ SIM |
| POST | `/v1.3/pendest/pendenciaestoque` | Incluir pendências de estoque | ⚠️ SIM |
| GET | `/v1.3/vdonline/unidade/{cnpj}/pdv/{pdv}/datainicio/{datainicio}/datafim/{datafim}/lastid/{lastid}` | Buscar vendas online por PDV | ⚠️ SIM |
| POST | `/v1.4/clientes` | Inserir novo cliente | ⚠️ SIM |
| GET | `/v1.4/clientes/cnpj_cpf/{CPF_CNPJ}` | Obter dados do cliente | ⚠️ SIM |
| GET | `/v1.4/clientes/email/{email}` | Obter dados do cliente | ⚠️ SIM |
| GET | `/v1.4/clientes/lastid/{lastID}` | Obter cadastro de clientes | ⚠️ SIM |
| GET | `/v1.4/clientes/{codigo}` | Obter dados do cliente | ⚠️ SIM |
| PUT | `/v1.4/clientes/{codigo}` | Editar Cliente | ⚠️ SIM |
| GET | `/v1.4/financeiro/pendenciasFinanceiras/dataInicial/{dataInicial}/dataFinal/{dataFinal}` | Pendências financeiras | ⚠️ SIM |
| GET | `/v1.4/financeiro/pendenciasFinanceiras/transacao/{transacao}` | Pendências financeiras | ⚠️ SIM |
| GET | `/v1.4/fornecedor/cnpj_cpf/{cnpj_cpf}` | Fornecedor filtrado pelo CPF ou CNPJ | ⚠️ SIM |
| GET | `/v1.4/fornecedor/listaFornecedores/lastid/{lastId}` | Cadastro dos Fornecedores | ⚠️ SIM |
| GET | `/v1.4/fornecedor/{codigo}` | Fornecedor filtrado pelo código | ⚠️ SIM |
| GET | `/v1.4/movimentoprodutos/listarmovimentos/lastid/{lastId}` | Listar movimentos de produtos | ⚠️ SIM |
| GET | `/v1.4/pedidocompra/listarpedidos/lastid/{lastID}/dataInicial/{datainicial}` | Listar pedidos de compra | ⚠️ SIM |
| GET | `/v1.4/pedidocompra/listarpedidos/pedidossemrcm/lastid/{lastID}/fornecedor/{cnpj}/datainicial/{dataInicial}/datafinal/{dataFinal}` | Listar pedidos de compra sem Recebimento | ⚠️ SIM |
| GET | `/v1.4/pedidocompra/{codigo}` | Listar pedidos de compra | ⚠️ SIM |
| POST | `/v1.4/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| GET | `/v1.4/pedidos/listar/status/datamodificacao/{datahora}/lastid/{lastId}` | Consultar status pedido de venda | ⚠️ SIM |
| PUT | `/v1.4/pedidos/{codigo}` | Editar Pedido de Venda | ⚠️ SIM |
| POST | `/v1.4/pendest/incluir` | Incluir pendências de estoque | ⚠️ SIM |
| GET | `/v1.4/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}` | Obter cadastro de produtos | ⚠️ SIM |
| GET | `/v1.4/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/grupo/{grupo}` | Obter dados do produto | ⚠️ SIM |
| GET | `/v1.4/unidades` | Listar Unidades | ⚠️ SIM |
| GET | `/v1.4/unidades/{CNPJ}` | Listar unidade | ⚠️ SIM |
| GET | `/v1.4/vdonline/unidade/{cnpj}/pdv/{pdv}/datainicio/{datainicio}/datafim/{datafim}/lastid/{lastid}` | Buscar vendas online por PDV | ⚠️ SIM |
| POST | `/v1.5/clientes` | Inserir novo cliente | ⚠️ SIM |
| GET | `/v1.5/clientes/cnpj_cpf/{CPF_CNPJ}` | Obter dados do cliente | ⚠️ SIM |
| PUT | `/v1.5/clientes/{codigo}` | Editar Cliente | ⚠️ SIM |
| GET | `/v1.5/financeiro/pendenciasFinanceiras/transacao/{transacao}` | Pendências financeiras | ⚠️ SIM |
| GET | `/v1.5/movimentoprodutos/listarmovimentos/lastid/{lastId}` | Listar movimentos de produtos | ⚠️ SIM |
| GET | `/v1.5/pedidocompra/listarpedidos/lastid/{lastID}/dataInicial/{datainicial}` | Listar pedidos de compra | ⚠️ SIM |
| GET | `/v1.5/pedidocompra/listarpedidos/pedidossemrcm/lastid/{lastID}/fornecedor/{cnpj}/datainicial/{dataInicial}/datafinal/{dataFinal}` | Listar pedidos de compra sem Recebimento | ⚠️ SIM |
| GET | `/v1.5/pedidocompra/listarpedidos/pedidossemrcm/lastid/{lastID}/fornecedor/{cnpj}/datainicial/{dataInicial}/datafinal/{dataFinal}/vinc/{vinc}` | Listar pedidos de compra sem Recebimento | ⚠️ SIM |
| POST | `/v1.5/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| GET | `/v1.5/pedidos/listar/status/datamodificacao/{datahora}/lastid/{lastId}` | Consultar status pedido de venda | ⚠️ SIM |
| PUT | `/v1.5/pedidos/{codigo}` | Editar Pedido de Venda | ⚠️ SIM |
| GET | `/v1.5/pedidos/{codigo}/status` | Consultar status pedido de venda | ⚠️ SIM |
| POST | `/v1.5/pendest/incluir` | Incluir pendências de estoque | ⚠️ SIM |
| GET | `/v1.5/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}` | Obter cadastro de produtos | ⚠️ SIM |
| GET | `/v1.5/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/departamento/{departamento}` | Obter dados do produto | ⚠️ SIM |
| GET | `/v1.5/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/grupo/{grupo}` | Obter dados do produto | ⚠️ SIM |
| GET | `/v1.5/unidades` | Listar Unidades | ⚠️ SIM |
| GET | `/v1.5/unidades/{CNPJ}` | Listar unidade | ⚠️ SIM |
| GET | `/v1.5/vdonline/unidade/{cnpj}/pdv/{pdv}/datainicio/{datainicio}/datafim/{datafim}/lastid/{lastid}` | Buscar vendas online por PDV | ⚠️ SIM |
| POST | `/v1.6/clientes` | Inserir novo cliente | ⚠️ SIM |
| GET | `/v1.6/clientes/lastid/{lastID}` | Obter cadastro de clientes | ⚠️ SIM |
| GET | `/v1.6/clientes/{codigo}` | Obter dados do cliente | ⚠️ SIM |
| GET | `/v1.6/movimentoprodutos/listarmovimentos/lastid/{lastId}` | Listar movimentos de produtos | ⚠️ SIM |
| POST | `/v1.6/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| GET | `/v1.6/pedidos/status` | Consultar status pedido de venda | ⚠️ SIM |
| GET | `/v1.6/pedidos/{codigo}/status` | Consultar status pedido de venda | ⚠️ SIM |
| POST | `/v1.7/clientes` | Inserir novo cliente | ⚠️ SIM |
| GET | `/v1.7/clientes/lastid/{lastId}` | Obter cadastro de clientes | ⚠️ SIM |
| GET | `/v1.7/movimentoprodutos/listarmovimentos/lastid/{lastId}` | Listar movimentos de produtos | ⚠️ SIM |
| GET | `/v1.7/pedidocompra/listarpedidos/lastid/{lastID}/dataInicial/{datainicial}` | Listar pedidos de compra | ⚠️ SIM |
| GET | `/v1.7/pedidocompra/listarpedidos/pedidossemrcm/lastid/{lastID}/fornecedor/{cnpj}/unidade/{cnpjUnid}/datainicial/{dataInicial}/datafinal/{dataFinal}/vinc/{vinc}` | Listar pedidos de compra sem Recebimento | ⚠️ SIM |
| POST | `/v1.7/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| POST | `/v1.8/clientes` | Inserir novo cliente | ⚠️ SIM |
| GET | `/v1.8/clientes/lastid/{lastId}` | Obter cadastro de clientes |  |
| GET | `/v1.8/movimentoprodutos/listarmovimentos/lastid/{lastId}` | Listar movimentos de produtos | ⚠️ SIM |
| GET | `/v1.8/pedidocompra/listarpedidos/lastid/{lastID}/dataInicial/{datainicial}` | Listar pedidos de compra | ⚠️ SIM |
| GET | `/v1.8/pedidocompra/listarpedidos/pedidossemrcm/lastid/{lastID}/fornecedor/{cnpj}/unidade/{cnpjUnid}/datainicial/{dataInicial}/datafinal/{dataFinal}/vinc/{vinc}` | Listar pedidos de compra sem Recebimento | ⚠️ SIM |
| GET | `/v1.8/pedidocompra/{codigo}` | Listar pedidos de compra | ⚠️ SIM |
| POST | `/v1.8/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| POST | `/v1.9/clientes` | Inserir novo cliente | ⚠️ SIM |
| GET | `/v1.9/clientes/{codigo}` | Obter dados do cliente |  |
| GET | `/v1.9/movimentoprodutos/listarmovimentos/lastid/{lastId}` | Listar movimentos de produtos | ⚠️ SIM |
| GET | `/v1.9/pedidocompra/listarpedidos/lastid/{lastID}` | Listar pedidos de compra | ⚠️ SIM |
| POST | `/v1.9/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| POST | `/v1.9/pedidos/{codigo}/item` | Inserir novo item ao pedido | ⚠️ SIM |
| PUT | `/v1.9/pedidos/{codigo}/item/{codigoItem}` | Editar Item do Pedido | ⚠️ SIM |
| DELETE | `/v1.9/pedidos/{codigo}/item/{codigoItem}` | Excluir item do Pedido | ⚠️ SIM |
| GET | `/v1.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/departamento/{departamento}` | Obter dados do produto | ⚠️ SIM |
| GET | `/v1.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/grupo/{grupo}` | Obter dados do produto | ⚠️ SIM |
| GET | `/v2.0/pedidocompra/listarpedidos/lastid/{lastID}` | Listar pedidos de compra | ⚠️ SIM |
| POST | `/v2.0/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| POST | `/v2.0/pedidos/{codigo}/item` | Inserir novo item ao pedido | ⚠️ SIM |
| GET | `/v2.1/pedidocompra/listarpedidos/lastid/{lastID}` | Listar pedidos de compra | ⚠️ SIM |
| GET | `/v2.1/pedidocompra/listarpedidos/pedidossemrcm/lastid/{lastID}/fornecedor/{cnpj}/unidade/{cnpjUnid}/datainicial/{dataInicial}/datafinal/{dataFinal}/vinc/{vinc}` | Listar pedidos de compra sem Recebimento | ⚠️ SIM |
| GET | `/v2.1/pedidocompra/{codigo}` | Listar pedidos de compra | ⚠️ SIM |
| POST | `/v2.1/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| GET | `/v2.2/pedidocompra/listarpedidos/lastid/{lastID}` | Listar pedidos de compra | ⚠️ SIM |
| POST | `/v2.2/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| GET | `/v2.3/pedidocompra/listarpedidos/lastid/{lastID}` | Listar pedidos de compra | ⚠️ SIM |
| GET | `/v2.3/pedidocompra/{codigo}` | Listar pedidos de compra | ⚠️ SIM |
| POST | `/v2.3/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| POST | `/v2.5/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| POST | `/v2.6/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| POST | `/v2.7/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| GET | `/v2.7/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v2.7/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos` | Lista de produtos ativos detalhado | ⚠️ SIM |
| GET | `/v2.7/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos/dataHoraManutencao/{dataHoraManutencao}` | Lista de produtos ativos detalhado | ⚠️ SIM |
| GET | `/v2.7/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/departamento/{departamento}` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v2.7/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/grupo/{grupo}` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v2.7/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/marcados` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v2.7/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/semcalcularestoque` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v2.7/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/setor/{setor}` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v2.7/produtounidade/listaprodutos/{lastId}/unidade/{CNPJ}/detalhado/dataHoraManutencao/{dataHoraManutencao}` |  | ⚠️ SIM |
| GET | `/v2.7/produtounidade/{codigoBarras}/unidade/{CNPJ}/detalhado/consultarcodigobarras` | Obter dados do produto | ⚠️ SIM |
| GET | `/v2.7/produtounidade/{codigo}/unidade/{CNPJ}/detalhado` | Obter dados do produto | ⚠️ SIM |
| GET | `/v2.7/produtounidade/{codigo}/unidade/{CNPJ}/detalhado/estoque` | Obter dados do produto | ⚠️ SIM |
| POST | `/v2.8/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| GET | `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos` | Lista de produtos ativos detalhado | ⚠️ SIM |
| GET | `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos/dataHoraManutencao/{dataHoraManutencao}` | Lista de produtos ativos detalhado | ⚠️ SIM |
| GET | `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/departamento/{departamento}` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/grupo/{grupo}` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/marcados` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/semcalcularestoque` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/setor/{setor}` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v2.8/produtounidade/listaprodutos/{lastId}/unidade/{CNPJ}/detalhado/dataHoraManutencao/{dataHoraManutencao}` |  | ⚠️ SIM |
| GET | `/v2.8/produtounidade/{codigoBarras}/unidade/{CNPJ}/detalhado/consultarcodigobarras` | Obter dados do produto | ⚠️ SIM |
| GET | `/v2.8/produtounidade/{codigo}/unidade/{CNPJ}/detalhado` | Obter dados do produto | ⚠️ SIM |
| GET | `/v2.8/produtounidade/{codigo}/unidade/{CNPJ}/detalhado/estoque` | Obter dados do produto | ⚠️ SIM |
| POST | `/v2.9/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| GET | `/v2.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v2.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos` | Lista de produtos ativos detalhado | ⚠️ SIM |
| GET | `/v2.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos/dataHoraManutencao/{dataHoraManutencao}` | Lista de produtos ativos detalhado | ⚠️ SIM |
| GET | `/v2.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/departamento/{departamento}` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v2.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/grupo/{grupo}` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v2.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/marcados` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v2.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/semcalcularestoque` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v2.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/setor/{setor}` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v2.9/produtounidade/listaprodutos/{lastId}/unidade/{CNPJ}/detalhado/dataHoraManutencao/{dataHoraManutencao}` |  | ⚠️ SIM |
| GET | `/v2.9/produtounidade/listaprodutos/{lastRelease}/unidade/{CNPJ}/detalhado/customrelease` |  | ⚠️ SIM |
| GET | `/v2.9/produtounidade/{codigoBarras}/unidade/{CNPJ}/detalhado/consultarcodigobarras` | Obter dados do produto | ⚠️ SIM |
| GET | `/v2.9/produtounidade/{codigo}/unidade/{CNPJ}/detalhado` | Obter dados do produto | ⚠️ SIM |
| GET | `/v2.9/produtounidade/{codigo}/unidade/{CNPJ}/detalhado/estoque` | Obter dados do produto | ⚠️ SIM |
| POST | `/v3.0/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| GET | `/v3.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v3.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos` | Lista de produtos ativos detalhado | ⚠️ SIM |
| GET | `/v3.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos/dataHoraManutencao/{dataHoraManutencao}` | Lista de produtos ativos detalhado | ⚠️ SIM |
| GET | `/v3.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/departamento/{departamento}` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v3.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/grupo/{grupo}` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v3.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/marcados` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v3.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/semcalcularestoque` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v3.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/setor/{setor}` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v3.0/produtounidade/listaprodutos/{lastId}/unidade/{CNPJ}/detalhado/dataHoraManutencao/{dataHoraManutencao}` |  | ⚠️ SIM |
| GET | `/v3.0/produtounidade/listaprodutos/{lastRelease}/unidade/{CNPJ}/detalhado/customrelease` |  | ⚠️ SIM |
| GET | `/v3.0/produtounidade/{codigoBarras}/unidade/{CNPJ}/detalhado/consultarcodigobarras` | Obter dados do produto | ⚠️ SIM |
| GET | `/v3.0/produtounidade/{codigo}/unidade/{CNPJ}/detalhado` | Obter dados do produto | ⚠️ SIM |
| GET | `/v3.0/produtounidade/{codigo}/unidade/{CNPJ}/detalhado/estoque` | Obter dados do produto | ⚠️ SIM |
| POST | `/v3.1/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| GET | `/v3.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v3.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos` | Lista de produtos ativos detalhado | ⚠️ SIM |
| GET | `/v3.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos/dataHoraManutencao/{dataHoraManutencao}` | Lista de produtos ativos detalhado | ⚠️ SIM |
| GET | `/v3.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/departamento/{departamento}` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v3.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/semcalcularestoque` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v3.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/setor/{setor}` | Obter dados dos produtos | ⚠️ SIM |
| GET | `/v3.1/produtounidade/listaprodutos/{lastId}/unidade/{CNPJ}/detalhado/dataHoraManutencao/{dataHoraManutencao}` |  | ⚠️ SIM |
| GET | `/v3.1/produtounidade/listaprodutos/{lastRelease}/unidade/{CNPJ}/detalhado/customrelease` |  | ⚠️ SIM |
| GET | `/v3.1/produtounidade/{codigoBarras}/unidade/{CNPJ}/detalhado/consultarcodigobarras` | Obter dados do produto | ⚠️ SIM |
| GET | `/v3.1/produtounidade/{codigo}/unidade/{CNPJ}/detalhado` | Obter dados do produto | ⚠️ SIM |
| GET | `/v3.1/produtounidade/{codigo}/unidade/{CNPJ}/detalhado/estoque` | Obter dados do produto | ⚠️ SIM |
| POST | `/v3.2/pedidos` | Inserir Pedido de Venda | ⚠️ SIM |
| GET | `/v3.2/produtounidade/listaprodutos/{lastRelease}/unidade/{CNPJ}/detalhado/customrelease` |  | ⚠️ SIM |

## Detalhes

### GET `/v1.0/agendas/datainicio/{dataInicio}/datafim/{dataFim}/unidade/{CNPJ}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Buscar agenda de ofertas

Buscar agendas de ofertas da unidade dentro do período informado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `dataInicio` | path | sim | string | Data inicial da agenda, (Formato "dd-mm-yyyy") |
| `dataFim` | path | sim | string | Data final da agenda, (Formato "dd-mm-yyyy") |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |

**Respostas:**

- `200` Agendas retornadas — **GetAgendasOfertasV1** = object { response }

---

### GET `/v1.0/agendas/periodoFinal/unidade/{cnpj}/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Buscar agenda de ofertas

Buscar agendas de ofertas da unidade dentro do período informado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` |  | não |  |  |
| `lastId` |  | não |  |  |
| `datainicio` | query | sim | string | Data inicial da agenda, (Formato "dd-mm-yyyy") |
| `datafim` | query | sim | string | Data final da agenda, (Formato "dd-mm-yyyy") |

**Respostas:**

- `200` Agendas retornadas — **GetAgendasOfertasV1_1** = object { response }

---

### GET `/v1.0/agendas/periodoInicio/unidade/{cnpj}/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Buscar agenda de ofertas

Buscar agendas de ofertas da unidade dentro do período informado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` |  | não |  |  |
| `lastId` |  | não |  |  |
| `datainicio` | query | sim | string | Data inicial da agenda, (Formato "dd-mm-yyyy") |
| `datafim` | query | sim | string | Data final da agenda, (Formato "dd-mm-yyyy") |

**Respostas:**

- `200` Agendas retornadas — **GetAgendasOfertasV1_1** = object { response }

---

### POST `/v1.0/auditoria/documentos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Marcar como realizada a auditoria de documento

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: False):

- **RequestMarcaAuditoriaDocV_1_0** = object { transacao, operacao, usuarioErp, observacao }

**Respostas:**

- `200`  — **ResponseMarcaAuditoriaDocV_1_0** = object { response }

---

### PUT `/v1.0/auditoria/documentos/desmarcar`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Desmarcar como realizada a auditoria de documento

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `transacao` | query | sim | string | Transação do movimento a ser desmardado |
| `operacao` | query | sim | string | Operação do movimento a ser desmardado |

**Respostas:**

- `200`  — **ResponseMarcaAuditoriaDocV_1_0** = object { response }

---

### POST `/v1.0/auth`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Autenticar sessão

Autenticar sessão com usuário e senha

**Request body** (application/json, obrigatório: True):

- **AutenticarSessao** = object { usuario, senha }

**Respostas:**

- `200` Sessão autenticada — **RespostaPadrao** = object { response }

---

### GET `/v1.0/bens`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Retorna um Bem

Retorna um Bem pelo código ou plaqueta

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | query | não | string | Código do bem |
| `plaqueta` | query | não | string | Número da plaqueta |

**Respostas:**

- `200` Dados carregados com sucesso — **bens_V_1_0** = object { response }

---

### PUT `/v1.0/bens/update/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Alterar um Bem

Alterar dados referente a um Bem pelo seu código

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | integer | Código do Bem |

**Request body** (application/json, obrigatório: True):

- **bens_update_req_V_1_0** = object { descricao, complemento, funcao, gbenCodigo, numeroserie, plaqueta, codigoncm, ccstRateio, marca, identutil, vctogarantia, corretor, vlsegurado, franquia, vigsegi, vigsegf, apoliceseg, codresponsavel, peso, observacao }

**Respostas:**

- `200` Pedido de compra inserido — **bens_update_res_V_1_0** = object { response }

---

### GET `/v1.0/cestabasica/listarcestas/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar o cadastro de cestas básicas

Consultar o cadastro de cestas básicas do ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Último código de cesta lido, quando for a primeira leitura informar "0"  (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Cadastro de cestas básicas recuperado — **ConsultarCestasBasicasResponse** = object { response, cestasBasicas, maxCod }

---

### GET `/v1.0/cidades/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Buscar cidades cadastradas

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` |  | não |  |  |

**Respostas:**

- `200` Dados carregados com sucesso — **cadastroCidadeV1** = object { response }

---

### GET `/v1.0/classecommerce`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar dados de Classes Commerce

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Dados carregados com sucesso — **getClassVipCommerce** = object { response }

---

### GET `/v1.0/clientes/email/{email}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do cliente

Obter dados do cliente pelo email

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `email` | path | sim | string | Email do cliente |

**Respostas:**

- `200` Dados do cliente — **ConsultarDadosClienteResponse** = object { response }

---

### GET `/v1.0/clientes/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do cliente

Obter dados do cliente pelo código

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do cliente |

**Respostas:**

- `200` Dados do cliente — **ConsultarDadosClienteResponse** = object { response }

---

### PUT `/v1.0/clientes/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Editar Cliente

Editar dados de determinado cliente

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do cliente |

**Request body** (application/json, obrigatório: True):

- **EnviarDadosEditCliente** = object { nome, sexo, tipo, fone, uf, cep, cidade, endereco, bairro, cpf, rg, email }

**Respostas:**

- `200` Cliente Alterado — **RespostaPadrao** = object { response }

---

### GET `/v1.0/compradores/{lastID}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter lista de compradores cadastrados

Consulta dados referentes aos compradores.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | string | Código do último comprador consultado. Envie "0" caso queira consultar todos os compradores (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados com sucesso — **ListaCompradores_V_1_0** = object { response }

---

### POST `/v1.0/controleentregas`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Controle de entrega

Gravar controle de entrega

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **GravarControleEntrega** = object { data, dataVenda, entregador, unidade, cliente, bairro, cidade, endereco, complemento, nome, fone, valor, pdv, volumes, cupom, observacao1, observacao2, hora, referencia, numeroCaixas, dataBaixa }

**Respostas:**

- `200` Controle de entrega gravado com sucesso — **RespostaControleEntrega** = object { response }

---

### GET `/v1.0/controleentregas/{transacao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter Controle de entrega

Consulta dados referentes ao Controle de entrega.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `transacao` | path | sim | string | Transação do Controle de entrega. |

**Respostas:**

- `200` Dados carregados — **ConsultaControleEntrega** = object { response }

---

### GET `/v1.0/estoques`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter classificação de estoques com seus identificadores

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Configuração de Estoques — **ConsultarEstoquesV10** = object { response }

---

### GET `/v1.0/fde/lancamentos/{lastRelease}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter os lançamentos do tipo FDE

Obter os lançamentos do tipo FDE com base no código release

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastRelease` | path | sim | string | Código a ser considerado a maior na pesquisa de lançamentos (Enviar 0 para a primeira consulta) |
| `limit` | query | não | number | Número máximo de movimentos que será retornado na consulta |

**Respostas:**

- `200`  — **ResponseFdeLancamentos1_0** = object { response }

---

### GET `/v1.0/financeiro/centrodecustos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar centro de custos

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Consultar centro de custos — **ConsultarCentroCustosResponse** = object { response }

---

### GET `/v1.0/financeiro/cliente/{CPF_CNPJ}/saldolimitecheque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar limite no cheque

Consultar limite de crédito do cliente no cheque

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF_CNPJ` | path | sim | number | CPF/CNPJ do cliente a ser consultado |

**Respostas:**

- `200` Limite de crédito no cheque retornado — **ConsultarLimCredResponse** = object { response }

---

### GET `/v1.0/financeiro/cliente/{CPF_CNPJ}/saldolimitecredito`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar limite de crédito do cliente

Consultar limite de crédito do cliente no estabelecimento

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF_CNPJ` | path | sim | number | CPF/CNPJ do cliente a ser consultado |

**Respostas:**

- `200` Limite de crédito retornado — **ConsultarLimCredResponse** = object { response }

---

### GET `/v1.0/financeiro/cliente/{CPF_CNPJ}/saldolimitecredito/cartao`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar limite de crédito de cartão do cliente

Consultar limite de crédito de cartão do cliente no estabelecimento

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF_CNPJ` | path | sim | string | CPF/CNPJ do cliente a ser consultado |

**Respostas:**

- `200` Limite de crédito do cartão retornado — **ConsultarLimCredResponse** = object { response }

---

### GET `/v1.0/financeiro/funcionario/{CPF}/saldolimitecredito`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar limite de crédito do funcionário

Consultar limite de crédito do funcionário no estabelecimento

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF` | path | sim | number | CPF do funcionário a ser consultado |

**Respostas:**

- `200` Limite de crédito retornado — **ConsultarLimCredResponse** = object { response }

---

### GET `/v1.0/financeiro/movFinalizadoras/dataInicial/{dataInicial}/dataFinal/{dataFinal}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** MovFinalizadorasDet

Retorna dados da tabela MovFinalizadorasDet.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `dataInicial` | path | sim | string | Data inicial do período (Formato dd-mm-yyyy) |
| `dataFinal` | path | sim | string | Data final do período (Formato dd-mm-yyyy) |
| `cnpj` | query | sim | string | cnpj da Unidade que deve ser considerada no filtro |

**Respostas:**

- `200`  — **RespostaMovFinalizadoras_V_1_0** = object { response }

---

### GET `/v1.0/financeiro/movFormaVendaPDV/lastID/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200`  — **RespostaMovFormaVdaPDV_V_1_0** = object { response }

---

### GET `/v1.0/financeiro/pendenciasFinanceiras/dataInicial/{dataInicial}/dataFinal/{dataFinal}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Pendências financeiras

Pendências financeiras filtrados por data e cnpj da unidade.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `dataInicial` | path | sim | string | Data inicial do período (Formato dd-mm-yyyy) |
| `dataFinal` | path | sim | string | Data final do período (Formato dd-mm-yyyy) |
| `cnpj` | query | sim | string | cnpj da Unidade que deve ser considerada no filtro |

**Respostas:**

- `200` Dados carregados com sucesso — **listaPendenciasFinanceirasFornecedorResponse** = object { response }

---

### GET `/v1.0/financeiro/pendenciasFinanceiras/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200` Requisição processada com sucesso — **ResponsePendenciasFinanceiras_V_1_0** = object { response }

---

### GET `/v1.0/financeiro/planocontas`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar plano de contas

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Consultar plano de contas Gerencial — **ConsultarPlanoContasResponseV1_0** = object { response }

---

### GET `/v1.0/fiscal/getnfecupom/cupom/{cupom}/pdv/{pdv}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Nota fiscal eletrônica emitida para um determinado cupom fiscal

Buscar nota fiscal eletrônica emitida para um determinado cupom fiscal.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cupom` | path | sim | string | Número do cupom fiscal |
| `pdv` | path | sim | string | Código do PDV onde o cupom foi emitido |

**Respostas:**

- `200` Dados carregados com sucesso — **NfeByCupom** = object { response }

---

### GET `/v1.0/flexapp/concorrente`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Recuperar cadastro de concorrentes

Cadastro de concorrentes

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaGetConcorrentes** = object { response }

---

### GET `/v1.0/formaspagamento`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Cadastro de formas de pagamento

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Dados carregados com sucesso — **listaFormasPagamentoResponse** = object { response }

---

### GET `/v1.0/fornecedor/listaFornecedores/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Cadastro dos Fornecedores

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Código do último fornecedor consultado. Envie "0" caso queira consultar todos os fornecedores (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados com sucesso — **listaFornecedoresResponse** = object { response }

---

### GET `/v1.0/fornecedor/pendenciasFinanceiras/dataInicial/{dataInicial}/dataFinal/{dataFinal}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Pendências financeiras de fornecedores

Pendências financeiras de fornecedores filtrados por data e código da entidade ou CNPJ_CPF.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `dataInicial` | path | sim | string | Data inicial do período (Formato dd-mm-yyyy) |
| `dataFinal` | path | sim | string | Data final do período (Formato dd-mm-yyyy) |
| `codigo` | query | sim | string | Código Entidade do fornecedor a ser filtrado. |
| `cnpj` | query | sim | string | cnpj da unidade. |

**Respostas:**

- `200` Dados carregados com sucesso — **listaPendenciasFinanceirasFornecedorResponse** = object { response }

---

### PUT `/v1.0/fornecedor/situacao`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Alterar situação do fornecedor

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` | query | sim | string | cnpj do fornecedor |
| `updateVinculados` | query | não | boolean | indica se atualiza os fornecedores vinculados |
| `updateCnpjRaiz` | query | não | boolean | indica se atualiza os fornecedores com mesmo CNPJ raiz |

**Request body** (application/json, obrigatório: True):

- **UpdateSituacaoFornecedorV1_0** = object { situacao }

**Respostas:**

- `200` Situação fornecedor alterada com sucesso — **ResponseUpdateSituacaoFornecedorV1_0** = object { response }

---

### GET `/v1.0/fornecedor/{codigo}/regranegocio`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Cadastro dos Fornecedores

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do fornecedor a ser consultado. |
| `cnpjUnidade` | query | sim | string | Cnpj da unidade a ser considerada na consulta. |

**Respostas:**

- `200` Dados carregados com sucesso — **RegraNegocioResponse_V1** = object { response }

---

### GET `/v1.0/funcionario/codcpf/{codcpf}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar cadastro de funcionário

Consultar cadastro de funcionário por meio do código ou CPF.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codcpf` | path | sim | string | Código ou CPF do funcionário. |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaFuncionario_V_1_0** = object { response }

---

### GET `/v1.0/funcionario/lastid/{lastid}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar cadastro de funcionários

Consultar cadastro de funcionários por meio de paginação.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastid` | path | sim | string | Código do último funcionário ou 0. |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaFuncionarios_V_1_0** = object { response }

---

### GET `/v1.0/grupos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar o cadastro de grupos de produtos

Consultar o cadastro de grupos de produtos do ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Cadastro de grupos recuperado — **ConsultarCadGruposResponse** = object { response }

---

### POST `/v1.0/grupos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir o cadastro de grupos de produtos

Inserir o novo cadastro de grupos de produtos do ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **InserirGrupoV_1_00** = object { classificacao, descricao, prodServ, decimaisEst, recuo, periodos, codigoNCM, comissao, dpto_codigo, comportamento, classFiscal, tipoItem, dtEstMin, ctrlEstMin, percAbast, abatimento }

**Respostas:**

- `200` Grupo inserido — **InserirGrupoResponse** = object { response }

---

### PUT `/v1.0/grupos/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200` Grupo alterado — **UpdateGrupoResponse** = object { response }

---

### DELETE `/v1.0/grupos/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Deletar o cadastro de grupos de produtos

Deletar o cadastro de grupos de produtos do ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | integer | codigo do cadastro do grupo de produtos a ser deletado |

**Respostas:**

- `200` Grupo deletado — **DeleteGrupoResponse** = object { response }

---

### POST `/v1.0/industcomp`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Cadastrar produto industrializado

Efetuar o cadastro de produto industrializado, podendo efeturar o cadastro também dos itens de 'receita'

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: False):

- **RequestCadastroProdutosIndustrializados** = object { codigo, descricao, tipo, unidade, rendimento, pesoTotal, precoTotal, dataCusto, comportamento, fase, tempoProducao, observacao, quantidadeMinimaProduzir, quantidadeProduzir, quantidadeMultiplaProduzir, baseProducao, tempoAntecedencia, tempoProducaoHomensHora, prioridadeProducao, tempoPreparo, estoqueSeguranca, baixaEstoqueMateriaPrima, fatorProducao, AgrupamentoUnidadesValidas, departamento, itens }

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaPadrao_SemMessageV2** = object { response }

---

### GET `/v1.0/industcomp/lastId/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar cadastro dos produtos industrializados

Consultar o cadastro dos produtos industrializados

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Código do último produto consultado. Envie "0" caso queira consultar todos os produtos (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaConsultaProdutosIndustrializados** = object { response }

---

### GET `/v1.0/industcomp/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar cadastro de produto industrializado

Consultar o cadastro de produto industrializado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do a produto consultado. |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaConsultaProdutoIndustrializado** = object { response }

---

### PUT `/v1.0/industcomp/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Editar um produto industrializado

Efetuar a edição de produto industrializado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do a produto a ser editado. |

**Request body** (application/json, obrigatório: False):

- **Industrializado** = object { codigo, descricao, tipo, unidade, rendimento, pesoTotal, precoTotal, dataCusto, comportamento, fase, tempoProducao, observacao, quantidadeMinimaProduzir, quantidadeProduzir, quantidadeMultiplaProduzir, baseProducao, tempoAntecedencia, tempoProducaoHomensHora, prioridadeProducao, tempoPreparo, estoqueSeguranca, baixaEstoqueMateriaPrima, fatorProducao, AgrupamentoUnidadesValidas, departamento }

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaPadrao_SemMessageV2** = object { response }

---

### DELETE `/v1.0/industcomp/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Deletar um produto industrializado

Efetuar a exclusão do cadastro de industrialização

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do a produto a ser editado. |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaPadrao_SemMessageV2** = object { response }

---

### POST `/v1.0/industdecomp`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Cadastrar produto da 'receita' de um industrializado

Cadastrar produto que faz parte da 'receita' de um industrializado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: False):

- **ProdutoDeIndustrializadoCadastro** = object { codigoIndustrializado, codigoItem, unidade, quantComercializacao, quantReceita, pesoItem, precoItem, fase }

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaPadrao_SemMessageV2** = object { response }

---

### DELETE `/v1.0/industdecomp/codigo1/{codigo1}/codigo2/{codigo2}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Deletar um produto 'receita'

Efetuar a exclusão do cadastro de um produto da 'receita' pertencente de um industrializado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo1` | path | sim | string | Código do produto industrializado. |
| `codigo2` | path | sim | string | Código do produto 'receita' |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaPadrao_SemMessageV2** = object { response }

---

### GET `/v1.0/industdecomp/codigo1/{codigo1}/codigo2/{codigo2}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar cadastro de um produto pertencente a um industrializado

Consultar cadastro de um produto pertencente a 'receita' de um produto industrializado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo1` | path | sim | string | Código do produto industrializado. |
| `codigo2` | path | sim | string | Código do produto 'receita' |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaConsultaProdutoReceitaIndustrializado** = object { response }

---

### GET `/v1.0/industdecomp/{codigo1}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar cadastro dos produtos 'receita' de um produto industrializado

Consultar cadastro dos produtos da 'receita' de um produto industrializado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo1` | path | sim | string | Código do produto industrializado a ser consultado |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaConsultaTodosProdutosReceitaIndustrializado** = object { response }

---

### PUT `/v1.0/industdecomp/{codigo1}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Editar o cadastro de um produto 'receita'

Editar o cadastro de um produto da 'receita' pertencente a um produto industrializado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo1` | path | sim | string | Código do produto industrializado a qual o item a ser editado pertence. |

**Request body** (application/json, obrigatório: False):

- **ProdutoDeIndustrializado** = object { codigoItem, unidade, quantComercializacao, quantReceita, pesoItem, precoItem, fase }

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaPadrao_SemMessageV2** = object { response }

---

### GET `/v1.0/logout`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Efetuar logout

Destruir a sessão e limpar o cache

**Respostas:**

- `200` Logout efetuado — **RespostaPadrao** = object { response }

---

### POST `/v1.0/metasprod`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir novas Metas de Produtos

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: False):

- **bodyMetasProd_V1** = object { metas }

**Respostas:**

- `200` Meta gravada com sucesso — **metasProdSucess** = object { response }

---

### PUT `/v1.0/metasprod`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Alterar Meta de Produto cadastrada

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: False):

- **bodyMetaProd_V1** = object { data, cnpjUnidade, departamento, grupo, vendas, lucros, estoques, giro, percentCmv, margemContrib, compras, perdas, verbas, verbasLiq, devolucoes, faltas, percentLucros, sobras }

**Respostas:**

- `200` Meta gravada com sucesso — **metasProdSucess** = object { response }

---

### GET `/v1.0/metasprod/cnpj/{cnpj}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar Metas de Produtos de uma unidade

Consultar metas de produtos de uma unidade, podendo ser filtrado por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` | path | sim | string | Cnpj da unidade |
| `data` | query | não | string | Data inicio a ser considerada, sendo retornado datas iguais ou maiores que a informada |
| `tipo` | query | não | string | Filtro por tipo de metas: 'M' - Mensal; 'G' - Por Grupo; 'D' - Por Departamento |

**Respostas:**

- `200` Dados carregados com sucesso — **getMetasProd_V1** = object { response }

---

### GET `/v1.0/movimentoprodutos/listarmovimentos/lastid/{lastID}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar movimentos de produtos

Listar movimentos de produtos por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `datainicial` | query | sim | string | Data em que inicia-se a leitura dos movimentos, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `tipoconsulta` | query | sim | string | Tipo da consulta, tipos válidos (CODIGO_DCTO, TIPO_DCTO) |
| `valores` | query | sim | string | Valores para filtro, enviar tipos de documento quando informar (tipoconsulta = TIPO_DCTO) e quando enviar (tipoconsulta = CODIGO_DCTO) deve-se enviar os códigos dos documentos que devem ser considerados no filtro |

**Respostas:**

- `200` Movimentos retornados — **MovProdDResponse** = object { response }

---

### GET `/v1.0/movimentoprodutos/listarmovimentosevp/lastid/{lastID}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar movimentos de produtos vendidos no PDV

Listar movimentos de produtos vendidos no PDV por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `datainicial` | query | sim | string | Data em que inicia-se a leitura dos movimentos, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `documentos` | query | sim | string | Valores para filtro, deve-se enviar os códigos dos documentos que devem ser considerados no filtro |

**Respostas:**

- `200` Movimentos retornados — **VdaDetResponse** = object { response }

---

### GET `/v1.0/movimentoprodutos/semrecebimento/documentos/{docs}/codDocumento/{codDocumento}/unidade/{cnpj}/catentidade/{catentidade}/codentidade/{codentidade}/datainicial/{dataini}/datafinal/{datafim}/validardestino/{validar}/lastid/{lastid}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Busca de Movimentos de Produtos Sem RCM

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `docs` | path | sim | string | Tipo do documento da movimentação. Docs Permitidos: PBX;EAQ;EOE;EET;EDV;ETE;EBR;EEC;EES;EOS;EST;EDC;ETS;EBC;ECI;ETM;ESC;EFE;ESE;EPE;ESS;EVD;ETA;EVA |
| `codigo do documento` | path | sim | string | codigo de documento que tem dentro do tipo de documento |
| `cnpj` | path | sim | string | CNPJ da unidade a consultar |
| `catentidade` | path | sim | string | Categoria da entidade a consultar. Valores válidos: F;U;C;N; (Fornecedor;Unidade;Cliente;Nenhuma) |
| `codentidade` | path | sim | string | Código da entidade a consultar |
| `dataini` | path | sim | string | Data em que inicia-se a consulta por movimentos, considera-se até o dia indicado em datafim (Formato "dd-mm-yyyy") |
| `datafim` | path | sim | string | Data em que finaliza-se a consulta por movimentos (Formato "dd-mm-yyyy") |
| `validar` | path | sim | boolean | Flag para validaro ou não o destino |
| `lastid` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados processados com sucesso — **MovProdRCMResponseV10** = object { response }

---

### GET `/v1.0/movimentos/cnpj/{cnpj}/gerencial-rat`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar movimentos gerenciais de rateio de uma unidade

Consultar movimentos gerenciais de rateio de uma unidade dentro de um período (Período máximo de 15 dias)

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

- `200`  — **ConsultarMovimentosGerenciaisRatResponse** = object { response }

---

### GET `/v1.0/negociacoes`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar negociações disponíveis

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `unidade` | query | sim | string | código da unidade |
| `datainicial` | query | sim | string | Data Inicial para filtro |
| `datafinal` | query | sim | string | Data Inicial para filtro |
| `fornecedor` | query | sim | string | Data Inicial para filtro |

**Respostas:**

- `200` Dados carregados com sucesso — **Retorno_ConsultaNegociacoes_V_1_0** = object { response }

---

### POST `/v1.0/nlq`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir NLQ

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: False):

- **NlqInsert_V_1_0** = object { origemApp, origemVersao, origemIdentificador, CodDcto, usuario, ListProduto }

**Respostas:**

- `200` Dados carregados com sucesso — **Retorno_PostNLQ_V_1_0** = object { response }

---

### GET `/v1.0/patrimonial/bens`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Retorna o cadastro de bens patrimoniais

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | query | não | string | Código do bem |
| `plaqueta` | query | não | string | Número da plaqueta |
| `identificador` | query | não | string | Identificador que pode corresponder o código ou a plaqueta |
| `unidade` | query | não | string | Unidade em que o bem está localizado |
| `lastId` | query | não | number | ID retornado na última requisição para utilizar na paginação (Keyset/Seek Pagination) |
| `limit` | query | não | number | Limite máximo de bens retornados na requisição (Default: Limite configurado) |

**Respostas:**

- `200` Requisição processada com sucesso — **bens_V_1_0** = object { response }

---

### GET `/v1.0/pedidocompra/listarpedidos/lastid/{lastID}/dataInicial/{datainicial}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra

Listar pedidos de compra por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `datainicial` | path | sim | string | Data em que inicia-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponse_V_1_00** = object { response, lastid }

---

### POST `/v1.0/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir pedido de venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **AddPedidoPostDeprecated0** = object { data, codigoCliente, formaPagamento, codigoVendedor, observacao, especie, itens }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponse** = object { response }

---

### GET `/v1.0/pedidos/listar/status/datamodificacao/{datahora}/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar status pedido de venda

Consultar o status de um pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `datahora` | path | sim | string | Data e hora da modificação do status do pedido. A data e hora deve estar no formato "dd-MM-yyyy hh:mm:ss" |
| `lastId` | path | sim | string | Código do último pedido de venda consultado. Envie "0" caso queira consultar todos os fornecedores (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Status do pedido retornado — **ConsultarDataModPedido** = object { response }

---

### GET `/v1.0/pedidos/pedidocliente/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar processamento do pedido de venda pelo número de pedido do cliente

Consultar processamento da inserção do pedido de venda pelo número de pedido do cliente

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido |

**Respostas:**

- `200` Status do pedido — **StatusProcessamentoPedidoResponsev3** = object { response }

---

### GET `/v1.0/pedidos/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar processamento do pedido de venda

Consultar processamento da inserção do pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido |

**Respostas:**

- `200` Status do pedido — **StatusProcessamentoPedidoResponseDeprecated** = object { response }

---

### PUT `/v1.0/pedidos/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Editar Pedido de Venda

Editar dados do pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do pedido de venda |

**Request body** (application/json, obrigatório: True):

- **EditarPedidoDeprecated0** = object { data, codigoCliente, formaPagamento, codigoVendedor, observacao, especie, itens }

**Respostas:**

- `200` Pedido Alterado — **RespostaPadrao** = object { response }

---

### POST `/v1.0/pedidos/{codigo}/item`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir novo item ao pedido

Inserir um novo item ao pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do pedido de venda |

**Request body** (application/json, obrigatório: True):

- **ItemPedido** = object { codigoProduto, qtdUnitaria, qtdEmbalagem, valorProduto, percDesconto }

**Respostas:**

- `200` Item adicionado — **RespostaPadrao** = object { response }

---

### PUT `/v1.0/pedidos/{codigo}/item/{codigoItem}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Editar Item do Pedido

Editar item do pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do pedido de venda |
| `codigoItem` | path | sim | number | Código do produto |

**Request body** (application/json, obrigatório: True):

- **ItemPedido** = object { codigoProduto, qtdUnitaria, qtdEmbalagem, valorProduto, percDesconto }

**Respostas:**

- `200` Item alterado com sucesso — **RespostaPadrao** = object { response }

---

### GET `/v1.0/pedidos/{codigo}/status`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar status pedido de venda

Consultar o status de um pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido de venda |

**Respostas:**

- `200` Status do pedido retornado — **ConsultarStatusAltPVDResponse** = object { response }

---

### POST `/v1.0/pendest/incluir`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Incluir pendências de estoque

Incluir pendências de estoque no sistema

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de Autenticação |

**Request body** (application/json, obrigatório: True):

- **V_1_3_pendest_incluir** = object { Inclusoes, Baixas }

**Respostas:**

- `200` Iniciado processamento das pendências de estoque. Retorna um recibo para verificar o status desse processamento. — { response: object { status, messages, content } }

---

### GET `/v1.0/pendest/que/lastid/{lastID}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter pendências de estoque

Obter pendências de estoque da empresa

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | string | Último id lido na paginação, enviar zero para consultar desde a o início do cadastro.  (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados retornados — **ObterPendResponse** = object { response }

---

### GET `/v1.0/precadastro`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados de pré cadastro do produto

Obter dados de pré cadastro de produtos

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` PreCadastro de produto recuperado com sucesso — **ConsultarPreCadastrosV_1_0** = object { response }

---

### POST `/v1.0/precadastro`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir dados de pré cadastro do produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PreCadastroPostV_1_0** = object { unid_codigo, descricao, complemento, marca, codBarras, descrPdvs, emb, qemb, prod_Codigo, codNcm, obs, balanca, peso, pesoLiq, prodFuncao, cest, codCaixa, lastro, camadas, forn_Codigo, validade, altura, largura, profundidade, codProdFor }

**Respostas:**

- `200` PreCadastro de produto recuperado com sucesso — **InsertPreCadastroV_1_0** = object { response }

---

### GET `/v1.0/precadastro/{sequencia}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados de pré cadastro do produto

Obter dados de pré cadastro do produto incluído pelo endPoint de inclusão de pré Cadastro

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `sequencia` | path | sim | number | Sequencia de indentificação do pré cadastro |

**Respostas:**

- `200` PreCadastro de produto recuperado com sucesso — **ConsultarPreCadastroV_1_0** = object { response }

---

### GET `/v1.0/precocliente/lastid/{lastid}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

### GET `/v1.0/produto/codigobarrasalterados/ativos/unidade/{unidade}/lastid/{lastID}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados de códigos de barras alternativos dos produtos ativos

Obter dados de códigos de barras alternativos para os produtos ativos

Este serviço irá retornar os itens páginados conforme configuração no servidor

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `unidade` | path | sim | string | Unidade do cliente |
| `lastID` | path | sim | number | Codigo do ultimo produto que retornou na lista. Para a primeira página de registros enviar esse valor igual a zero. (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados — **ConsultarCodBarrasAlternativoListaResponse** = object { response }

---

### GET `/v1.0/produto/codigobarrasalterados/lastid/{lastID}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados de códigos de barras alternativos

Obter dados de códigos de barras alternativos para o produto

Este serviço irá retornar os itens páginados conforme configuração no servidor

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Codigo do ultimo produto que retornou na lista. Para a primeira página de registros enviar esse valor igual a zero. (mesmo passando 0 os dados retornam paginados) |
| `dataAlteracao` | query | não | string | Data de alteração ( dd-MM-yyyy ) a ser considerada para alterações posteiores ou iguais a data informada |

**Respostas:**

- `200` Dados carregados — **ConsultarCodBarrasAlternativoListaResponse** = object { response }

---

### GET `/v1.0/produto/excluidos/lastid/{lastid}/dataexclusao/{dataexclusao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

### GET `/v1.0/produto/listaprodutos/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar cadastro de um produto

Consultar o cadastro geral de um produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | number | Codigo do ultimo produto que retornou na lista. Para a primeira página de registros enviar esse valor igual a zero. (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados — **ConsultarCadastroProdutosResponse** = object { response }

---

### GET `/v1.0/produto/listaprodutos/{lastId}/detalhado`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar cadastro de um produto

Consultar o cadastro detalhado de um produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | number | Codigo do ultimo produto que retornou na lista. Para a primeira página de registros enviar esse valor igual a zero. (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados — **ConsultarCadastroProdutosDetalhadoResponse** = object { response }

---

### PUT `/v1.0/produto/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Editar cadastro de um produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | código do produto |

**Request body** (application/json, obrigatório: False):

- **EditProdutoV_1_0** = object { descricao, complemento, marca, classe, tipo, descrPdvs, peso, pesoLiq, emb, qemb, extra1, extra2, extra3, extra4, extra5, extra6, extra7, extra8, extra9, altura, largura, profundidade, lastro, camadas, descritivo, codCaixa, display, descricaoCliente, codigoNCM, classFiscal, temperatura, varPeso }

**Respostas:**

- `200`  — **RespostaEditProdutoV_1_0** = object { response }

---

### GET `/v1.0/produto/{codigo}/codigobarrasalterados`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados de códigos de barras alternativos

Obter dados de códigos de barras alternativos para o produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Codigo do produto |

**Respostas:**

- `200` Dados carregados — **ConsultarCodBarrasAlternativoProdResponse** = object { response }

---

### GET `/v1.0/produto/{codigo}/detalhado`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar cadastro de um produto

Consultar o cadastro detalhado de um produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Codigo do produto a ser consultado |

**Respostas:**

- `200` Dados carregados — **ConsultarCadastroProdutoDetalhadoResponse** = object { response }

---

### GET `/v1.0/produto/{prodCodigo}/fornecedor/{fornCodigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados dos codigos do fornecedor vinculados a um produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `prodCodigo` | path | sim | string | Código interno do Produto a ser consultado |
| `fornCodigo` | path | sim | string | Código interno do fornecedor a ser consultado |

**Respostas:**

- `200`  — **ProdutoFornecedorResponse_V_1_0** = object { response }

---

### GET `/v1.0/produtos/lastid/{lastId}/fornecedor/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados dos produtos vinculados ao fornecedor

Obter dados dos produtos vinculados ao fornecedor informado, sendo resultado paginado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Código do último produto consultado. Envie '0' caso queira consultar todos os produtos (mesmo passando 0 os dados retornam paginados) |
| `codigo` | path | sim | string | Código interno do fornecedor a ser consultado |

**Respostas:**

- `200`  — **ProdutosFornecedorRes** = object { response }

---

### POST `/v1.0/produtounidade/auditoriaestoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Incluir auditoria de estoque

Incluir auditoria de estoque no sistema

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **IncluirAuditoriaPost** = object { auditorias }

**Respostas:**

- `200` Auditoria de estoque adicionada — **RespostaPadrao** = object { response }

---

### GET `/v1.0/produtounidade/auditoriaestoque/{lastID}/datainicial/{dataInicial}/datafinal/{dataFinal}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter auditorias de estoque

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | string | Código do último comprador consultado. Envie "0" caso queira consultar todos os compradores (mesmo passando 0 os dados retornam paginados) |
| `dataInicial` | path | sim | string | Data inicial do período (Formato dd-mm-yyyy) |
| `dataFinal` | path | sim | string | Data final do período (Formato dd-mm-yyyy) |
| `unidades` | query | sim | string | Código das unidades separadas por ;   Exemplo unidades=001;002;003 |

**Respostas:**

- `200`  — **RespostaGetAuditoriaEstoque** = object { response }

---

### GET `/v1.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter cadastro de produtos

Obter cadastro de produtos da unidade, retornará de 100 em 100 registros. Enquanto o código do ultimo produto retornado for menor que o maxCod indica que existem mais produtos a serem consultados.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade que deseja consultar o cadastro |
| `departamentos` | query | não | string | Departamentos dos produtos que deseja filtrar separados por ';' |
| `limit` | query | não | string | Limite de registros a serem retornados por requisição, Default 100 |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoDeprecatedResponse** = object { response, maxCod }

---

### GET `/v1.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/departamento/{departamento}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do produto

Consulta dados de um determinado produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `departamento` | path | sim | string | Código do departamento a consultar |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoDeprecatedResponse** = object { response, maxCod }

---

### GET `/v1.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados dos produtos

Consulta dados detalhados dos produtos com informação de estoque.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoV1** = object { response }

---

### GET `/v1.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/departamento/{departamento}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados dos produtos

Consulta dados detalhados dos produtos de um determinado departamento.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `departamento` | path | sim | string | Código do departamento |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoV1** = object { response }

---

### GET `/v1.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/grupo/{grupo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados dos produtos

Consulta dados detalhados dos produtos de um determinado grupo.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `grupo` | path | sim | string | Código do grupo |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoV1** = object { response }

---

### GET `/v1.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/semcalcularestoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados dos produtos

Consulta dados detalhados dos produtos sem calcular estoque.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoV1** = object { response }

---

### GET `/v1.0/produtounidade/listaprodutos/{lastId}/unidade/{CNPJ}/detalhado/dataalteracao/{dataAlteracao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados dos produtos

Consulta dados detalhados dos produtos a partir da data de alteracao informada.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` |  | não |  |  |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `dataAlteracao` | path | sim | string | Data da alteração a ser considerada na consulta (Formato "dd-mm-yyyy") |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoV1** = object { response }

---

### POST `/v1.0/produtounidade/pendenciaestoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Incluir pendências de estoque

Incluir pendências de estoque no sistema

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **IncluirPendPost** = object { dataMovimento, dataEntrega, unidadeOrigem, unidadeDestino, tipoPendencia, codigoPendencia, especie, codigoDocumento, categoriaParticipante, participante, pendencias }

**Respostas:**

- `200` Pendência de estoque adicionada — **RespostaPadrao** = object { response }

---

### POST `/v1.0/produtounidade/unidade/{CNPJ}/atualizaretiquetaprecos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Atualizar etiqueta de preços

Atualizar etiqueta de preços da unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CNPJ` | path | sim | string | CNPJ da unidade |

**Request body** (application/json, obrigatório: True):

- **AtualizarEtiquetasPost_V_1_0** = object { codigoProduto, preco }

**Respostas:**

- `200` Etiquetas atualizadas — **RespostaPadrao** = object { response }

---

### GET `/v1.0/produtounidade/unidade/{CNPJ}/departamento/{departamento}/rcm/{calcularRCM}/vdonline/{considerarVendaOnline}/datainicial/{dataInicial}/datafinal/{dataFinal}/snapshotestoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter snapshot do estoque

Obter snapshot do estoque no período

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `departamento` | path | sim | string | Código do departamento dos produtos a consultar |
| `calcularRCM` | path | sim | string | Define se irá considerar recebimentos de mercadorias sem que haja entrada registrada da mesma, a qual será acrescida ao estoque disponível.  Pode receber os valores "SIM" e "NAO". |
| `considerarVendaOnline` | path | sim | string | Define se irá considerar venda online de mercadorias, a qual será deduzida do estoque disponível  Pode receber os valores "SIM" e "NAO". |
| `dataInicial` | path | sim | string | Data Inicial do período (Formato "dd-mm-yyyy") |
| `dataFinal` | path | sim | string | Data Final do período (Formato "dd-mm-yyyy") |

**Respostas:**

- `200` Snapshot do estoque retornado — **SnapShotProdutoResponse** = object { response }

---

### GET `/v1.0/produtounidade/{codBarras}/unidade/{CNPJ}/estoquecodigobarras`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do produto

Obter dados do produto pelo código de barras

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codBarras` | path | sim | string | Codigo de barras do produto |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |

**Respostas:**

- `200` Dados carregados — **ConsultarEstProdutoResponse** = object { response }

---

### GET `/v1.0/produtounidade/{codigoProduto}/unidade/{CNPJ}/rcm/{calcularRCM}/vdonline/{considerarVendaOnline}/datainicial/{dataInicial}/datafinal/{dataFinal}/snapshotestoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter snapshot do estoque

Obter snapshot do estoque do produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigoProduto` | path | sim | string | Código do produto a consultar |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `calcularRCM` | path | sim | string | Define se irá considerar recebimentos de mercadorias sem que haja entrada registrada da mesma, a qual será acrescida ao estoque disponível.  Pode receber os valores "SIM" e "NAO". |
| `considerarVendaOnline` | path | sim | string | Define se irá considerar venda online de mercadorias, a qual será deduzida do estoque disponível  Pode receber os valores "SIM" e "NAO". |
| `dataInicial` | path | sim | string | Data Inicial do período (Formato "dd-mm-yyyy") |
| `dataFinal` | path | sim | string | Data Final do período (Formato "dd-mm-yyyy") |

**Respostas:**

- `200` Snapshot do estoque retornado — **SnapShotProdutosResponse** = object { response }

---

### GET `/v1.0/produtounidade/{codigo}/unidade/{CNPJ}/detalhado/estoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do produto

Consulta dados detalhados do produto.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do produto consultado. |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoV1** = object { response }

---

### GET `/v1.0/produtounidade/{lastID}/unidade/{CNPJ}/etiquetaspendentes/{campoConsiderar}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar etiquetas pendentes

Consultar etiquetas pendentes da unidade

O retorno será paginado, com número de itens definido em configuração do serviço.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do produto que retornou da lista. Para solicitar a primeira página de informações, enviar :lastID igual a zero.  (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `campoConsiderar` | path | sim | string | Preço a ser considerado  Possíveis valores: PRECO_PDV, PRECO_VENDA |

**Respostas:**

- `200` Etiquetas pendentes retornadas — **EtiquetasPendentesResponse_V_1_0** = object { response }

---

### POST `/v1.0/programacaoprecos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir uma nova Programação de Preço

Inserir um novo cadastro de Programação de Preço

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **InserirProgramacaoPrecos** = object { status, codigoAgenda, unidade, codigoProduto, precoAlteracao, uf, dataInicial, dataFinal, horaInicial, horaFinal, precoVenda, prioridade, oferta, qtdeMaximaCliente, fatorPreco, obs, dataInicialRel, dataFinalRel, autorizado }

**Respostas:**

- `200` Programação de Preço inserido — **InserirProgramPrecoResponse** = object { response }

---

### POST `/v1.0/recmerc/inserir`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Incluir recebimentos de mercadoria

Incluir recebimentos de mercadoria para a unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **IncluirRecPost** = object { unidade, codigoDcto, numero, serie, dataMovimento, categoriaEntidade, codigoEntidade, produtos }

**Respostas:**

- `200` Recebimento incluido — **RespostaPadrao** = object { response }

---

### GET `/v1.0/subcontas/movimentos/release/{release}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar os movimentos de sub contas

Consultar os movimentos de sub contas, filtrando por unidade e/ou código de sub conta

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `release` | path | sim | integer | release do último fornecedor consultado. Envie "0" caso queira consultar todos os fornecedores (mesmo passando 0 os dados retornam paginados). |
| `unidade` | query | não | string | Código da unidade ou cnpj a ser usado como filtro |
| `subConta` | query | não | string | Código da sub conta a ser usado como filtro |
| `limit` | query | não | string | Número de dados retornados na consulta |

**Respostas:**

- `200` Requisição processada com sucesso — **ConsultaMovSubContasV1_0** = object { response }

---

### GET `/v1.0/usuarios/`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter cadastro de usuarios

Obter o cadastro de usuarios do sistema ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Cadastro de usuários retornado — **ConsultarCadUsuariosDeprecatedResponse** = object { response }

---

### GET `/v1.0/usuarios/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do usuario

Obter dados do usuario do sistema ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Codigo do usuario |

**Respostas:**

- `200` Dados do usuário retornado — **ConsultarDadosUsuarioDeprecatedResponse** = object { response }

---

### GET `/v1.0/vdonline/unidade/{cnpj}/pdv/{pdv}/datainicio/{datainicio}/datafim/{datafim}/lastid/{lastid}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Buscar vendas online por PDV

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` | path | sim | string | CNPJ da unidade |
| `pdv` | path | sim | string | codigo do PDV |
| `datainicio` | path | sim | string | Data inicial da venda (Formato "dd-mm-yyyy") |
| `datafim` | path | sim | string | Data final da venda |
| `lastid` | path | sim | string | Código da última venda consultada. Envie "0" caso queira consultar todas as vendas (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados com sucesso — **vdonlineVdPdv** = object { response }

---

### GET `/v1.0/vendedores/{lastID}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar Vendedores

Retorna lista de vendedores

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Na consulta deve-se informar sempre o último ID que foi lido, quando for o inicio da consulta informa-se 0. (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Lista retornada — **RespostaListaDeVendedores** = object { response }

---

### GET `/v1.0/xmlNfe/chave/{chave}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter Xml da NFe

Método para obter o xml da chave informada

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `chave` | path | sim | string | Chave da Xml |

**Respostas:**

- `200` Xml carregado com sucesso — **RespostaXmlChave** = object { response }

---

### GET `/v1.0/xmlNfe/unidade/{cnpj_cpf}/dataEmissao/{dataEmissao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter Xml da NFe

Método para consultar as chaves de notas emitidas na data e unidade informada

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj_cpf` | path | sim | string | CNPJ/CPF da unidade |
| `dataEmissao` | path | sim | string | Data de Emissão da NFe |

**Respostas:**

- `200` Xml da NFe carregado com sucesso — **RespostaXmlDataUnid** = object { response }

---

### GET `/v1.1/agendas/datainicio/{dataInicio}/datafim/{dataFim}/unidade/{cnpj}/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200` Agendas retornadas — **GetAgendasOfertasV1_1** = object { response }

---

### POST `/v1.1/auth`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Autenticar sessão

Autenticar sessão com usuário e senha

**Request body** (application/json, obrigatório: True):

- **AutenticarSessao** = object { usuario, senha }

**Respostas:**

- `200` Sessão autenticada — **RespostaAutenticacao_V_1_1** = object { response }

---

### POST `/v1.1/clientes`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir novo cliente

Inserir novo cliente na base de dados

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **EnviarDadosNovoCliente** = object { nome, sexo, tipo, tipoCliente, fone, celular, foneComercial, uf, cep, cidade, endereco, bairro, numero, complemento, dataNascimento, cpf, rg, orgaoExpRG, ufExpRG, estadoCivil, profissao, escolaridade, email, contaContabil, contaGerencial }

**Respostas:**

- `200` Cliente adicionado — **EnviarDadosNovoClienteResponse** = object { response }

---

### GET `/v1.1/clientes/cnpj_cpf/{CPF_CNPJ}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do cliente

Obter dados do cliente pelo CPF/CNPJ

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF_CNPJ` | path | sim | string | CPF/CNPJ do cliente |

**Respostas:**

- `200` Dados do cliente — **ConsultarDadosClienteResponse** = object { response }

---

### GET `/v1.1/compradores/listar/{lastID}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter lista de compradores cadastrados

Consulta dados referentes aos compradores.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | string | Código do último comprador consultado. Envie "0" caso queira consultar todos os compradores (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados com sucesso — **ListaCompradores** = object { response }

---

### GET `/v1.1/compradores/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter lista de compradores cadastrados

Consulta dados referentes aos compradores.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do comprador a ser consultado. |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaComprador** = object { response }

---

### POST `/v1.1/controleentregas`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Controle de entrega

Gravar controle de entrega

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **ControleEntregaV11** = object { transacao, status, statusOperacional, data, dataVenda, codEntregador, unidade, cliente, bairro, cidade, endereco, complemento, nome, fone, valor, pdv, volumes, cupom, observacao1, observacao2, hora, referencia, numeroCaixas, dataBaixa, enderecoNumero, enderecoCep, veiculo, kmInicio, kmFim, idNfe }

**Respostas:**

- `200` Controle de entrega gravado com sucesso — **ControleEntregaResponseSemMessage** = object { response }

---

### GET `/v1.1/financeiro/funcionario/{CPF}/saldolimitecredito`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

### GET `/v1.1/financeiro/pendenciasFinanceiras/dataInicial/{dataInicial}/dataFinal/{dataFinal}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Pendências financeiras

Pendências financeiras filtrados por data e cnpj da unidade.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `dataInicial` | path | sim | string | Data inicial do período (Formato dd-mm-yyyy) |
| `dataFinal` | path | sim | string | Data final do período (Formato dd-mm-yyyy) |
| `cnpj` | query | sim | string | cnpj da Unidade que deve ser considerada no filtro |

**Respostas:**

- `200` Dados carregados com sucesso — **listaPendenciasFinanceirasFornecedorResponse_V_1_1** = object { response }

---

### GET `/v1.1/fiscal/getnfecupom`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Nota fiscal eletrônica emitida para um determinado cupom fiscal

Buscar nota fiscal eletrônica emitida para um determinado cupom fiscal.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `unidade` | query | sim | string | Unidade do cupom fiscal |
| `cupom` | query | sim | string | Número do cupom fiscal |
| `pdv` | query | sim | string | Código do PDV onde o cupom foi emitido |

**Respostas:**

- `200` Dados carregados com sucesso — **NfeByCupom** = object { response }

---

### POST `/v1.1/flexapp/movpesquisa`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir pesquisa de preços

Inserir pesquisa de preços feita no concorrente

**Request body** (application/json, obrigatório: True):

- **PesquisaDePreco** = object { items }

**Respostas:**

- `200` Dados processados com sucesso — **RespostaPesquisaDePreco** = object { response }

---

### GET `/v1.1/flexapp/movpesquisa`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados de pesquisa de preços

Obter dados de pesquisa preços feitas no concorrente

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `dataInicial` | query | sim | string | dataInicial no padrão dd-mm-yyyy |
| `dataFinal` | query | sim | string | dataFinal no padrão dd-mm-yyyy |
| `unidade` | query | não | string | código interno da unidade |
| `ean` | query | não | string | código de barras (EAN) |

**Respostas:**

- `200` Dados processados com sucesso — **RespostaMovPesquisa** = object { response }

---

### GET `/v1.1/flexapp/prodpesquisa`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Recuperar produtos para pesquisa de preço

Produtos para pesquisa de preço

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaProdPesquisa** = object { response }

---

### GET `/v1.1/formaspagamento`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Cadastro de formas de pagamento

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | query | não | string | codigo da forma de pagamento a ser filtrada |

**Respostas:**

- `200` Dados carregados com sucesso — **listaFormasPagamentoResponse_V_1_1** = object { response }

---

### GET `/v1.1/funcionario/codcpf/{codcpf}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

### GET `/v1.1/funcionario/lastid/{lastid}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar cadastro de funcionários

Consultar cadastro de funcionários por meio de paginação.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastid` | path | sim | string | Código do último funcionário ou 0. |
| `nome` | query | não | string | Nome do funcionário. |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaFuncionarios** = object { response }

---

### POST `/v1.1/industcomp`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Cadastrar produto industrializado

Efetuar o cadastro de produto industrializado, podendo efeturar o cadastro também dos itens de 'receita'

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: False):

- **RequestCadastroProdutosIndustrializados** = object { codigo, descricao, tipo, unidade, rendimento, pesoTotal, precoTotal, dataCusto, comportamento, fase, tempoProducao, observacao, quantidadeMinimaProduzir, quantidadeProduzir, quantidadeMultiplaProduzir, baseProducao, tempoAntecedencia, tempoProducaoHomensHora, prioridadeProducao, tempoPreparo, estoqueSeguranca, baixaEstoqueMateriaPrima, fatorProducao, AgrupamentoUnidadesValidas, departamento, itens }

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaPadrao_SemMessageV2** = object { response }

---

### GET `/v1.1/industcomp/lastId/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar cadastro dos produtos industrializados

Consultar o cadastro dos produtos industrializados

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Código do último produto consultado. Envie "0" caso queira consultar todos os produtos (mesmo passando 0 os dados retornam paginados) |
| `unidade` | query | não | string | CNPJ da unidade do produto a ser consultado. |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaConsultaProdutosIndustrializados** = object { response }

---

### GET `/v1.1/industcomp/{codigo}/unidade/{CNPJ}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar cadastro de produto industrializado

Consultar o cadastro de produto industrializado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do a produto consultado. |
| `CNPJ` | path | sim | string | CNPJ da unidade do produto a ser consultado. |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaConsultaProdutoIndustrializado** = object { response }

---

### PUT `/v1.1/industcomp/{codigo}/unidade/{CNPJ}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Editar um produto industrializado

Efetuar a edição de produto industrializado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do a produto a ser editado. |
| `CNPJ` | path | sim | string | CNPJ da unidade do produto a ser editado. |

**Request body** (application/json, obrigatório: False):

- **Industrializado** = object { codigo, descricao, tipo, unidade, rendimento, pesoTotal, precoTotal, dataCusto, comportamento, fase, tempoProducao, observacao, quantidadeMinimaProduzir, quantidadeProduzir, quantidadeMultiplaProduzir, baseProducao, tempoAntecedencia, tempoProducaoHomensHora, prioridadeProducao, tempoPreparo, estoqueSeguranca, baixaEstoqueMateriaPrima, fatorProducao, AgrupamentoUnidadesValidas, departamento }

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaPadrao_SemMessageV2** = object { response }

---

### DELETE `/v1.1/industcomp/{codigo}/unidade/{CNPJ}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Deletar um produto industrializado

Efetuar a exclusão do cadastro de industrialização

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do produto industrializado a ser deletado. |
| `CNPJ` | path | sim | string | CNPJ da unidade do produto industrializado a ser deletado. |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaPadrao_SemMessageV2** = object { response }

---

### POST `/v1.1/industdecomp`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Cadastrar produto da 'receita' de um industrializado

Cadastrar produto que faz parte da 'receita' de um industrializado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: False):

- **ProdutoDeIndustrializadoCadastro** = object { codigoIndustrializado, codigoItem, unidade, quantComercializacao, quantReceita, pesoItem, precoItem, fase }

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaPadrao_SemMessageV2** = object { response }

---

### DELETE `/v1.1/industdecomp/codigo1/{codigo1}/codigo2/{codigo2}/unidade/{CNPJ}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200` Dados carregados com sucesso — **RespostaPadrao_SemMessageV2** = object { response }

---

### GET `/v1.1/industdecomp/codigo1/{codigo1}/codigo2/{codigo2}/unidade/{CNPJ}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200` Dados carregados com sucesso — **RespostaConsultaProdutoReceitaIndustrializado** = object { response }

---

### GET `/v1.1/industdecomp/{codigo1}/unidade/{CNPJ}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar cadastro dos produtos 'receita' de um produto industrializado

Consultar cadastro dos produtos da 'receita' de um produto industrializado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo1` | path | sim | string | Código do produto industrializado |
| `CNPJ` | path | sim | string | CNPJ da unidade do produto a ser consultado. |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaConsultaTodosProdutosReceitaIndustrializado** = object { response }

---

### PUT `/v1.1/industdecomp/{codigo1}/unidade/{CNPJ}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Editar o cadastro de um produto 'receita'

Editar o cadastro de um produto da 'receita' pertencente a um produto industrializado

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo1` | path | sim | string | Código do produto industrializado a qual o produto a ser editado pertence. |
| `CNPJ` | path | sim | string | CNPJ da unidade do produto a ser editado. |
| `fase` | query | não | string | Fase do produto a ser editado  (Se não informado, o valor padrão para fase será = '0'). |

**Request body** (application/json, obrigatório: False):

- **ProdutoDeIndustrializado** = object { codigoItem, unidade, quantComercializacao, quantReceita, pesoItem, precoItem, fase }

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaPadrao_SemMessageV2** = object { response }

---

### GET `/v1.1/movimentoprodutos/listarmovimentos/lastid/{lastID}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar movimentos de produtos

Listar movimentos de produtos por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `datainicial` | query | sim | string | Data em que inicia-se a leitura dos movimentos, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `tipoconsulta` | query | sim | string | Tipo da consulta, tipos válidos (CODIGO_DCTO, TIPO_DCTO) |
| `valores` | query | sim | string | Valores para filtro, enviar tipos de documento quando informar (tipoconsulta = TIPO_DCTO) e quando enviar (tipoconsulta = CODIGO_DCTO) deve-se enviar os códigos dos documentos que devem ser considerados no filtro |
| `departamentos` | query | não | string | Departamentos a serem considerados no filtro |

**Respostas:**

- `200` Movimentos retornados — **MovProdDResponse** = object { response }

---

### GET `/v1.1/pedidocompra/listarpedidos/lastid/{lastID}/dataInicial/{datainicial}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra

Listar pedidos de compra por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `datainicial` | path | sim | string | Data em que inicia-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponse_V_1_01** = object { response, lastid }

---

### GET `/v1.1/pedidocompra/listarpedidos/pedidossemrcm/lastid/{lastID}/fornecedor/{cnpj}/datainicial/{dataInicial}/datafinal/{dataFinal}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra sem Recebimento

Listar pedidos de compra sem recebimento por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `cnpj` | path | sim | string | Cnpj do fornecedor do pedido |
| `dataInicial` | path | sim | string | Data em que inicia-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `dataFinal` | path | sim | string | Data em que finaliza-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponse_V_1_01** = object { response, lastid }

---

### POST `/v1.1/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **AddPedidoPostDeprecated1** = object { data, codigoCliente, formaPagamento, codigoVendedor, observacao, especie, codigoDocumento, itens }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponse** = object { response }

---

### GET `/v1.1/pedidos/listapedidos/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar pedidos de venda

Consultar todos os pedidos de vendas, podendo ser filtrados por data de Inclusão, status, código de Carregamento, código de Rota e código do Pedido do Cliente.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `loadItens` | query | não | boolean | Se informado com valor 'true', será carregado os itens de cada pedido |
| `status` | query | não | string | Filtra os pedidos pelo status, podendo ser B, P ou A |
| `carregamento` | query | não | string | Código do carregamento a ser filtrado |
| `dataInclusao` | query | não | string | Data a ser comparada com a data de movimento do pedido |
| `rota` | query | não | string | Código da rota a ser filtrada |
| `codPedCliente` | query | não | string | Número do pedido do cliente a ser filtrado |

**Respostas:**

- `200`  — **ListaPedidosComFiltrosResponse** = object { response }

---

### GET `/v1.1/pedidos/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar processamento do pedido de venda

Consultar processamento da inserção do pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido |

**Respostas:**

- `200` Status do pedido — **StatusProcessamentoPedidoResponse** = object { response }

---

### PUT `/v1.1/pedidos/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Editar Pedido de Venda

Editar dados do pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do pedido de venda |

**Request body** (application/json, obrigatório: True):

- **EditarPedido** = object { unidade, data, codigoCliente, formaPagamento, codigoVendedor, observacao, desconto, especie, itens }

**Respostas:**

- `200` Pedido Alterado — **RespostaPadrao** = object { response }

---

### POST `/v1.1/pedidos/{codigo}/financeiro`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Enviar dados pedido de venda

Método para enviar dados financeiros do pedido de venda para ser processado pelo sistema ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido de venda |

**Request body** (application/json, obrigatório: True):

- **EnviarDadosFinanceiroPost_V_1_1** = object { financeiro }

**Respostas:**

- `200` Dados processados com sucesso — **RespostaPadrao** = object { response }

---

### POST `/v1.1/pendest/pendenciaestoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Incluir pendências de estoque

Incluir pendências de estoque no sistema

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **IncluirPendBaixaPost** = object { Inclusoes, Baixas }

**Respostas:**

- `200` Pendência de estoque adicionada — **RespostaPadrao** = object { response }

---

### GET `/v1.1/pendest/que/lastid/{lastID}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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
| `CodigoPendencencia` | query | não | string | Codigo de pendencia |
| `TipoPendencia` | query | não | string | Tipo da pendencia |
| `DataInicial` | query | não | string | Data inicial a se considerar no periodo. (Formato "dd-MM-yyyy") |
| `DataFinal` | query | não | string | Data final a se considerar no periodo.. (Formato "dd-MM-yyyy") |
| `Status` | query | não | string | Status da pendencia, valores possíveis: BAIXADA, PENDENTE |
| `Transacao` | query | não | string | Transação da pendencia |

**Respostas:**

- `200` Dados retornados — **ObterPendResponse** = object { response }

---

### GET `/v1.1/produto/listaprodutos/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar cadastro de um produto

Consultar o cadastro geral de um produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | number | Codigo do ultimo produto que retornou na lista. Para a primeira página de registros enviar esse valor igual a zero. (mesmo passando 0 os dados retornam paginados) |
| `codPreco` | query | não | string | Filtra os produtos por código de preço |

**Respostas:**

- `200` Dados carregados — **ConsultarCadastroProdutosResponse** = object { response }

---

### GET `/v1.1/produto/listaprodutos/{lastId}/detalhado`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar cadastro de um produto

Consultar o cadastro detalhado de um produto

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | number | Codigo do ultimo produto que retornou na lista. Para a primeira página de registros enviar esse valor igual a zero. (mesmo passando 0 os dados retornam paginados) |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |

**Respostas:**

- `200` Dados carregados — **ConsultarCadastroProdutosDetalhadoResponseV2** = object { response }

---

### POST `/v1.1/produtounidade/auditoriaestoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Incluir auditoria de estoque

Incluir auditoria de estoque no sistema

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **IncluirAuditoriaPostV1_1** = object { origem, auditorias }

**Respostas:**

- `200` Auditoria de estoque adicionada — **RespostaPostAuditoriaEstoqueV1_1** = object { response }

---

### GET `/v1.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter cadastro de produtos

Obter cadastro de produtos da unidade, retornará de 100 em 100 registros. Enquanto o código do ultimo produto retornado for menor que o maxCod indica que existem mais produtos a serem consultados.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade que deseja consultar o cadastro |

**Respostas:**

- `200` Dados carregados — **ConsultarAltProdutoResponse** = object { response }

---

### GET `/v1.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/departamento/{departamento}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do produto

Consulta dados de um determinado produto de um departamento

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto que retornou da lista. Para solicitar a primeira página de informações, enviar :lastID igual a zero.  (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `departamento` | path | sim | string | Código do departamento a consultar |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoResponse** = object { response, maxCod }

---

### GET `/v1.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/semcalcularestoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter cadastro de produtos

Obter cadastro de produtos da unidade, retornará de 100 em 100 registros. Enquanto o código do ultimo produto retornado for menor que o maxCod indica que existem mais produtos a serem consultados.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade que deseja consultar o cadastro |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoResponseV1** = object { response }

---

### GET `/v1.1/produtounidade/{lastID}/unidade/{CNPJ}/etiquetaspendentes/{campoConsiderar}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar etiquetas pendentes

Consultar etiquetas pendentes da unidade

O retorno será paginado, com número de itens definido em configuração do serviço.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do produto que retornou da lista. Para solicitar a primeira página de informações, enviar :lastID igual a zero.  (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `campoConsiderar` | path | sim | string | Preço a ser considerado  Possíveis valores: PRECO_PDV, PRECO_VENDA |

**Respostas:**

- `200` Etiquetas pendentes retornadas — **EtiquetasPendentesResponse_V_1_1** = object { response }

---

### GET `/v1.1/usuarios/`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter cadastro de usuarios

Obter o cadastro de usuarios do sistema ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Cadastro de usuários retornado — **ConsultarCadUsuariosResponse** = object { response }

---

### GET `/v1.1/usuarios/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do usuario

Obter dados do usuario do sistema ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Codigo do usuario |

**Respostas:**

- `200` Dados do usuário retornado — **ConsultarDadosUsuarioResponse** = object { response }

---

### GET `/v1.1/usuarios/{codigo}/detalhado`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do usuario detalhado

Obter dados do usuario detalhado do sistema ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Codigo do usuario |

**Respostas:**

- `200` Dados do usuário retornado — **ConsultarDadosUsuarioDetalhadoResponse** = object { response }

---

### GET `/v1.1/usuariosexternos/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do usuario externo

Obter dados do usuario externo do sistema ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Codigo do usuario externo |

**Respostas:**

- `200` Dados do usuário retornado — **ConsultarDadosUsuarioExternoResponse** = object { response }

---

### GET `/v1.1/vdonline/unidade/{cnpj}/pdv/{pdv}/datainicio/{datainicio}/datafim/{datafim}/lastid/{lastid}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Buscar vendas online por PDV

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` | path | sim | string | CNPJ da unidade |
| `pdv` | path | sim | string | codigo do PDV |
| `datainicio` | path | sim | string | Data inicial da venda (Formato "dd-mm-yyyy") |
| `datafim` | path | sim | string | Data final da venda |
| `lastid` | path | sim | string | Código da última venda consultada. Envie "0" caso queira consultar todas as vendas (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados com sucesso — **vdonlineVdPdv_V_1_1** = object { response }

---

### GET `/v1.1/xmlNfe/unidade/{cnpj_cpf}/dataEmissao/{dataEmissao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter Xml da NFe

Método para consultar as chaves de notas emitidas na data e unidade informada

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj_cpf` | path | sim | string | CNPJ/CPF da unidade |
| `dataEmissao` | path | sim | string | Data de Emissão da NFe |

**Respostas:**

- `200` Xml da NFe carregado com sucesso — **RespostaXmlDataUnidV11** = object { response }

---

### GET `/v1.2/cestabasica/listarcestas/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar o cadastro de cestas básicas

Consultar o cadastro de cestas básicas do ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Último código de cesta lido, quando for a primeira leitura informar "0"  (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Cadastro de cestas básicas recuperado — **ConsultarCestasBasicasResponseV2** = object { response }

---

### POST `/v1.2/clientes`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir novo cliente

Inserir novo cliente na base de dados

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **EnviarDadosNovoCliente** = object { nome, sexo, tipo, tipoCliente, fone, celular, foneComercial, uf, cep, cidade, endereco, bairro, numero, complemento, dataNascimento, cpf, rg, orgaoExpRG, ufExpRG, estadoCivil, profissao, escolaridade, email, contaContabil, contaGerencial }

**Respostas:**

- `200` Cliente adicionado — **EnviarDadosNovoClienteResponse** = object { response }

---

### POST `/v1.2/controleentregas`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Controle de entrega

Gravar controle de entrega

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **ControleEntregaV12** = object { transacao, status, statusOperacional, data, dataVenda, codEntregador, unidade, cliente, bairro, cidade, endereco, complemento, nome, fone, valor, pdv, volumes, cupom, observacao1, observacao2, hora, referencia, numeroCaixas, dataBaixa, enderecoNumero, enderecoCep, veiculo, kmInicio, kmFim, idNfe, horaVenda }

**Respostas:**

- `200` Controle de entrega gravado com sucesso — **ControleEntregaResponseSemMessage** = object { response }

---

### GET `/v1.2/financeiro/pendenciasFinanceiras/dataInicial/{dataInicial}/dataFinal/{dataFinal}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Pendências financeiras

Pendências financeiras filtrados por data e cnpj da unidade.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `dataInicial` | path | sim | string | Data inicial do período (Formato dd-mm-yyyy) |
| `dataFinal` | path | sim | string | Data final do período (Formato dd-mm-yyyy) |
| `cnpj` | query | sim | string | cnpj da Unidade que deve ser considerada no filtro |
| `codigo` | query | não | string | Código da entidade que pode ser considerada no filtro |
| `categoria` | query | não | string | Categoria da entidade que pode ser considerada no filtro |

**Respostas:**

- `200` Dados carregados com sucesso — **listaPendenciasFinanceirasFornecedorResponse_V_1_2** = object { response }

---

### GET `/v1.2/financeiro/pendenciasFinanceiras/transacao/{transacao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200` Dados carregados com sucesso — **listaPendenciasFinanceirasFornecedorResponse_V_1_2** = object { response }

---

### POST `/v1.2/flexapp/movpesquisa`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir pesquisa de preços

Inserir pesquisa de preços feita no concorrente

**Request body** (application/json, obrigatório: True):

- **PesquisaDePrecoV_1_2** = object { itens }

**Respostas:**

- `200` Dados processados com sucesso — **RespostaPesquisaDePreco** = object { response }

---

### GET `/v1.2/industcomp/lastId/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200` Dados carregados com sucesso — **RespostaConsultaProdutosIndustrializados_V1_2** = object { response }

---

### GET `/v1.2/industcomp/{codigo}/unidade/{CNPJ}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200` Dados carregados com sucesso — **RespostaConsultaProdutoIndustrializados_V1_2** = object { response }

---

### GET `/v1.2/movimentoprodutos/listarmovimentos/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar movimentos de produtos

Listar movimentos de produtos por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` |  | não |  |  |
| `datainicial` | query | sim | string | Data em que inicia-se a leitura dos movimentos, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `tipoconsulta` | query | sim | string | Tipo da consulta, tipos válidos (CODIGO_DCTO, TIPO_DCTO) |
| `valores` | query | sim | string | Valores para filtro, enviar tipos de documento quando informar (tipoconsulta = TIPO_DCTO) e quando enviar (tipoconsulta = CODIGO_DCTO) deve-se enviar os códigos dos documentos que devem ser considerados no filtro |
| `departamentos` | query | não | string | Departamentos a serem considerados no filtro |

**Respostas:**

- `200`  — **MovProdDResponse_V_1_2** = object { response }

---

### POST `/v1.2/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **AddPedidoPostDeprecated2** = object { data, codigoCliente, formaPagamento, codigoVendedor, observacao, especie, desconto, codigoDocumento, itens }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponse** = object { response }

---

### GET `/v1.2/pedidos/listapedidos/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar pedidos de venda

Consultar todos os pedidos de vendas, podendo ser filtrados por data de Inclusão, status, código de Carregamento, código de Rota e código do Pedido do Cliente.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `loadItens` | query | não | boolean | Se informado com valor 'true', será carregado os itens de cada pedido |
| `status` | query | não | string | Filtra os pedidos pelo status, podendo ser B, P ou A |
| `carregamento` | query | não | string | Código do carregamento a ser filtrado |
| `dataInclusao` | query | não | string | Data a ser comparada com a data de movimento do pedido |
| `rota` | query | não | string | Código da rota a ser filtrada |
| `codPedCliente` | query | não | string | Número do pedido do cliente a ser filtrado |

**Respostas:**

- `200`  — **ListaPedidosComFiltrosResponse** = object { response }

---

### GET `/v1.2/pedidos/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar processamento do pedido de venda

Consultar processamento da inserção do pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido |

**Respostas:**

- `200` Status do pedido — **StatusProcessamentoPedidoResponsev2** = object { response }

---

### PUT `/v1.2/pedidos/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Editar Pedido de Venda

Editar dados do pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do pedido de venda |

**Request body** (application/json, obrigatório: True):

- **EditarPedido** = object { unidade, data, codigoCliente, formaPagamento, codigoVendedor, observacao, desconto, especie, itens }

**Respostas:**

- `200` Pedido Alterado — **RespostaPadrao** = object { response }

---

### GET `/v1.2/pedidos/{codigo}/status`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar status pedido de venda

Consultar o status de um pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido de venda |

**Respostas:**

- `200` Status do pedido retornado — **ConsultarStatusAltPVDResponsev2** = object { response }

---

### POST `/v1.2/pendest/pendenciaestoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Incluir pendências de estoque

Incluir pendências de estoque no sistema

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **IncluirPendBaixaPost** = object { Inclusoes, Baixas }

**Respostas:**

- `200` Pendência de estoque adicionada — **IncluirPendResponse** = object { response }

---

### POST `/v1.2/produtounidade/auditoriaestoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Incluir auditoria de estoque

Incluir auditoria de estoque no sistema

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **IncluirAuditoriaPostV1_2** = object { origem, dataHoraDispositivo, auditorias }

**Respostas:**

- `200` Auditoria de estoque adicionada — **RespostaPostAuditoriaEstoqueV1_1** = object { response }

---

### GET `/v1.2/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/departamento/{departamento}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do produto

Consulta dados de um determinado produto de um departamento

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto que retornou da lista. Para solicitar a primeira página de informações, enviar :lastID igual a zero.  (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `departamento` | path | sim | string | Código do departamento a consultar |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoResponse** = object { response, maxCod }

---

### GET `/v1.2/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/grupo/{grupo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do produto

Consulta dados de um determinado produto de um grupo

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto que retornou da lista. Para solicitar a primeira página de informações, enviar :lastID igual a zero.  (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `grupo` | path | sim | string | Código do grupo a consultar |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoResponse** = object { response, maxCod }

---

### GET `/v1.2/usuariosexternos/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do usuario externo

Obter dados do usuario externo do sistema ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Codigo do usuario externo |

**Respostas:**

- `200` Dados do usuário retornado — **ConsultarDadosUsuarioExternoResponse_V_1_2** = object { response }

---

### GET `/v1.2/vdonline/unidade/{cnpj}/pdv/{pdv}/datainicio/{datainicio}/datafim/{datafim}/lastid/{lastid}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Buscar vendas online por PDV

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` | path | sim | string | CNPJ da unidade |
| `pdv` | path | sim | string | codigo do PDV |
| `datainicio` | path | sim | string | Data inicial da venda (Formato "dd-mm-yyyy") |
| `datafim` | path | sim | string | Data final da venda |
| `lastid` | path | sim | string | Código da última venda consultada. Envie "0" caso queira consultar todas as vendas (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados com sucesso — **vdonlineVdPdv_V_1_2** = object { response }

---

### GET `/v1.3/cestabasica/listarcestas/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar o cadastro de cestas básicas

Consultar o cadastro de cestas básicas do ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Último código de cesta lido, quando for a primeira leitura informar "0"  (mesmo passando 0 os dados retornam paginados) |
| `codigo` | query | não | string | retorna a cesta basica de acordo com o codigo especificado. |

**Respostas:**

- `200` Cadastro de cestas básicas recuperado — **ConsultarCestasBasicasResponseV2** = object { response }

---

### POST `/v1.3/clientes`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir novo cliente

Inserir novo cliente na base de dados

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **ClienteV2** = object { nome, sexo, tipo, tipoCliente, fone, celular, foneComercial, uf, cep, cidade, endereco, bairro, numero, classe, complemento, dataNascimento, cpf, cnpj, rg, ie, orgaoExpRG, ufExpRG, estadoCivil, profissao, escolaridade, email, contaContabil, contaGerencial }

**Respostas:**

- `200` Cliente adicionado — **EnviarDadosNovoClienteResponseV2** = object { response }

---

### GET `/v1.3/clientes/cnpj_cpf/{CPF_CNPJ}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do cliente

Obter dados do cliente pelo CPF/CNPJ

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF_CNPJ` | path | sim | string | CPF/CNPJ do cliente |

**Respostas:**

- `200` Dados do cliente — **ResponseDadosClienteV3** = object { response }

---

### GET `/v1.3/clientes/email/{email}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do cliente

Obter dados do cliente pelo email

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `email` | path | sim | string | Email do cliente |

**Respostas:**

- `200` Dados do cliente — **ResponseDadosClienteV3** = object { response }

---

### GET `/v1.3/clientes/lastid/{lastID}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter cadastro de clientes

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | string | Último id (codigo) retornado |

**Respostas:**

- `200` Dados do cliente — **ResponseCadClientesv3** = object { response }

---

### GET `/v1.3/clientes/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do cliente

Obter dados do cliente pelo código

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do cliente |

**Respostas:**

- `200` Dados do cliente — **ResponseDadosClienteV3** = object { response }

---

### PUT `/v1.3/clientes/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Editar Cliente

Editar dados de determinado cliente

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do cliente |

**Request body** (application/json, obrigatório: True):

- **ClienteV3** = object { Nome, Sexo, Tipo, Fone, Uf, Cep, Classe, Cidade, Endereco, Bairro, Cpf, Rg, Email }

**Respostas:**

- `200` Cliente Alterado — **EnviarDadosNovoClienteResponse** = object { response }

---

### GET `/v1.3/financeiro/pendenciasFinanceiras/dataInicial/{dataInicial}/dataFinal/{dataFinal}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados com sucesso — **listaPendenciasFinanceirasFornecedorResponse_V_1_3** = object { response }

---

### GET `/v1.3/financeiro/pendenciasFinanceiras/transacao/{transacao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200` Dados carregados com sucesso — **listaPendenciasFinanceirasFornecedorResponse_V_1_3** = object { response }

---

### GET `/v1.3/fornecedor/cnpj_cpf/{cnpj_cpf}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Fornecedor filtrado pelo CPF ou CNPJ

Busca de fornecedor, filtrando pelo CPF ou CNPJ

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj_cpf` | path | sim | string | cnpj do fornecedor |

**Respostas:**

- `200` Dados carregados com sucesso — **responseFornecedor_V_1_3** = object { response }

---

### GET `/v1.3/fornecedor/listaFornecedores/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Cadastro dos Fornecedores

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Código do último fornecedor consultado. Envie "0" caso queira consultar todos os fornecedores (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados com sucesso — **ListaFornecTipoV1_3** = object { status, messages, fornecedores }

---

### GET `/v1.3/fornecedor/listaFornecedores/lastid/{lastId}/datahoramanutencao/{datahoramanutencao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Cadastro dos Fornecedores

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Código do último fornecedor consultado. Envie "0" caso queira consultar todos os fornecedores (mesmo passando 0 os dados retornam paginados) |
| `datahoramanutencao` | path | sim | string | Data e hora a ser considerada para o filtro de manutenções realizadas após a data e hora informada formato "dd-MM-yyyy hh:mm:ss" |

**Respostas:**

- `200` Dados carregados com sucesso — **ListaFornecTipoV1_3** = object { status, messages, fornecedores }

---

### GET `/v1.3/fornecedor/listaFornecedores/lastid/{lastId}/tipos/{tipos}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Fornecedores filtrados pelo tipo

Busca de fornecedores, filtrando pelo tipo

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Código do último fornecedor consultado. Envie "0" caso queira consultar todos os fornecedores (mesmo passando 0 os dados retornam paginados) |
| `tipos` | path | sim | string | Tipo do fornecedor |

**Respostas:**

- `200` Dados carregados com sucesso — **ListaFornecTipoV1_3** = object { status, messages, fornecedores }

---

### GET `/v1.3/fornecedor/pedidosbaixados/lastid/{lastId}/unidade/{cnpjUnid}/datainicial/{dataInicial}/datafinal/{dataFinal}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200` Dados caregados — **ListaFornecTipoV1_3** = object { status, messages, fornecedores }

---

### GET `/v1.3/fornecedor/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Fornecedor filtrado pelo código

Busca de fornecedor, filtrando pelo código

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | código interno do fornecedor |

**Respostas:**

- `200` Dados carregados com sucesso — **responseFornecedor_V_1_3** = object { response }

---

### GET `/v1.3/movimentoprodutos/listarmovimentos/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar movimentos de produtos

Listar movimentos de produtos por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` |  | não |  |  |
| `datainicial` | query | sim | string | Data em que inicia-se a leitura dos movimentos, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `tipoconsulta` | query | sim | string | Tipo da consulta, tipos válidos (CODIGO_DCTO, TIPO_DCTO) |
| `valores` | query | sim | string | Valores para filtro, enviar tipos de documento quando informar (tipoconsulta = TIPO_DCTO) e quando enviar (tipoconsulta = CODIGO_DCTO) deve-se enviar os códigos dos documentos que devem ser considerados no filtro |
| `departamentos` | query | não | string | Departamentos a serem considerados no filtro |

**Respostas:**

- `200`  — **MovProdDResponse_V_1_3** = object { response }

---

### POST `/v1.3/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **AddPedidoPost** = object { unidade, data, codigoCliente, formaPagamento, codigoVendedor, observacao, especie, desconto, codigoDocumento, itens }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponse** = object { response }

---

### GET `/v1.3/pedidos/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar processamento do pedido de venda

Consultar processamento da inserção do pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido |

**Respostas:**

- `200` Status do pedido — **StatusProcessamentoPedidoResponsev3** = object { response }

---

### GET `/v1.3/pedidos/{codigo}/status`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar status pedido de venda

Consultar o status de um pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido de venda |

**Respostas:**

- `200` Status do pedido retornado — **ConsultarStatusAltPVDResponseV13** = object { response }

---

### POST `/v1.3/pendest/incluir`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Incluir pendências de estoque

Incluir pendências de estoque no sistema, podendo baixar outras transações

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de Autenticação |

**Request body** (application/json, obrigatório: True):

- **V_1_3_pendest_incluir** = object { Inclusoes, Baixas }

**Respostas:**

- `200` Iniciado processamento das pendências de estoque. Retorna um recibo para verificar o status desse processamento. — { response: object { status, messages, content } }

---

### POST `/v1.3/pendest/pendenciaestoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Incluir pendências de estoque

Incluir pendências de estoque no sistema

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **V_1_3_pendest_incluir** = object { Inclusoes, Baixas }

**Respostas:**

- `200` Pendência de estoque adicionada — **IncluirPendResponse_V_1_3** = object { response }

---

### GET `/v1.3/vdonline/unidade/{cnpj}/pdv/{pdv}/datainicio/{datainicio}/datafim/{datafim}/lastid/{lastid}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Buscar vendas online por PDV

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` | path | sim | string | CNPJ da unidade |
| `pdv` | path | sim | string | codigo do PDV |
| `datainicio` | path | sim | string | Data inicial da venda (Formato "dd-mm-yyyy") |
| `datafim` | path | sim | string | Data final da venda |
| `lastid` | path | sim | string | Código da última venda consultada. Envie "0" caso queira consultar todas as vendas (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados com sucesso — **vdonlineVdPdv_V_1_3** = object { response }

---

### POST `/v1.4/clientes`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir novo cliente

Inserir novo cliente na base de dados

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **ClienteV4** = object { nome, sexo, tipo, tipoCliente, fone, celular, foneComercial, uf, cep, cidade, endereco, bairro, numero, classe, complemento, dataNascimento, cpf, cnpj, rg, ie, orgaoExpRG, ufExpRG, estadoCivil, profissao, escolaridade, email, contaContabil, contaGerencial, contribuinte }

**Respostas:**

- `200` Cliente adicionado — **EnviarDadosNovoClienteResponseV2** = object { response }

---

### GET `/v1.4/clientes/cnpj_cpf/{CPF_CNPJ}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do cliente

Obter dados do cliente pelo CPF/CNPJ

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF_CNPJ` | path | sim | string | CPF/CNPJ do cliente |

**Respostas:**

- `200` Dados do cliente — **ResponseDadosClienteV4** = object { response }

---

### GET `/v1.4/clientes/email/{email}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do cliente

Obter dados do cliente pelo email

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `email` | path | sim | string | Email do cliente |

**Respostas:**

- `200` Dados do cliente — **ResponseDadosClienteV4** = object { response }

---

### GET `/v1.4/clientes/lastid/{lastID}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter cadastro de clientes

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | string | Último id (codigo) retornado |

**Respostas:**

- `200` Dados do cliente — **ResponseCadClientesv4** = object { response }

---

### GET `/v1.4/clientes/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do cliente

Obter dados do cliente pelo código

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do cliente |

**Respostas:**

- `200` Dados do cliente — **ResponseDadosClienteV4** = object { response }

---

### PUT `/v1.4/clientes/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Editar Cliente

Editar dados de determinado cliente

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do cliente |

**Request body** (application/json, obrigatório: True):

- **ClienteV4** = object { nome, sexo, tipo, tipoCliente, fone, celular, foneComercial, uf, cep, cidade, endereco, bairro, numero, classe, complemento, dataNascimento, cpf, cnpj, rg, ie, orgaoExpRG, ufExpRG, estadoCivil, profissao, escolaridade, email, contaContabil, contaGerencial, contribuinte }

**Respostas:**

- `200` Cliente Alterado — **EnviarDadosNovoClienteResponse** = object { response }

---

### GET `/v1.4/financeiro/pendenciasFinanceiras/dataInicial/{dataInicial}/dataFinal/{dataFinal}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200` Dados carregados com sucesso — **listaPendenciasFinanceirasFornecedorResponse_V_1_4** = object { response }

---

### GET `/v1.4/financeiro/pendenciasFinanceiras/transacao/{transacao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200` Dados carregados com sucesso — **listaPendenciasFinanceirasFornecedorResponse_V_1_4** = object { response }

---

### GET `/v1.4/fornecedor/cnpj_cpf/{cnpj_cpf}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Fornecedor filtrado pelo CPF ou CNPJ

Busca de fornecedor, filtrando pelo CPF ou CNPJ

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj_cpf` | path | sim | string | cnpj do fornecedor |

**Respostas:**

- `200` Dados carregados com sucesso — **responseFornecedor_V_1_4** = object { response }

---

### GET `/v1.4/fornecedor/listaFornecedores/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Cadastro dos Fornecedores

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` | path | sim | string | Código do último fornecedor consultado. Envie "0" caso queira consultar todos os fornecedores (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados com sucesso — **ListaFornecTipoV1_4** = object { status, messages, fornecedores }

---

### GET `/v1.4/fornecedor/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Fornecedor filtrado pelo código

Busca de fornecedor, filtrando pelo código

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | código interno do fornecedor |

**Respostas:**

- `200` Dados carregados com sucesso — **responseFornecedor_V_1_4** = object { response }

---

### GET `/v1.4/movimentoprodutos/listarmovimentos/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar movimentos de produtos

Listar movimentos de produtos por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` |  | não |  |  |
| `datainicial` | query | sim | string | Data em que inicia-se a leitura dos movimentos, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `tipoconsulta` | query | sim | string | Tipo da consulta, tipos válidos (CODIGO_DCTO, TIPO_DCTO) |
| `valores` | query | sim | string | Valores para filtro devem ser enviados com ; (ponto e virgula) como separador, enviar tipos de documento quando informar (tipoconsulta = TIPO_DCTO) e quando enviar (tipoconsulta = CODIGO_DCTO) deve-se enviar os códigos dos documentos que devem ser considerados no filtro |
| `departamentos` | query | não | string | Departamentos a serem considerados no filtro |
| `produto` | query | não | number | Código do produto a ser considerado no filtro |
| `unidade` | query | não | number | Unidade/Loja que deseja considerar no filtro |

**Respostas:**

- `200`  — **MovProdDResponse_V_1_4** = object { response }

---

### GET `/v1.4/pedidocompra/listarpedidos/lastid/{lastID}/dataInicial/{datainicial}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra

Listar pedidos de compra por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `datainicial` | path | sim | string | Data em que inicia-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseLV14** = object { response, lastid }

---

### GET `/v1.4/pedidocompra/listarpedidos/pedidossemrcm/lastid/{lastID}/fornecedor/{cnpj}/datainicial/{dataInicial}/datafinal/{dataFinal}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra sem Recebimento

Listar pedidos de compra sem recebimento por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `cnpj` | path | sim | string | Cnpj do fornecedor do pedido |
| `dataInicial` | path | sim | string | Data em que inicia-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `dataFinal` | path | sim | string | Data em que finaliza-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseLV14** = object { response, lastid }

---

### GET `/v1.4/pedidocompra/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra

Listar pedidos de compra por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido de compra |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseV14** = object { response }

---

### POST `/v1.4/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV3** = object { unidade, data, codigoCliente, formaPagamento, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, itens }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponse** = object { response }

---

### GET `/v1.4/pedidos/listar/status/datamodificacao/{datahora}/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar status pedido de venda

Consultar o status de um pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `datahora` | path | sim | string | Data e hora da modificação do status do pedido. A data e hora deve estar no formato "dd-MM-yyyy hh:mm:ss" |
| `lastId` | path | sim | string | Código do último pedido de venda consultado. Envie "0" caso queira consultar todos os fornecedores (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Status do pedido retornado — **ConsultarDataModPedidoV14** = object { response }

---

### PUT `/v1.4/pedidos/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Editar Pedido de Venda

Editar dados do pedido de venda.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do pedido de venda |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV2** = object { unidade, data, codigoCliente, formaPagamento, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, email, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, itens }

**Respostas:**

- `200` Pedido Alterado — **RespostaPadrao** = object { response }

---

### POST `/v1.4/pendest/incluir`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Incluir pendências de estoque

Incluir pendências de estoque no sistema, podendo baixar outras transações

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de Autenticação |

**Request body** (application/json, obrigatório: True):

- **V_1_4_pendest_incluir** = object { Inclusoes }

**Respostas:**

- `200` Iniciado processamento das pendências de estoque. Retorna um recibo para verificar o status desse processamento. — { response: object { status, messages, content } }

---

### GET `/v1.4/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter cadastro de produtos

Obter cadastro de produtos da unidade, retornará de 100 em 100 registros. Enquanto o código do ultimo produto retornado for menor que o maxCod indica que existem mais produtos a serem consultados.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade que deseja consultar o cadastro |

**Respostas:**

- `200` Dados carregados — **ConsultarAltProdutoResponse4** = object { response }

---

### GET `/v1.4/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/grupo/{grupo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do produto

Consulta dados de um determinado produto de um grupo

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto que retornou da lista. Para solicitar a primeira página de informações, enviar :lastID igual a zero.  (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `grupo` | path | sim | string | Código do grupo a consultar |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoResponseNovo** = object { response, maxCod }

---

### GET `/v1.4/unidades`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar Unidades

Listar as unidades da empresa

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Lista de unidades — **ListarUnidadesResponseV_1_4** = object { response }

---

### GET `/v1.4/unidades/{CNPJ}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar unidade

Listar dados da unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CNPJ` | path | sim | string | CNPJ da unidade |

**Respostas:**

- `200` Dados da unidade — **UnidadeResponseV_1_4** = object { response }

---

### GET `/v1.4/vdonline/unidade/{cnpj}/pdv/{pdv}/datainicio/{datainicio}/datafim/{datafim}/lastid/{lastid}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Buscar vendas online por PDV

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` | path | sim | string | CNPJ da unidade |
| `pdv` | path | sim | string | codigo do PDV |
| `datainicio` | path | sim | string | Data inicial da venda (Formato "dd-mm-yyyy") |
| `datafim` | path | sim | string | Data final da venda |
| `lastid` | path | sim | string | Código da última venda consultada. Envie "0" caso queira consultar todas as vendas (mesmo passando 0 os dados retornam paginados) |
| `cnpjCpf` | query | não | string | Cnpj ou Cpf do cliente do cupom de venda |
| `cnpjCpfCrm` | query | não | string | Cnpj ou Cpf do cliente do CRM de venda |

**Respostas:**

- `200` Dados carregados com sucesso — **vdonlineVdPdv_V_1_4** = object { response }

---

### POST `/v1.5/clientes`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir novo cliente

Inserir novo cliente na base de dados

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **ClienteV5** = object { nome, sexo, tipo, tipoCliente, fone, celular, foneComercial, classe, enderecoResidencial, enderecoComercial, dataNascimento, cpf, cnpj, rg, ie, orgaoExpRG, ufExpRG, estadoCivil, profissao, escolaridade, email, contaContabil, contaGerencial, contribuinte }

**Respostas:**

- `200` Cliente adicionado — **EnviarDadosNovoClienteResponseV2** = object { response }

---

### GET `/v1.5/clientes/cnpj_cpf/{CPF_CNPJ}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do cliente

Obter dados do cliente pelo CPF/CNPJ

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CPF_CNPJ` | path | sim | string | CPF/CNPJ do cliente |
| `outrosextras` | query | não | boolean | True para processar os Campos Extras do cliente e retornar o atributo 'camposExtras' |

**Respostas:**

- `200` Dados do cliente — **ResponseDadosClienteV5** = object { response }

---

### PUT `/v1.5/clientes/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Editar Cliente

Editar dados de determinado cliente

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do cliente |

**Request body** (application/json, obrigatório: True):

- **ClienteV5** = object { nome, sexo, tipo, tipoCliente, fone, celular, foneComercial, classe, enderecoResidencial, enderecoComercial, dataNascimento, cpf, cnpj, rg, ie, orgaoExpRG, ufExpRG, estadoCivil, profissao, escolaridade, email, contaContabil, contaGerencial, contribuinte }

**Respostas:**

- `200` Cliente Alterado — **EnviarDadosNovoClienteResponse** = object { response }

---

### GET `/v1.5/financeiro/pendenciasFinanceiras/transacao/{transacao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200` Dados carregados com sucesso — **listaPendenciasFinanceirasFornecedorResponse_V_1_5** = object { response }

---

### GET `/v1.5/movimentoprodutos/listarmovimentos/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar movimentos de produtos

Listar movimentos de produtos por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` |  | não |  |  |
| `datainicial` | query | sim | string | Data em que inicia-se a leitura dos movimentos, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `datafinal` | query | sim | string | Data em que finaliza-se a leitura dos movimentos (Formato "dd-mm-yyyy") |
| `tipoconsulta` | query | sim | string | Tipo da consulta, tipos válidos (CODIGO_DCTO, TIPO_DCTO) |
| `valores` | query | sim | string | Valores para filtro devem ser enviados com ; (ponto e virgula) como separador, enviar tipos de documento quando informar (tipoconsulta = TIPO_DCTO) e quando enviar (tipoconsulta = CODIGO_DCTO) deve-se enviar os códigos dos documentos que devem ser considerados no filtro |
| `departamentos` | query | não | string | Departamentos a serem considerados no filtro |
| `produto` | query | não | number | Código do produto a ser considerado no filtro |
| `unidade` | query | não | number | Unidade/Loja que deseja considerar no filtro |

**Respostas:**

- `200`  — **MovProdDResponse_V_1_5** = object { response }

---

### GET `/v1.5/pedidocompra/listarpedidos/lastid/{lastID}/dataInicial/{datainicial}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra

Listar pedidos de compra por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `datainicial` | path | sim | string | Data em que inicia-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `status` | query | sim | string | Informar um dos seguintes valores, "P" para Pendentes, "B" para Baixados ou "C" para Cancelados |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseLV14** = object { response, lastid }

---

### GET `/v1.5/pedidocompra/listarpedidos/pedidossemrcm/lastid/{lastID}/fornecedor/{cnpj}/datainicial/{dataInicial}/datafinal/{dataFinal}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra sem Recebimento

Listar pedidos de compra sem recebimento por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `cnpj` | path | sim | string | Cnpj do fornecedor do pedido |
| `dataInicial` | path | sim | string | Data em que inicia-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `dataFinal` | path | sim | string | Data em que finaliza-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseLV15** = object { response, lastid }

---

### GET `/v1.5/pedidocompra/listarpedidos/pedidossemrcm/lastid/{lastID}/fornecedor/{cnpj}/datainicial/{dataInicial}/datafinal/{dataFinal}/vinc/{vinc}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra sem Recebimento

Listar pedidos de compra sem recebimento por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `cnpj` | path | sim | string | Cnpj do fornecedor do pedido |
| `dataInicial` | path | sim | string | Data em que inicia-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `dataFinal` | path | sim | string | Data em que finaliza-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `vinc` | path | sim | string | Indicar se a rota deve buscar os pedidos dos fornecedores vinculados (deve-se utilizar valores SIM ou NAO) |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseLV15** = object { response, lastid }

---

### POST `/v1.5/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV4** = object { unidade, data, codigoCliente, formaPagamento, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, email, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, turnoEntrega, dataPrevista, valorFrete, itens }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponse** = object { response }

---

### GET `/v1.5/pedidos/listar/status/datamodificacao/{datahora}/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar status pedido de venda

Consultar o status de um pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `datahora` | path | sim | string | Data e hora da modificação do status do pedido. A data e hora deve estar no formato "dd-MM-yyyy hh:mm:ss" |
| `lastId` | path | sim | string | Código do último pedido de venda consultado. Envie "0" caso queira consultar todos os fornecedores (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Status do pedido retornado — **ConsultarStatusDataModPedidoV15** = object { response }

---

### PUT `/v1.5/pedidos/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Editar Pedido de Venda

Editar dados do pedido de venda.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do pedido de venda |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV4** = object { unidade, data, codigoCliente, formaPagamento, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, email, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, turnoEntrega, dataPrevista, valorFrete, itens }

**Respostas:**

- `200` Pedido Alterado — **RespostaPadrao** = object { response }

---

### GET `/v1.5/pedidos/{codigo}/status`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar status pedido de venda

Consultar o status de um pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido de venda |

**Respostas:**

- `200` Status do pedido retornado — **ConsultarStatusAltPVDResponseV15** = object { response }

---

### POST `/v1.5/pendest/incluir`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Incluir pendências de estoque

Observação: a Grade de unidades com quantidades (`unidades`) dentro das pendências é exigida apenas quando o comportamento "QU" estiver habilitado no documento PES.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de Autenticação |

**Request body** (application/json, obrigatório: True):

- **V_1_5_pendest_incluir** = object { Inclusoes, Baixas }

**Respostas:**

- `200` Iniciado processamento das pendências de estoque. Retorna um recibo para verificar o status desse processamento. — { status: string(string) ex: "ok"; messages: `messages` (ver reference/schemas.md); content: number ex: 124 }

---

### GET `/v1.5/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter cadastro de produtos

Obter cadastro de produtos da unidade, retornará de 100 em 100 registros. Enquanto o código do ultimo produto retornado for menor que o maxCod indica que existem mais produtos a serem consultados.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade que deseja consultar o cadastro |

**Respostas:**

- `200` Dados carregados — **ConsultarAltProdutoResponse5** = object { response }

---

### GET `/v1.5/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/departamento/{departamento}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do produto

Consulta dados de um determinado produto de um departamento

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto que retornou da lista. Para solicitar a primeira página de informações, enviar :lastID igual a zero.  (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `departamento` | path | sim | string | Código do departamento a consultar |

**Respostas:**

- `200` Dados carregados — **ConsultarEstProdutoResponse5** = object { response }

---

### GET `/v1.5/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/grupo/{grupo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do produto

Consulta dados de um determinado produto de um grupo

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto que retornou da lista. Para solicitar a primeira página de informações, enviar :lastID igual a zero.  (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `grupo` | path | sim | string | Código do grupo a consultar |

**Respostas:**

- `200` Dados carregados — **ConsultarEstProdutoResponse5** = object { response }

---

### GET `/v1.5/unidades`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar Unidades

Listar as unidades da empresa

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` | query | não | string | cnpj da unidade a ser filtrada |
| `codigo` | query | não | string | código da unidade a ser filtrada |

**Respostas:**

- `200` Lista de unidades — **ListarUnidadesResponseV_1_5** = object { response }

---

### GET `/v1.5/unidades/{CNPJ}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar unidade

Listar dados da unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CNPJ` | path | sim | string | CNPJ da unidade |

**Respostas:**

- `200` Dados da unidade — **UnidadeResponseV_1_5** = object { response }

---

### GET `/v1.5/vdonline/unidade/{cnpj}/pdv/{pdv}/datainicio/{datainicio}/datafim/{datafim}/lastid/{lastid}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Buscar vendas online por PDV

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` | path | sim | string | CNPJ da unidade |
| `pdv` | path | sim | string | codigo do PDV |
| `datainicio` | path | sim | string | Data inicial da venda (Formato "dd-mm-yyyy") |
| `datafim` | path | sim | string | Data final da venda |
| `lastid` | path | sim | string | Valor do campo 'codgio' da última venda retornada. Envie "0" caso queira consultar todas as vendas (mesmo passando 0 os dados retornam paginados) |
| `cnpjCpf` | query | não | string | Cnpj ou Cpf do cliente do cupom de venda |
| `cnpjCpfCrm` | query | não | string | Cnpj ou Cpf do cliente do CRM de venda |

**Respostas:**

- `200` Dados carregados com sucesso — **vdonlineVdPdv_V_1_5** = object { response }

---

### POST `/v1.6/clientes`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir novo cliente

Inserir novo cliente na base de dados

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **ClienteV6** = object { nome, sexo, tipo, tipoCliente, fone, celular, foneComercial, classe, enderecoResidencial, enderecoComercial, dataNascimento, cpf, cnpj, rg, ie, orgaoExpRG, ufExpRG, estadoCivil, profissao, escolaridade, email, contaContabil, contaGerencial, contribuinte, unidadeCadastro }

**Respostas:**

- `200` Cliente adicionado — **EnviarDadosNovoClienteResponseV2** = object { response }

---

### GET `/v1.6/clientes/lastid/{lastID}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter cadastro de clientes

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | string | Último id (codigo) retornado |

**Respostas:**

- `200` Dados do cliente — **ResponseCadClientes_v1.6** = object { response }

---

### GET `/v1.6/clientes/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do cliente

Obter dados do cliente pelo código

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do cliente |

**Respostas:**

- `200` Dados do cliente — **ResponseCadClientes_v1.6** = object { response }

---

### GET `/v1.6/movimentoprodutos/listarmovimentos/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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
| `unidade` | query | não | string | Unidade/Loja que deseja considerar no filtro |
| `transacao` | query | não | string | Número da transação a ser considerada no filtro. Obrigatório caso a dataInicial não seja informada |

**Respostas:**

- `200`  — **MovProdDResponse_V_1_5** = object { response }

---

### POST `/v1.6/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV5** = object { unidade, data, codigoCliente, formaPagamento, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, email, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, turnoEntrega, dataPrevista, valorFrete, camposExtras, itens }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponse** = object { response }

---

### GET `/v1.6/pedidos/status`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar status pedido de venda

Consultar o status de um pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `pdv` | query | sim | string | Código do pdv |
| `cupom` | query | sim | string | Cupom |
| `unidade` | query | sim | string | Código da unidade |
| `data` | query | sim | string | Data de movimento formato (dd-MM-yyyy) |

**Respostas:**

- `200` Status do pedido retornado — **ConsultarStatusAltPVDResponseV16** = object { response }

---

### GET `/v1.6/pedidos/{codigo}/status`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Consultar status pedido de venda

Consultar o status de um pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido de venda |

**Respostas:**

- `200` Status do pedido retornado — **ConsultarStatusAltPVDResponseV16** = object { response }

---

### POST `/v1.7/clientes`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir novo cliente

Inserir novo cliente na base de dados

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **ClienteV7** = object { nome, sexo, tipo, tipoCliente, fone, celular, foneComercial, classe, enderecoResidencial, enderecoComercial, dataNascimento, cpf, cnpj, rg, ie, orgaoExpRG, ufExpRG, estadoCivil, profissao, escolaridade, email, contaContabil, contaGerencial, contribuinte, unidadeCadastro, observacao, vendedor }

**Respostas:**

- `200` Cliente adicionado — **EnviarDadosNovoClienteResponseV2** = object { response }

---

### GET `/v1.7/clientes/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter cadastro de clientes

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` |  | não |  |  |
| `dtHrManut` | query | não | string | Data e hora de modificação do cadastro dos clientes a ser considerada. Formato 'YYYY-MM-DD hh:mm:ss' |
| `nome` | query | não | string | Nome do cliente. |
| `razaoSocial` | query | não | string | Razão social do cliente. |
| `outrosextras` |  | não |  |  |

**Respostas:**

- `200` Dados do cliente — **ResponseCadClientes_v1.7** = object { response }

---

### GET `/v1.7/movimentoprodutos/listarmovimentos/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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
| `unidade` | query | não | string | Unidade/Loja que deseja considerar no filtro |
| `transacao` | query | não | string | Número da transação a ser considerada no filtro. Obrigatório caso a dataInicial não seja informada |

**Respostas:**

- `200`  — **MovProdDResponse_V_1_7** = object { response }

---

### GET `/v1.7/pedidocompra/listarpedidos/lastid/{lastID}/dataInicial/{datainicial}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra

Listar pedidos de compra por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `datainicial` | path | sim | string | Data em que inicia-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `status` | query | sim | string | Informar um dos seguintes valores, "P" para Pendentes, "B" para Baixados ou "C" para Cancelados |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseLV17** = object { response, lastid }

---

### GET `/v1.7/pedidocompra/listarpedidos/pedidossemrcm/lastid/{lastID}/fornecedor/{cnpj}/unidade/{cnpjUnid}/datainicial/{dataInicial}/datafinal/{dataFinal}/vinc/{vinc}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra sem Recebimento

Listar pedidos de compra sem recebimento por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `cnpj` | path | sim | string | Cnpj do fornecedor do pedido |
| `cnpjUnid` | path | sim | string | Cnpj da unidade do pedido |
| `dataInicial` | path | sim | string | Data em que inicia-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `dataFinal` | path | sim | string | Data em que finaliza-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `vinc` | path | sim | string | Indicar se a rota deve buscar os pedidos dos fornecedores vinculados (deve-se utilizar valores SIM ou NAO) |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseLV17** = object { response, lastid }

---

### POST `/v1.7/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV7** = object { unidade, data, codigoCliente, formaPagamento, numeroPedidoCliente, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, email, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, turnoEntrega, dataPrevista, valorFrete, camposExtras, itens }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponse** = object { response }

---

### POST `/v1.8/clientes`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir novo cliente

Inserir novo cliente na base de dados

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **Cliente_v1_8** = object { nome, sexo, tipo, tipoCliente, fone, celular, foneComercial, classe, enderecoResidencial, enderecoComercial, dataNascimento, cpf, cnpj, rg, ie, orgaoExpRG, ufExpRG, estadoCivil, profissao, escolaridade, email, contaContabil, contaGerencial, contribuinte, unidadeCadastro, observacao, vendedor, ramoAtividade }

**Respostas:**

- `200` Cliente adicionado — **EnviarDadosNovoClienteResponseV2** = object { response }

---

### GET `/v1.8/clientes/lastid/{lastId}`

**Resumo:** Obter cadastro de clientes

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` |  | não |  |  |
| `dtHrManut` | query | não | string | Data e hora de modificação do cadastro dos clientes a ser considerada. Formato 'YYYY-MM-DD hh:mm:ss' |
| `nome` | query | não | string | Nome do cliente. |
| `razaoSocial` | query | não | string | Razão social do cliente. |
| `outrosextras` |  | não |  |  |

**Respostas:**

- `200` Dados do cliente — **ResponseCadClientes_v1.8** = object { response }

---

### GET `/v1.8/movimentoprodutos/listarmovimentos/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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
| `unidade` | query | não | string | Unidade/Loja que deseja considerar no filtro |
| `transacao` | query | não | string | Número da transação a ser considerada no filtro. Obrigatório caso a dataInicial não seja informadaz |

**Respostas:**

- `200`  — **MovProdDResponse_V_1_8** = object { response }

---

### GET `/v1.8/pedidocompra/listarpedidos/lastid/{lastID}/dataInicial/{datainicial}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra

Listar pedidos de compra por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `datainicial` | path | sim | string | Data em que inicia-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `status` | query | sim | string | Informar um dos seguintes valores, "P" para Pendentes, "B" para Baixados ou "C" para Cancelados |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseLV18** = object { response, lastid }

---

### GET `/v1.8/pedidocompra/listarpedidos/pedidossemrcm/lastid/{lastID}/fornecedor/{cnpj}/unidade/{cnpjUnid}/datainicial/{dataInicial}/datafinal/{dataFinal}/vinc/{vinc}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra sem Recebimento

Listar pedidos de compra sem recebimento por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `cnpj` | path | sim | string | Cnpj do fornecedor do pedido |
| `cnpjUnid` | path | sim | string | Cnpj da unidade do pedido |
| `dataInicial` | path | sim | string | Data em que inicia-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `dataFinal` | path | sim | string | Data em que finaliza-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `vinc` | path | sim | string | Indicar se a rota deve buscar os pedidos dos fornecedores vinculados (deve-se utilizar valores SIM ou NAO) |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseLV18** = object { response, lastid }

---

### GET `/v1.8/pedidocompra/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra

Listar pedidos de compra por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido de compra |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseV18** = object { response }

---

### POST `/v1.8/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV18** = object { unidade, data, codigoCliente, formaPagamento, numeroPedidoCliente, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, email, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, turnoEntrega, dataPrevista, valorFrete, despesaAcessoria, camposExtras, itens }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponse** = object { response }

---

### POST `/v1.9/clientes`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir novo cliente

Inserir novo cliente na base de dados

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **Cliente_v1_9** = object { nome, sexo, tipo, tipoCliente, fone, celular, foneComercial, classe, enderecoResidencial, enderecoComercial, dataNascimento, cpf, cnpj, rg, ie, orgaoExpRG, ufExpRG, estadoCivil, profissao, escolaridade, email, contaContabil, contaGerencial, contribuinte, unidadeCadastro, observacao, vendedor, ramoAtividade, caracTrib }

**Respostas:**

- `200` Cliente adicionado — **EnviarDadosNovoClienteResponseV2** = object { response }

---

### GET `/v1.9/clientes/{codigo}`

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

### GET `/v1.9/movimentoprodutos/listarmovimentos/lastid/{lastId}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200`  — **MovimentosMovProdD_V_1_9** = array de object { id, chavePrimaria, transacao, operacao, tipoMovimento, tipo, status, chaveNfe, data, codigoEntidade, categoriaEntidade, unidade, numero, serie, codBenef, codEstoque, fatorEstoque, codigoProduto, sequencial, quantidadeUnitaria, quantidadeEmbalagem, embCom, embTrib, subTribEnt, ipiDevol, valorBcBruto, valor, icms, icmsSimplesFed, icmsCritica, valorIcmsInf, valorIcms, valorFCP, aliqFCP, cstIPI, percReducaoBC, percentualIPI, percentualDesconto, outrosAcrescimos, valorSubTrib, bcSubTribInf, alSubTribinf, despesasAdicionais, percentualISS, simbologiaICMS, valorPIS, valorCofins, bcPisCofins, aliqPis, aliqCofins, cstPis, cstCofins, cfop, cst, bcIpi, percReducaoBcSt, valorUnitario, ctCompra, ctMedio, ctTransf, ctEmpresa, ctFiscal, prCompra, tipoDcto, dataEmissao, qtdeTrib, qtdeCom, comissaoValor, comissaoBase, comissaoPerc, nextra, cextra, xml }

---

### GET `/v1.9/pedidocompra/listarpedidos/lastid/{lastID}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra

Listar pedidos de compra por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `dataInicial` | query | não | string | Data em que inicia-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `dataFinal` | query | não | string | Data em que encerra-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `dataInicialBaixa` | query | não | string | Data em que inicia-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `dataFinalBaixa` | query | não | string | Data em que encerra-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `unidade` | query | não | string | Código da unidade de destino do pedido de compra |
| `status` | query | sim | string | Informar um dos seguintes valores, "P" para Pendentes, "B" para Baixados ou "C" para Cancelados |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseLV19** = object { response }

---

### POST `/v1.9/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV19** = object { unidade, data, codigoCliente, formaPagamento, numeroPedidoCliente, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, email, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, turnoEntrega, dataPrevista, valorFrete, despesaAcessoria, camposExtras, itens }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponse** = object { response }

---

### POST `/v1.9/pedidos/{codigo}/item`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir novo item ao pedido

Inserir um novo item ao pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do pedido de venda |

**Request body** (application/json, obrigatório: True):

- **ItemPedidoV19** = object { codigoProduto, qtdUnitaria, qtdEmbalagem, valorProduto, percDesconto, valorProdFlex }

**Respostas:**

- `200` Item adicionado — **RespostaPadrao** = object { response }

---

### PUT `/v1.9/pedidos/{codigo}/item/{codigoItem}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Editar Item do Pedido

Editar item do pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do pedido de venda |
| `codigoItem` | path | sim | number | Código do produto |

**Request body** (application/json, obrigatório: True):

- **ItemPedidoV19** = object { codigoProduto, qtdUnitaria, qtdEmbalagem, valorProduto, percDesconto, valorProdFlex }

**Respostas:**

- `200` Item alterado com sucesso — **RespostaPadrao** = object { response }

---

### DELETE `/v1.9/pedidos/{codigo}/item/{codigoItem}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Excluir item do Pedido

Exclui determinado item do pedido de venda.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do pedido de venda |
| `codigoItem` | path | sim | number | Código do produto |

**Respostas:**

- `200` Item excluído com sucesso — **RespostaPadrao** = object { response }

---

### GET `/v1.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/departamento/{departamento}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do produto

Consulta dados de um determinado produto de um departamento

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto que retornou da lista. Para solicitar a primeira página de informações, enviar :lastID igual a zero.  (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `departamento` | path | sim | string | Código do departamento a consultar |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoV19** = object { response }

---

### GET `/v1.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/grupo/{grupo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados do produto

Consulta dados de um determinado produto de um grupo

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto que retornou da lista. Para solicitar a primeira página de informações, enviar :lastID igual a zero. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `grupo` | path | sim | string | Código do grupo a consultar |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoV19** = object { response }

---

### GET `/v2.0/pedidocompra/listarpedidos/lastid/{lastID}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra

Listar pedidos de compra por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `dataInicial` | query | não | string | Data em que inicia-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `dataFinal` | query | não | string | Data em que encerra-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `dataInicialBaixa` | query | não | string | Data em que inicia-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `dataFinalBaixa` | query | não | string | Data em que encerra-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `unidade` | query | não | string | Código da unidade de destino do pedido de compra |
| `status` | query | sim | string | Informar um dos seguintes valores, "P" para Pendentes, "B" para Baixados ou "C" para Cancelados |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseLV20** = object { response }

---

### POST `/v2.0/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV20** = object { unidade, data, codigoCliente, formaPagamento, numeroPedidoCliente, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, email, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, turnoEntrega, dataPrevista, valorFrete, despesaAcessoria, transportador, camposExtras, itens }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponseSemMessage** = object { response }

---

### POST `/v2.0/pedidos/{codigo}/item`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir novo item ao pedido

Inserir um novo item ao pedido de venda

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do pedido de venda |

**Request body** (application/json, obrigatório: True):

- **ItemPedidoV19** = object { codigoProduto, qtdUnitaria, qtdEmbalagem, valorProduto, percDesconto, valorProdFlex }

**Respostas:**

- `200` Item adicionado — **RespostaPadrao_SemMessage** = object { response }

---

### GET `/v2.1/pedidocompra/listarpedidos/lastid/{lastID}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra

Listar pedidos de compra por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `dataInicial` | query | não | string | Data em que inicia-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `dataFinal` | query | não | string | Data em que encerra-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `dataInicialBaixa` | query | não | string | Data em que inicia-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `dataFinalBaixa` | query | não | string | Data em que encerra-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `unidade` | query | não | string | Código da unidade de destino do pedido de compra |
| `status` | query | sim | string | Informar um dos seguintes valores, "P" para Pendentes, "B" para Baixados ou "C" para Cancelados |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseLV21** = object { response }

---

### GET `/v2.1/pedidocompra/listarpedidos/pedidossemrcm/lastid/{lastID}/fornecedor/{cnpj}/unidade/{cnpjUnid}/datainicial/{dataInicial}/datafinal/{dataFinal}/vinc/{vinc}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra sem Recebimento

Listar pedidos de compra sem recebimento por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `cnpj` | path | sim | string | Cnpj do fornecedor do pedido |
| `cnpjUnid` | path | sim | string | Cnpj da unidade do pedido |
| `dataInicial` | path | sim | string | Data em que inicia-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `dataFinal` | path | sim | string | Data em que finaliza-se a leitura dos pedidos de compra, considera-se até o dia atual (Formato "dd-mm-yyyy") |
| `vinc` | path | sim | string | Indicar se a rota deve buscar os pedidos dos fornecedores vinculados (deve-se utilizar valores SIM ou NAO) |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseLV21** = object { response }

---

### GET `/v2.1/pedidocompra/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra

Listar pedidos de compra por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido de compra |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseV21** = object { response }

---

### POST `/v2.1/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV21** = object { unidade, data, codigoCliente, formaPagamento, numeroPedidoCliente, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, email, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, turnoEntrega, dataPrevista, valorFrete, despesaAcessoria, transportador, camposExtras, itens }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponseSemMessage** = object { response }

---

### GET `/v2.2/pedidocompra/listarpedidos/lastid/{lastID}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra

Listar pedidos de compra por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `dataInicial` | query | não | string | Data em que inicia-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `dataFinal` | query | não | string | Data em que encerra-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `dataInicialBaixa` | query | não | string | Data em que inicia-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `dataFinalBaixa` | query | não | string | Data em que encerra-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `unidade` | query | não | string | Código da unidade de destino do pedido de compra |
| `status` | query | sim | string | Informar um dos seguintes valores, "P" para Pendentes, "B" para Baixados ou "C" para Cancelados |
| `fornecedor` | query | não | string | Código do fornecedor do pedido de compra |
| `vinculados` | query | não | boolean | Indica se deve considerar fornecedores vinculados ao fornecedor informado |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseLV21** = object { response }

---

### POST `/v2.2/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV22** = object { unidade, unidadeRetirada, data, codigoCliente, formaPagamento, numeroPedidoCliente, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, email, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, turnoEntrega, dataPrevista, valorFrete, despesaAcessoria, transportador, camposExtras, itens }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponseSemMessage** = object { response }

---

### GET `/v2.3/pedidocompra/listarpedidos/lastid/{lastID}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra

Listar pedidos de compra por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Último id lido nas requisições anteriores, quando for a primeira vez a consultar deve ser passado como "0" (mesmo passando 0 os dados retornam paginados) |
| `dataInicial` | query | não | string | Data em que inicia-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `dataFinal` | query | não | string | Data em que encerra-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `dataInicialBaixa` | query | não | string | Data em que inicia-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `dataFinalBaixa` | query | não | string | Data em que encerra-se a leitura dos pedidos de compra (Formato "dd-mm-yyyy") |
| `unidade` | query | não | string | Código da unidade de destino do pedido de compra |
| `status` | query | sim | string | Informar um dos seguintes valores, "P" para Pendentes, "B" para Baixados ou "C" para Cancelados |
| `fornecedor` | query | não | string | Código do fornecedor do pedido de compra |
| `vinculados` | query | não | boolean | Indica se deve considerar fornecedores vinculados ao fornecedor informado |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseLV23** = object { response }

---

### GET `/v2.3/pedidocompra/{codigo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Listar pedidos de compra

Listar pedidos de compra por data

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do pedido de compra |

**Respostas:**

- `200` Pedidos de compra retornadas — **PedCompraResponseV23** = object { response }

---

### POST `/v2.3/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV23** = object { unidade, unidadeRetirada, data, codigoCliente, formaPagamento, numeroPedidoCliente, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, email, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, turnoEntrega, dataPrevista, valorFrete, despesaAcessoria, transportador, camposExtras, itens, financeiro }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponseSemMessage** = object { response }

---

### POST `/v2.5/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV25** = object { unidade, origem, unidadeRetirada, data, codigoCliente, formaPagamento, numeroPedidoCliente, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, email, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, turnoEntrega, dataPrevista, valorFrete, despesaAcessoria, transportador, camposExtras, itens, financeiro }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponseSemMessage** = object { response }

---

### POST `/v2.6/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV26** = object { unidade, origem, unidadeRetirada, data, codigoCliente, formaPagamento, numeroPedidoCliente, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, email, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, turnoEntrega, dataPrevista, valorFrete, despesaAcessoria, transportador, camposExtras, itens, financeiro }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponseSemMessage** = object { response }

---

### POST `/v2.7/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV27** = object { unidade, origem, unidadeRetirada, data, codigoCliente, formaPagamento, numeroPedidoCliente, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, email, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, turnoEntrega, dataPrevista, valorFrete, despesaAcessoria, transportador, camposExtras, itens, financeiro }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponseSemMessage** = object { response }

---

### GET `/v2.7/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados dos produtos

Consulta dados detalhados dos produtos com informação de estoque.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Código do último produto consultado. Envie "0" caso queira consultar todas as informações. (mesmo passando 0 os dados retornam paginados) |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |
| `loadtributacao` | query | não | boolean | Se informado e marcado como 'true', será retornada a tributacao do produto no atributo 'tributacao', se encontrar tributação retornará como null |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV27** = object { response }

---

### GET `/v2.7/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV27** = object { response }

---

### GET `/v2.7/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos/dataHoraManutencao/{dataHoraManutencao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV27** = object { response }

---

### GET `/v2.7/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/departamento/{departamento}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV27** = object { response }

---

### GET `/v2.7/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/grupo/{grupo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV27** = object { response }

---

### GET `/v2.7/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/marcados`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoComEstoqueV27** = object { response }

---

### GET `/v2.7/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/semcalcularestoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV27** = object { response }

---

### GET `/v2.7/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/setor/{setor}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV27** = object { response }

---

### GET `/v2.7/produtounidade/listaprodutos/{lastId}/unidade/{CNPJ}/detalhado/dataHoraManutencao/{dataHoraManutencao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastId` |  | não |  |  |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `dataHoraManutencao` | path | sim | string | Data e hora de alteração (dd-MM-yyyy HH:mm:ss) |
| `outrosextras` | query | não | boolean | Se informado e marcado como 'true', será retornado os Campos Extras não nativos do sistema no atributo 'Extras' de tipo Array |
| `loadtributacao` | query | não | boolean | Se informado e marcado como 'true', será retornada a tributacao do produto no atributo 'tributacao', se encontrar tributação retornará como null |

**Respostas:**

- `200`  — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV27** = object { response }

---

### GET `/v2.7/produtounidade/{codigoBarras}/unidade/{CNPJ}/detalhado/consultarcodigobarras`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoDetalhadoV27** = object { response }

---

### GET `/v2.7/produtounidade/{codigo}/unidade/{CNPJ}/detalhado`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200`  — **ConsultarProdutoDetalhadoV27** = object { response }

---

### GET `/v2.7/produtounidade/{codigo}/unidade/{CNPJ}/detalhado/estoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200`  — **ConsultarProdutoEstoqueDetalhadoComEstoqueV27** = object { response }

---

### POST `/v2.8/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV28** = object { unidade, origem, unidadeRetirada, data, codigoCliente, formaPagamento, numeroPedidoCliente, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, email, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, turnoEntrega, dataPrevista, valorFrete, despesaAcessoria, transportador, rota, camposExtras, itens, financeiro }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponseSemMessage** = object { response }

---

### GET `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados dos produtos

Consulta dados detalhados dos produtos com informação de estoque.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV28** = object { response }

---

### GET `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV28** = object { response }

---

### GET `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos/dataHoraManutencao/{dataHoraManutencao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV28** = object { response }

---

### GET `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/departamento/{departamento}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV28** = object { response }

---

### GET `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/grupo/{grupo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV28** = object { response }

---

### GET `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/marcados`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoComEstoqueV28** = object { response }

---

### GET `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/semcalcularestoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV28** = object { response }

---

### GET `/v2.8/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/setor/{setor}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV28** = object { response }

---

### GET `/v2.8/produtounidade/listaprodutos/{lastId}/unidade/{CNPJ}/detalhado/dataHoraManutencao/{dataHoraManutencao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200`  — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV28** = object { response }

---

### GET `/v2.8/produtounidade/{codigoBarras}/unidade/{CNPJ}/detalhado/consultarcodigobarras`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoDetalhadoV28** = object { response }

---

### GET `/v2.8/produtounidade/{codigo}/unidade/{CNPJ}/detalhado`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200`  — **ConsultarProdutoDetalhadoV28** = object { response }

---

### GET `/v2.8/produtounidade/{codigo}/unidade/{CNPJ}/detalhado/estoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200`  — **ConsultarProdutoEstoqueDetalhadoComEstoqueV28** = object { response }

---

### POST `/v2.9/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV29** = `PedidoVendaV28` (ver reference/schemas.md) & object { entregador }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponseSemMessage** = object { response }

---

### GET `/v2.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados dos produtos

Consulta dados detalhados dos produtos com informação de estoque.

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
| `codPreco` | query | não | string | Filtra os produtos por código de preço |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV29** = object { response }

---

### GET `/v2.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV29** = object { response }

---

### GET `/v2.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos/dataHoraManutencao/{dataHoraManutencao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV29** = object { response }

---

### GET `/v2.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/departamento/{departamento}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV29** = object { response }

---

### GET `/v2.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/grupo/{grupo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV29** = object { response }

---

### GET `/v2.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/marcados`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoComEstoqueV29** = object { response }

---

### GET `/v2.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/semcalcularestoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV29** = object { response }

---

### GET `/v2.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/setor/{setor}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV29** = object { response }

---

### GET `/v2.9/produtounidade/listaprodutos/{lastId}/unidade/{CNPJ}/detalhado/dataHoraManutencao/{dataHoraManutencao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200`  — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV29** = object { response }

---

### GET `/v2.9/produtounidade/listaprodutos/{lastRelease}/unidade/{CNPJ}/detalhado/customrelease`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `limit` | query | sim | string | Total de registros por página |
| `fieldName` | query | sim | number | Nome do campo de release customizado |
| `lastRelease` | path | sim | number | Código do último release consultado. Envie "0" caso queira consultar desde o primeiro release (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200`  — **ConsultarProdutoEstoqueDetalhadoCustomReleaseV29** = object { response }

---

### GET `/v2.9/produtounidade/{codigoBarras}/unidade/{CNPJ}/detalhado/consultarcodigobarras`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoDetalhadoV29** = object { response }

---

### GET `/v2.9/produtounidade/{codigo}/unidade/{CNPJ}/detalhado`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200`  — **ConsultarProdutoDetalhadoV29** = object { response }

---

### GET `/v2.9/produtounidade/{codigo}/unidade/{CNPJ}/detalhado/estoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200`  — **ConsultarProdutoEstoqueDetalhadoComEstoqueV29** = object { response }

---

### POST `/v3.0/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV30** = `PedidoVendaV29` (ver reference/schemas.md) & object { dados_adicionais }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponseSemMessage** = object { response }

---

### GET `/v3.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados dos produtos

Consulta dados detalhados dos produtos com informação de estoque.

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
| `codPreco` | query | não | string | Filtra os produtos por código de preço |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV30** = object { response }

---

### GET `/v3.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV30** = object { response }

---

### GET `/v3.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos/dataHoraManutencao/{dataHoraManutencao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV30** = object { response }

---

### GET `/v3.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/departamento/{departamento}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV30** = object { response }

---

### GET `/v3.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/grupo/{grupo}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV30** = object { response }

---

### GET `/v3.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/marcados`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoComEstoqueV30** = object { response }

---

### GET `/v3.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/semcalcularestoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV30** = object { response }

---

### GET `/v3.0/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/setor/{setor}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV30** = object { response }

---

### GET `/v3.0/produtounidade/listaprodutos/{lastId}/unidade/{CNPJ}/detalhado/dataHoraManutencao/{dataHoraManutencao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200`  — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV30** = object { response }

---

### GET `/v3.0/produtounidade/listaprodutos/{lastRelease}/unidade/{CNPJ}/detalhado/customrelease`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `limit` | query | sim | string | Total de registros por página |
| `fieldName` | query | sim | number | Nome do campo de release customizado |
| `lastRelease` | path | sim | number | Código do último release consultado. Envie "0" caso queira consultar desde o primeiro release (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200`  — **ConsultarProdutoEstoqueDetalhadoCustomReleaseV30** = object { response }

---

### GET `/v3.0/produtounidade/{codigoBarras}/unidade/{CNPJ}/detalhado/consultarcodigobarras`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoDetalhadoV30** = object { response }

---

### GET `/v3.0/produtounidade/{codigo}/unidade/{CNPJ}/detalhado`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200`  — **ConsultarProdutoDetalhadoV30** = object { response }

---

### GET `/v3.0/produtounidade/{codigo}/unidade/{CNPJ}/detalhado/estoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200`  — **ConsultarProdutoEstoqueDetalhadoComEstoqueV30** = object { response }

---

### POST `/v3.1/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV31** = object { unidade, origem, unidadeRetirada, data, codigoCliente, formaPagamento, numeroPedidoCliente, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, email, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, turnoEntrega, dataPrevista, valorFrete, despesaAcessoria, transportador, rota, entregador, dados_adicionais, camposExtras, itens, financeiro }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponseSemMessage** = object { response }

---

### GET `/v3.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Obter dados dos produtos

Consulta dados detalhados dos produtos com informação de estoque.

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
| `codPreco` | query | não | string | Filtra os produtos por código de preço |
| `loadCodBarrasAlt` | query | não | boolean | Se informado e marcado como 'true', será retornado os códigos de barras alternativos de cada produto |

**Respostas:**

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV31** = object { response }

---

### GET `/v3.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

### GET `/v3.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/ativos/dataHoraManutencao/{dataHoraManutencao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV31** = object { response }

---

### GET `/v3.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/departamento/{departamento}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV31** = object { response }

---

### GET `/v3.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/semcalcularestoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV31** = object { response }

---

### GET `/v3.1/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/detalhado/setor/{setor}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200` Dados carregados — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV31** = object { response }

---

### GET `/v3.1/produtounidade/listaprodutos/{lastId}/unidade/{CNPJ}/detalhado/dataHoraManutencao/{dataHoraManutencao}`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200`  — **ConsultarProdutoEstoqueDetalhadoSemEstoqueV31** = object { response }

---

### GET `/v3.1/produtounidade/listaprodutos/{lastRelease}/unidade/{CNPJ}/detalhado/customrelease`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CNPJ` | path | sim | string | CNPJ da unidade a consultar |
| `limit` | query | sim | string | Total de registros por página |
| `fieldName` | query | sim | number | Nome do campo de release customizado |
| `lastRelease` | path | sim | number | Código do último release consultado. Envie "0" caso queira consultar desde o primeiro release (mesmo passando 0 os dados retornam paginados) |
| `loadCodBarrasAlt` | query | não | boolean | Se informado e marcado como 'true', será retornado os códigos de barras alternativos de cada produto |

**Respostas:**

- `200`  — **ConsultarProdutoEstoqueDetalhadoCustomReleaseV31** = object { response }

---

### GET `/v3.1/produtounidade/{codigoBarras}/unidade/{CNPJ}/detalhado/consultarcodigobarras`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200` Dados carregados — **ConsultarProdutoDetalhadoV31** = object { response }

---

### GET `/v3.1/produtounidade/{codigo}/unidade/{CNPJ}/detalhado`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200`  — **ConsultarProdutoDetalhadoV31** = object { response }

---

### GET `/v3.1/produtounidade/{codigo}/unidade/{CNPJ}/detalhado/estoque`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

- `200`  — **ConsultarProdutoEstoqueDetalhadoComEstoqueV31** = object { response }

---

### POST `/v3.2/pedidos`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

**Resumo:** Inserir Pedido de Venda

Inserir um novo pedido de venda na base

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PedidoVendaV32** = `PedidoVendaV31` (ver reference/schemas.md) & object { origemDataHora, taxaEntrega }

**Respostas:**

- `200` Pedido adicionado. — **AddPedidoResponseSemMessage** = object { response }

---

### GET `/v3.2/produtounidade/listaprodutos/{lastRelease}/unidade/{CNPJ}/detalhado/customrelease`

> ⚠️ **ENDPOINT DEPRECIADO** — evitar uso em código novo.

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

**Respostas:**

- `200`  — **ConsultarProdutoEstoqueDetalhadoCustomReleaseV32** = object { response }

---
