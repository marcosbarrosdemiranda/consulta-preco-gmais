# Dicionário de Schemas

859 schemas definidos no spec. Gerado automaticamente — use Ctrl+F / grep para localizar.

## AddPedidoPost

{ unidade: string(string) ex: "001"; data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 166880; formaPagamento: string(string) ex: "001"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; desconto: number(double) ex: 0; codigoDocumento: string ex: "6100"; itens: `PedidoVenda` (ver reference/schemas.md) }

## AddPedidoPostDeprecated0

{ data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 166880; formaPagamento: string(string) ex: "001"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; itens: `PedidoVenda` (ver reference/schemas.md) }

## AddPedidoPostDeprecated1

{ data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 166880; formaPagamento: string(string) ex: "001"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; codigoDocumento: string ex: "6100"; itens: `PedidoVenda` (ver reference/schemas.md) }

## AddPedidoPostDeprecated2

{ data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 166880; formaPagamento: string(string) ex: "001"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; desconto: number(double) ex: 0; codigoDocumento: string ex: "6100"; itens: `PedidoVenda` (ver reference/schemas.md) }

## AddPedidoResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

No retorno quando o status for "ok" retornará o atributo "codigopedido", esse código deve ser armazenado para consulta futura, pois o método é assincrono.

{ response: object { status, message, messages, codigopedido } }

## AddPedidoResponseSemMessage

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

No retorno quando o status for "ok" retornará o atributo "codigopedido", esse código deve ser armazenado para consulta futura, pois o método é assincrono.

{ response: object { status, messages, codigopedido } }

## Agendas

Agendas de recebimento

array de { transacao: string(string) ex: "1.10089944E8"; status: string(string) ex: "N"; unidade: string(string) ex: "001"; fornecedor: integer ex: 100625; numeroPedidoCompra: string(string) ex: "316001"; trocas: string(string) ex: "N"; codigoFormaPagamento: string(string) ex: "030"; nomeContato: string(string) ex: "José Ronaldo"; foneContato: string(string) ex: "4137541234"; dataHoraAgenda: string(string) ex: "201403261755"; inicioDescarregamento: string(string) ex: "201403260830"; fimDescarregamento: string(string) ex: "201403260900"; pontoDescarregamento: integer ex: 1; caixas: integer ex: 0; peso: integer ex: 0; volume: integer ex: 0; paletes: integer ex: 0; efetivada: string(string) ex: ""; codigoUsuario: integer ex: 1; codigoUsuarioAutorizador: integer ex: 0; codigoUsuarioCancelamento: integer ex: 0; observacao: string(string) ex: ""; dataCancelamento: string(string) ex: "26/09/2019"; dataUltimaImpressao: string(string) ex: "26/09/2019"; horaUltimaImpressao: string(string) ex: ""; dataHoraEfetivacao: string(string) ex: ""; numeroNF: string(string) ex: ""; especie: string(string) ex: ""; quantidadeProdutos: integer ex: 0 }

## AgendasOfertaV1

{ Codigo: integer ex: 1001; Descricao: string(string) ex: "Teste"; DataInicio: string(string) ex: "01/01/2016"; DataFim: string(string) ex: "31/01/2016"; Unidades: string(string) ex: "001"; Situacao: string(string) ex: "PrecoCobrirOferta"; Divulgacao: string(string) ex: "Rádio"; DataLiberacao: string(string) ex: "15/03/2019"; Produtos: `ProdutosAgendaV1` (ver reference/schemas.md) }

## AgendasOfertaV1_1

{ Codigo: integer ex: 1001; Descricao: string(string) ex: "Teste"; DataInicio: string(string) ex: "01/01/2016"; DataFim: string(string) ex: "31/01/2016"; Unidades: string(string) ex: "001"; Situacao: string(string) ex: "Processada"; Divulgacao: string(string) ex: "Rádio"; DataLiberacao: string(string) ex: "15/03/2019"; Produtos: `ProdutosAgendaV1` (ver reference/schemas.md) }

## AgendasOferta_V1.2

{ Codigo: integer ex: 1001; Descricao: string(string) ex: "Teste"; DataInicio: string(string) ex: "01/01/2016"; DataFim: string(string) ex: "31/01/2016"; Unidades: string(string) ex: "001"; Situacao: string(string) ex: "Processada"; Divulgacao: string(string) ex: "Rádio"; DataLiberacao: string(string) ex: "15/03/2019"; Produtos: `ProdutosAgenda_V1.2` (ver reference/schemas.md) }

## AlterarSenhaClientePost

{ cliente: string(string) ex: "00000000000"; senha: string(string) ex: "123456" }

## AlterarStatusControleEntrega

{ transacao: string(string) ex: "00110001874"; status: string(string) ex: "PENDENTE"; statusOperacional: string(string) ex: "DESPACHADO" }

## AtualizarEtiquetasPost_V_1_0

{ codigoProduto: number ex: 100014; preco: number(double) ex: 1.25 }

## AtualizarEtiquetasPost_V_1_1

{ etiquetas: array de object { codigoProduto, preco, preco2, preco3, preco4, preco5 } }

## Auditorias

{ unidade: string(string) ex: "00000000000000"; codigoProduto: number ex: 10162; qtdeReferencia: number(double) ex: 15; quantidade: number(double) ex: 16; data: string(string) ex: "20/05/2015"; idEstoque: string(string) ex: "1" }

## AuditoriasV_1_1

{ id: string(string); unidade: string(string) ex: "00000000000000"; codigoProduto: number ex: 10162; quantidade: number(double) ex: 16; data: string(string) ex: "20/05/2015"; idEstoque: string(string) ex: "1"; acumular: boolean(boolean) ex: true }

## AuditoriasV_1_2

{ id: string(string); unidade: string(string) ex: "00000000000000"; codigoProduto: number ex: 10162; quantidade: number(double) ex: 16; data: string(string) ex: "20/05/2015"; idEstoque: string(string) ex: "1"; acumular: boolean(boolean) ex: true; dataHoraLeitura: string(dd/MM/yyyy HH:mm:ss Z) ex: "17/03/2025 16:04:26 -0300" }

## AutenticarClientePost

{ cliente: number ex: 1; senha: string(string) ex: "123456" }

## AutenticarFuncionarioPost

{ funcionario: string(string) ex: "00000000000"; senha: string(string) ex: "123456" }

## AutenticarPost

**AutenticarSessao** = object { usuario, senha }

## AutenticarSessao

O atributo pode retornar

{ usuario: string(string) ex: "100000"; senha: string(string) ex: "123456" }

## BaixaEntregasV1_1

{ response: object { status, appVersion, messages, content } }

## BaixaPendenciaEstoqueDto

{ transacao: string; operacao: string; sequencial: integer; qtde: number(double); dataBaixa: string ex: "dd/MM/yyyy"; status: string }

## BaixarEntregaRequestV_1

{ transacao: string ex: "00148762883"; entregador: string ex: "002"; kmFim: integer ex: 2340; observacao2: string ex: "Entrega finalizada com sucesso" }

## BaixarEntregasV_1_0

Quando o atributo "status" for "ok", a baixa da entrega foi realizada com sucesso. Os dados atualizados da entrega são retornados no campo "controleEntrega".

{ response: object { status, messages, message } }

## BaixarPontosCliente

{ Valor: number(double) ex: 1.15; Pdv: string(string) ex: "39.0"; Cupom: number ex: 215412 }

## BloquearUsuarioResponse

{ status: string ex: "ok"; appVersion: string ex: "4.0.0.165"; messages: array de object { message }; content: string ex: "Usuário bloqueado com sucesso" }

## CCustoFDE

Centro de custo associado a uma contrapartida

{ unidade: string ex: "001"; cCusto: string ex: "1000221"; parcela: integer ex: 1; valor: number(double) ex: 10.0 }

## CadClientes_v1.6

array de **ClienteDados_v1.6** = object { codigo, nome, razaoSocial, tipos, CnpjCpf, rgIe, dtExpRG, orgExpRG, ufExpRG, sexo, dadosResidenciais, dadosComerciais, foneCel, dtNasc, naturalidade, classe, email, emailCorr, endCorr, empresa, funcao, ramal, estadoCivil, profissao, escolaridade, contaContabil, contaGerencial, contribuinte, ramoAtividade, camposExtras }

## CadClientes_v1.7

array de **ClienteDados_v1.7** = `ClienteDados_v1.6` (ver reference/schemas.md) & object { dataCadastro }

## CadClientes_v1.8

array de **ClienteDados_v1.8** = `ClienteDados_v1.6` (ver reference/schemas.md) & object { dataCadastro, fpgt_Codigo }

## CadClientes_v1.9

array de **ClienteDados_v1.9** = `ClienteDados_v1.8` (ver reference/schemas.md) & object { situacao, codVinc, vendedor, dependentes }

## CadClientesv3

array de **ClienteDadosV3** = object { codigo, nome, razaoSocial, tipos, CnpjCpf, rgIe, dtExpRG, orgExpRG, ufExpRG, sexo, dadosResidenciais, dadosComerciais, foneCel, dtNasc, naturalidade, classe, email, emailCorr, endCorr, empresa, funcao, ramal }

## CadClientesv4

array de **ClienteDadosV4** = object { codigo, nome, razaoSocial, tipos, CnpjCpf, rgIe, dtExpRG, orgExpRG, ufExpRG, sexo, dadosResidenciais, dadosComerciais, foneCel, dtNasc, naturalidade, classe, email, emailCorr, endCorr, empresa, funcao, ramal, estadoCivil, profissao, escolaridade, contaContabil, contaGerencial, contribuinte }

## CadastrarCidade

{ descricao: string(string) ex: "Curitiba"; uf: string(string) ex: "PR"; codigoPais: string(string) ex: "1058"; codigoIBGE: integer(integer) ex: 1058 }

## CalcelarBaixa

{ Transacao: string ex: "1.1409285E8" }

## CamposExtras

{ clie_extra1: string(string) ex: "teste 1"; clie_extra2: string(string) ex: "extra 2"; clie_extra3: string(string) ex: "extra3"; clie_extra4: string(string); clie_extra5: string(string); clie_extra6: string(string); clie_extra7: number ex: 7; clie_extra8: number ex: 8; clie_extra9: string(string); outros: array de object { nome, tipo, valor } }

## CamposExtrasCliente

{ Extra1: string(string) ex: "extra1 asd"; Extra2: string(string) ex: "extra2 asd"; Extra3: string(string) ex: "extra3 asd"; Extra4: string(string) ex: "extra4 asd"; Extra5: string(string) ex: "extra5 asd"; Extra6: string(string) ex: "extra6 asd"; Extra7: number(double) ex: 24.71; Extra8: number(double) ex: 200.2; Extra9: string(string) ex: "22/06/2019" }

## CamposExtras_10_ao_99

{ extra10: string; extra11: string; extra12: string; extra13: string; extra14: string; extra15: string; extra16: string; extra17: string; extra18: string; extra19: string; extra20: string; extra21: string; extra22: string; extra23: string; extra24: string; extra25: string; extra26: string; extra27: string; extra28: string; extra29: string; extra30: string; extra31: string; extra32: string; extra33: string; extra34: string; extra35: string; extra36: string; extra37: string; extra38: string; extra39: string; extra40: string; extra41: string; extra42: string; extra43: string; extra44: string; extra45: string; extra46: string; extra47: string; extra48: string; extra49: string; extra50: string; extra51: string; extra52: string; extra53: string; extra54: string; extra55: string; extra56: string; extra57: string; extra58: string; extra59: string; extra60: string; extra61: string; extra62: string; extra63: string; extra64: string; extra65: string; extra66: string; extra67: string; extra68: string; extra69: string; extra70: string; extra71: string; extra72: string; extra73: string; extra74: string; extra75: string; extra76: string; extra77: string; extra78: string; extra79: string; extra80: string; extra81: string; extra82: string; extra83: string; extra84: string; extra85: string; extra86: string; extra87: string; extra88: string; extra89: string; extra90: string; extra91: string; extra92: string; extra93: string; extra94: string; extra95: string; extra96: string; extra97: string; extra98: string; extra99: string; eraseExtras: array de any }

## CancelamentoFDE

{ transacao: string(string) ex: "00222437464"; motivo: string(string) ex: "Cancelamento" }

## CancelamentoTransacaoResponse_V_1_0

{ response: object { status, messages, content } }

## CancelarTransacao_V_1_0

{ transacao: string(string) ex: "00110523164"; motivo: string(string) ex: "motivo do cancelamento"; origemApp: string(string) ex: "Insomnia"; origemVersao: string(string) ex: "1.0"; origemIdentificador: string(string) ex: "Insomnia teste" }

## CestaBasica

CestaBasica

array de { codigo: string ex: "001"; descricao: string(string) ex: "Cesta Basica Teste"; unidade: string(string) ex: "001"; codigoProduto: number ex: 10162; produtos: `ProdCestaBasica` (ver reference/schemas.md) }

## Cliente

{ Codigo: number ex: 1; Nome: string(string) ex: "Cliente 1"; razaoSocial: string(string) ex: "Cliente"; CnpjCpf: string(string) ex: "00000000000"; rgIe: string(string) ex: "000000000"; dtExpRG: string(string) ex: "01/01/2015"; orgExpRG: string(string) ex: ""; ufExpRG: string(string) ex: "PR"; sexo: string(string) ex: "M"; dadosResidenciais: `EnderecoRes` (ver reference/schemas.md); dadosComerciais: `EnderecoCom` (ver reference/schemas.md); foneCel: string(string) ex: ""; dtNasc: string(string) ex: "02/02/1975"; naturalidade: string(string) ex: ""; classe: string(string) ex: ""; email: string(string) ex: "cli@mail.com"; emailCorr: string(string) ex: ""; endCorr: string(string) ex: ""; empresa: string(string) ex: ""; funcao: string(string) ex: ""; ramal: integer ex: 0 }

## ClienteDadosV3

{ codigo: integer ex: 138371; nome: string(string) ex: "Sandra Maria Gonsalves De Melo"; razaoSocial: string(string) ex: "Sandra Maria Gonsalves De Melo"; tipos: string(string) ex: "SM"; CnpjCpf: string(string) ex: "50677047991"; rgIe: string(string) ex: "36145439"; dtExpRG: string(string) ex: ""; orgExpRG: string(string) ex: ""; ufExpRG: string(string) ex: "PR"; sexo: string(string) ex: "F"; dadosResidenciais: `dadosResidenciais` (ver reference/schemas.md); dadosComerciais: `dadosComerciais` (ver reference/schemas.md); foneCel: string(string) ex: "4498651504"; dtNasc: string(string) ex: ""; naturalidade: string(string) ex: "Brasileira"; classe: string(string) ex: ""; email: string(string) ex: ""; emailCorr: string(string) ex: "S"; endCorr: string(string) ex: "0"; empresa: string(string) ex: "5"; funcao: string(string) ex: ""; ramal: integer ex: 0 }

## ClienteDadosV4

{ codigo: integer ex: 138371; nome: string(string) ex: "Sandra Maria Gonsalves De Melo"; razaoSocial: string(string) ex: "Sandra Maria Gonsalves De Melo"; tipos: string(string) ex: "SM"; CnpjCpf: string(string) ex: "50677047991"; rgIe: string(string) ex: "36145439"; dtExpRG: string(string) ex: ""; orgExpRG: string(string) ex: ""; ufExpRG: string(string) ex: "PR"; sexo: string(string) ex: "F"; dadosResidenciais: `dadosResidenciais` (ver reference/schemas.md); dadosComerciais: `dadosComerciais` (ver reference/schemas.md); foneCel: string(string) ex: "4498651504"; dtNasc: string(string) ex: ""; naturalidade: string(string) ex: "Brasileira"; classe: string(string) ex: ""; email: string(string) ex: ""; emailCorr: string(string) ex: "S"; endCorr: string(string) ex: "0"; empresa: string(string) ex: "5"; funcao: string(string) ex: ""; ramal: integer ex: 0; estadoCivil: string(string) ex: "SOLTEIRO"; profissao: string(string) ex: ""; escolaridade: string(string) ex: "SUPERIOR"; contaContabil: integer ex: 212152; contaGerencial: integer ex: 212152; contribuinte: string(string) ex: "S" }

## ClienteDadosV5

{ codigo: integer ex: 138371; nome: string(string) ex: "Sandra Maria Gonsalves De Melo"; razaoSocial: string(string) ex: "Sandra Maria Gonsalves De Melo"; tipos: string(string) ex: "SM"; CnpjCpf: string(string) ex: "50677047991"; rgIe: string(string) ex: "36145439"; dtExpRG: string(string) ex: ""; orgExpRG: string(string) ex: ""; ufExpRG: string(string) ex: "PR"; sexo: string(string) ex: "F"; dadosResidenciais: `dadosResidenciais` (ver reference/schemas.md); dadosComerciais: `dadosComerciais` (ver reference/schemas.md); foneCel: string(string) ex: "4498651504"; dtNasc: string(string) ex: ""; naturalidade: string(string) ex: "Brasileira"; classe: string(string) ex: ""; email: string(string) ex: ""; emailCorr: string(string) ex: "S"; endCorr: string(string) ex: "0"; empresa: string(string) ex: "5"; funcao: string(string) ex: ""; ramal: integer ex: 0; estadoCivil: string(string) ex: "SOLTEIRO"; profissao: string(string) ex: ""; escolaridade: string(string) ex: "SUPERIOR"; contaContabil: integer ex: 212152; contaGerencial: integer ex: 212152; contribuinte: string(string) ex: "S"; camposExtras: `CamposExtras` (ver reference/schemas.md) }

## ClienteDados_v1.6

{ codigo: integer ex: 138371; nome: string(string) ex: "Sandra Maria Gonsalves De Melo"; razaoSocial: string(string) ex: "Sandra Maria Gonsalves De Melo"; tipos: string(string) ex: "SM"; CnpjCpf: string(string) ex: "50677047991"; rgIe: string(string) ex: "36145439"; dtExpRG: string(string) ex: ""; orgExpRG: string(string) ex: ""; ufExpRG: string(string) ex: "PR"; sexo: string(string) ex: "F"; dadosResidenciais: `dadosResidenciais` (ver reference/schemas.md); dadosComerciais: `dadosComerciais` (ver reference/schemas.md); foneCel: string(string) ex: "4498651504"; dtNasc: string(string) ex: ""; naturalidade: string(string) ex: "Brasileira"; classe: string(string) ex: ""; email: string(string) ex: ""; emailCorr: string(string) ex: "S"; endCorr: string(string) ex: "0"; empresa: string(string) ex: "5"; funcao: string(string) ex: ""; ramal: integer ex: 0; estadoCivil: string(string) ex: "SOLTEIRO"; profissao: string(string) ex: ""; escolaridade: string(string) ex: "SUPERIOR"; contaContabil: integer ex: 212152; contaGerencial: integer ex: 212152; contribuinte: string(string) ex: "S"; ramoAtividade: string(string) ex: "GERENTE"; camposExtras: `CamposExtras` (ver reference/schemas.md) }

## ClienteDados_v1.7

**ClienteDados_v1.6** = object { codigo, nome, razaoSocial, tipos, CnpjCpf, rgIe, dtExpRG, orgExpRG, ufExpRG, sexo, dadosResidenciais, dadosComerciais, foneCel, dtNasc, naturalidade, classe, email, emailCorr, endCorr, empresa, funcao, ramal, estadoCivil, profissao, escolaridade, contaContabil, contaGerencial, contribuinte, ramoAtividade, camposExtras } & { dataCadastro: string(dd/mm/yyyy) ex: "10/07/2024" }

## ClienteDados_v1.8

**ClienteDados_v1.6** = object { codigo, nome, razaoSocial, tipos, CnpjCpf, rgIe, dtExpRG, orgExpRG, ufExpRG, sexo, dadosResidenciais, dadosComerciais, foneCel, dtNasc, naturalidade, classe, email, emailCorr, endCorr, empresa, funcao, ramal, estadoCivil, profissao, escolaridade, contaContabil, contaGerencial, contribuinte, ramoAtividade, camposExtras } & { dataCadastro: string(dd/mm/yyyy) ex: "10/07/2024"; fpgt_Codigo: string(string) ex: "001" }

## ClienteDados_v1.9

**ClienteDados_v1.8** = `ClienteDados_v1.6` (ver reference/schemas.md) & object { dataCadastro, fpgt_Codigo } & { situacao: string(string) ex: "N"; codVinc: integer ex: 0; vendedor: object { codigo, nome, vendedoresAlternativos, rotaEntrega, sequenciaEntrega, formaPagamentoCodigo, classe, localPagamento, abatimento, transportador, regiaoVendas }; dependentes: array de object { codigo, clieCodigo, nome, nomeCartao, grauVinc, cpf, dtNasc, empresa, funcao, endCom, bairCom, muniCodigo, cepCom, foneCom, ramal, rendaComprovada, rendaNaoComprovada, descrRendaNaoComp, dtCadastro } }

## ClienteSaldoPontos

{ Valor: number(double) ex: 5.868; ValorLiberado: number(double) ex: 5.868; Saldo: number(double) ex: 97.789; SaldoLiberado: number(double) ex: 97.789 }

## ClienteV2

{ nome: string(string) ex: "Paulo Silva"; sexo: string(string) ex: "M"; tipo: string(string) ex: "F"; tipoCliente: string(string) ex: ""; fone: string(string) ex: "5154654"; celular: string(string) ex: "956465853"; foneComercial: string(string) ex: "45465468"; uf: string(string) ex: "PR"; cep: string(string) ex: "2654654"; cidade: integer ex: 5; endereco: string(string) ex: "Rua 2"; bairro: string(string) ex: ""; numero: string(string) ex: ""; classe: string(string) ex: "564"; complemento: string(string) ex: ""; dataNascimento: string(string) ex: "25/08/1984"; cpf: string(string) ex: "552158584"; cnpj: string(string) ex: ""; rg: string(string) ex: "5654654"; ie: string(string) ex: ""; orgaoExpRG: string(string) ex: "SESPR"; ufExpRG: string(string) ex: "PR"; estadoCivil: string(string) ex: "SOLTEIRO"; profissao: string(string) ex: ""; escolaridade: string(string) ex: "SUPERIOR"; email: string(string) ex: "email@email.com.br"; contaContabil: integer ex: 100024; contaGerencial: integer ex: 100001 }

## ClienteV3

{ Nome: string(string) ex: "Paulo Silva"; Sexo: string(string) ex: "M"; Tipo: string(string) ex: "F"; Fone: string(string) ex: "5154654"; Uf: string(string) ex: "PR"; Cep: string(string) ex: "2654654"; Classe: string(string) ex: "sssssdasd"; Cidade: string(string) ex: "Curitiba"; Endereco: string(string) ex: "Rua 2"; Bairro: string(string) ex: ""; Cpf: string(string) ex: "20116794003"; Rg: string(string) ex: "5654654"; Email: string(string) ex: "email@email.com.br" }

## ClienteV4

{ nome: string(string) ex: "Paulo Silva"; sexo: string(string) ex: "M"; tipo: string(string) ex: "F"; tipoCliente: string(string) ex: ""; fone: string(string) ex: "5154654"; celular: string(string) ex: "956465853"; foneComercial: string(string) ex: "45465468"; uf: string(string) ex: "PR"; cep: string(string) ex: "2654654"; cidade: integer ex: 5; endereco: string(string) ex: "Rua 2"; bairro: string(string) ex: ""; numero: string(string) ex: ""; classe: string(string) ex: "564"; complemento: string(string) ex: ""; dataNascimento: string(string) ex: "25/08/1984"; cpf: string(string) ex: "552158584"; cnpj: string(string) ex: ""; rg: string(string) ex: "5654654"; ie: string(string) ex: ""; orgaoExpRG: string(string) ex: "SESPR"; ufExpRG: string(string) ex: "PR"; estadoCivil: string(string) ex: "SOLTEIRO"; profissao: string(string) ex: ""; escolaridade: string(string) ex: "SUPERIOR"; email: string(string) ex: "email@email.com.br"; contaContabil: integer ex: 100024; contaGerencial: integer ex: 100001; contribuinte: string(string) ex: "S" }

## ClienteV5

{ nome: string(string) ex: "Paulo Silva"; sexo: string(string) ex: "M"; tipo: string(string) ex: "F"; tipoCliente: string(string) ex: ""; fone: string(string) ex: "5154654"; celular: string(string) ex: "956465853"; foneComercial: string(string) ex: "45465468"; classe: string(string) ex: "564"; enderecoResidencial: `EnderecoClienteV1` (ver reference/schemas.md); enderecoComercial: `EnderecoClienteV1` (ver reference/schemas.md); dataNascimento: string(string) ex: "25/08/1984"; cpf: string(string) ex: "552158584"; cnpj: string(string) ex: ""; rg: string(string) ex: "5654654"; ie: string(string) ex: ""; orgaoExpRG: string(string) ex: "SESPR"; ufExpRG: string(string) ex: "PR"; estadoCivil: string(string) ex: "SOLTEIRO"; profissao: string(string) ex: ""; escolaridade: string(string) ex: "SUPERIOR"; email: string(string) ex: "email@email.com.br"; contaContabil: integer ex: 100024; contaGerencial: integer ex: 100001; contribuinte: string(string) ex: "S" }

## ClienteV6

{ nome: string(string) ex: "Paulo Silva"; sexo: string(string) ex: "M"; tipo: string(string) ex: "F"; tipoCliente: string(string) ex: ""; fone: string(string) ex: "5154654"; celular: string(string) ex: "956465853"; foneComercial: string(string) ex: "45465468"; classe: string(string) ex: "564"; enderecoResidencial: `EnderecoClienteV1` (ver reference/schemas.md); enderecoComercial: `EnderecoClienteV1` (ver reference/schemas.md); dataNascimento: string(string) ex: "25/08/1984"; cpf: string(string) ex: "552158584"; cnpj: string(string) ex: ""; rg: string(string) ex: "5654654"; ie: string(string) ex: ""; orgaoExpRG: string(string) ex: "SESPR"; ufExpRG: string(string) ex: "PR"; estadoCivil: string(string) ex: "SOLTEIRO"; profissao: string(string) ex: ""; escolaridade: string(string) ex: "SUPERIOR"; email: string(string) ex: "email@email.com.br"; contaContabil: integer ex: 100024; contaGerencial: integer ex: 100001; contribuinte: string(string) ex: "S"; unidadeCadastro: string(string) ex: "001" }

## ClienteV7

{ nome: string(string) ex: "Paulo Silva"; sexo: string(string) ex: "M"; tipo: string(string) ex: "F"; tipoCliente: string(string) ex: ""; fone: string(string) ex: "5154654"; celular: string(string) ex: "956465853"; foneComercial: string(string) ex: "45465468"; classe: string(string) ex: "564"; enderecoResidencial: `EnderecoClienteV1` (ver reference/schemas.md); enderecoComercial: `EnderecoClienteV1` (ver reference/schemas.md); dataNascimento: string(string) ex: "25/08/1984"; cpf: string(string) ex: "552158584"; cnpj: string(string) ex: ""; rg: string(string) ex: "5654654"; ie: string(string) ex: ""; orgaoExpRG: string(string) ex: "SESPR"; ufExpRG: string(string) ex: "PR"; estadoCivil: string(string) ex: "SOLTEIRO"; profissao: string(string) ex: ""; escolaridade: string(string) ex: "SUPERIOR"; email: string(string) ex: "email@email.com.br"; contaContabil: integer ex: 100024; contaGerencial: integer ex: 100001; contribuinte: string(string) ex: "S"; unidadeCadastro: string(string) ex: "001"; observacao: string ex: "Teste 1.7"; vendedor: string ex: "1234" }

## Cliente_v1_8

{ nome: string(string) ex: "Paulo Silva"; sexo: string(string) ex: "M"; tipo: string(string) ex: "F"; tipoCliente: string(string) ex: ""; fone: string(string) ex: "5154654"; celular: string(string) ex: "956465853"; foneComercial: string(string) ex: "45465468"; classe: string(string) ex: "564"; enderecoResidencial: `EnderecoClienteV1` (ver reference/schemas.md); enderecoComercial: `EnderecoClienteV1` (ver reference/schemas.md); dataNascimento: string(string) ex: "25/08/1984"; cpf: string(string) ex: "552158584"; cnpj: string(string) ex: ""; rg: string(string) ex: "5654654"; ie: string(string) ex: ""; orgaoExpRG: string(string) ex: "SESPR"; ufExpRG: string(string) ex: "PR"; estadoCivil: string(string) ex: "SOLTEIRO"; profissao: string(string) ex: ""; escolaridade: string(string) ex: "SUPERIOR"; email: string(string) ex: "email@email.com.br"; contaContabil: integer ex: 100024; contaGerencial: integer ex: 100001; contribuinte: string(string) ex: "S"; unidadeCadastro: string(string) ex: "001"; observacao: string ex: "Teste 1.8"; vendedor: string ex: "1234"; ramoAtividade: string ex: "GERENTE" }

## Cliente_v1_9

{ nome: string(string) ex: "Paulo Silva"; sexo: string(string) ex: "M"; tipo: string(string) ex: "F"; tipoCliente: string(string) ex: ""; fone: string(string) ex: "5154654"; celular: string(string) ex: "956465853"; foneComercial: string(string) ex: "45465468"; classe: string(string) ex: "564"; enderecoResidencial: `EnderecoClienteV1` (ver reference/schemas.md); enderecoComercial: `EnderecoClienteV1` (ver reference/schemas.md); dataNascimento: string(string) ex: "25/08/1984"; cpf: string(string) ex: "552158584"; cnpj: string(string) ex: ""; rg: string(string) ex: "5654654"; ie: string(string) ex: ""; orgaoExpRG: string(string) ex: "SESPR"; ufExpRG: string(string) ex: "PR"; estadoCivil: string(string) ex: "SOLTEIRO"; profissao: string(string) ex: ""; escolaridade: string(string) ex: "SUPERIOR"; email: string(string) ex: "email@email.com.br"; contaContabil: integer ex: 100024; contaGerencial: integer ex: 100001; contribuinte: string(string) ex: "S"; unidadeCadastro: string(string) ex: "001"; observacao: string ex: "Teste 1.8"; vendedor: string ex: "1234"; ramoAtividade: string ex: "GERENTE"; caracTrib: string ex: "A" }

## Cliente_v2_0

**Cliente_v1_9** = object { nome, sexo, tipo, tipoCliente, fone, celular, foneComercial, classe, enderecoResidencial, enderecoComercial, dataNascimento, cpf, cnpj, rg, ie, orgaoExpRG, ufExpRG, estadoCivil, profissao, escolaridade, email, contaContabil, contaGerencial, contribuinte, unidadeCadastro, observacao, vendedor, ramoAtividade, caracTrib } & { razaoSocial: string(string) ex: "Razão social do cliente" }

## CodigoPendencia

{ codigo: string(string) ex: "002"; descricao: string(string) ex: "Trocas Pendentes"; bxparcial: string(string) ex: "S"; sugcompra: string(string) ex: "N"; tipo: string(string) ex: "TC"; pzelim: number(integer) ex: 0; pzelimbx: number(integer) ex: 0; comportamento: string(string) ex: "" }

## Compradores

{ codigo: string(string) ex: "001"; nome: string(string) ex: "Nilson Borghi"; alcada: number(number) ex: 0; dptos: string(string) ex: "Códigos dos departamentos separados por ;"; grupos: string(string) ex: "Códigos dos grupos separados por ;" }

## Compradores_V_1_0

{ codigo: string(string) ex: "001"; nome: string(string) ex: "Nilson Borghi" }

## Compradores_V_1_2

{ codigo: string(string) ex: "001"; nome: string(string) ex: "Nilson Borghi"; alcada: number(number) ex: 0; dptos: string(string) ex: "Códigos dos departamentos separados por ;"; grupos: string(string) ex: "Códigos dos grupos separados por ;"; comportamentos: string(string) ex: "Comportamentos do comprador separados por ;" }

## ConcorrentesV1_0

{ itens: array de object { codigo, nome, nomeReduzido, unidades, unidadesValidas } }

## ConcorrentesV1_1

{ itens: array de object { codigo, nome, nomeReduzido, unidades, unidadesValidas, camposExtras } }

## ConsultaCancelamentoTransacaoResponse_V_1_0

{ response: object { status, messages, content } }

## ConsultaControleEntrega

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, controleEntrega } }

## ConsultaControleEntregaV1_1

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, controleEntrega } }

## ConsultaDocumentosAtivosUsuario_V_1_0

{ response: object { status, messages, content } }

## ConsultaDocumentos_V_1_0

{ response: object { status, appVersion, messages, content } }

## ConsultaMovSubContasV1_0

{ response: `ResponsePadrao` (ver reference/schemas.md) & object { content } }

## ConsultaMovSubContasV1_0Item

{ release: number ex: 15; codigo: number ex: 15; transacao: string(string) ex: "00119332540"; status: string(string) ex: "N"; dataMovimento: string(string) ex: "09/05/2023"; contaGerencial: number ex: 111101; unidade: string(string) ex: "003"; subConta: string(string) ex: "401"; regra: string(string) ex: "10"; valor: number ex: 14.12; tipoLancamento: string(string) ex: "DEBITO"; projeto: string(string) ex: "" }

## ConsultaProgramaPreco

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento. 

O atributo "precoAlteracao" do objeto "programacoes" indica qual preço será alterado: prVenda1, prVenda2, prVenda3, prVenda4 e prVenda5

{ response: object { status, message, messages, programacoes } }

## ConsultaReciboOk_V_1_0

array de { recibo: number ex: 162; dataHoraProc: string(dd/MM/aaaa hh:MM:ss) ex: "20/01/2025 11:13:14"; controles: array de string }

## ConsultaSubContasV1_0

{ response: `ResponsePadrao` (ver reference/schemas.md) & object { content } }

## ConsultaSubContasV1_0Item

{ codigo: string ex: "001"; classificacao: string ex: "1"; descricao: string ex: "Descrição"; unidades: string ex: "001;004;003;102;101;002"; departamento: string ex: "001"; grupo: string ex: "" }

## ConsultarAltProdutoResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, produto } }

## ConsultarAltProdutoResponse4

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, produto } }

## ConsultarAltProdutoResponse5

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, produto } }

## ConsultarCadGruposResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, messages, content } }

## ConsultarCadGruposResponseV1_1

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, grupos } }

## ConsultarCadProdutosDeprecatedResponse

{ response: object { status, messages, produto }; maxCod: string(string) ex: "792500" }

## ConsultarCadProdutosResponse

{ response: object { status, messages, produto }; maxCod: string(string) ex: "792500" }

## ConsultarCadUsuariosDeprecatedResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, usuarios } }

## ConsultarCadUsuariosResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, usuarios } }

## ConsultarCadUsuariosResponseV1_2

{ response: object { status, appVersion, messages, content } }

## ConsultarCadastroProdutoDetalhadoResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, produto } }

## ConsultarCadastroProdutoDetalhadoResponseV2

{ response: object { status, messages, produto } }

## ConsultarCadastroProdutoResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, produto } }

## ConsultarCadastroProdutosDetalhadoResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, produtos } }

## ConsultarCadastroProdutosDetalhadoResponseV2

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, produtos } }

## ConsultarCadastroProdutosResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, produtos } }

## ConsultarCentroCustosResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, centroDeCustos } }

## ConsultarCestasBasicasResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages }; cestasBasicas: `CestaBasica` (ver reference/schemas.md); maxCod: string ex: "001" }

## ConsultarCestasBasicasResponseV2

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, messages, content } }

## ConsultarClientePlacaVeiculoReponde

{ response: object { status, messages, cliente } }

## ConsultarCodBarrasAlternativoListaResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, codigosAlterados } }

## ConsultarCodBarrasAlternativoListaResponseV11

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, codigosAlterados } }

## ConsultarCodBarrasAlternativoProdResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, codigosAlterados } }

## ConsultarCodBarrasAlternativoProdResponseV11

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, codigosAlterados } }

## ConsultarDadosClienteResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, cliente } }

## ConsultarDadosUsuarioDeprecatedResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, usuario } }

## ConsultarDadosUsuarioDetalhadoResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, usuario } }

## ConsultarDadosUsuarioDetalhadoResponseV1_2

{ response: object { status, appVersion, messages, content } }

## ConsultarDadosUsuarioExternoResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, usuario } }

## ConsultarDadosUsuarioExternoResponse_V_1_2

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, usuario } }

## ConsultarDadosUsuarioExternoResponse_V_1_3

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, usuario } }

## ConsultarDadosUsuarioResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, usuario } }

## ConsultarDadosUsuarioResponseV1_2

{ response: object { status, appVersion, messages, content } }

## ConsultarDataModPedido

{ response: object { status, message, messages, pedidos } }

## ConsultarDataModPedidoV14

{ response: object { status, message, messages, pedidos } }

## ConsultarEstAltProdutoResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, produto } }

## ConsultarEstAltProdutoResponse5

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, produto } }

## ConsultarEstAltProdutoResponseNovo

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, produto } }

## ConsultarEstProdutoDeprecatedResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, produto } }

## ConsultarEstProdutoResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, produto } }

## ConsultarEstProdutoResponse5

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, produto } }

## ConsultarEstProdutoResponseNova

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, produto } }

## ConsultarEstProdutoResponseV28

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, produto } }

## ConsultarEstoqueAlterado

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, produtos } }

## ConsultarEstoqueDisponivel

{ response: object { Status, Messages, produtos } }

## ConsultarEstoquesV10

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, estoques } }

## ConsultarExtratoPontosResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, Extrato } }

## ConsultarImagensProdResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, Produto } }

## ConsultarLimCredResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, message, messages, saldoLimite } }

## ConsultarMovimentosContabeisResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, movimentos } }

## ConsultarMovimentosGerenciaisRatResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, movimentos } }

## ConsultarMovimentosGerenciaisResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, movimentos } }

## ConsultarPlacasVeiculosClienteResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, veiculos } }

## ConsultarPlanoContabilResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, planoContas } }

## ConsultarPlanoContasResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, planoContas } }

## ConsultarPlanoContasResponseV1_0

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, planoContas } }

## ConsultarPreCadastroV_1_0

{ response: object { status, messages, preCadastro } }

## ConsultarPreCadastroV_1_1

{ response: object { status, messages, preCadastro } }

## ConsultarPreCadastrosV_1_0

{ response: object { status, messages, preCadastros } }

## ConsultarPreCadastrosV_1_1

{ response: object { status, messages, preCadastros } }

## ConsultarProdutoComEstoqueV28

{ response: object { Status, Messages, Produto } }

## ConsultarProdutoDeprecatedResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, produtos }; maxCod: number ex: 278475 }

## ConsultarProdutoDetalhadoV27

{ response: object { Status, Messages, Produto } }

## ConsultarProdutoDetalhadoV28

{ response: object { Status, Messages, Produto } }

## ConsultarProdutoDetalhadoV29

{ response: object { Status, Messages, Produto } }

## ConsultarProdutoDetalhadoV30

{ response: object { Status, Messages, Produto } }

## ConsultarProdutoDetalhadoV31

{ response: object { Status, Messages, Produto } }

## ConsultarProdutoDetalhadoV32

{ response: object { Status, Messages, Produto } }

## ConsultarProdutoEstoqueDetalhadoComEstoqueV27

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, Messages, produtos } }

## ConsultarProdutoEstoqueDetalhadoComEstoqueV28

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, Messages, produtos } }

## ConsultarProdutoEstoqueDetalhadoComEstoqueV29

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, Messages, produtos } }

## ConsultarProdutoEstoqueDetalhadoComEstoqueV30

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, Messages, produtos } }

## ConsultarProdutoEstoqueDetalhadoComEstoqueV31

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, Messages, produtos } }

## ConsultarProdutoEstoqueDetalhadoComEstoqueV32

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, Messages, produtos } }

## ConsultarProdutoEstoqueDetalhadoCustomReleaseV29

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas

{ response: object { status, messages, produtos } }

## ConsultarProdutoEstoqueDetalhadoCustomReleaseV30

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas

{ response: object { status, messages, produtos } }

## ConsultarProdutoEstoqueDetalhadoCustomReleaseV31

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas

{ response: object { status, messages, produtos } }

## ConsultarProdutoEstoqueDetalhadoCustomReleaseV32

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas

{ response: object { status, messages, produtos } }

## ConsultarProdutoEstoqueDetalhadoSemEstoqueV27

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas

{ response: object { status, messages, produtos } }

## ConsultarProdutoEstoqueDetalhadoSemEstoqueV28

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas

{ response: object { status, messages, produtos } }

## ConsultarProdutoEstoqueDetalhadoSemEstoqueV29

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas

{ response: object { status, messages, produtos } }

## ConsultarProdutoEstoqueDetalhadoSemEstoqueV30

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas

{ response: object { status, messages, produtos } }

## ConsultarProdutoEstoqueDetalhadoSemEstoqueV31

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas

{ response: object { status, messages, produtos } }

## ConsultarProdutoEstoqueDetalhadoSemEstoqueV32

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas

{ response: object { status, messages, produtos } }

## ConsultarProdutoEstoqueDetalhadoV1

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, produtos } }

## ConsultarProdutoExcluidosV10

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, excluidos } }

## ConsultarProdutoResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, produtos }; maxCod: number ex: 278475 }

## ConsultarProdutoResponseNovo

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, produtos }; maxCod: number ex: 278475 }

## ConsultarProdutoResponseV1

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, produto } }

## ConsultarProdutoResponseV27

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, produtos } }

## ConsultarProdutoResponseV28

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, produto } }

## ConsultarProdutoV19

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, produtos } }

## ConsultarProdutoV20

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, produtos } }

## ConsultarProdutoV28

{ response: object { Status, Messages, Produto } }

## ConsultarSaldoContasResponse

{ response: object { status, message, messages, saldo } }

## ConsultarStatusAltPVDResponse

Deve ser avaliado o atributo "status" que está contido no objeto "processamento". Possíveis valores:

Pendente:     Ainda não foi processado
Erro:         Ocorreu erro durante o processamento do pedido
Processando:  Ainda em processamento
Aguardando reprocessamento: quando um pedido teve alguma alteração e aguardo novo processamento do mesmo
Pedido Cancelado: Pedido Cancelado não pode ser alterado
Aguardando Cancelamento: Aguardando Cancelamento e removendo dependencia do pedido na base de dados

Pedido efetivado:
  Processado: Processamento concluído
  Pago:       Pagamento efetuado
  Baixado:    Pedido importado e faturado pelo EVL

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, processamento } }

## ConsultarStatusAltPVDResponseV13

Deve ser avaliado o atributo "status" que está contido no objeto "processamento". Possíveis valores:

Pendente:     Ainda não foi processado
Erro:         Ocorreu erro durante o processamento do pedido
Processando:  Ainda em processamento
Aguardando reprocessamento: quando um pedido teve alguma alteração e aguardo novo processamento do mesmo
Pedido Cancelado: Pedido Cancelado não pode ser alterado
Aguardando Cancelamento: Aguardando Cancelamento e removendo dependencia do pedido na base de dados

Pedido efetivado:
  Processado: Processamento concluído
  Pago:       Pagamento efetuado
  Baixado:    Pedido importado e faturado pelo EVL

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, processamento } }

## ConsultarStatusAltPVDResponseV15

Deve ser avaliado o atributo "status" que está contido no objeto "processamento". Possíveis valores:

Pendente:     Ainda não foi processado
Erro:         Ocorreu erro durante o processamento do pedido
Processando:  Ainda em processamento
Aguardando reprocessamento: quando um pedido teve alguma alteração e aguardo novo processamento do mesmo
Pedido Cancelado: Pedido Cancelado não pode ser alterado
Aguardando Cancelamento: Aguardando Cancelamento e removendo dependencia do pedido na base de dados

Pedido efetivado:
  Processado: Processamento concluído
  Pago:       Pagamento efetuado
  Baixado:    Pedido importado e faturado pelo EVL

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, processamento } }

## ConsultarStatusAltPVDResponseV16

Deve ser avaliado o atributo "status" que está contido no objeto "processamento". Possíveis valores:

Pendente:     Ainda não foi processado
Erro:         Ocorreu erro durante o processamento do pedido
Processando:  Ainda em processamento
Aguardando reprocessamento: quando um pedido teve alguma alteração e aguardo novo processamento do mesmo
Pedido Cancelado: Pedido Cancelado não pode ser alterado
Aguardando Cancelamento: Aguardando Cancelamento e removendo dependencia do pedido na base de dados

Pedido efetivado:
  Processado: Processamento concluído
  Pago:       Pagamento efetuado
  Baixado:    Pedido importado e faturado pelo EVL

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, processamento } }

## ConsultarStatusAltPVDResponseV18

Deve ser avaliado o atributo "status" que está contido no objeto "processamento". Possíveis valores:

Pendente:     Ainda não foi processado
Erro:         Ocorreu erro durante o processamento do pedido
Processando:  Ainda em processamento
Aguardando reprocessamento: quando um pedido teve alguma alteração e aguardo novo processamento do mesmo
Pedido Cancelado: Pedido Cancelado não pode ser alterado
Aguardando Cancelamento: Aguardando Cancelamento e removendo dependencia do pedido na base de dados

Pedido efetivado:
  Processado: Processamento concluído
  Pago:       Pagamento efetuado
  Baixado:    Pedido importado e faturado pelo EVL

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, processamento } }

## ConsultarStatusAltPVDResponsev2

Deve ser avaliado o atributo "status" que está contido no objeto "processamento". Possíveis valores:

Pendente:     Ainda não foi processado
Erro:         Ocorreu erro durante o processamento do pedido
Processando:  Ainda em processamento
Aguardando reprocessamento: quando um pedido teve alguma alteração e aguardo novo processamento do mesmo
Pedido Cancelado: Pedido Cancelado não pode ser alterado
Aguardando Cancelamento: Aguardando Cancelamento e removendo dependencia do pedido na base de dados

Pedido efetivado:
  Processado: Processamento concluído
  Pago:       Pagamento efetuado
  Baixado:    Pedido importado e faturado pelo EVL

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, processamento } }

## ConsultarStatusDataModPedidoV15

{ response: object { status, messages, pedidos } }

## ConsultarStatusDataModPedidoV18

{ response: object { status, messages, pedidos } }

## ConsultarVendasClienteResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, vendas } }

## ContrapartidaFDE

Contrapartida/lançamento contábil de um documento FDE

{ conta: integer ex: 300023; unidade: string ex: "001"; valor: number(double) ex: 15.0; valorMoeda: number(double) ex: 0.0; dc: string ex: "C"; historico: string ex: "1002"; complemento: string ex: "Complemento do Hist"; numeroDcto: string ex: "929292"; especie: string ex: "1002"; cCustos: array de `CCustoFDE` (ver reference/schemas.md); subContas: array de `SubContaFDE` (ver reference/schemas.md) }

## ControleEntregaPendentesV1_0

{ Entregador: string ex: "123"; bairro: string ex: "Centro"; cliente: integer ex: 1050; cupom: string ex: "12543"; data: string(date-time) ex: "2026-03-24T10:30:00"; pdv: string ex: "003"; transacao: string ex: "00127691685"; valor: number(double) ex: 250.0 }

## ControleEntregaResponseSemMessage

{ response: object { status, messages, transacao } }

## ControleEntregaV11

{ transacao: number(integer) ex: "00148762883"; status: number(integer) ex: "PENDENTE"; statusOperacional: string(string) ex: "NORMAL, PENDENTE ou CANCELADO"; data: number(integer) ex: "24/06/2020"; dataVenda: number(integer) ex: "14/09/2019"; codEntregador: number(integer) ex: "002"; unidade: number(integer) ex: "001"; cliente: number(integer) ex: 103055; bairro: number(integer) ex: "Centro"; cidade: number(integer) ex: "São Bernardo"; endereco: number(integer) ex: "Rua Izaac Ferreira Da Cruz, 1238"; complemento: number(integer) ex: ""; nome: number(integer) ex: "Kelen Cristiane Merlin"; fone: number(integer) ex: ""; valor: number(integer) ex: 510.58; pdv: number(integer) ex: "011"; volumes: number(integer) ex: 33; cupom: number(integer) ex: "21564"; observacao1: number(integer) ex: "observacao1"; observacao2: number(integer) ex: "observacao2"; hora: number(integer) ex: "15:30:54"; referencia: number(integer) ex: "Próximo a Pm"; numeroCaixas: number(integer) ex: "56"; dataBaixa: string(string) ex: "25/06/2020"; enderecoNumero: number(integer) ex: 618; enderecoCep: string(string) ex: "83400330"; veiculo: number(integer) ex: 1; kmInicio: number(integer) ex: 2300; kmFim: number(integer) ex: 2340; idNfe: string(string) ex: "" }

## ControleEntregaV12

{ transacao: number(integer) ex: "00148762883"; status: number(integer) ex: "PENDENTE"; statusOperacional: string(string) ex: "NORMAL, PENDENTE ou CANCELADO"; data: number(integer) ex: "24/06/2020"; dataVenda: number(integer) ex: "14/09/2019"; codEntregador: number(integer) ex: "002"; unidade: number(integer) ex: "001"; cliente: number(integer) ex: 103055; bairro: number(integer) ex: "Centro"; cidade: number(integer) ex: "São Bernardo"; endereco: number(integer) ex: "Rua Izaac Ferreira Da Cruz, 1238"; complemento: number(integer) ex: ""; nome: number(integer) ex: "Kelen Cristiane Merlin"; fone: number(integer) ex: ""; valor: number(integer) ex: 510.58; pdv: number(integer) ex: "011"; volumes: number(integer) ex: 33; cupom: number(integer) ex: "21564"; observacao1: number(integer) ex: "observacao1"; observacao2: number(integer) ex: "observacao2"; hora: number(integer) ex: "15:30:54"; referencia: number(integer) ex: "Próximo a Pm"; numeroCaixas: number(integer) ex: "56"; dataBaixa: string(string) ex: "25/06/2020"; enderecoNumero: number(integer) ex: 618; enderecoCep: string(string) ex: "83400330"; veiculo: number(integer) ex: 1; kmInicio: number(integer) ex: 2300; kmFim: number(integer) ex: 2340; idNfe: string(string) ex: ""; horaVenda: string(hh:mm:ss) ex: "23:59:59" }

## ControleEntregaV13

{ transacao: number(integer) ex: "00148762883"; status: number(integer) ex: "PENDENTE"; statusOperacional: string(string) ex: "NORMAL, PENDENTE ou CANCELADO"; data: number(integer) ex: "24/06/2020"; dataVenda: number(integer) ex: "14/09/2019"; codEntregador: number(integer) ex: "002"; unidade: number(integer) ex: "001"; cliente: number(integer) ex: 103055; bairro: number(integer) ex: "Centro"; cidade: number(integer) ex: "São Bernardo"; endereco: number(integer) ex: "Rua Izaac Ferreira Da Cruz, 1238"; complemento: number(integer) ex: ""; nome: number(integer) ex: "Kelen Cristiane Merlin"; fone: number(integer) ex: ""; valor: number(integer) ex: 510.58; pdv: number(integer) ex: "011"; volumes: number(integer) ex: 33; cupom: number(integer) ex: "21564"; observacao1: number(integer) ex: "observacao1"; observacao2: number(integer) ex: "observacao2"; hora: number(integer) ex: "15:30:54"; referencia: number(integer) ex: "Próximo a Pm"; numeroCaixas: number(integer) ex: "56"; dataBaixa: string(string) ex: "25/06/2020"; enderecoNumero: number(integer) ex: 618; enderecoCep: string(string) ex: "83400330"; veiculo: number(integer) ex: 1; kmInicio: number(integer) ex: 2300; kmFim: number(integer) ex: 2340; idNfe: string(string) ex: ""; horaVenda: string(hh:mm:ss) ex: "23:59:59"; codigoAgenda: number ex: 10; valorCupom: number ex: 10 }

## DadoEnvioStatus

{ status: string ex: "Em Separação" }

## DadosBaixa

{ transacao: string ex: "00024354654654"; notaFiscal: string ex: ""; sequencial: number ex: 0; data: string ex: "20/04/2017"; quantidadeUnitaria: number(double) ex: 2; quantidadeEmbalagem: number ex: 2; valor: number(double) ex: 2; ipi: number(double) ex: 0; desconto: number(double) ex: 0; valorSubTrib: number(double) ex: 0; acrescimoFinanceiro: number(double) ex: 0; despesaAcessoria: number(double) ex: 0 }

## DadosBaixaV14

{ transacao: string ex: "00024354654654"; notaFiscal: string ex: ""; sequencial: number ex: 0; data: string ex: "20/04/2017"; quantidadeUnitaria: number(double) ex: 2; quantidadeEmbalagem: number ex: 2; valor: number(double) ex: 2; ipi: number(double) ex: 0; desconto: number(double) ex: 0; bonificacao: number(double) ex: 0; valorSubTrib: number(double) ex: 0; acrescimoFinanceiro: number(double) ex: 0; despesaAcessoria: number(double) ex: 0; devolver: string ex: "N"; quantidadeDevolver: number(double) ex: 0; distribuicao: string ex: ""; idNfe: string ex: "41190100000000000000550010000002331105508640" }

## DeleteGrupoResponse

{ response: object { status, messages } }

## DeleteGrupoResponseV1_1

{ response: object { status, appVersion, messages, content } }

## DeleteMessagesRespost

{ message: string ex: "Grupo deletado com sucesso" }

## Departamento

array de { codigo: string(string) ex: "999"; descricao: string(string) ex: "Geral" }

## DesativarUsuarioResponse

{ status: string ex: "ok"; appVersion: string ex: "4.0.0.165"; messages: array de object { message }; content: string ex: "Usuário desativado com sucesso" }

## Documento

{ codigo: string(string) ex: "7100"; descricao: string(string) ex: "Entrada de Mercadorias"; config: string(string) ex: "S"; catentidade: string(string) ex: "F"; datacontabil: string(string) ex: "A"; pger_conta: number(integer) ex: 0; debito: string(string) ex: "113201"; credito: string(string) ex: "211102"; hist_codigo: string(string) ex: "7712"; impr_codigo: string(string) ex: "102"; natfiscalest: string(string) ex: ""; natfiscalint: string(string) ex: ""; natfiscalext: string(string) ex: ""; natfiscalst: string(string) ex: ""; natfiscalstint: string(string) ex: ""; seriesdcto: string(string) ex: "1"; especiesdcto: string(string) ex: "NF;NFE"; modelosdcto: string(string) ex: "1;55"; simbologiasicms: string(string) ex: "07;12;17;18;19;25;DI;IS;OT;ST"; simbologiasipi: string(string) ex: ""; simbologiasiss: string(string) ex: ""; reducbcicms: string(string) ex: "N"; espe_codigoi: string(string) ex: "5205"; espe_codigof: string(string) ex: "5210"; entsai: string(string) ex: "E"; avpz: string(string) ex: ""; impostosvalidos: string(string) ex: "C;S"; unorigem: string(string) ex: "001"; undestino: string(string) ex: "002"; tfmesmaun: string(string) ex: "N"; utilizadecendio: string(string) ex: "N"; solicentorigem: string(string) ex: "N"; mesmaentidade: string(string) ex: "N"; geral: string(string) ex: ""; moed_codigo: string(string) ex: ""; multiplaspf: string(string) ex: "N"; estsaida: string(string) ex: "0"; estentrada: string(string) ex: "1"; totais: string(string) ex: "C;S;P;G;F;A;D;M;B;H;T;E"; edicaoprodutos: string(string) ex: "C;R;P;D;M;B;U;Q;V;T"; critica: string(string) ex: "5"; transportador: string(string) ex: "N"; vendedor: string(string) ex: "N"; numerodcto: string(string) ex: "N"; nfprodutor: string(string) ex: "N"; funrural: number(double) ex: 0; perccomissao: number(double) ex: 0; ctasabatfin: string(string) ex: ""; ctasacresfin: string(string) ex: ""; codigosbaixar: string(string) ex: "200;300;500"; codigosbaixarautom: string(string) ex: "201"; atcustos: string(string) ex: "P;C;E;T;F;M;O;Q;R;S;U;2;3;5;9"; valorassociado: string(string) ex: "N"; validaestoque: string(string) ex: "N"; calculacomissao: string(string) ex: "N"; debfunrural: number(integer) ex: 0; crefunrural: number(integer) ex: 0; gerarpendest: string(string) ex: ""; unidpendest: string(string) ex: ""; entpendest: string(string) ex: "M"; tpbxpendest: string(string) ex: "Q"; mvtodecomposicao: string(string) ex: "N"; imprimir: string(string) ex: "1"; formato: string(string) ex: ""; copias: number(integer) ex: 0; edtimpresso: string(string) ex: "N"; inicializar: string(string) ex: "N"; unpedido: string(string) ex: "001;002;003"; utilizafpgto: string(string) ex: "S"; fpgtovalidas: string(string) ex: "000;001;002;003;004;005;006;007;008;009;010"; faquisvalidas: string(string) ex: ""; utilizaarredbonif: string(string) ex: ""; codigospendavisar: string(string) ex: ""; codigospedint: string(string) ex: ""; obsbase: string ex: ""; mensagem: string(string) ex: ""; qtdesunit: string(string) ex: ""; unidpedint: string(string) ex: ""; unidsugestao: string(string) ex: ""; inicpreco: string(string) ex: "P"; iniccondicoes: string(string) ex: "N"; atualizatabforn: string(string) ex: "S"; formatopreped: string(string) ex: ""; formatoreceb: string(string) ex: ""; baixacompleta: string(string) ex: "S"; atrasomaximo: number(integer) ex: 0; ajustardistrib: string(string) ex: "N"; informast: string(string) ex: ""; validabaixa: string(string) ex: ""; codpenddistrib: string(string) ex: ""; tipobonif: string(string) ex: ""; dptospedido: string(string) ex: ""; rotaentrega: string(string) ex: ""; desconto: string(string) ex: "N"; despac: string(string) ex: "N"; frete: string(string) ex: "N"; editavalor: string(string) ex: "N"; edtsimbicms: string(string) ex: "N"; consprodutos: string(string) ex: "S"; formvalor: string(string) ex: "U"; calcsubtrib: string(string) ex: "S"; exigependest: string(string) ex: "N"; exppdvs: string(string) ex: ""; percadicional: number(double) ex: 0; exigirpedcompra: string(string) ex: "N"; validarprod: string(string) ex: "1"; listarpend: string(string) ex: ""; guiacega: string(string) ex: ""; geraremail: string(string) ex: ""; redcustos: string(string) ex: "8888"; dptodebitado: string(string) ex: ""; espe_codigoip: string(string) ex: ""; espe_codigofp: string(string) ex: ""; dptosvalidos: string(string) ex: "046;065;076"; dptosinvalidos: string(string) ex: "004;005"; gruposvalidos: string(string) ex: ""; gruposinvalidos: string(string) ex: ""; debdifbxped: number(integer) ex: 0; creddifbxped: number(integer) ex: 0; histdifbxped: string(string) ex: ""; baixapfvinc: string(string) ex: ""; comportamento: string(string) ex: "LN"; ocbens: string(string) ex: ""; ocbensoutras: string(string) ex: ""; ocbensicms: string(string) ex: ""; cpocabecalho: string(string) ex: ""; gercon: string(string) ex: ""; contabgerencial: string(string) ex: ""; bcutilizada: string(string) ex: ""; simplesremessa: string(string) ex: ""; funcao: string(string) ex: ""; intervalo: string(string) ex: ""; ctadebvlorig: string(string) ex: ""; ctacredvlorig: string(string) ex: ""; ctadebdep: string(string) ex: ""; ctacreddep: string(string) ex: ""; ctadebval: string(string) ex: ""; ctacredval: string(string) ex: ""; usualt: number(integer) ex: 0; dtalt: string(date) ex: "2018-10-11"; horaalt: string(string) ex: 54077; usuaud: number(integer) ex: 0; dtaud: string(date) ex: "2018-10-11"; horaaud: string(string) ex: 54618; setoresvalidos: string(string) ex: "00200;00600"; setoresinvalidos: string(string) ex: ""; tpdesp: string(string) ex: ""; prod_codigo: number(integer) ex: 0; tipoligacao: string(string) ex: ""; grupotensao: string(string) ex: ""; tipoassinante: string(string) ex: ""; classeconsumo: string(string) ex: ""; ajuste_codigo: string(string) ex: ""; i101: number(integer) ex: 0; i102: number(integer) ex: 0; i103: number(integer) ex: 0; i104: number(integer) ex: 0; i105: number(integer) ex: 0; i106: number(integer) ex: 0; i107: number(integer) ex: 0; i108: number(integer) ex: 0; i109: number(integer) ex: 0; i110: number(integer) ex: 0; i111: number(integer) ex: 0; i112: number(integer) ex: 0; i113: number(integer) ex: 0; i114: number(integer) ex: 0; i115: number(integer) ex: 0; i116: number(integer) ex: 0; i117: number(integer) ex: 0; i118: number(integer) ex: 0; i119: number(integer) ex: 0; i120: number(integer) ex: 0; i121: number(integer) ex: 0; i122: number(integer) ex: 0; i123: number(integer) ex: 0; i124: number(integer) ex: 0; i125: number(integer) ex: 0; i126: number(integer) ex: 0; i127: number(integer) ex: 0; i128: number(integer) ex: 0; i129: number(integer) ex: 0; i130: number(integer) ex: 0; f101: number(double) ex: 0; f102: number(double) ex: 0; f103: number(double) ex: 0; f104: number(double) ex: 0; f105: number(double) ex: 0; f106: number(double) ex: 0; f107: number(double) ex: 0; f108: number(double) ex: 0; f109: number(double) ex: 0; f110: number(double) ex: 0; f111: number(double) ex: 0; f112: number(double) ex: 0; f113: number(double) ex: 0; f114: number(double) ex: 0; f115: number(double) ex: 0; f116: number(double) ex: 0; f117: number(double) ex: 0; f118: number(double) ex: 0; f119: number(double) ex: 0; f120: number(double) ex: 0; c101: string(string) ex: ""; c102: string(string) ex: ""; c103: string(string) ex: ""; c104: string(string) ex: ""; c105: string(string) ex: ""; c106: string(string) ex: ""; c107: string(string) ex: ""; c108: string(string) ex: ""; c109: string(string) ex: ""; c110: string(string) ex: ""; c111: string(string) ex: ""; c112: string(string) ex: ""; c113: string(string) ex: ""; c114: string(string) ex: ""; c115: string(string) ex: ""; c116: string(string) ex: ""; c117: string(string) ex: ""; c118: string(string) ex: ""; c119: string(string) ex: ""; c120: string(string) ex: ""; c201: string(string) ex: ""; c202: string(string) ex: ""; c203: string(string) ex: ""; c204: string(string) ex: ""; c205: string(string) ex: ""; c206: string(string) ex: ""; c207: string(string) ex: ""; c208: string(string) ex: ""; c209: string(string) ex: ""; c210: string(string) ex: ""; c211: string(string) ex: ""; c212: string(string) ex: ""; c213: string(string) ex: ""; c214: string(string) ex: ""; c215: string(string) ex: ""; c216: string(string) ex: ""; c217: string(string) ex: ""; c218: string(string) ex: ""; c219: string(string) ex: ""; c220: string(string) ex: ""; c301: string(string) ex: ""; c302: string(string) ex: ""; c303: string(string) ex: ""; c304: string(string) ex: ""; c305: string(string) ex: ""; c306: string(string) ex: ""; c307: string(string) ex: ""; c308: string(string) ex: ""; c309: string(string) ex: ""; c310: string(string) ex: ""; c311: string(string) ex: ""; c312: string(string) ex: ""; c313: string(string) ex: ""; c314: string(string) ex: ""; c315: string(string) ex: ""; c316: string(string) ex: ""; c317: string(string) ex: ""; c318: string(string) ex: ""; c319: string(string) ex: ""; c320: string(string) ex: ""; usuarios: string(text) ex: ""; usuaudit: string(text) ex: ""; ativo: string(string) ex: "S"; gilrat: number(double) ex: 0; senar: number(double) ex: 0; debgilrat: string(string) ex: ""; cregilrat: string(string) ex: ""; debsenar: string(string) ex: ""; cresenar: string(string) ex: "" }

## DocumentoConfigCCV_Definicao_V_4_0

Condição da regra. As condições formam uma árvore: as filhas ficam em SubRegras, e a Classificacao indica a posição (1.01 > 1.01.01 > 1.01.01.01).
O ERP percorre cada nível na ordem da Classificacao e para na primeira condição atendida que tenha Percentual maior que zero, que define a comissão da regra.
Se a condição atendida tiver Percentual zero, a avaliação desce para as suas SubRegras; se não for atendida, segue para a condição seguinte do mesmo nível.

{ Classificacao: string ex: "1.01"; Variavel: string ex: "PD"; TipoAvaliacao: string [I, D, A, O, E, U, C, N, P, R]; Valor: string ex: "30,000"; Percentual: number ex: 5.0; SubRegras: array de `DocumentoConfigCCV_Definicao_V_4_0` (ver reference/schemas.md) }

## DocumentoConfigCCV_Pontos_V_4_0

Tabelas de pontos (aba Pontos), usadas pelas políticas com FormaRemuneracao T

{ Tabelas: array de object { Codigo, Descricao, Faixas } }

## DocumentoConfigCCV_Regras_V_4_0

Políticas de comissão (aba Regras)

{ Conjuntos: array de object { Codigo, Descricao, DataIni, DataFim, FormaRemuneracao, Frequencia, DiaApuracao, TabPontos, Regras } }

## DocumentoConfigCCV_V_4_0

{ codigo: string ex: "6500"; descricao: string ex: "Comissão Vendedores"; tipoApuracao: string; regras: `DocumentoConfigCCV_Regras_V_4_0` (ver reference/schemas.md); pontos: `DocumentoConfigCCV_Pontos_V_4_0` (ver reference/schemas.md) }

## DocumentoFDE

Objeto que representa um Documento FDE (Fiscal Data Entry) com todas as informações do documento fiscal, itens, impostos e contrapartidas.

{ unidade: string ex: "001"; dataMvto: string ex: "02/01/2022"; dataEmissao: string ex: "02/01/2022"; codigoDocumento: string ex: "1002"; modeloDcto: string ex: "55"; serieDcto: string ex: "1"; numeroDcto: string ex: "1064"; especie: string ex: "NFE"; totalDcto: number(double) ex: 150.0; chaveDfe: string ex: "12345678901234567890123456789012345678901244"; catEntidade: string ex: "F"; codEntidade: string ex: "100006"; observacao: string ex: "Compra de uniformes"; indFrete: string ex: "9"; icmsBc: number(double) ex: 150; icmsValor: number(double) ex: 18.0; icmsStBc: number(double) ex: 0; icmsStValor: number(double) ex: 0; pisBc: number(double) ex: 0; pisValor: number(double) ex: 0; cofinsBc: number(double) ex: 0; cofinsValor: number(double) ex: 0; issValor: number(double) ex: 0; itens: array de `ItemFDE` (ver reference/schemas.md); pendencias: array de `PendenciaFDE` (ver reference/schemas.md); contrapartidas: array de `ContrapartidaFDE` (ver reference/schemas.md); refDctos: array de `RefDocumentoFDE` (ver reference/schemas.md); infAdicFrete: array de `InfoAdicFreteFDE` (ver reference/schemas.md) }

## DocumentoFdeRequest

{ response: object { status, messages, content } }

## EditProdutoV_1_0

{ descricao: string(string) ex: "Apres Aurora Peperi Kg modificado"; complemento: string(string) ex: "String"; marca: string(string) ex: "String"; classe: string(string) ex: "String"; tipo: string(string) ex: "String"; descrPdvs: string(string) ex: "String"; peso: number ex: 0; pesoLiq: number ex: 0; emb: string(string) ex: "String"; qemb: number ex: 0; extra1: string(string) ex: "String"; extra2: string(string) ex: "String"; extra3: string(string) ex: "String"; extra4: number ex: 0; extra5: string(string); extra6: string(string) ex: "String"; extra7: string(string) ex: "String"; extra8: number ex: 0; extra9: number ex: 0; altura: number ex: 0; largura: number ex: 0; profundidade: number ex: 0; lastro: number ex: 0; camadas: number ex: 0; descritivo: string(string) ex: "String"; codCaixa: string(string) ex: "String"; display: number ex: 0; descricaoCliente: string(string) ex: "String"; codigoNCM: string(string) ex: "String"; classFiscal: string(string) ex: "String"; temperatura: number ex: 0; varPeso: number ex: 0 }

## EditProdutoV_1_1

**EditProdutoV_1_0** = object { descricao, complemento, marca, classe, tipo, descrPdvs, peso, pesoLiq, emb, qemb, extra1, extra2, extra3, extra4, extra5, extra6, extra7, extra8, extra9, altura, largura, profundidade, lastro, camadas, descritivo, codCaixa, display, descricaoCliente, codigoNCM, classFiscal, temperatura, varPeso } & **CamposExtras_10_ao_99** = object { extra10, extra11, extra12, extra13, extra14, extra15, extra16, extra17, extra18, extra19, extra20, extra21, extra22, extra23, extra24, extra25, extra26, extra27, extra28, extra29, extra30, extra31, extra32, extra33, extra34, extra35, extra36, extra37, extra38, extra39, extra40, extra41, extra42, extra43, extra44, extra45, extra46, extra47, extra48, extra49, extra50, extra51, extra52, extra53, extra54, extra55, extra56, extra57, extra58, extra59, extra60, extra61, extra62, extra63, extra64, extra65, extra66, extra67, extra68, extra69, extra70, extra71, extra72, extra73, extra74, extra75, extra76, extra77, extra78, extra79, extra80, extra81, extra82, extra83, extra84, extra85, extra86, extra87, extra88, extra89, extra90, extra91, extra92, extra93, extra94, extra95, extra96, extra97, extra98, extra99, eraseExtras }

## EditarEntrega

{ transacao: string(string) ex: "00127694579"; bairro: string(string) ex: "Centro Cívico"; cidade: string(string) ex: "Curitiba"; observacao1: string(string) ex: "Cliente alterou o endereço de entrega."; fone: string(string) ex: "(41) 99999-8888"; valor: number(double) ex: 153.75; kmFim: integer(integer) ex: 54321; veiculo: integer(integer) ex: 10 }

## EditarEntregaRequestV_1

{ transacao: string ex: "00148762883"; bairro: string ex: "Centro Atualizado"; volumes: integer ex: 12; observacao1: string ex: "Atualização solicitada"; hora: string ex: "17:00:00"; numeroCaixas: string ex: "9"; cupom: string ex: "123456"; pdv: string ex: "005"; valor: number ex: 987.65; veiculo: integer ex: 2 }

## EditarEntregasV_1_0

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages".
O campo "controleEntrega" traz os dados atualizados após a edição.

{ response: object { status, messages, message } }

## EditarPedido

{ unidade: string(string) ex: "001"; data: string(string) ex: "01/01/2018"; codigoCliente: integer ex: 1; formaPagamento: string(string) ex: "001"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "Observações"; desconto: number(double) ex: 0; especie: integer ex: 1; itens: `ItensPedido` (ver reference/schemas.md) }

## EditarPedidoDeprecated0

{ data: string(string) ex: "01/01/2018"; codigoCliente: integer ex: 1; formaPagamento: string(string) ex: "001"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "Observações"; especie: integer ex: 1; itens: `ItensPedido` (ver reference/schemas.md) }

## EditarPedidoDeprecated1

{ data: string(string) ex: "01/01/2018"; codigoCliente: integer ex: 1; formaPagamento: string(string) ex: "001"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "Observações"; desconto: number(double) ex: 0; especie: integer ex: 1; itens: `ItensPedido` (ver reference/schemas.md) }

## EfetivCadProduto

{ descricao: string ex: "Garr Term Aladdin Mesa Rosca 1l"; complemento: string ex: ""; grupCodigo: string ex: 10715; grupNome: string ex: "Utensilio Para Café"; dptoCodigo: string ex: 998; tribCodigo: string ex: 96170010; marca: string ex: "Aladdin"; classe: string ex: "REVENDA"; tipo: string ex: ""; funcao: string ex: ""; codestoque: number ex: 0; fatorestoque: number ex: 0; codpreco: number ex: 0; codbarras: string ex: 7891108039916; descrpdvs: string ex: "Garr Term Aladdin Me"; peso: number ex: 0; pesoliq: number ex: 0; emb: string ex: "UN"; qemb: number ex: 1; pzrepos: number ex: 0; pzentrega: number ex: 0; diasseg: number ex: 0; vslhCodigo: string ex: ""; balanca: string ex: "N"; contrest: string ex: "S"; datacad: string ex: "05/05/2005"; usucad: number ex: 0; dataalt: string ex: "03/06/2024"; usualt: number ex: 9972; extra1: string ex: "N"; extra2: string ex: ""; extra3: string ex: "S"; extra4: number ex: 0; extra5: number ex: 0; extra6: string ex: 238; extra7: string ex: "N"; extra8: number ex: 0; extra9: number ex: 0; altura: number ex: 0; largura: number ex: 0; profundidade: number ex: 0; lastro: number ex: 0; camadas: number ex: 0; fatoremb: number ex: 1; faquisicao: string ex: ""; status: string ex: "N"; dataexcl: string ex: "30/12/1999"; usuexcl: number ex: 0; gardCodigo: string ex: ""; descritivo: string ex: ""; codcaixa: string ex: ""; display: number ex: 0; tptrocas: string ex: ""; grpreco: string ex: ""; descricaocliente: string ex: ""; ativounidades: string ex: "001;002;003;004;005;006;007;100;101;"; bloqueadounidades: string ex: "001;"; codigoncm: string ex: 96170010; classfiscal: string ex: ""; fornCodigo: number ex: 0; codigoex: string ex: ""; pesomaximo: number ex: 0; volumemaximo: number ex: 0; temperatura: number ex: 0; compCodigo: string ex: 309; valminima: number ex: 0; sensCodigo: number ex: 0; varpeso: number ex: 0; centralcodigo: number ex: 0; centraldescricao: string ex: ""; sazoCodigo: string ex: ""; simiCodigo: string ex: ""; codcompra: number ex: 0; descricaoecomm: string ex: ""; complementoecomm: string ex: ""; marcaecomm: string ex: ""; dthrmanutencao: string ex: "10/06/2024 11:00:00"; dthrintegracao: string ex: "13/06/2024 15:47:33"; carpCodigo: string ex: ""; origemcad: string ex: ""; ecommid: number ex: 0; datarecupexcl: string ex: "10/06/2024"; release: number ex: 51268 }

## EfetivCadProdutoRes

{ codigo: integer ex: 94; cadTipo: string ex: "PROD"; cadCodigo: string ex: "979784"; etapaAprov: string ex: "1"; status: string ex: "P"; release: integer; eventos: array de object; produto: `EfetivCadProdutoResumo` (ver reference/schemas.md) }

## EfetivCadProdutoResumo

{ codigo: integer ex: 979784; descricao: string ex: "Agenda Corporativa Premium Verde 2027"; grupNome: string ex: "Produtos Sem Departamento"; dptoCodigo: string ex: "302"; marca: string ex: "Xxxx"; codPreco: integer; codBarras: string ex: "7899876543217"; peso: number; pesoLiq: number; dataCad: string; usuCad: integer; usuAlt: integer; status: string ex: "P"; dataExcl: string; usuExcl: integer; descritivo: string; ativoUnidades: string ex: "001;002;003;004;010;011;201"; bloqueadoUnidades: string ex: "001;002;003;004;010;011;201"; departamento: string; release: integer }

## EfetivCadPromotor

{ nome: string(string) ex: "José da Silva"; obs: string(string) ex: "obs teste"; fone: string(string) ex: "425435843"; email: string(string) ex: "afg@af.cdas"; dtvenccad: string(string) ex: "01/01/2026"; supervisornome: string(string) ex: "matheus"; supervisorfone: string(string) ex: "1241515"; supervisoremail: string(string) ex: "asfg@aiksgfhi.sdgs"; cpf: string(string) ex: "544352143"; fonecel: string(string) ex: "5136513"; supervisorfonecel: string(string) ex: ""; contatoalt: string(string) ex: ""; supervisorcontatoalt: string(string) ex: ""; ufexprg: string(string) ex: "pr"; rg: string(string) ex: "1453132132"; dtnasc: string(string) ex: "01/01/2000"; fornecedores: array de any }

## EfetivCadPromotorConsultaContentRes

**ResponsePadrao** = object { status, appVersion, messages } & { content: array de `EfetivCadPromotorConsultaRes` (ver reference/schemas.md) }

## EfetivCadPromotorConsultaRes

{ codigo: number ex: 7; cadTipo: string(string) ex: "PROMO"; cadCodigo: string(string) ex: "10005"; etapaAprov: string(string) ex: "1"; status: string(string) ex: "P"; release: number ex: 5; eventos: array de object { codigo, efcd_codigo, dataHora, usua_codigo, eventoCodigo, complemento, origem }; cadastro: `PromotorEfetivCadastro` (ver reference/schemas.md) }

## EfetivCadPromotorRes

**ResponsePadrao** = object { status, appVersion, messages } & { content: number ex: 12 }

## Endereco

{ cep: string ex: "86070000"; logradouro: string ex: "Av Brasilia, Nº 1058"; numero: string ex: "21"; bairro: string ex: "Jd Do Sol"; complemento: string ex: ""; cidade: integer ex: 4565 }

## EnderecoClienteV1

{ uf: string(string) ex: "PR"; cep: string(string) ex: "2654654"; cidade: integer ex: 5; endereco: string(string) ex: "Rua 2"; bairro: string(string) ex: ""; numero: string(string) ex: ""; complemento: string(string) ex: "" }

## EnderecoCom

{ endereco: string ex: "Rua teste"; numero: string ex: "1"; complemento: string ex: ""; bairro: string ex: "Teste"; cidade: string ex: ""; uf: string ex: "PR"; cep: string ex: ""; fone: string ex: ""; foneCel: string ex: "" }

## EnderecoRes

{ endereco: string ex: "Rua teste"; numero: string ex: "1"; complemento: string ex: ""; bairro: string ex: "Teste"; cidade: string ex: ""; uf: string ex: "PR"; cep: string ex: ""; fone: string ex: "" }

## Entregas

Retorna uma lista de entregas. Caso status seja diferente de "ok", verificar mensagens de erro.

{ transacao: string(string) ex: "00127694447"; status: string(string) ex: "B"; statusOperacional: string(string) ex: "BAIXADO"; numeroEndereco: integer(integer) ex: 3; cepsCodigo: string(string) ex: "29158-142"; veiECodigo: integer(integer) ex: 4; kmInicio: integer(integer) ex: 33425; kmFim: integer(integer) ex: 44525; xmlIdNfe: string(string) ex: "41180212913720000127570130000003261000003260"; data: string(string) ex: "26/05/2025"; dataVenda: string(string) ex: "26/05/2025"; entradaCodigo: string(string) ex: "001"; unidadeCodigo: string(string) ex: "001"; clienteCodigo: integer(integer) ex: 100005; bairro: string(string) ex: "Centro Cívico"; cidade: string(string) ex: "Curitiba"; endereco: string(string) ex: "Rua Gustavo Barroso, 80"; complementoEndereco: string(string) ex: "Cond Lucilio De Held Apto 901"; nome: string(string) ex: "Sergio Yoshimi Obara"; fone: string(string) ex: "(41) 99999-8888"; valor: number(double) ex: 153.75; valorCupom: number(double) ex: 0.0; impresso: integer(integer) ex: 5; pdvCodigo: string(string) ex: "012"; volumes: integer(integer) ex: 5; cupom: string(string) ex: "4432"; observacao1: string(string) ex: "Cliente alterou o endereço de entrega."; observacao2: string(string) ex: "Entrega realizada com sucesso"; hora: string(string) ex: "09:41:03"; pontoReferencia: string(string) ex: "Prédio Espelhado"; numeroDasCaixas: string(string) ex: "12"; dataBaixa: string(string) ex: "26/05/2025"; usuarioLancamento: integer(integer) ex: 9999; horaVenda: string(string) ex: "15:32:53"; codigo: string(string) ex: "112" }

## EntregasV_1_0

{ transacao: string ex: "00148762883"; status: string ex: "PENDENTE"; statusOperacional: string ex: "NORMAL, PENDENTE ou CANCELADO"; data: string ex: "24/06/2020"; dataVenda: string ex: "14/09/2019"; codEntregador: string ex: "002"; unidade: string ex: "001"; cliente: integer ex: 103055; bairro: string ex: "Centro"; cidade: string ex: "São Bernardo"; endereco: string ex: "Rua Izaac Ferreira Da Cruz, 1238"; complemento: string ex: ""; nome: string ex: "Kelen Cristiane Merlin"; fone: string ex: ""; valor: number ex: 510.58; pdv: string ex: "011"; volumes: integer ex: 33; cupom: string ex: "21564"; observacao1: string ex: "observacao1"; observacao2: string ex: "observacao2"; hora: string ex: "15:30:54"; referencia: string ex: "Próximo a Pm"; numeroCaixas: string ex: "56"; dataBaixa: string ex: "25/06/2020"; enderecoNumero: integer ex: 618; enderecoCep: string ex: "83400330"; veiculo: integer ex: 1; kmInicio: integer ex: 2300; kmFim: integer ex: 2340; idNfe: string ex: ""; horaVenda: string(hh:mm:ss) ex: "23:59:59" }

## EnviarDadosEditCliente

{ nome: string(string) ex: "Paulo Silva"; sexo: string(string) ex: "M"; tipo: string(string) ex: "F"; fone: string(string) ex: "5154654"; uf: string(string) ex: "PR"; cep: string(string) ex: "2654654"; cidade: string(string) ex: "Curitiba"; endereco: string(string) ex: "Rua 2"; bairro: string(string) ex: ""; cpf: string(string) ex: "20116794003"; rg: string(string) ex: "5654654"; email: string(string) ex: "email@email.com.br" }

## EnviarDadosFinanceiroPost_V_1_1

{ financeiro: `Financeiro_V_1_1` (ver reference/schemas.md) }

## EnviarDadosNovoCliente

{ nome: string(string) ex: "Paulo Silva"; sexo: string(string) ex: "M"; tipo: string(string) ex: "F"; tipoCliente: string(string) ex: ""; fone: string(string) ex: "5154654"; celular: string(string) ex: "956465853"; foneComercial: string(string) ex: "45465468"; uf: string(string) ex: "PR"; cep: string(string) ex: "2654654"; cidade: number(integer) ex: 5; endereco: string(string) ex: "Rua 2"; bairro: string(string) ex: ""; numero: string(string) ex: ""; complemento: string(string) ex: ""; dataNascimento: string(string) ex: "25/08/1984"; cpf: string(string) ex: "62976"; rg: string(string) ex: "5654654"; orgaoExpRG: string(string) ex: "SESPR"; ufExpRG: string(string) ex: "PR"; estadoCivil: string(string) ex: "SOLTEIRO"; profissao: string(string) ex: ""; escolaridade: string(string) ex: "SUPERIOR"; email: string(string) ex: "email@email.com.br"; contaContabil: number(Integer) ex: 100024; contaGerencial: number(Integer) ex: 100001 }

## EnviarDadosNovoClienteDeprecated

{ nome: string(string) ex: "Paulo Silva"; sexo: string(string) ex: "M"; tipo: string(string) ex: "F"; fone: string(string) ex: "5154654"; celular: string(string) ex: "956465853"; foneComercial: string(string) ex: "45465468"; uf: string(string) ex: "PR"; cep: string(string) ex: "2654654"; cidade: number(integer) ex: 5; endereco: string(string) ex: "Rua 2"; bairro: string(string) ex: ""; numero: string(string) ex: ""; complemento: string(string) ex: ""; dataNascimento: string(string) ex: "25/08/1984"; cpf: string(string) ex: "62976"; rg: string(string) ex: "5654654"; orgaoExpRG: string(string) ex: "SESPR"; ufExpRG: string(string) ex: "PR"; estadoCivil: string(string) ex: "SOLTEIRO"; profissao: string(string) ex: ""; escolaridade: string(string) ex: "SUPERIOR"; email: string(string) ex: "email@email.com.br"; contaContabil: number(Integer) ex: 100024; contaGerencial: number(Integer) ex: 100001 }

## EnviarDadosNovoClienteResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, cliente } }

## EnviarDadosNovoClienteResponseV2

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, cliente } }

## Error400

{ appVersion: string(string) ex: "5.0.7.103"; content: string(string) ex: "Conteúdo do xml não foi informado" }

## Error404

{ appVersion: string(string) ex: "5.0.0.117"; content: string(string) ex: "Nenhum registro encontrado" }

## Especies

{ codigo: string ex: "0000"; descricao: string ex: ""; comportamento: string ex: "" }

## EspeciesResponse

{ response: object { status, message, messages, especies } }

## EstProdutoAltV20

{ Codigo: integer ex: 10162; SKU: integer ex: 10162; CodigoBarras: string(string) ex: "1050695"; CodigoNCM: string(string) ex: "18069000"; Descricao: string(string) ex: "Kinder Ovo"; DescricaoCliente: string(string) ex: "Cliente"; Complemento: string(string) ex: ""; Marca: string(string) ex: "Dorizon"; Estoque: number(double) ex: 0; Preco: number(double) ex: 0; Grupo: string(string) ex: "10000"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "18-04-2018"; PrecoNormal: number(double) ex: 0; CodigoUnidade: string(string) ex: "001"; CodigoDepartamento: string(string) ex: "999"; Departamento: string(string) ex: "Geral"; Ativo: boolean ex: true; CodigoTributario: string(string) ex: "905"; Estoque1: number(double) ex: 10; Estoque2: number(double) ex: 0; Estoque3: number(double) ex: 0; Estoque4: number(double) ex: 0; Estoque5: number(double) ex: 0; PrecoLista: number(double) ex: 0; PrecoPDV: number(double) ex: 3.89; PrecoPDV2: number(double) ex: 0; PrecoPDV3: number(double) ex: 0; PrecoPDV4: number(double) ex: 0; PrecoPDV5: number(double) ex: 0; PrecoEtiqueta: number(double) ex: 3.2; PrecoCartaz: number(double) ex: 0; PrecoVenda3: number(double) ex: 0; PrecoVenda4: number(double) ex: 0; PrecoVenda5: number(double) ex: 0; FatorPr3: number(double) ex: 0; FatorPr4: number(double) ex: 0; FatorPr5: number(double) ex: 0; CustoCompra: number(double) ex: 76.3639; CustoEmpresa: number(double) ex: 76.3639; CustoFiscal: number(double) ex: 76.3639; CustoMedio: number(double) ex: 76.3639; CustoTranferencia: number(double) ex: 76.3639; TipoEmbalagem: string(string) ex: "UN"; QuantidadeEmbalagem: integer ex: 0 }

## EstoqueAlterado

{ codigoProduto: integer ex: 425524; estoque: number(double) ex: 50; dataHoraAlteracao: string(string) ex: "27/06/2019 12:10:01" }

## EstoqueByProdutoFilter

{ response: object { status, messages, estoques } }

## EstoquesV10

array de { id: integer ex: 1; descricao: string ex: "Trocas" }

## EtiquetasPendentesResponse_V_1_0

{ response: object { status, message, messages, maisregistros, etiquetas } }

## EtiquetasPendentesResponse_V_1_1

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, etiquetas } }

## EtiquetasPendentesResponse_V_1_2

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, etiquetas } }

## Etiquetas_V_1_0

{ codigoProduto: number ex: 100014; preco: number(double) ex: 1.25 }

## Etiquetas_V_1_1

{ codigoProduto: number ex: 100014; preco: number(double) ex: 1.25 }

## Etiquetas_V_1_2

{ codigoProduto: number ex: 100014; preco: number(double) ex: 1.25; dataAltPr: string ex: "16/11/2023"; preco2: number(double) ex: 1.25; dataAltPr2: string ex: "16/11/2023"; preco3: number(double) ex: 1.25; fator3: number(double) ex: 1.25; dataAltPr3: string ex: 1.25; preco4: number(double) ex: 1.25; fator4: number(double) ex: 1.25; dataAltPr4: string ex: "16/11/2023"; preco5: number(double) ex: 1.25; fator5: number(double) ex: 1.25; dataAltPr5: string ex: "16/11/2023" }

## Extrato

{ saldoInicial: number ex: 0; movimentacoes: `MovimentacoesExtrato` (ver reference/schemas.md); saldoFinal: number ex: -876.43 }

## ExtratoPontos

{ Transacao: string ex: "296128"; DataMovimento: string(string) ex: "02-01-2010"; Unidade: string(string) ex: "001"; Historico: string ex: "001"; TipoMovimento: string ex: "EV"; DataValidade: string ex: "03-01-2010"; NumeroPontos: number(double) ex: 42; SaldoPontos: number(double) ex: 3195; SaldoLiberado: number(double) ex: 3195; Valor: number ex: 43; PDV: string ex: "040"; Cupom: string ex: "19732"; DataExpiracao: string ex: "" }

## ExtratoResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, extrato } }

## FdeLancamento1_0

{ codDcto: number ex: 2020; release: number ex: 16876541; transacao: string(string) ex: "00221944010"; dataLcto: string(string) ex: "2016-05-06"; dataMvto: string(string) ex: "2016-05-06"; unidade: string(string) ex: "001"; usuarioLcto: number ex: 1004; totalDcto: number ex: 158.45; existemAnexo: boolean ex: true; fornecedor: number ex: 12456454; descricao: string(string) ex: "Inclusão De Pendências Folha De Pagamento"; centroCusto: array de object { codigo, contaGerencial, valor, operacao }; gerencial: array de object { conta, valor, operacao }; itens: array de object { descricao, quantidade, valor }; infExtras: array de object { nome, tipo, conteudo } }

## Financeiro_V_1_1

array de { formaPagamento: string(string); indCodBandeiraNFe: string(string); cnpjInstPagamento: string(string); valorTroco: number(double); itens: array de `ItemFinanceiro` (ver reference/schemas.md) }

## Financeiro_V_2_6

array de { formaPagamento: string(string); indCodBandeiraNFe: string(string); cnpjInstPagamento: string(string); valorTroco: number(double); itens: array de `ItemFinanceiroV2_6` (ver reference/schemas.md) }

## Financeiro_V_2_7

array de { formaPagamento: string(string); indCodBandeiraNFe: string(string); cnpjInstPagamento: string(string); valorTroco: number(double); itens: array de `ItemFinanceiroV2_7` (ver reference/schemas.md) }

## Financeiro_V_2_8

array de { formaPagamento: string(string); indCodBandeiraNFe: string(string); cnpjInstPagamento: string(string); valorTroco: number(double); itens: array de `ItemFinanceiroV2_8` (ver reference/schemas.md) }

## FornecRdiasReleaseListV1_0

array de **FornecRdiasReleaseV1_0** = object { codigo, nome, razaoSocial, cnpjcpf, situacao, codVinc, inscricaoEstadual, inscricaoMunicipal, regJuntaComercial, atividade, endereco, enderecoNumero, enderecoCompl, bairro, cep, cxPostal, muni_Codigo, fone, fax, email, marcas, percFunrural, obsPedidos, contaContabil, comp_Codigo, transfFundos, enderecoInd, muniInd_Codigo, foneIndustria, faxIndustria, codEAN, obsTrocas, dataCad, dataAlt, dtHrManutencao, usua_Codigo, contribuinte, bloqAutPgto, atTabPrForn, caracTrib, contaBloqueio, prontaEntrega, senhaCot, status, extra1, tipos, contribPrev, release, regra }

## FornecRdiasReleaseV1_0

{ codigo: number ex: 10510; nome: string(string) ex: "Hwr Industria e Comercio De Embalagens"; razaoSocial: string(string) ex: "Hwr Industria e Comercio De Embalagens"; cnpjcpf: string(string) ex: "07628008000146"; situacao: string(string) ex: "I"; codVinc: number ex: 0; inscricaoEstadual: string(string) ex: "78001593"; inscricaoMunicipal: string(string) ex: "78001593"; regJuntaComercial: string(string) ex: ""; atividade: string(string) ex: "Comercio Atacadista De Embalagens"; endereco: string(string) ex: "Rua Artur Sebastiao De Toledo Ribas"; enderecoNumero: string(string) ex: "1719"; enderecoCompl: string(string) ex: ""; bairro: string(string) ex: "Cantagalo"; cep: string(string) ex: "25803060"; cxPostal: string(string) ex: ""; muni_Codigo: number ex: 0; fone: string(string) ex: "222621-1633"; fax: string(string) ex: "228802-3686"; email: string(string) ex: "lagoscontabil@superig.com.br"; marcas: string(string) ex: ""; percFunrural: number ex: 0; obsPedidos: string(string) ex: ""; contaContabil: number ex: 0; comp_Codigo: string(string) ex: ""; transfFundos: string(string) ex: "N"; enderecoInd: string(string) ex: ""; muniInd_Codigo: string(string); foneIndustria: string(string) ex: ""; faxIndustria: string(string) ex: ""; codEAN: string(string) ex: ""; obsTrocas: string(string) ex: ""; dataCad: string(string) ex: "2014-01-10T03:00:00.000+00:00"; dataAlt: string(string) ex: "2018-07-19T03:00:00.000+00:00"; dtHrManutencao: string(string) ex: "2025-01-01T03:00:00.000+00:00"; usua_Codigo: string(string); contribuinte: string(string); bloqAutPgto: string(string); atTabPrForn: string(string); caracTrib: string(string); contaBloqueio: string(string); prontaEntrega: string(string); senhaCot: string(string); status: string(string); extra1: string(string); tipos: string(string); contribPrev: string(string); release: number ex: 2; regra: array de object { prazo_medio_pagamento, base_prazo_pagamento, frequencia_media_pedido, prazo_medio_entrega_pedido, codigo_unidade } }

## FornecReleaseListV1_0

{ response: object { status, appVersion, messages, content } }

## FornecReleaseV1_0

{ codigo: number ex: 10510; nome: string(string) ex: "Hwr Industria e Comercio De Embalagens"; razaoSocial: string(string) ex: "Hwr Industria e Comercio De Embalagens"; cnpjcpf: string(string) ex: "07628008000146"; situacao: string(string) ex: "I"; codVinc: number ex: 0; inscricaoEstadual: string(string) ex: "78001593"; inscricaoMunicipal: string(string) ex: "78001593"; regJuntaComercial: string(string) ex: ""; atividade: string(string) ex: "Comercio Atacadista De Embalagens"; endereco: string(string) ex: "Rua Artur Sebastiao De Toledo Ribas"; enderecoNumero: string(string) ex: "1719"; enderecoCompl: string(string) ex: ""; bairro: string(string) ex: "Cantagalo"; cep: string(string) ex: "25803060"; cxPostal: string(string) ex: ""; muni_Codigo: number ex: 0; fone: string(string) ex: "222621-1633"; fax: string(string) ex: "228802-3686"; email: string(string) ex: "lagoscontabil@superig.com.br"; marcas: string(string) ex: ""; percFunrural: number ex: 0; obsPedidos: string(string) ex: ""; contaContabil: number ex: 0; comp_Codigo: string(string) ex: ""; transfFundos: string(string) ex: "N"; enderecoInd: string(string) ex: ""; muniInd_Codigo: string(string); foneIndustria: string(string) ex: ""; faxIndustria: string(string) ex: ""; codEAN: string(string) ex: ""; obsTrocas: string(string) ex: ""; dataCad: string(string) ex: "2014-01-10T03:00:00.000+00:00"; dataAlt: string(string) ex: "2018-07-19T03:00:00.000+00:00"; dtHrManutencao: string(string) ex: "2025-01-01T03:00:00.000+00:00"; usua_Codigo: string(string); contribuinte: string(string); bloqAutPgto: string(string); atTabPrForn: string(string); caracTrib: string(string); contaBloqueio: string(string); prontaEntrega: string(string); senhaCot: string(string); status: string(string); extra1: string(string); tipos: string(string); contribPrev: string(string); release: number ex: 2 }

## FornecedorResponseV1

{ response: object { status, message, messages, fornecedores } }

## FornecedorResponseV1_5

{ response: object { status, appVersion, messages, content } }

## FornecedorV1_5

{ codigo: integer ex: 100048; release: integer ex: 6171; nome: string ex: "A j Sitta & Cia Ltda"; razaoSocial: string ex: "A j Sitta & Cia Ltda"; cnpjcpf: string ex: "77260610000159"; situacao: string ex: "N"; codVinc: integer ex: 0; inscricaoEstadual: string ex: "6011150002"; inscricaoMunicipal: string ex: ""; regJuntaComercial: string ex: ""; atividade: string ex: "Fermento"; endereco: `Endereco` (ver reference/schemas.md); cxPostal: string ex: ""; fone: string ex: "4333275281"; fax: string ex: ""; email: string ex: ""; marcas: string ex: "Itaiquara;"; percFunrural: number ex: 0; obsPedidos: string ex: ""; contaContabil: integer ex: 0; comp_Codigo: string ex: ""; transfFundos: string ex: "N"; enderecoInd: string ex: ""; muniInd_Codigo: integer ex: 4565; foneIndustria: string ex: ""; faxIndustria: string ex: ""; codEAN: string ex: ""; obsTrocas: string ex: ""; dataCad: string ex: "20/12/1997"; dataAlt: string ex: "06/02/2026"; dtHrManutencao: string ex: "06/02/2026T15:04:28"; usua_Codigo: integer ex: 118; contribuinte: string ex: "S"; bloqAutPgto: string ex: "N"; atTabPrForn: string ex: "S"; caracTrib: string ex: "H"; contaBloqueio: integer ex: 0; prontaEntrega: string ex: "S"; senhaCot: string; status: string ex: "N"; extra1: integer ex: 0; tipos: string ex: "AUTO"; contribPrev: string ex: "" }

## GetAgendasOfertasV1

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, Message, Messages, Agendas } }

## GetAgendasOfertasV1_1

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, Messages, Agendas } }

## GetAgendasOfertasV1_2

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, appVersion, Messages, content } }

## GravarControleEntrega

{ data: string(string) ex: "15/09/2019"; dataVenda: string(string) ex: "14/09/2019"; entregador: string(string) ex: "002"; unidade: string(string) ex: "001"; cliente: number(integer) ex: 103055; bairro: string(string) ex: "Rebouças"; cidade: string(string) ex: "Curitiba"; endereco: string(string) ex: "Avenida Presidente Getúlio Vargas, 427"; complemento: string(string) ex: "Próximo ao batalhão da PM"; nome: string(string) ex: "Rp Info"; fone: string(string) ex: "4132220808"; valor: number(double) ex: 510.58; pdv: string(string) ex: "011"; volumes: number(integer) ex: 25; cupom: string(string) ex: "21564"; observacao1: string(string) ex: "observacao1"; observacao2: string(string) ex: "observacao2"; hora: string(string) ex: 57714; referencia: string(string) ex: "Próximo a PM"; numeroCaixas: number(integer) ex: 24; dataBaixa: string(string) ex: "17/09/2019" }

## GrupoMessagesRespost

{ messages: array de object { message } }

## Grupos

{ codigo: string ex: "00000"; classificacao: string ex: ""; descricao: string(string) ex: "Importacao produtos"; prodServ: string ex: "p"; decimaisEst: number(double) ex: 0; recuo: number(double) ex: 0; periodos: number(double) ex: 4; codigoNCM: string ex: ""; comissao: number(double) ex: 0; dpto_codigo: string ex: ""; comportamento: string ex: ""; classFiscal: string ex: ""; tipoItem: string ex: ""; dtEstMin: string ex: "06/03/2018"; ctrlEstMin: number(double) ex: 0; percAbast: number(double) ex: 0; abatimento: number(double) ex: 0; margem: number(double) ex: 0 }

## ICMSItem

Informações de ICMS de um item

{ cst: string ex: "000"; baseCalculo: number(double) ex: 100; aliquota: number(double) ex: 12; valor: number(double) ex: 12 }

## ImagemProd

ImagemProd

array de { tipo: string ex: "BMP"; imagem: string ex: "" }

## IncluirAuditoriaPost

{ auditorias: `Auditorias` (ver reference/schemas.md) }

## IncluirAuditoriaPostV1_1

{ origem: string ex: "NOME_APLICATIVO_CONSUMIDOR"; auditorias: `AuditoriasV_1_1` (ver reference/schemas.md) }

## IncluirAuditoriaPostV1_2

{ origem: string ex: "NOME_APLICATIVO_CONSUMIDOR"; dataHoraDispositivo: string(dd/MM/yyyy HH:mm:ss Z) ex: "17/03/2025 16:13:26 -0300"; auditorias: `AuditoriasV_1_2` (ver reference/schemas.md) }

## IncluirAuditoriaPostV1_3

{ id: string ex: "identificador da auditoria, id controlado pelo consumidor do serviço"; origem: string ex: "NOME_APLICATIVO_CONSUMIDOR"; dataHoraDispositivo: string(dd/MM/yyyy HH:mm:ss Z) ex: "17/03/2025 16:13:26 -0300"; auditorias: `AuditoriasV_1_2` (ver reference/schemas.md) }

## IncluirESMPost

{ unidadeOrigem: string ex: "00000000000000"; unidadeDestino: string ex: "00000000000000"; codigoDocumento: string ex: "1231"; codigoPendencia: string ex: "300;350"; dataMovimento: string ex: "20/04/2018"; pendencias: object { codigoProduto, operacaoBaixar, qtdeBaixar, sequencial } }

## IncluirPendBaixaPost

{ Inclusoes: `IncluirPendPost` (ver reference/schemas.md); Baixas: object { pendencias } }

## IncluirPendPost

{ dataMovimento: string(string) ex: "20/04/2018"; dataEntrega: string(string) ex: "20/04/2018"; unidadeOrigem: string(string) ex: "001"; unidadeDestino: string(string) ex: "002"; tipoPendencia: string(string) ex: "TC"; codigoPendencia: string ex: "100"; especie: string ex: "4000"; codigoDocumento: string ex: "8400"; categoriaParticipante: string ex: "FORNECEDOR"; participante: string ex: "00000000000000"; pendencias: object { codigoProduto, valor, quantidadeEmbalagem, quantidadeUnitaria } }

## IncluirPendResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, transacao } }

## IncluirPendResponse_V_1_3

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, transacao } }

## IncluirRecPost

{ unidade: string ex: "00000000000000"; codigoDcto: number ex: 7514; numero: string ex: "321354"; serie: string ex: "1"; dataMovimento: string ex: "20/04/2018"; categoriaEntidade: string ex: "FORNECEDOR"; codigoEntidade: string ex: "10006"; produtos: object { codigo, quantidadeUnitaria, quantidadeEmbalagem, dataFabricacao, dataValidade, temperatura, horaInicio, horaFim, lote } }

## Industrializado

{ codigo: number ex: 100577; descricao: string(string) ex: "Osso Bovino Desossa Dianteiro Kg"; tipo: string(string) ex: "IC"; unidade: string(string) ex: "000"; rendimento: number ex: 1.0; pesoTotal: number ex: 0.0; precoTotal: number ex: 0.0; dataCusto: string(string) ex: "28/02/2020"; comportamento: string(string) ex: ""; fase: number ex: 0; tempoProducao: string(string) ex: ""; observacao: string(string) ex: ""; quantidadeMinimaProduzir: number ex: 0.0; quantidadeProduzir: number ex: 0.0; quantidadeMultiplaProduzir: number ex: 0.0; baseProducao: string(string) ex: ""; tempoAntecedencia: number ex: 0; tempoProducaoHomensHora: number ex: 0; prioridadeProducao: number ex: 0; tempoPreparo: number ex: 0; estoqueSeguranca: number ex: 0.0; baixaEstoqueMateriaPrima: string(string) ex: ""; fatorProducao: number ex: 0.0; AgrupamentoUnidadesValidas: string(string) ex: ""; departamento: string(string) ex: "037" }

## IndustrializadoEdicao_V1_2

{ descricao: string(string) ex: "Osso Bovino Desossa Dianteiro Kg"; tipo: string(string) ex: "IC"; unidade: string(string) ex: "000"; rendimento: number ex: 1.0; pesoTotal: number ex: 0.0; precoTotal: number ex: 0.0; dataCusto: string(string) ex: "28/02/2020"; comportamento: string(string) ex: ""; fase: number ex: 0; tempoProducao: string(string) ex: ""; observacao: string(string) ex: ""; quantidadeMinimaProduzir: number ex: 0.0; quantidadeProduzir: number ex: 0.0; quantidadeMultiplaProduzir: number ex: 0.0; baseProducao: string(string) ex: ""; tempoAntecedencia: number ex: 0; tempoProducaoHomensHora: number ex: 0; prioridadeProducao: number ex: 0; tempoPreparo: number ex: 0; estoqueSeguranca: number ex: 0.0; baixaEstoqueMateriaPrima: string(string) ex: ""; fatorProducao: number ex: 0.0; AgrupamentoUnidadesValidas: string(string) ex: ""; departamento: string(string) ex: "037" }

## Industrializado_V1_2

{ codigo: number ex: 111898; descricao: string(string) ex: "Carne Bov Alcatra S/ Osso Kg"; tipo: string(string) ex: "IC"; unidade: string(string) ex: "001"; rendimento: number ex: 1; pesoTotal: number ex: 0; precoTotal: number ex: 0; dataCusto: string(string) ex: "22/11/2021"; comportamento: string(string) ex: ""; fase: number ex: 0; tempoProducao: string(string) ex: ""; observacao: string(string) ex: ""; quantidadeMinimaProduzir: number ex: 0; quantidadeProduzir: number ex: 0; quantidadeMultiplaProduzir: number ex: 0; baseProducao: string(string) ex: ""; tempoAntecedencia: number ex: 0; tempoProducaoHomensHora: number ex: 0; prioridadeProducao: number ex: 0; tempoPreparo: number ex: 0; estoqueSeguranca: number ex: 0; baixaEstoqueMateriaPrima: string(string) ex: ""; fatorProducao: number ex: 0; AgrupamentoUnidadesValidas: string(string) ex: ""; departamento: string(string) ex: "001"; codigosBarras: array de string ex: "0000000004206" }

## Industrializado_V1_3

{ codigo: number ex: 111898; descricao: string(string) ex: "Carne Bov Alcatra S/ Osso Kg"; tipo: string(string) ex: "IC"; unidade: string(string) ex: "001"; rendimento: number ex: 1; pesoTotal: number ex: 0; precoTotal: number ex: 0; dataCusto: string(string) ex: "22/11/2021"; comportamento: string(string) ex: ""; fase: number ex: 0; tempoProducao: string(string) ex: ""; observacao: string(string) ex: ""; quantidadeMinimaProduzir: number ex: 0; quantidadeProduzir: number ex: 0; quantidadeMultiplaProduzir: number ex: 0; baseProducao: string(string) ex: ""; tempoAntecedencia: number ex: 0; tempoProducaoHomensHora: number ex: 0; prioridadeProducao: number ex: 0; tempoPreparo: number ex: 0; estoqueSeguranca: number ex: 0; baixaEstoqueMateriaPrima: string(string) ex: ""; fatorProducao: number ex: 0; agrupamentoUnidadesValidas: string(string) ex: ""; departamento: string(string) ex: "001"; codigosBarras: array de string ex: "0000000004206" }

## InfoAdicFreteFDE

Informações adicionais de frete do documento FDE

{ tipoCte: string ex: "0"; indNatFrete: string ex: "1"; indTpFrete: string ex: "1"; cstPis: string ex: "50"; muniOrigem: string ex: "4106902"; codBcCredPis: string ex: "13" }

## InserirGrupoResponse

{ response: object { status, messages, id } }

## InserirGrupoResponseV1_1

{ response: object { status, appVersion, messages, content } }

## InserirGrupoV_1_00

O atributo pode retornar

{ classificacao: string(string) ex: "1.001.01.01.002.003"; descricao: string(string) ex: "Arroz Parboilizado Até 10kg"; prodServ: string(string) ex: "P"; decimaisEst: integer(integer) ex: 3; recuo: integer(integer) ex: 0; periodos: integer(integer) ex: 4; codigoNCM: string(string) ex: "10063021"; comissao: number(double) ex: 0.0; dpto_codigo: string(string) ex: "042"; comportamento: string(string) ex: "QD"; classFiscal: string(string) ex: "100"; tipoItem: string(string) ex: "00"; dtEstMin: string(date) ex: "19/03/2021"; ctrlEstMin: integer(integer) ex: 17018; percAbast: integer(integer) ex: 0; abatimento: number(double) ex: 0.0 }

## InserirProgramPrecoResponse

{ response: object { status, messages, id } }

## InserirProgramacaoPrecos

{ status: string ex: "0"; codigoAgenda: string ex: "0001"; unidade: string ex: "001"; codigoProduto: integer(integer) ex: 436631; precoAlteracao: string ex: "1"; uf: string ex: "PR"; dataInicial: string ex: "11/03/2021"; dataFinal: string ex: "13/03/2021"; horaInicial: string ex: "22"; horaFinal: string ex: "13"; precoVenda: number(double) ex: 185.8; prioridade: string ex: "4"; oferta: string ex: "N"; qtdeMaximaCliente: number(integer) ex: 15; fatorPreco: number(integer) ex: 3; obs: string ex: "observação"; dataInicialRel: string ex: "11/03/2021"; dataFinalRel: string ex: "13/03/2021"; autorizado: string ex: "S" }

## InserirProgramacaoPrecosV1_1

{ id: string ex: "1"; status: string ex: "0"; codigoAgenda: string ex: "0001"; unidade: string ex: "001"; codigoProduto: integer(integer) ex: 436631; precoAlteracao: string ex: "1"; uf: string ex: "PR"; dataInicial: string ex: "11/03/2021"; dataFinal: string ex: "13/03/2021"; horaInicial: string ex: "22"; horaFinal: string ex: "13"; precoVenda: number(double) ex: 185.8; prioridade: string ex: "4"; oferta: string ex: "N"; qtdeMaximaCliente: number(integer) ex: 15; fatorPreco: number(integer) ex: 3; obs: string ex: "observação"; dataInicialRel: string ex: "11/03/2021"; dataFinalRel: string ex: "13/03/2021"; autorizado: string ex: "S" }

## InserirProgramacoesPrecos

{ programacoes: array de `InserirProgramacaoPrecosV1_1` (ver reference/schemas.md) }

## InserirProgramasPrecosResponseV1_1

{ response: object { status, messages, resultados } }

## InsertFornecedorV1_0

{ cnpjcpf: string(string) ex: "12345678000195"; razaoSocial: string(string) ex: "Fornecedor Exemplo LTDA"; nome: string(string) ex: "Fornecedor Exemplo"; email: string(string) ex: "contato@fornecedorexemplo.com"; situacao: string(string) ex: "A"; status: string(string) ex: "N"; inscricaoestadual: string(string) ex: "123456789"; contribuinte: string(string) ex: "S"; dtHrManutencao: string(string) ex: "11/01/2024 11:00:00"; dataCad: string(string) ex: "11/01/2024"; usua_Codigo: number ex: 101; enderecoResidencial: object { cidade, cep, endereco, bairro, numero, complemento }; fone: string(string) ex: "+5541999999999" }

## InsertMovPdvV1

{ data: string(string) ex: "05/03/2021"; pdv: string(string) ex: 2; cupom: string(string) ex: 1234; codigoUnidade: string(string) ex: 1; valor: number(double) ex: 106.59; tipo: string(string) ex: "R"; categoriaEntidade: string(string) ex: "F"; codigosPendencias: string(string) ex: 10254; cnpjCpf: string(string) ex: "12345678901"; dataVencimento: string(string) ex: "10/05/2021"; cmc7: string(string) ex: "cmc7" }

## InsertPreCadastroV_1_0

{ response: object { status, messages, sequencia } }

## ItemFDE

Item/linha de um documento FDE

{ descricao: string ex: "Avental para padaria"; tipoItem: string ex: "07"; valor: number(double) ex: 100.0; qtde: number(double) ex: 1; descontoValor: number(double) ex: 0.0; seguroValor: number(double) ex: 0.0; freteValor: number(double) ex: 0.0; despAcessoriaValor: number(double) ex: 0.0; cfop: string ex: "1556"; controleTrib: string ex: "102030"; codBcCredPis: string ex: "13"; icms: `ICMSItem` (ver reference/schemas.md) }

## ItemFinanceiro

{ contaBaixa: string(string); parcela: integer; nsuHost: string(string); nsuSitef: string(string); nsuAutorizacao: string(string); autorizador: string(string); binCartao: string(string); banco: string(string); agencia: string(string); valor: number(double) }

## ItemFinanceiroV2_6

{ contaBaixa: string(string); parcela: integer; nsuHost: string(string); nsuSitef: string(string); nsuAutorizacao: string(string); autorizador: string(string); binCartao: string(string); banco: string(string); agencia: string(string); valor: number(double) }

## ItemFinanceiroV2_7

{ contaBaixa: string(string); parcela: integer; nsuHost: string(string); nsuSitef: string(string); nsuAutorizacao: string(string); autorizador: string(string); binCartao: string(string); banco: string(string); agencia: string(string); valor: number(double); pixId: string(string); transacaoIdEcomm: string(string) }

## ItemFinanceiroV2_8

{ contaBaixa: string(string); parcela: integer; nsuHost: string(string); nsuSitef: string(string); nsuAutorizacao: string(string); autorizador: string(string); binCartao: string(string); banco: string(string); agencia: string(string); valor: number(double); pixId: string(string); transacaoIdEcomm: string(string); bandeiraCartao: string ex: "Mastercard"; cnpjPag: string(string); ufPag: string(string); cnpjReceb: string(string); idTermPag: string(string); dataPag: string(string) }

## ItemPedido

{ codigoProduto: integer ex: 100170; qtdUnitaria: number(double) ex: 1; qtdEmbalagem: number ex: 2; valorProduto: number(double) ex: 2.5; percDesconto: number(double) ex: 0 }

## ItemPedidoV19

{ codigoProduto: integer ex: 100170; qtdUnitaria: number(double) ex: 1; qtdEmbalagem: number ex: 2; valorProduto: number(double) ex: 2.5; percDesconto: number(double) ex: 0; valorProdFlex: number(double) ex: 2.7 }

## ItemPedidoV21

{ codigoProduto: integer ex: 100170; qtdUnitaria: number ex: 1; qtdEmbalagem: integer ex: 2; valorProduto: number(double) ex: 2.5; percDesconto: number(double) ex: 2; valorProdFlex: number(double) ex: 2 }

## ItensCamposExtrasV1

{ nome: string ex: "valor1"; tipo: string ex: "String"; valor: string ex: "teste123" }

## ItensCodAlterados

{ codigoProduto: number ex: 102059; codigoBarras: string(string) ex: "7895800307823"; numPreco: string(string) ex: "0"; fatorEmbalagem: string(string) ex: "0"; data: string(string) ex: "05/05/2016" }

## ItensCodAlteradosV11

**ItensCodAlterados** = object { codigoProduto, codigoBarras, numPreco, fatorEmbalagem, data } & { precoVendaUnidadeMedida: number ex: 12; precoVenda: number ex: 12 }

## ItensFormaPagamento

{ codigo: string ex: "001"; descricao: string ex: "A Vista"; descricaoReduzida: string ex: "A Vista" }

## ItensFormaPagamento_V_1_1

{ codigo: string(string) ex: "000"; descricao: string(string) ex: "A Prazo 10 Dias"; descricaoReduzida: string(string) ex: "10 Diass"; prazos: string(string) ex: "10"; aplicação: string(string) ex: "R;P;C;V"; acrescimos: number ex: 0; comissao: number ex: 0; descontos: number ex: 0; entrada: number ex: 0; taxaJuros: number ex: 0 }

## ItensFormaPagamento_V_1_2

{ codigo: string(string) ex: "000"; descricao: string(string) ex: "A Prazo 10 Dias"; descricaoReduzida: string(string) ex: "10 Diass"; prazos: string(string) ex: "10"; aplicação: string(string) ex: "R;P;C;V"; acrescimos: number ex: 0; comissao: number ex: 0; descontos: number ex: 0; entrada: number ex: 0; taxaJuros: number ex: 0; indicadorForma: string ex: "01" }

## ItensMovProdRCMV10

Items

array de { codigoProduto: number ex: 242934; sequencial: number ex: 1; quantidadeUnitaria: number(double) ex: 10; quantidadeEmbalagem: number(double) ex: 10; valor: number(double) ex: 6; icms: number(double) ex: 0; percReducaoBC: number(double) ex: 0; percentualIPI: number(double) ex: 0; percentualDesconto: number(double) ex: 0; outrosAcrescimos: number(double) ex: 0; outrosAbatimentos: number(double) ex: 0; valorSubTrib: number(double) ex: 0; despesasAdicionais: number(double) ex: 0; percentualISS: number(double) ex: 0; simbologiaICMS: string ex: ""; valorPIS: number(double) ex: 0; valorCofins: number(double) ex: 0; bcPisCofins: number(double) ex: 0; aliqPis: number(double) ex: 0; aliqCofins: number(double) ex: 0; cstPis: string ex: ""; cstCofins: string ex: ""; cfop: string ex: ""; cst: string ex: ""; bcIpi: number(double) ex: 0; percReducaoBcSt: number(double) ex: 0; valorUnitario: number(double) ex: 2 }

## ItensPedCompraV14

ItensPedCompra

array de { codigoProduto: number ex: 210463; quantidadeUnitaria: number ex: 24; tamanhoEmbalagem: number ex: 24; quantidadeEmbalagem: number ex: 24; valor: number(double) ex: 39.6; ipi: number(double) ex: 0; desconto: number(double) ex: 0; bonificacao: number ex: 0; valorSubTrib: number(double) ex: 0; acrescimoFinanceiro: number(double) ex: 0; sequencial: number ex: 1; baixa: `DadosBaixaV14` (ver reference/schemas.md) }

## ItensPedCompraV17

ItensPedCompra

array de { codigoProduto: number ex: 210463; quantidadeUnitaria: number ex: 24; tamanhoEmbalagem: number ex: 24; quantidadeEmbalagem: number ex: 24; valor: number(double) ex: 39.6; ipi: number(double) ex: 0; desconto: number(double) ex: 0; bonificacao: number ex: 0; valorSubTrib: number(double) ex: 0; acrescimoFinanceiro: number(double) ex: 0; sequencial: number ex: 1; valMinima: number(double) ex: 0; baixa: `DadosBaixaV14` (ver reference/schemas.md) }

## ItensPedCompra_V_1_00

ItensPedCompra

array de { codigoProduto: number ex: 210463; quantidadeUnitaria: number ex: 24; tamanhoEmbalagem: number ex: 24; valor: number(double) ex: 39.6; ipi: number(double) ex: 0; desconto: number(double) ex: 0; bonificacao: number ex: 0; valorSubTrib: number(double) ex: 0; acrescimoFinanceiro: number(double) ex: 0; sequencial: number ex: 1; baixa: `DadosBaixa` (ver reference/schemas.md) }

## ItensPedCompra_V_1_01

ItensPedCompra

array de { codigoProduto: number ex: 210463; quantidadeUnitaria: number ex: 24; quantidadeEmbalagem: number ex: 24; valor: number(double) ex: 39.6; ipi: number(double) ex: 0; desconto: number(double) ex: 0; bonificacao: number ex: 0; valorSubTrib: number(double) ex: 0; acrescimoFinanceiro: number(double) ex: 0; sequencial: number ex: 1; baixa: `DadosBaixa` (ver reference/schemas.md) }

## ItensPedVendaV2

{ codigoProduto: integer ex: 100170; qtdUnitaria: number ex: 1; qtdEmbalagem: integer ex: 2; valorProduto: number(double) ex: 2.5; percDesconto: number(double) ex: 2 }

## ItensPedVendaV21

{ codigoProduto: integer ex: 100170; qtdUnitaria: number ex: 1; qtdEmbalagem: integer ex: 2; valorProduto: number(double) ex: 2.5; percDesconto: number(double) ex: 2; valorProdFlex: number(double) ex: 2 }

## ItensPedVendaV22

{ codigoProduto: integer ex: 100170; qtdUnitaria: number ex: 1; qtdEmbalagem: integer ex: 2; valorProduto: number(double) ex: 2.5; percDesconto: number(double) ex: 2; valorProdFlex: number(double) ex: 2; valorDesconto: number(double) ex: 0.5; valorAcrescimo: number(double) ex: 1.8 }

## ItensPedVendaV27

{ codigoProduto: integer ex: 100170; qtdUnitaria: number ex: 12; qtdEmbalagem: integer ex: 12; valorProduto: number(double) ex: 2; percDesconto: number(double) ex: 2; valorProdFlex: number(double) ex: 6; valorDesconto: number(double) ex: 0.5; valorAcrescimo: number(double) ex: 1.8; valorBrutoTotal: number(double) ex: 2.0; valorProdPadrao: number(double) ex: 13.0; valorFlexBase: number(number) ex: "Valor Unitário Base Valor Flex"; valorComissao: number(number) ex: "Valor da Comissão" }

## ItensPedVendaV3

{ codigoProduto: integer ex: 100170; qtdUnitaria: number ex: 1; qtdEmbalagem: integer ex: 2; valorProduto: number(double) ex: 2.5; percDesconto: number(double) ex: 2; valorProdFlex: number(double) ex: 2 }

## ItensPedVendaV31

**ItensPedVendaV27** = object { codigoProduto, qtdUnitaria, qtdEmbalagem, valorProduto, percDesconto, valorProdFlex, valorDesconto, valorAcrescimo, valorBrutoTotal, valorProdPadrao, valorFlexBase, valorComissao } & { observacao: string(string) }

## ItensPedVendaV33

**ItensPedVendaV31** = `ItensPedVendaV27` (ver reference/schemas.md) & object { observacao } & { codigoVendedor: string(string) }

## ItensPedido

{ codigoProduto: integer ex: 100170; qtdUnitaria: number(double) ex: 1; qtdEmbalagem: number ex: 2; valorProduto: number(double) ex: 2.5; percDesconto: number(double) ex: 0 }

## ItensTransfProd

ItensTransfProd

array de { codigoProduto: number ex: 242934; sequencial: number ex: 1; quantidadeUnitaria: number(double) ex: 10; quantidadeEmbalagem: number(double) ex: 10; valor: number(double) ex: 6; icms: number(double) ex: 0; percReducaoBC: number(double) ex: 0; percentualIPI: number(double) ex: 0; percentualDesconto: number(double) ex: 0; outrosAcrescimos: number(double) ex: 0; valorSubTrib: number(double) ex: 0; despesasAdicionais: number(double) ex: 0; percentualISS: number(double) ex: 0; simbologiaICMS: string ex: ""; valorPIS: number(double) ex: 0; valorCofins: number(double) ex: 0; bcPisCofins: number(double) ex: 0; aliqPis: number(double) ex: 0; aliqCofins: number(double) ex: 0; cstPis: string ex: ""; cstCofins: string ex: ""; cfop: string ex: ""; cst: string ex: ""; bcIpi: number(double) ex: 0; percReducaoBcSt: number(double) ex: 0; valorUnitario: number(double) ex: 2 }

## ItensVenda

ItensVenda

array de { data: string(string) ex: "11/07/2014"; numeroDcto: string(string) ex: "24433"; unidade: string(string) ex: "001"; produtos: `ProdVenda` (ver reference/schemas.md) }

## ListaAgendas

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, agendas } }

## ListaCompradores

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, compradores } }

## ListaCompradores_V_1_0

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, compradores } }

## ListaCompradores_V_1_2

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, messages, content } }

## ListaEntregasV_1_0

{ response: object { status, messages, entregas } }

## ListaFornecReleaseV1_0

{ status: string(string) ex: "ok"; messages: `XmlMessages` (ver reference/schemas.md); fornecedores: `FornecReleaseListV1_0` (ver reference/schemas.md) }

## ListaFornecTipoV1_3

{ status: string(string) ex: "ok"; messages: `XmlMessages` (ver reference/schemas.md); fornecedores: `fornecedor_V_1_3` (ver reference/schemas.md) }

## ListaFornecTipoV1_4

{ status: string(string) ex: "ok"; messages: `XmlMessages` (ver reference/schemas.md); fornecedores: `fornecedor_V_1_4` (ver reference/schemas.md) }

## ListaItensPedidosComFiltrosResponse

{ response: object { status, messages, itens } }

## ListaPedidosComFiltrosResponse

{ response: object { status, messages, pedidos } }

## ListaPedidosComFiltrosResponse_V_1_2

{ response: object { status, messages, pedidos } }

## ListaTipo

{ status: string(string) ex: "ok"; message: string(string) ex: "Dados carregados com sucesso"; messages: `XmlMessages` (ver reference/schemas.md); tiposForn: `tiposFornec` (ver reference/schemas.md) }

## ListarSupervisoresResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, supervisores } }

## ListarUnidadesResponseV_1_4

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, unidades } }

## ListarUnidadesResponseV_1_5

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, unidades } }

## ListarVeiculosEntregaResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, veiculos } }

## ListarVeiculosEntregaResponseV1.1

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, content } }

## MediasResponse_V_1_0

{ response: object { status, appVersion, messages, content } }

## MensagemDeletarIndustrializado

string(string) ex: "Industrializado deletado com sucesso"

## MensagemDeletarProduto

string(string) ex: "Produto deletado com sucesso"

## MovBcoBxReq

Dados bancários relacionados à baixa financeira

{ documentoBancario: string ex: "DOC"; dataPrevista: string(date) ex: "29/08/2024"; observacao: string ex: "OK"; codigoHistorico: string ex: "0501"; complementoHistorico: string ex: "Depósito referente à baixa de títulos"; codigoBancario: string ex: "341" }

## MovDctosDto

Dados do movimento de documento financeiro gerado após a baixa

{ transacao: string ex: "TR000123456"; operacao: string ex: "OPR1234"; dataMvto: string(date) ex: "28/08/2024"; dataLcto: string(date) ex: "28/08/2024"; usua_lcto: integer ex: 123; espe_codigo: string ex: "CHQ"; status: string ex: "BAIXADO" }

## MovProdDResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, movimentos } }

## MovProdDResponse_V_1_2

{ response: object { status, messages, movimentos } }

## MovProdDResponse_V_1_3

{ response: object { status, messages, movimentos } }

## MovProdDResponse_V_1_4

{ response: object { status, messages, movimentos } }

## MovProdDResponse_V_1_5

{ response: object { status, messages, movimentos } }

## MovProdDResponse_V_1_7

{ response: object { status, messages, movimentos } }

## MovProdDResponse_V_1_8

{ response: object { status, messages, movimentos } }

## MovProdDResponse_V_1_9

{ response: object { status, messages, movimentos } }

## MovProdDResponse_V_2_0

{ response: object { status, messages, movimentos } }

## MovProdRCMResponseV10

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, movimentos } }

## MovProdRCMResponseV12

{ response: object { status, messages, content } }

## MovProdRCMV10

movimentos

array de { transacao: string ex: "2.10101148E8"; operacao: string ex: "2.101011481E9"; idNfe: string ex: "41191007493739000212550010000148211101011485"; data: string ex: "01/10/2019"; unidade: string ex: "7.493739000212E12"; numero: string ex: "13821"; serie: string ex: "1"; id: string ex: "2143"; categoriaEntidade: string ex: "U"; codigoEntidade: string ex: "3"; itens: `ItensMovProdRCMV10` (ver reference/schemas.md) }

## MovimentacoesExtrato

{ transacao: string(string) ex: "00110061276"; operacao: string(string) ex: "00110061276704"; conta: string(string) ex: "112502"; descricaoConta: string(string) ex: "Cheques Devolvidos em Cobrança"; numeroDocumento: string(string) ex: "931374"; parcela: string(string) ex: "1"; data: string(string) ex: "04/03/2010"; valor: number(double) ex: 100; saldo: string(double) ex: "150"; tipo: string(string) ex: "DEBITO"; baixaParcial: boolean ex: false }

## MovimentoDocumentoDto

{ transacao: string; operacao: string; status: string; dataLcto: string ex: "dd/MM/yyyy"; dataMvto: string ex: "dd/MM/yyyy"; unidCodigo: string; dctoCodigo: string; dctoTipo: string; numeroDcto: string; espeCodigo: string; valor: number(double); usuLcto: integer; usuCanc: integer; dataCanc: string ex: "dd/MM/yyyy"; impresso: integer; usuAudit: integer; dataAudit: string ex: "dd/MM/yyyy"; imprDcto: string; horaLcto: string; horaCanc: string; versao: string; horaAudit: string; motivoCanc: string; release: integer; observacao: string; tempoLcto: integer }

## MovimentosMovProdD

Movimentos de produtos

array de { id: number ex: 10000; chavePrimaria: string ex: "50610009822_2"; transacao: string ex: "50610009822"; operacao: string ex: "506100098221"; status: string ex: "NORMAL"; data: string ex: "12/06/2019"; codigoEntidade: string ex: "104671"; categoriaEntidade: string ex: "104671"; unidade: string ex: "001"; numero: string ex: "36363"; codigoProduto: number ex: 242934; sequencial: number ex: 1; quantidadeUnitaria: number(double) ex: 10; quantidadeEmbalagem: number(double) ex: 10; valor: number(double) ex: 6; icms: number(double) ex: 0; percReducaoBC: number(double) ex: 0; percentualIPI: number(double) ex: 0; percentualDesconto: number(double) ex: 0; outrosAcrescimos: number(double) ex: 0; valorSubTrib: number(double) ex: 0; despesasAdicionais: number(double) ex: 0; percentualISS: number(double) ex: 0; simbologiaICMS: string ex: ""; valorPIS: number(double) ex: 0; valorCofins: number(double) ex: 0; bcPisCofins: number(double) ex: 0; aliqPis: number(double) ex: 0; aliqCofins: number(double) ex: 0; cstPis: string ex: ""; cstCofins: string ex: ""; cfop: string ex: ""; cst: string ex: ""; bcIpi: number(double) ex: 0; percReducaoBcSt: number(double) ex: 0; valorUnitario: number(double) ex: 2 }

## MovimentosMovProdD_V_1_2

array de { id: number ex: 80017; chavePrimaria: string(string) ex: "00119311984_1"; transacao: string(string) ex: "00119311984"; operacao: string(string) ex: "001193119841"; status: string(string) ex: "NORMAL"; data: string(string) ex: "21/09/2021"; codigoEntidade: string(string) ex: "4"; categoriaEntidade: string(string) ex: "CLIENTE"; unidade: string(string) ex: "001"; numero: string(string) ex: "77917"; codigoProduto: number ex: 100017; sequencial: number ex: 1; quantidadeUnitaria: number ex: 1; quantidadeEmbalagem: number ex: 0; valor: number ex: 15; icms: number ex: 0; percReducaoBC: number ex: 0; percentualIPI: number ex: 0; percentualDesconto: number ex: 0; outrosAcrescimos: number ex: 0; valorSubTrib: number ex: 0; despesasAdicionais: number ex: 0; percentualISS: number ex: 0; simbologiaICMS: string(string) ex: "ST"; valorPIS: number ex: 0; valorCofins: number ex: 1; bcPisCofins: number ex: 15; aliqPis: number ex: 1; aliqCofins: number ex: 7; cstPis: string(string) ex: "01"; cstCofins: string(string) ex: "01"; cfop: string(string) ex: "5405"; cst: string(string) ex: "060"; bcIpi: number ex: 0; percReducaoBcSt: number ex: 0; valorUnitario: number ex: 15; ctCompra: number ex: 8; ctMedio: number ex: 8; ctTransf: number ex: 9; ctEmpresa: number ex: 9; ctFiscal: number ex: 8; prCompra: number ex: 9 }

## MovimentosMovProdD_V_1_3

array de { id: number ex: 80017; chavePrimaria: string(string) ex: "00119311984_1"; transacao: string(string) ex: "00119311984"; operacao: string(string) ex: "001193119841"; status: string(string) ex: "NORMAL"; chaveNfe: string(string) ex: "41140309353560000102550020000125211111015035"; data: string(string) ex: "21/09/2021"; codigoEntidade: string(string) ex: "4"; categoriaEntidade: string(string) ex: "CLIENTE"; unidade: string(string) ex: "001"; numero: string(string) ex: "77917"; codigoProduto: number ex: 100017; sequencial: number ex: 1; quantidadeUnitaria: number ex: 1; quantidadeEmbalagem: number ex: 0; valor: number ex: 15; icms: number ex: 0; percReducaoBC: number ex: 0; percentualIPI: number ex: 0; percentualDesconto: number ex: 0; outrosAcrescimos: number ex: 0; valorSubTrib: number ex: 0; despesasAdicionais: number ex: 0; percentualISS: number ex: 0; simbologiaICMS: string(string) ex: "ST"; valorPIS: number ex: 0; valorCofins: number ex: 1; bcPisCofins: number ex: 15; aliqPis: number ex: 1; aliqCofins: number ex: 7; cstPis: string(string) ex: "01"; cstCofins: string(string) ex: "01"; cfop: string(string) ex: "5405"; cst: string(string) ex: "060"; bcIpi: number ex: 0; percReducaoBcSt: number ex: 0; valorUnitario: number ex: 15; ctCompra: number ex: 8; ctMedio: number ex: 8; ctTransf: number ex: 9; ctEmpresa: number ex: 9; ctFiscal: number ex: 8; prCompra: number ex: 9 }

## MovimentosMovProdD_V_1_4

array de { id: number ex: 80017; chavePrimaria: string(string) ex: "00119311984_1"; transacao: string(string) ex: "00119311984"; operacao: string(string) ex: "001193119841"; status: string(string) ex: "NORMAL"; chaveNfe: string(string) ex: "41140309353560000102550020000125211111015035"; data: string(string) ex: "21/09/2021"; codigoEntidade: string(string) ex: "4"; categoriaEntidade: string(string) ex: "CLIENTE"; unidade: string(string) ex: "001"; numero: string(string) ex: "77917"; codigoProduto: number ex: 100017; sequencial: number ex: 1; quantidadeUnitaria: number ex: 1; quantidadeEmbalagem: number ex: 0; valor: number ex: 15; icms: number ex: 0; percReducaoBC: number ex: 0; percentualIPI: number ex: 0; percentualDesconto: number ex: 0; outrosAcrescimos: number ex: 0; valorSubTrib: number ex: 0; despesasAdicionais: number ex: 0; percentualISS: number ex: 0; simbologiaICMS: string(string) ex: "ST"; valorPIS: number ex: 0; valorCofins: number ex: 1; bcPisCofins: number ex: 15; aliqPis: number ex: 1; aliqCofins: number ex: 7; cstPis: string(string) ex: "01"; cstCofins: string(string) ex: "01"; cfop: string(string) ex: "5405"; cst: string(string) ex: "060"; bcIpi: number ex: 0; percReducaoBcSt: number ex: 0; valorUnitario: number ex: 15; ctCompra: number ex: 8; ctMedio: number ex: 8; ctTransf: number ex: 9; ctEmpresa: number ex: 9; ctFiscal: number ex: 8; prCompra: number ex: 9; tipoDcto: number ex: "EAQ" }

## MovimentosMovProdD_V_1_5

array de { id: number ex: 80017; chavePrimaria: string(string) ex: "00119311984_1"; transacao: string(string) ex: "00119311984"; operacao: string(string) ex: "001193119841"; status: string(string) ex: "NORMAL"; chaveNfe: string(string) ex: "41140309353560000102550020000125211111015035"; data: string(string) ex: "21/09/2021"; codigoEntidade: string(string) ex: "4"; categoriaEntidade: string(string) ex: "CLIENTE"; unidade: string(string) ex: "001"; numero: string(string) ex: "77917"; codigoProduto: number ex: 100017; sequencial: number ex: 1; quantidadeUnitaria: number ex: 1; quantidadeEmbalagem: number ex: 0; valor: number ex: 15; icms: number ex: 0; percReducaoBC: number ex: 0; percentualIPI: number ex: 0; percentualDesconto: number ex: 0; outrosAcrescimos: number ex: 0; valorSubTrib: number ex: 0; despesasAdicionais: number ex: 0; percentualISS: number ex: 0; simbologiaICMS: string(string) ex: "ST"; valorPIS: number ex: 0; valorCofins: number ex: 1; bcPisCofins: number ex: 15; aliqPis: number ex: 1; aliqCofins: number ex: 7; cstPis: string(string) ex: "01"; cstCofins: string(string) ex: "01"; cfop: string(string) ex: "5405"; cst: string(string) ex: "060"; bcIpi: number ex: 0; percReducaoBcSt: number ex: 0; valorUnitario: number ex: 15; ctCompra: number ex: 8; ctMedio: number ex: 8; ctTransf: number ex: 9; ctEmpresa: number ex: 9; ctFiscal: number ex: 8; prCompra: number ex: 9; tipoDcto: number ex: "EAQ"; valorIcms: number ex: 1.74; valorFCP: number ex: 0.2; aliqFCP: number ex: 2; serie: number ex: 1; cstIPI: string(string) ex: "99" }

## MovimentosMovProdD_V_1_7

array de { id: number ex: 80017; chavePrimaria: string(string) ex: "00119311984_1"; transacao: string(string) ex: "00119311984"; operacao: string(string) ex: "001193119841"; status: string(string) ex: "NORMAL"; chaveNfe: string(string) ex: "41140309353560000102550020000125211111015035"; data: string(string) ex: "21/09/2021"; codigoEntidade: string(string) ex: "4"; categoriaEntidade: string(string) ex: "CLIENTE"; unidade: string(string) ex: "001"; numero: string(string) ex: "77917"; codigoProduto: number ex: 100017; sequencial: number ex: 1; quantidadeUnitaria: number ex: 1; quantidadeEmbalagem: number ex: 0; valor: number ex: 15; icms: number ex: 0; percReducaoBC: number ex: 0; percentualIPI: number ex: 0; percentualDesconto: number ex: 0; outrosAcrescimos: number ex: 0; valorSubTrib: number ex: 0; despesasAdicionais: number ex: 0; percentualISS: number ex: 0; simbologiaICMS: string(string) ex: "ST"; valorPIS: number ex: 0; valorCofins: number ex: 1; bcPisCofins: number ex: 15; aliqPis: number ex: 1; aliqCofins: number ex: 7; cstPis: string(string) ex: "01"; cstCofins: string(string) ex: "01"; cfop: string(string) ex: "5405"; cst: string(string) ex: "060"; bcIpi: number ex: 0; percReducaoBcSt: number ex: 0; valorUnitario: number ex: 15; ctCompra: number ex: 8; ctMedio: number ex: 8; ctTransf: number ex: 9; ctEmpresa: number ex: 9; ctFiscal: number ex: 8; prCompra: number ex: 9; tipoDcto: number ex: "EAQ"; valorIcms: number ex: 1.74; valorFCP: number ex: 0.2; aliqFCP: number ex: 2; serie: number ex: 1; cstIPI: string(string) ex: "99"; dataEmissao: string(string) ex: "21/09/2021" }

## MovimentosMovProdD_V_1_8

array de { id: number ex: 95338; chavePrimaria: string ex: "00119326850_1"; transacao: string ex: "00119326850"; operacao: string ex: "001193268501"; tipo: string ex: 582117; status: string ex: "NORMAL"; chaveNfe: string ex: "41230307184848000167550010000782294193268503"; data: string ex: "29/03/2023"; codigoEntidade: string ex: 1; categoriaEntidade: string ex: "CLIENTE"; unidade: string ex: 1; numero: string ex: 78229; serie: string ex: 1; codBenef: string; codEstoque: number ex: 0; fatorEstoque: number ex: 0; codigoProduto: number ex: 112660; sequencial: number ex: 1; quantidadeUnitaria: number ex: 1; quantidadeEmbalagem: number ex: 1; embCom: string ex: "UN"; embTrib: string ex: "UN"; subTribEnt: number ex: 0; ipiDevol: number ex: 0; valorBcBruto: number ex: 6.99; valor: number ex: 6.99; icms: number ex: 0; icmsSimplesFed: number ex: 0; icmsCritica: number ex: 0; valorIcmsInf: number ex: 0.62; valorIcms: number ex: 0; valorFCP: number ex: 0; aliqFCP: number ex: 0; cstIPI: string; percReducaoBC: number ex: 0; percentualIPI: number ex: 0; percentualDesconto: number ex: 0; outrosAcrescimos: number ex: 0; valorSubTrib: number ex: 0; bcSubTribInf: number ex: 7.12; alSubTribinf: number ex: 16; despesasAdicionais: number ex: 0; percentualISS: number ex: 0; simbologiaICMS: string ex: "ST"; valorPIS: number ex: 0; valorCofins: number ex: 0; bcPisCofins: number ex: 0; aliqPis: number ex: 0; aliqCofins: number ex: 0; cstPis: string ex: 6; cstCofins: string ex: 6; cfop: string ex: 5405; cst: string ex: 48; bcIpi: number ex: 0; percReducaoBcSt: number ex: 0; valorUnitario: number ex: 6.99; ctCompra: number ex: 5.95; ctMedio: number ex: 6.025; ctTransf: number ex: 5.95; ctEmpresa: number ex: 5.95; ctFiscal: number ex: 5.95; prCompra: number ex: 5.13; tipoDcto: string ex: "EVL"; dataEmissao: string ex: "29/03/2023"; qtdeTrib: number ex: 1; qtdeCom: number ex: 1; comissaoValor: number ex: 0; comissaoBase: number ex: 0; comissaoPerc: number ex: 0; nextra: object { nextra1, nextra2, nextra3, nextra4, nextra5, nextra6, nextra7, nextra8, nextra9, nextra10, nextra11, nextra12, nextra13, nextra14, nextra15, nextra16, nextra17 }; cextra: object { cextra1, cextra2, cextra3, cextra4, cextra5 }; xml: object { seqXml, bcSubTribXml, alSubTribXml, subTribXml, icmsBcXml, icmsAliqXml, icmsValorXml } }

## MovimentosMovProdD_V_1_9

array de { id: number ex: 95338; chavePrimaria: string ex: "00119326850_1"; transacao: string ex: "00119326850"; operacao: string ex: "001193268501"; tipoMovimento: string(string) ex: "ENTRADA ou SAIDA"; tipo: string ex: 582117; status: string ex: "NORMAL"; chaveNfe: string ex: "41230307184848000167550010000782294193268503"; data: string ex: "29/03/2023"; codigoEntidade: string ex: 1; categoriaEntidade: string ex: "CLIENTE"; unidade: string ex: 1; numero: string ex: 78229; serie: string ex: 1; codBenef: string; codEstoque: number ex: 0; fatorEstoque: number ex: 0; codigoProduto: number ex: 112660; sequencial: number ex: 1; quantidadeUnitaria: number ex: 1; quantidadeEmbalagem: number ex: 1; embCom: string ex: "UN"; embTrib: string ex: "UN"; subTribEnt: number ex: 0; ipiDevol: number ex: 0; valorBcBruto: number ex: 6.99; valor: number ex: 6.99; icms: number ex: 0; icmsSimplesFed: number ex: 0; icmsCritica: number ex: 0; valorIcmsInf: number ex: 0.62; valorIcms: number ex: 0; valorFCP: number ex: 0; aliqFCP: number ex: 0; cstIPI: string; percReducaoBC: number ex: 0; percentualIPI: number ex: 0; percentualDesconto: number ex: 0; outrosAcrescimos: number ex: 0; valorSubTrib: number ex: 0; bcSubTribInf: number ex: 7.12; alSubTribinf: number ex: 16; despesasAdicionais: number ex: 0; percentualISS: number ex: 0; simbologiaICMS: string ex: "ST"; valorPIS: number ex: 0; valorCofins: number ex: 0; bcPisCofins: number ex: 0; aliqPis: number ex: 0; aliqCofins: number ex: 0; cstPis: string ex: 6; cstCofins: string ex: 6; cfop: string ex: 5405; cst: string ex: 48; bcIpi: number ex: 0; percReducaoBcSt: number ex: 0; valorUnitario: number ex: 6.99; ctCompra: number ex: 5.95; ctMedio: number ex: 6.025; ctTransf: number ex: 5.95; ctEmpresa: number ex: 5.95; ctFiscal: number ex: 5.95; prCompra: number ex: 5.13; tipoDcto: string ex: "EVL"; dataEmissao: string ex: "29/03/2023"; qtdeTrib: number ex: 1; qtdeCom: number ex: 1; comissaoValor: number ex: 0; comissaoBase: number ex: 0; comissaoPerc: number ex: 0; nextra: object { nextra1, nextra2, nextra3, nextra4, nextra5, nextra6, nextra7, nextra8, nextra9, nextra10, nextra11, nextra12, nextra13, nextra14, nextra15, nextra16, nextra17 }; cextra: object { cextra1, cextra2, cextra3, cextra4, cextra5 }; xml: object { seqXml, bcSubTribXml, alSubTribXml, subTribXml, icmsBcXml, icmsAliqXml, icmsValorXml } }

## MovimentosMovProdD_V_2_0

array de { id: number ex: 95338; chavePrimaria: string ex: "00119326850_1"; transacao: string ex: "00119326850"; operacao: string ex: "001193268501"; tipoMovimento: string(string) ex: "ENTRADA ou SAIDA"; tipo: string ex: 582117; status: string ex: "NORMAL"; chaveNfe: string ex: "41230307184848000167550010000782294193268503"; data: string ex: "29/03/2023"; hora: string ex: 38420; codigoEntidade: string ex: 1; categoriaEntidade: string ex: "CLIENTE"; unidade: string ex: 1; numero: string ex: 78229; serie: string ex: 1; codBenef: string; codEstoque: number ex: 0; fatorEstoque: number ex: 0; codigoProduto: number ex: 112660; sequencial: number ex: 1; quantidadeUnitaria: number ex: 1; quantidadeEmbalagem: number ex: 1; embCom: string ex: "UN"; embTrib: string ex: "UN"; subTribEnt: number ex: 0; ipiDevol: number ex: 0; valorBcBruto: number ex: 6.99; valor: number ex: 6.99; icms: number ex: 0; icmsSimplesFed: number ex: 0; icmsCritica: number ex: 0; valorIcmsInf: number ex: 0.62; valorIcms: number ex: 0; valorFCP: number ex: 0; aliqFCP: number ex: 0; cstIPI: string; percReducaoBC: number ex: 0; percentualIPI: number ex: 0; percentualDesconto: number ex: 0; outrosAcrescimos: number ex: 0; valorSubTrib: number ex: 0; bcSubTribInf: number ex: 7.12; alSubTribinf: number ex: 16; despesasAdicionais: number ex: 0; percentualISS: number ex: 0; simbologiaICMS: string ex: "ST"; valorPIS: number ex: 0; valorCofins: number ex: 0; bcPisCofins: number ex: 0; aliqPis: number ex: 0; aliqCofins: number ex: 0; cstPis: string ex: 6; cstCofins: string ex: 6; cfop: string ex: 5405; cst: string ex: 48; bcIpi: number ex: 0; percReducaoBcSt: number ex: 0; valorUnitario: number ex: 6.99; ctCompra: number ex: 5.95; ctMedio: number ex: 6.025; ctTransf: number ex: 5.95; ctEmpresa: number ex: 5.95; ctFiscal: number ex: 5.95; prCompra: number ex: 5.13; tipoDcto: string ex: "EVL"; dataEmissao: string ex: "29/03/2023"; qtdeTrib: number ex: 1; qtdeCom: number ex: 1; comissaoValor: number ex: 0; comissaoBase: number ex: 0; comissaoPerc: number ex: 0; nextra: object { nextra1, nextra2, nextra3, nextra4, nextra5, nextra6, nextra7, nextra8, nextra9, nextra10, nextra11, nextra12, nextra13, nextra14, nextra15, nextra16, nextra17 }; cextra: object { cextra1, cextra2, cextra3, cextra4, cextra5 }; xml: object { seqXml, bcSubTribXml, alSubTribXml, subTribXml, icmsBcXml, icmsAliqXml, icmsValorXml } }

## MovimentosVdaDet

Movimentos de produtos

array de { codigo: number ex: 10000; transacao: string ex: "50610009822"; status: string ex: "NORMAL"; data: string ex: "12/06/2019"; unidade: string ex: "001"; codigoProduto: number ex: 242934; sequencial: number ex: 1; quantidadeUnitaria: number(double) ex: 10; valor: number(double) ex: 6; percRedBC: number(double) ex: 12; valorDesc: number(double) ex: 6; valorAcFin: number(double) ex: 6; oferta: string ex: "S"; icms: number(double) ex: 18; codTrib: number(double) ex: 112541; pdv: string ex: "001"; cupom: string(string) ex: "001"; hora: string(string) ex: "11:35"; codigoCliente: number ex: 100005; cnpjCPF: string(string) ex: "12215213514"; valorDescFisc: number(double) ex: 18; valorAcFinFisc: number(double) ex: 18; cfop: string(string) ex: "5102"; cst: string(string) ex: "090"; cstPis: string(string) ex: "49"; aliqPis: number(double) ex: 1.65; aliqCofins: number(double) ex: 1.65; ccf: string(string) ex: "0001"; fcp: number(double) ex: 2; codigoBarras: string(string) ex: "0000000067959"; percRedBCFCP: number(double) ex: 0; bcICMS: number(double) ex: 0; bcFCP: number(double) ex: 0; valorICMS: number(double) ex: 0; valorFCP: number(double) ex: 0; stEfetRedBC: number(double) ex: 0; stEfetAliqST: number(double) ex: 0; stEfetAliqFCP: number(double) ex: 0; stEfetBC: number(double) ex: 0; stEfetValorICMS: number(double) ex: 0; natPisCofins: number(double) ex: 0; valorICMSDeson: number(double) ex: 0; vend_Codigo: number(double) ex: 0; stEfetValorFCP: number(double) ex: 0 }

## NfeByCupom

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, Nfe } }

## NfeByCupomV1_2

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, messages, content } }

## NlqInsert_V_1_0

{ origemApp: string(string) ex: "testeNLQInsomnia"; origemVersao: string(string) ex: "1.01.02"; origemIdentificador: string(string) ex: "RpInfo"; CodDcto: string(string) ex: "8885"; usuario: string(string) ex: "1"; ListProduto: array de object { Transacao, Operacao, Codigo, CodBarras, CodForn, FPgto, ListQtde } }

## NlqInsert_V_1_1

{ origemApp: string(string) ex: "testeNLQInsomnia"; origemVersao: string(string) ex: "1.01.02"; origemIdentificador: string(string) ex: "RpInfo"; CodDcto: string(string) ex: "8885"; usuario: string(string) ex: "1"; ListProduto: array de object { Transacao, Operacao, Codigo, CodBarras, CodForn, FPgto, ListQtde } }

## NotasSemRCMResponse_V_1_01

{ response: object { status, messages, content } }

## ObterCodPendResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, codigopendencia } }

## ObterCodsPendResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, codigospendencias } }

## ObterConfigDocumentoResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, documento } }

## ObterPendResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, pendencias } }

## OcorrenciaFDE

Ocorrência/crítica retornada pelo processamento do documento FDE no ERP

{ codigo: integer ex: 4009; mensagem: string ex: "A conta gerencial informada na pendência financeira deve existir no plano de contas gerencial: Informado: (211001) - Sequencial: (1)" }

## OcorrenciasEntidadeResponseV1

{ response: object { status, message, messages, ocorrencias } }

## ParcelasPendFinReq

Informações de cada parcela gerada no reparcelamento

{ valor: number(double) ex: 1500.75; dataVcto: string(date) ex: "30/09/2024"; port_codigo: string ex: "001"; espe_codigo: string ex: "CHQ" }

## PayloadBaixaPendFinReq

Payload para baixa de pendências financeiras

{ dctoCodigo: string ex: "2598"; dataMovimento: string(date) ex: "28/08/2024"; dataContabil: string(date) ex: "28/08/2024"; unidadeMovimento: string ex: "001"; unidadeAcessorios: string ex: "002"; contaBaixa: integer(int32) ex: 12345678; codigoHistorico: string ex: "0101"; complementoHistorico: string ex: "Baixa de pendências de fornecedores"; observacao: string ex: "Baixa realizada automaticamente pelo sistema"; especieCodigo: string ex: "CHQ"; numeroDocumento: string ex: "1234567890"; pendencias: array de `PendFinBxReq` (ver reference/schemas.md); dadosBancarios: `MovBcoBxReq` (ver reference/schemas.md) }

## PayloadReparcelamentoPendFinReq

Payload para reparcelamento de pendências financeiras

{ dctoCodigo: string ex: "2598"; dataMovimento: string(date) ex: "28/08/2024"; pfin_operacao: string ex: "OPR0000000012345678901234"; unidadeMovimento: string ex: "001"; observacao: string ex: "Reparcelamento em 3x de título vencido"; especieCodigo: string ex: "CHQ"; numeroDocumento: string ex: "1234567890"; parcelas: array de `ParcelasPendFinReq` (ver reference/schemas.md) }

## PedCompraResponseLV14

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, pedidos }; lastid: number ex: 1 }

## PedCompraResponseLV15

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, pedidosCompra }; lastid: number ex: 1 }

## PedCompraResponseLV17

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, pedidosCompra }; lastid: number ex: 1 }

## PedCompraResponseLV18

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, pedidosCompra }; lastid: number ex: 1 }

## PedCompraResponseLV19

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, pedidosCompra } }

## PedCompraResponseLV20

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, pedidosCompra } }

## PedCompraResponseLV21

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, pedidosCompra } }

## PedCompraResponseLV23

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, pedidosCompra } }

## PedCompraResponseV14

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, pedidos } }

## PedCompraResponseV18

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, pedidos } }

## PedCompraResponseV21

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, pedidos } }

## PedCompraResponseV23

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, pedidos } }

## PedCompraResponseV24

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, pedidos } }

## PedCompraResponse_V_1_00

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, maxCod, pedidos }; lastid: number ex: 1 }

## PedCompraResponse_V_1_01

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, maxCod, pedidos }; lastid: number ex: 1 }

## PedCompraSemRCMResponse_V_1_00

{ response: object { status, messages, pedidos } }

## PedVendaC

PedVendaC

array de { transacaoPedido: string(string) ex: "00110000010"; numero: integer ex: 23000; codigoUnidade: string(string) ex: "001"; numeroCarregamento: integer ex: 10; status: string(string) ex: "B"; dataMovimento: string(string) ex: "01/01/2020"; horaLcto: string(string) ex: "14:00:00"; dataBase: string(string) ex: "01/01/2020"; dataBaixa: string(string) ex: "02/01/2020"; codigoVendedor: string(string) ex: "001"; codigoRota: string(string) ex: "010"; codigoFpgto: string(string) ex: "630"; observacao: string(string) ex: "Observação"; valorFrete: number ex: 0; percFrete: number ex: 0; valorDesconto: number ex: 0; percDesconto: number ex: 0; valorDespAc: number ex: 0; percDespAc: number ex: 0; transacaoBaixa: string(string) ex: "00110000012"; pedidoCliente: string(string) ex: "137"; numeroCupom: string(string) ex: "147589"; codPDVBaixa: string(string) ex: "100"; unidadePDVBaixa: string(string) ex: "001"; seqEntrega: string(string) ex: "001"; itens: `PedVendaD` (ver reference/schemas.md) }

## PedVendaC_V2

{ transacao: string(string) ex: "00119307820"; numero: number ex: 5001; codigoUnidade: string(string) ex: "001"; numeroCarregamento: number ex: 0; status: string(string) ex: "B"; dataMovimento: string(string) ex: "17/06/2021"; horaLcto: string(string) ex: "16:37:45"; dataBase: string(string) ex: "17/06/2021"; dataBaixa: string(string) ex: "17/06/2021"; codigoVendedor: string(string) ex: ""; codigoRota: string(string) ex: ""; codigoFpgto: string(string) ex: "000"; observacao: string(string) ex: ""; valorFrete: number ex: 0; percFrete: number ex: 0; valorDesconto: number ex: 0; percDesconto: number ex: 0; valorDespAc: number ex: 0; percDespAc: number ex: 0; transacaoBaixa: string(string) ex: "00119307847"; pedidoCliente: string(string) ex: ""; numeroCupom: string(string) ex: ""; codPDVBaixa: string(string) ex: ""; unidadePDVBaixa: string(string) ex: ""; seqEntrega: string(string) ex: ""; codigoDocumento: string(string) ex: "0765"; codigoCliente: number ex: 4; codigoUsuario: number ex: 9999; codigoEspecie: string(string) ex: ""; codigoVincCliente: string(string) ex: ""; numeroConsolidado: number ex: 0; numeroTransProducao: string(string) ex: ""; itens: `PedVendaD_V2` (ver reference/schemas.md) }

## PedVendaC_V_1_2

{ transacao: string(string) ex: "00119307820"; numero: number ex: 5001; codigoUnidade: string(string) ex: "001"; numeroCarregamento: number ex: 0; status: string(string) ex: "B"; dataMovimento: string(string) ex: "17/06/2021"; horaLcto: string(string) ex: "16:37:45"; dataBase: string(string) ex: "17/06/2021"; dataBaixa: string(string) ex: "17/06/2021"; codigoVendedor: string(string) ex: ""; codigoRota: string(string) ex: ""; codigoFpgto: string(string) ex: "000"; observacao: string(string) ex: ""; valorFrete: number ex: 0; percFrete: number ex: 0; valorDesconto: number ex: 0; percDesconto: number ex: 0; valorDespAc: number ex: 0; percDespAc: number ex: 0; valorComissao: number ex: 0; transacaoBaixa: string(string) ex: "00119307847"; pedidoCliente: string(string) ex: ""; numeroCupom: string(string) ex: ""; codPDVBaixa: string(string) ex: ""; unidadePDVBaixa: string(string) ex: ""; seqEntrega: string(string) ex: ""; codigoDocumento: string(string) ex: "0765"; codigoCliente: number ex: 4; codigoUsuario: number ex: 9999; codigoEspecie: string(string) ex: ""; codigoVincCliente: string(string) ex: ""; numeroConsolidado: number ex: 0; numeroTransProducao: string(string) ex: ""; itens: `PedVendaD_V2` (ver reference/schemas.md) }

## PedVendaD

PedVendaD

array de { numeroCarregamento: integer ex: 10; codigoUnidade: string(string) ex: "001"; status: string(string) ex: "B"; codigoProduto: integer ex: 100009; sequencial: integer ex: 1; codigoRota: string(string) ex: ""; dataMovimento: string(string) ex: "01/01/2020"; dataBaixa: string(string) ex: "02/01/2020"; qtde: number ex: 120; qtdeEmbalagem: integer ex: 12; percDesconto: number ex: 0; valorTotal: number ex: 748.8; valorComissao: number ex: 0; qtdeOriginal: number ex: 10; precoVenda: number ex: 748.8; valorFlex: number ex: 0; valorUnitario: number ex: 6.24; numItemPedidoCliente: integer ex: 0 }

## PedVendaD_V2

PedVendaD

array de { numeroCarregamento: number ex: 0; codigoUnidade: string(string) ex: "001"; status: string(string) ex: "B"; codigoProduto: number ex: 100017; sequencial: number ex: 1; codigoRota: string(string) ex: ""; dataMovimento: string(string) ex: "17/06/2021"; dataBaixa: string(string) ex: "17/06/2021"; qtde: number ex: 1; qtdeEmbalagem: number ex: 0; percDesconto: number ex: 0; valorTotal: number ex: 15; valorComissao: number ex: 0; qtdeOriginal: number ex: 1; precoVenda: number ex: 15; valorFlex: number ex: 0; valorUnitario: number ex: 15; numItemPedidoCliente: number ex: 0; numeroPedido: number ex: 5001; simbologIcms: string(string) ex: "ST"; aliquotaIcms: number ex: 0; percReducBcIcms: number ex: 0; codigoEstoque: number ex: 1; serie: string(string); dataValidWms: string(string); substTribut: number ex: 0 }

## PedidoCompraDevolucaoLV10

{ itens: array de object { numeroPedido, codigo, devolver, quantidadeDevolver, obsDevolucao } }

## PedidoCompra_Inserir_Req_V_1_0

{ tipo: string ex: "C"; dctoCodigo: number ex: 2169; dataMvto: string ex: "27/05/2024"; unidLcto: string ex: 1; unidDest: string ex: 1; usuaCodigo: number ex: 172; fornCodigo: number ex: 169757; fpgtCodigo: number ex: 114; espeCodigo: string; valor: number ex: 10; tpFrete: string ex: "C"; percFrete: number ex: 10; adicFinanc: number ex: 10; despAcess: string; prazo: string; dtPrev: string; obs: string; tranCodigo: string; pedForn: string; formaDescarga: string ex: "N"; negTrocas: string; abatimentos: string; acrescimos: string; autorizacao: string ex: "A"; dataVencimento: string; itens: array de object { seq, tipo, prodCodigo, qtde, qemb, valor, tppreco, ipi, valoripi, desc, bonif, tpbonif, subtrib, tpsubtrib, acrescfin, distribuicao, strdesc, qtdepend, faquisicao, verba, sugestao, prpesquisa, dtpesquisa, concCodigo, prvenda, obsdev, unidDistrib, valminima, percfcpst, unidRedistrib, redistribuicao, codressup } }

## PedidoCompra_Inserir_res_V_1_0

{ response: object { status, messages, content } }

## PedidoCompra_LastRelease_V_1_0

{ response: object { status, messages, pedidos } }

## PedidoDeCompraLV14

PedidoDeCompra

array de { transacao: string ex: "00110000244"; id: number ex: 1; data: string ex: "28/08/2015"; unidade: string ex: "00000000000001"; fornecedor: string ex: "10006"; formaPagamento: string ex: "002"; valor: number(double) ex: 39.6; tipoFrete: string ex: "C"; percentualFrete: number(double) ex: 0; prazo: number ex: 0; observacao: string ex: ""; comprador: string ex: ""; dataPrevista: string ex: "07/05/2014"; status: string ex: "RECEBIDO"; itens: `ItensPedCompraV14` (ver reference/schemas.md) }

## PedidoDeCompraLV15

PedidoDeCompra

array de { transacao: string ex: "00110000244"; id: number ex: 1; idNfe: string ex: "41190877917680001632550010001253431790356458"; data: string ex: "28/08/2015"; unidade: string ex: "00000000000001"; fornecedor: string ex: "10006"; formaPagamento: string ex: "002"; valor: number(double) ex: 39.6; tipoFrete: string ex: "C"; percentualFrete: number(double) ex: 0; prazo: number ex: 0; observacao: string ex: ""; comprador: string ex: ""; dataPrevista: string ex: "07/05/2014"; status: string ex: "RECEBIDO"; itens: `ItensPedCompraV14` (ver reference/schemas.md) }

## PedidoDeCompraLV17

PedidoDeCompra

array de { transacao: string ex: "00110000244"; id: number ex: 1; idNfe: string ex: "41190877917680001632550010001253431790356458"; data: string ex: "28/08/2015"; unidade: string ex: "00000000000001"; fornecedor: string ex: "10006"; formaPagamento: string ex: "002"; valor: number(double) ex: 39.6; tipoFrete: string ex: "C"; percentualFrete: number(double) ex: 0; prazo: number ex: 0; observacao: string ex: ""; comprador: string ex: ""; dataPrevista: string ex: "07/05/2014"; status: string ex: "RECEBIDO"; itens: `ItensPedCompraV17` (ver reference/schemas.md) }

## PedidoDeCompraLV18

PedidoDeCompra

array de { transacao: string ex: "00110000244"; id: number ex: 1; idNfe: string ex: "41190877917680001632550010001253431790356458"; data: string ex: "28/08/2015"; unidade: string ex: "00000000000001"; fornecedor: string ex: "10006"; formaPagamento: string ex: "002"; valor: number(double) ex: 39.6; tipoFrete: string ex: "C"; percentualFrete: number(double) ex: 0; prazo: number ex: 0; observacao: string ex: ""; comprador: string ex: ""; dataPrevista: string ex: "07/05/2014"; status: string ex: "RECEBIDO"; transacaoEntrada: string ex: "00120000214"; numPed: number ex: 534728002; itens: array de object { codigoProduto, quantidadeUnitaria, tamanhoEmbalagem, quantidadeEmbalagem, valor, ipi, desconto, bonificacao, valorSubTrib, acrescimoFinanceiro, sequencial, valMinima, baixa } }

## PedidoDeCompraLV19

PedidoDeCompra

array de { transacao: string ex: "00110000244"; id: number ex: 1; idNfe: string ex: "41190877917680001632550010001253431790356458"; data: string ex: "28/08/2015"; unidade: string ex: "00000000000001"; fornecedor: string ex: "10006"; formaPagamento: string ex: "002"; valor: number(double) ex: 39.6; tipoFrete: string ex: "C"; percentualFrete: number(double) ex: 0; prazo: number ex: 0; observacao: string ex: ""; comprador: string ex: ""; dataPrevista: string ex: "07/05/2014"; status: string ex: "RECEBIDO"; transacaoEntrada: string ex: "00120000214"; itens: array de object { codigoProduto, quantidadeUnitaria, tamanhoEmbalagem, quantidadeEmbalagem, valor, ipi, desconto, bonificacao, valorSubTrib, acrescimoFinanceiro, sequencial, valMinima, baixa } }

## PedidoDeCompraLV20

PedidoDeCompra

array de { transacao: string ex: "00110000244"; id: number ex: 1; idNfe: string ex: "41190877917680001632550010001253431790356458"; data: string ex: "28/08/2015"; unidade: string ex: "00000000000001"; fornecedor: string ex: "10006"; formaPagamento: string ex: "002"; valor: number(double) ex: 39.6; tipoFrete: string ex: "C"; percentualFrete: number(double) ex: 0; prazo: number ex: 0; observacao: string ex: ""; comprador: string ex: ""; dataPrevista: string ex: "07/05/2014"; status: string ex: "RECEBIDO"; transacaoEntrada: string ex: "00120000214"; itens: array de object { codigoProduto, quantidadeUnitaria, tamanhoEmbalagem, quantidadeEmbalagem, valor, ipi, desconto, bonificacao, valorSubTrib, acrescimoFinanceiro, sequencial, valMinima, sugestao, baixa } }

## PedidoDeCompraLV21

PedidoDeCompra

array de { transacao: string ex: "00110000244"; id: number ex: 1; idNfe: string ex: "41190877917680001632550010001253431790356458"; data: string ex: "28/08/2015"; unidade: string ex: "00000000000001"; fornecedor: string ex: "10006"; formaPagamento: string ex: "002"; valor: number(double) ex: 39.6; tipoFrete: string ex: "C"; percentualFrete: number(double) ex: 0; prazo: number ex: 0; observacao: string ex: ""; comprador: string ex: ""; dataPrevista: string ex: "07/05/2014"; status: string ex: "RECEBIDO"; transacaoEntrada: string ex: "00120000214"; itens: array de object { codigoProduto, quantidadeUnitaria, tamanhoEmbalagem, quantidadeEmbalagem, valor, ipi, desconto, bonificacao, valorSubTrib, acrescimoFinanceiro, sequencial, valMinima, sugestao, baixa } }

## PedidoDeCompraLV23

PedidoDeCompra

array de { transacao: string ex: "00110000244"; id: number ex: 1; numPed: number ex: 14465284; idNfe: string ex: "41190877917680001632550010001253431790356458"; data: string ex: "28/08/2015"; unidade: string ex: "00000000000001"; fornecedor: string ex: "10006"; formaPagamento: string ex: "002"; valor: number(double) ex: 39.6; tipoFrete: string ex: "C"; percentualFrete: number(double) ex: 0; prazo: number ex: 0; observacao: string ex: ""; comprador: string ex: ""; dataPrevista: string ex: "07/05/2014"; status: string ex: "RECEBIDO"; autorizacao: string ex: "A"; transacaoEntrada: string ex: "00120000214"; numPedOriginal: string ex: "00215"; itens: array de object { codigoProduto, quantidadeUnitaria, tamanhoEmbalagem, quantidadeEmbalagem, valor, ipi, desconto, bonificacao, valorSubTrib, acrescimoFinanceiro, sequencial, valMinima, sugestao, baixa } }

## PedidoDeCompraLV24

PedidoDeCompra

array de { transacao: string ex: "00110000244"; id: number ex: 1; numPed: number ex: 14465284; idNfe: string ex: "41190877917680001632550010001253431790356458"; data: string ex: "28/08/2015"; unidade: string ex: "00000000000001"; fornecedor: string ex: "10006"; formaPagamento: string ex: "002"; valor: number(double) ex: 39.6; tipoFrete: string ex: "C"; percentualFrete: number(double) ex: 0; prazo: number ex: 0; observacao: string ex: ""; comprador: string ex: ""; dataPrevista: string ex: "07/05/2014"; dataRecebimento: string ex: "07/05/2014"; status: string ex: "RECEBIDO"; autorizacao: string ex: "A"; transacaoEntrada: string ex: "00120000214"; numPedOriginal: string ex: "00215"; itens: array de object { codigoProduto, quantidadeUnitaria, tamanhoEmbalagem, quantidadeEmbalagem, valor, ipi, desconto, bonificacao, valorSubTrib, acrescimoFinanceiro, sequencial, valMinima, sugestao, baixa } }

## PedidoDeCompraV14

PedidoDeCompra

{ transacao: string ex: "00110000244"; id: number ex: 1; data: string ex: "28/08/2015"; unidade: string ex: "00000000000001"; fornecedor: string ex: "10006"; formaPagamento: string ex: "002"; valor: number(double) ex: 39.6; tipoFrete: string ex: "C"; percentualFrete: number(double) ex: 0; prazo: number ex: 0; observacao: string ex: ""; comprador: string ex: ""; dataPrevista: string ex: "07/05/2014"; status: string ex: "RECEBIDO"; itens: `ItensPedCompraV14` (ver reference/schemas.md) }

## PedidoDeCompraV18

PedidoDeCompra

{ transacao: string ex: "00110000244"; id: number ex: 1; data: string ex: "28/08/2015"; unidade: string ex: "00000000000001"; fornecedor: string ex: "10006"; formaPagamento: string ex: "002"; valor: number(double) ex: 39.6; tipoFrete: string ex: "C"; percentualFrete: number(double) ex: 0; prazo: number ex: 0; observacao: string ex: ""; comprador: string ex: ""; dataPrevista: string ex: "07/05/2014"; status: string ex: "RECEBIDO"; transacaoEntrada: string ex: "00110010379"; itens: `ItensPedCompraV14` (ver reference/schemas.md) }

## PedidoDeCompraV21

PedidoDeCompra

{ transacao: string ex: "00110000244"; id: number ex: 1; data: string ex: "28/08/2015"; unidade: string ex: "00000000000001"; fornecedor: string ex: "10006"; formaPagamento: string ex: "002"; valor: number(double) ex: 39.6; tipoFrete: string ex: "C"; percentualFrete: number(double) ex: 0; prazo: number ex: 0; observacao: string ex: ""; comprador: string ex: ""; dataPrevista: string ex: "07/05/2014"; status: string ex: "RECEBIDO"; transacaoEntrada: string ex: "00110010379"; itens: `ItensPedCompraV14` (ver reference/schemas.md) }

## PedidoDeCompra_V_1_00

PedidoDeCompra

array de { transacao: string ex: "00110000244"; id: number ex: 1; data: string ex: "28/08/2015"; unidade: string ex: "00000000000001"; fornecedor: string ex: "10006"; formaPagamento: string ex: "002"; valor: number(double) ex: 39.6; tipoFrete: string ex: "C"; percentualFrete: number(double) ex: 0; prazo: number ex: 0; observacao: string ex: ""; itens: `ItensPedCompra_V_1_00` (ver reference/schemas.md) }

## PedidoDeCompra_V_1_01

PedidoDeCompra

array de { transacao: string ex: "00110000244"; id: number ex: 1; data: string ex: "28/08/2015"; unidade: string ex: "00000000000001"; fornecedor: string ex: "10006"; formaPagamento: string ex: "002"; valor: number(double) ex: 39.6; tipoFrete: string ex: "C"; percentualFrete: number(double) ex: 0; prazo: number ex: 0; observacao: string ex: ""; itens: `ItensPedCompra_V_1_01` (ver reference/schemas.md) }

## PedidoVenda

{ codigoProduto: number ex: 100170; qtdUnitaria: number(double) ex: 1; qtdEmbalagem: number ex: 2; valorProduto: number(double) ex: 2.5; percDesconto: number(double) ex: 0 }

## PedidoVendaV18

{ unidade: string(string) ex: "001"; data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 103055; formaPagamento: string(string) ex: "001"; numeroPedidoCliente: string ex: "35214"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; desconto: number ex: 2.4; codigoDocumento: string(string) ex: "6100"; nome: string(string) ex: "Nome teste"; email: string(string) ex: ""; cpf: string(string) ex: "51654616451"; rg: string(string) ex: "546546511"; cnpj: string(string) ex: "51654616846551"; inscricaoEstadual: string(string) ex: "56516544"; endereco: string(string) ex: "Avenida Presidente Getúlio Vargas ss"; numero: string(string) ex: "4272"; complemento: string(string) ex: "4º Andar - Desenv"; bairro: string(string) ex: "Rebouças s"; cidade: integer ex: 10000; cep: string(string) ex: "80610040"; fone: string(string) ex: "32220888"; turnoEntrega: string(string) ex: "Manhã das 09:00 as 11:10"; dataPrevista: string(string) ex: "09/04/2019"; valorFrete: number(double) ex: 2.5; despesaAcessoria: number(double) ex: 1.2; camposExtras: `ItensCamposExtrasV1` (ver reference/schemas.md); itens: `ItensPedVendaV2` (ver reference/schemas.md) }

## PedidoVendaV19

{ unidade: string(string) ex: "001"; data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 103055; formaPagamento: string(string) ex: "001"; numeroPedidoCliente: string ex: "35214"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; desconto: number ex: 2.4; codigoDocumento: string(string) ex: "6100"; nome: string(string) ex: "Nome teste"; email: string(string) ex: ""; cpf: string(string) ex: "51654616451"; rg: string(string) ex: "546546511"; cnpj: string(string) ex: "51654616846551"; inscricaoEstadual: string(string) ex: "56516544"; endereco: string(string) ex: "Avenida Presidente Getúlio Vargas ss"; numero: string(string) ex: "4272"; complemento: string(string) ex: "4º Andar - Desenv"; bairro: string(string) ex: "Rebouças s"; cidade: integer ex: 10000; cep: string(string) ex: "80610040"; fone: string(string) ex: "32220888"; turnoEntrega: string(string) ex: "Manhã das 09:00 as 11:10"; dataPrevista: string(string) ex: "09/04/2019"; valorFrete: number(double) ex: 2.5; despesaAcessoria: number(double) ex: 1.2; camposExtras: `ItensCamposExtrasV1` (ver reference/schemas.md); itens: `ItensPedVendaV3` (ver reference/schemas.md) }

## PedidoVendaV2

{ unidade: string(string) ex: "001"; data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 103055; formaPagamento: string(string) ex: "001"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; desconto: integer ex: 0; codigoDocumento: string(string) ex: "6100"; nome: string(string) ex: "Nome teste"; email: string(string) ex: ""; cpf: string(string) ex: "51654616451"; rg: string(string) ex: "546546511"; cnpj: string(string) ex: "51654616846551"; inscricaoEstadual: string(string) ex: "56516544"; endereco: string(string) ex: "Avenida Presidente Getúlio Vargas ss"; numero: string(string) ex: "4272"; complemento: string(string) ex: "4º Andar - Desenv"; bairro: string(string) ex: "Rebouças s"; cidade: integer ex: 10000; cep: string(string) ex: "80610040"; fone: string(string) ex: "32220888"; itens: `ItensPedVendaV2` (ver reference/schemas.md) }

## PedidoVendaV20

{ unidade: string(string) ex: "001"; data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 103055; formaPagamento: string(string) ex: "001"; numeroPedidoCliente: string ex: "35214"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; desconto: number ex: 2.4; codigoDocumento: string(string) ex: "6100"; nome: string(string) ex: "Nome teste"; email: string(string) ex: ""; cpf: string(string) ex: "51654616451"; rg: string(string) ex: "546546511"; cnpj: string(string) ex: "51654616846551"; inscricaoEstadual: string(string) ex: "56516544"; endereco: string(string) ex: "Avenida Presidente Getúlio Vargas ss"; numero: string(string) ex: "4272"; complemento: string(string) ex: "4º Andar - Desenv"; bairro: string(string) ex: "Rebouças s"; cidade: integer ex: 10000; cep: string(string) ex: "80610040"; fone: string(string) ex: "32220888"; turnoEntrega: string(string) ex: "Manhã das 09:00 as 11:10"; dataPrevista: string(string) ex: "09/04/2019"; valorFrete: number(double) ex: 2.5; despesaAcessoria: number(double) ex: 1.2; transportador: string(string) ex: "00001"; camposExtras: `ItensCamposExtrasV1` (ver reference/schemas.md); itens: `ItensPedVendaV3` (ver reference/schemas.md) }

## PedidoVendaV21

{ unidade: string(string) ex: "001"; data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 103055; formaPagamento: string(string) ex: "001"; numeroPedidoCliente: string ex: "35214"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; desconto: number ex: 2.4; codigoDocumento: string(string) ex: "6100"; nome: string(string) ex: "Nome teste"; email: string(string) ex: ""; cpf: string(string) ex: "51654616451"; rg: string(string) ex: "546546511"; cnpj: string(string) ex: "51654616846551"; inscricaoEstadual: string(string) ex: "56516544"; endereco: string(string) ex: "Avenida Presidente Getúlio Vargas ss"; numero: string(string) ex: "4272"; complemento: string(string) ex: "4º Andar - Desenv"; bairro: string(string) ex: "Rebouças s"; cidade: integer ex: 10000; cep: string(string) ex: "80610040"; fone: string(string) ex: "32220888"; turnoEntrega: string(string) ex: "Manhã das 09:00 as 11:10"; dataPrevista: string(string) ex: "09/04/2019"; valorFrete: number(double) ex: 2.5; despesaAcessoria: number(double) ex: 1.2; transportador: string(string) ex: "00001"; camposExtras: `ItensCamposExtrasV1` (ver reference/schemas.md); itens: `ItensPedVendaV21` (ver reference/schemas.md) }

## PedidoVendaV22

{ unidade: string(string) ex: "001"; unidadeRetirada: string(string) ex: "002"; data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 103055; formaPagamento: string(string) ex: "001"; numeroPedidoCliente: string ex: "35214"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; desconto: number ex: 2.4; codigoDocumento: string(string) ex: "6100"; nome: string(string) ex: "Nome teste"; email: string(string) ex: ""; cpf: string(string) ex: "51654616451"; rg: string(string) ex: "546546511"; cnpj: string(string) ex: "51654616846551"; inscricaoEstadual: string(string) ex: "56516544"; endereco: string(string) ex: "Avenida Presidente Getúlio Vargas ss"; numero: string(string) ex: "4272"; complemento: string(string) ex: "4º Andar - Desenv"; bairro: string(string) ex: "Rebouças s"; cidade: integer ex: 10000; cep: string(string) ex: "80610040"; fone: string(string) ex: "32220888"; turnoEntrega: string(string) ex: "Manhã das 09:00 as 11:10"; dataPrevista: string(string) ex: "09/04/2019"; valorFrete: number(double) ex: 2.5; despesaAcessoria: number(double) ex: 1.2; transportador: string(string) ex: "00001"; camposExtras: `ItensCamposExtrasV1` (ver reference/schemas.md); itens: `ItensPedVendaV22` (ver reference/schemas.md) }

## PedidoVendaV23

{ unidade: string(string) ex: "001"; unidadeRetirada: string(string) ex: "002"; data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 103055; formaPagamento: string(string) ex: "001"; numeroPedidoCliente: string ex: "35214"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; desconto: number ex: 2.4; codigoDocumento: string(string) ex: "6100"; nome: string(string) ex: "Nome teste"; email: string(string) ex: ""; cpf: string(string) ex: "51654616451"; rg: string(string) ex: "546546511"; cnpj: string(string) ex: "51654616846551"; inscricaoEstadual: string(string) ex: "56516544"; endereco: string(string) ex: "Avenida Presidente Getúlio Vargas ss"; numero: string(string) ex: "4272"; complemento: string(string) ex: "4º Andar - Desenv"; bairro: string(string) ex: "Rebouças s"; cidade: integer ex: 10000; cep: string(string) ex: "80610040"; fone: string(string) ex: "32220888"; turnoEntrega: string(string) ex: "Manhã das 09:00 as 11:10"; dataPrevista: string(string) ex: "09/04/2019"; valorFrete: number(double) ex: 2.5; despesaAcessoria: number(double) ex: 1.2; transportador: string(string) ex: "00001"; camposExtras: `ItensCamposExtrasV1` (ver reference/schemas.md); itens: `ItensPedVendaV22` (ver reference/schemas.md); financeiro: `Financeiro_V_1_1` (ver reference/schemas.md) }

## PedidoVendaV25

{ unidade: string(string) ex: "001"; origem: string(string) ex: "Identificador do consumidor do serviço, pode informar qualquer identificador, exemplo: nome do aplicativo ou nome da empresa"; unidadeRetirada: string(string) ex: "002"; data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 103055; formaPagamento: string(string) ex: "001"; numeroPedidoCliente: string ex: "35214"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; desconto: number ex: 2.4; codigoDocumento: string(string) ex: "6100"; nome: string(string) ex: "Nome teste"; email: string(string) ex: ""; cpf: string(string) ex: "51654616451"; rg: string(string) ex: "546546511"; cnpj: string(string) ex: "51654616846551"; inscricaoEstadual: string(string) ex: "56516544"; endereco: string(string) ex: "Avenida Presidente Getúlio Vargas ss"; numero: string(string) ex: "4272"; complemento: string(string) ex: "4º Andar - Desenv"; bairro: string(string) ex: "Rebouças s"; cidade: integer ex: 10000; cep: string(string) ex: "80610040"; fone: string(string) ex: "32220888"; turnoEntrega: string(string) ex: "Manhã das 09:00 as 11:10"; dataPrevista: string(string) ex: "09/04/2019"; valorFrete: number(double) ex: 2.5; despesaAcessoria: number(double) ex: 1.2; transportador: string(string) ex: "00001"; camposExtras: `ItensCamposExtrasV1` (ver reference/schemas.md); itens: `ItensPedVendaV22` (ver reference/schemas.md); financeiro: `Financeiro_V_1_1` (ver reference/schemas.md) }

## PedidoVendaV26

{ unidade: string(string) ex: "001"; origem: string(string) ex: "Identificador do consumidor do serviço, pode informar qualquer identificador, exemplo: nome do aplicativo ou nome da empresa"; unidadeRetirada: string(string) ex: "002"; data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 103055; formaPagamento: string(string) ex: "001"; numeroPedidoCliente: string ex: "35214"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; desconto: number ex: 2.4; codigoDocumento: string(string) ex: "6100"; nome: string(string) ex: "Nome teste"; email: string(string) ex: ""; cpf: string(string) ex: "51654616451"; rg: string(string) ex: "546546511"; cnpj: string(string) ex: "51654616846551"; inscricaoEstadual: string(string) ex: "56516544"; endereco: string(string) ex: "Avenida Presidente Getúlio Vargas ss"; numero: string(string) ex: "4272"; complemento: string(string) ex: "4º Andar - Desenv"; bairro: string(string) ex: "Rebouças s"; cidade: integer ex: 10000; cep: string(string) ex: "80610040"; fone: string(string) ex: "32220888"; turnoEntrega: string(string) ex: "Manhã das 09:00 as 11:10"; dataPrevista: string(string) ex: "09/04/2019"; valorFrete: number(double) ex: 2.5; despesaAcessoria: number(double) ex: 1.2; transportador: string(string) ex: "00001"; camposExtras: `ItensCamposExtrasV1` (ver reference/schemas.md); itens: `ItensPedVendaV22` (ver reference/schemas.md); financeiro: `Financeiro_V_2_6` (ver reference/schemas.md) }

## PedidoVendaV27

{ unidade: string(string) ex: "001"; origem: string(string) ex: "Identificador do consumidor do serviço, pode informar qualquer identificador, exemplo: nome do aplicativo ou nome da empresa"; unidadeRetirada: string(string) ex: "002"; data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 103055; formaPagamento: string(string) ex: "001"; numeroPedidoCliente: string ex: "35214"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; desconto: number ex: 2.4; codigoDocumento: string(string) ex: "6100"; nome: string(string) ex: "Nome teste"; email: string(string) ex: ""; cpf: string(string) ex: "51654616451"; rg: string(string) ex: "546546511"; cnpj: string(string) ex: "51654616846551"; inscricaoEstadual: string(string) ex: "56516544"; endereco: string(string) ex: "Avenida Presidente Getúlio Vargas ss"; numero: string(string) ex: "4272"; complemento: string(string) ex: "4º Andar - Desenv"; bairro: string(string) ex: "Rebouças s"; cidade: integer ex: 10000; cep: string(string) ex: "80610040"; fone: string(string) ex: "32220888"; turnoEntrega: string(string) ex: "Manhã das 09:00 as 11:10"; dataPrevista: string(string) ex: "09/04/2019"; valorFrete: number(double) ex: 2.5; despesaAcessoria: number(double) ex: 1.2; transportador: string(string) ex: "00001"; camposExtras: `ItensCamposExtrasV1` (ver reference/schemas.md); itens: `ItensPedVendaV27` (ver reference/schemas.md); financeiro: `Financeiro_V_2_7` (ver reference/schemas.md) }

## PedidoVendaV28

{ unidade: string(string) ex: "001"; origem: string(string) ex: "Identificador do consumidor do serviço, pode informar qualquer identificador, exemplo: nome do aplicativo ou nome da empresa"; unidadeRetirada: string(string) ex: "002"; data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 103055; formaPagamento: string(string) ex: "001"; numeroPedidoCliente: string ex: "35214"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; desconto: number ex: 2.4; codigoDocumento: string(string) ex: "6100"; nome: string(string) ex: "Nome teste"; email: string(string) ex: ""; cpf: string(string) ex: "51654616451"; rg: string(string) ex: "546546511"; cnpj: string(string) ex: "51654616846551"; inscricaoEstadual: string(string) ex: "56516544"; endereco: string(string) ex: "Avenida Presidente Getúlio Vargas ss"; numero: string(string) ex: "4272"; complemento: string(string) ex: "4º Andar - Desenv"; bairro: string(string) ex: "Rebouças s"; cidade: integer ex: 10000; cep: string(string) ex: "80610040"; fone: string(string) ex: "32220888"; turnoEntrega: string(string) ex: "Manhã das 09:00 as 11:10"; dataPrevista: string(string) ex: "09/04/2019"; valorFrete: number(double) ex: 2.5; despesaAcessoria: number(double) ex: 1.2; transportador: string(string) ex: "00001"; rota: string(string) ex: "002"; camposExtras: `ItensCamposExtrasV1` (ver reference/schemas.md); itens: `ItensPedVendaV27` (ver reference/schemas.md); financeiro: `Financeiro_V_2_8` (ver reference/schemas.md) }

## PedidoVendaV29

**PedidoVendaV28** = object { unidade, origem, unidadeRetirada, data, codigoCliente, formaPagamento, numeroPedidoCliente, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, email, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, turnoEntrega, dataPrevista, valorFrete, despesaAcessoria, transportador, rota, camposExtras, itens, financeiro } & { entregador: string(string) ex: "002" }

## PedidoVendaV3

{ unidade: string(string) ex: "001"; data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 103055; formaPagamento: string(string) ex: "001"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; desconto: integer ex: 0; codigoDocumento: string(string) ex: "6100"; nome: string(string) ex: "Nome teste"; cpf: string(string) ex: "51654616451"; rg: string(string) ex: "546546511"; cnpj: string(string) ex: "51654616846551"; inscricaoEstadual: string(string) ex: "56516544"; endereco: string(string) ex: "Avenida Presidente Getúlio Vargas ss"; numero: string(string) ex: "4272"; complemento: string(string) ex: "4º Andar - Desenv"; bairro: string(string) ex: "Rebouças s"; cidade: integer ex: 10000; cep: string(string) ex: "80610040"; fone: string(string) ex: "32220888"; itens: `ItensPedVendaV2` (ver reference/schemas.md) }

## PedidoVendaV30

**PedidoVendaV29** = `PedidoVendaV28` (ver reference/schemas.md) & object { entregador } & { dados_adicionais: string(string) ex: "Dados adicionais para a Nfe" }

## PedidoVendaV31

{ unidade: string(string) ex: "001"; origem: string(string) ex: "Identificador do consumidor do serviço, pode informar qualquer identificador, exemplo: nome do aplicativo ou nome da empresa"; unidadeRetirada: string(string) ex: "002"; data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 103055; formaPagamento: string(string) ex: "001"; numeroPedidoCliente: string ex: "35214"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; desconto: number ex: 2.4; codigoDocumento: string(string) ex: "6100"; nome: string(string) ex: "Nome teste"; email: string(string) ex: ""; cpf: string(string) ex: "51654616451"; rg: string(string) ex: "546546511"; cnpj: string(string) ex: "51654616846551"; inscricaoEstadual: string(string) ex: "56516544"; endereco: string(string) ex: "Avenida Presidente Getúlio Vargas ss"; numero: string(string) ex: "4272"; complemento: string(string) ex: "4º Andar - Desenv"; bairro: string(string) ex: "Rebouças s"; cidade: integer ex: 10000; cep: string(string) ex: "80610040"; fone: string(string) ex: "32220888"; turnoEntrega: string(string) ex: "Manhã das 09:00 as 11:10"; dataPrevista: string(string) ex: "09/04/2019"; valorFrete: number(double) ex: 2.5; despesaAcessoria: number(double) ex: 1.2; transportador: string(string) ex: "00001"; rota: string(string) ex: "002"; entregador: string(string) ex: "002"; dados_adicionais: string(string) ex: "Dados adicionais para a Nfe"; camposExtras: `ItensCamposExtrasV1` (ver reference/schemas.md); itens: `ItensPedVendaV31` (ver reference/schemas.md); financeiro: `Financeiro_V_2_8` (ver reference/schemas.md) }

## PedidoVendaV32

**PedidoVendaV31** = object { unidade, origem, unidadeRetirada, data, codigoCliente, formaPagamento, numeroPedidoCliente, codigoVendedor, observacao, especie, desconto, codigoDocumento, nome, email, cpf, rg, cnpj, inscricaoEstadual, endereco, numero, complemento, bairro, cidade, cep, fone, turnoEntrega, dataPrevista, valorFrete, despesaAcessoria, transportador, rota, entregador, dados_adicionais, camposExtras, itens, financeiro } & { origemDataHora: string(dd/MM/yyyy HH:mm:ss) ex: "26/02/2025 13:31:14"; taxaEntrega: number(number) ex: 0.0 }

## PedidoVendaV33

**PedidoVendaV32** = `PedidoVendaV31` (ver reference/schemas.md) & object { origemDataHora, taxaEntrega } & { camposExtras: `ItensCamposExtrasV1` (ver reference/schemas.md); itens: `ItensPedVendaV33` (ver reference/schemas.md); financeiro: `Financeiro_V_2_8` (ver reference/schemas.md) }

## PedidoVendaV4

{ unidade: string(string) ex: "001"; data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 103055; formaPagamento: string(string) ex: "001"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; desconto: integer ex: 0; codigoDocumento: string(string) ex: "6100"; nome: string(string) ex: "Nome teste"; email: string(string) ex: ""; cpf: string(string) ex: "51654616451"; rg: string(string) ex: "546546511"; cnpj: string(string) ex: "51654616846551"; inscricaoEstadual: string(string) ex: "56516544"; endereco: string(string) ex: "Avenida Presidente Getúlio Vargas ss"; numero: string(string) ex: "4272"; complemento: string(string) ex: "4º Andar - Desenv"; bairro: string(string) ex: "Rebouças s"; cidade: integer ex: 10000; cep: string(string) ex: "80610040"; fone: string(string) ex: "32220888"; turnoEntrega: string(string) ex: "Manhã das 09:00 as 11:10"; dataPrevista: string(string) ex: "09/04/2019"; valorFrete: number(double) ex: 2.5; itens: `ItensPedVendaV2` (ver reference/schemas.md) }

## PedidoVendaV5

{ unidade: string(string) ex: "001"; data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 103055; formaPagamento: string(string) ex: "001"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; desconto: number ex: 2.4; codigoDocumento: string(string) ex: "6100"; nome: string(string) ex: "Nome teste"; email: string(string) ex: ""; cpf: string(string) ex: "51654616451"; rg: string(string) ex: "546546511"; cnpj: string(string) ex: "51654616846551"; inscricaoEstadual: string(string) ex: "56516544"; endereco: string(string) ex: "Avenida Presidente Getúlio Vargas ss"; numero: string(string) ex: "4272"; complemento: string(string) ex: "4º Andar - Desenv"; bairro: string(string) ex: "Rebouças s"; cidade: integer ex: 10000; cep: string(string) ex: "80610040"; fone: string(string) ex: "32220888"; turnoEntrega: string(string) ex: "Manhã das 09:00 as 11:10"; dataPrevista: string(string) ex: "09/04/2019"; valorFrete: number(double) ex: 2.5; camposExtras: `ItensCamposExtrasV1` (ver reference/schemas.md); itens: `ItensPedVendaV2` (ver reference/schemas.md) }

## PedidoVendaV7

{ unidade: string(string) ex: "001"; data: string(string) ex: "21/11/2014"; codigoCliente: integer ex: 103055; formaPagamento: string(string) ex: "001"; numeroPedidoCliente: string ex: "35214"; codigoVendedor: string(string) ex: "103"; observacao: string(string) ex: "observações"; especie: integer ex: 1; desconto: number ex: 2.4; codigoDocumento: string(string) ex: "6100"; nome: string(string) ex: "Nome teste"; email: string(string) ex: ""; cpf: string(string) ex: "51654616451"; rg: string(string) ex: "546546511"; cnpj: string(string) ex: "51654616846551"; inscricaoEstadual: string(string) ex: "56516544"; endereco: string(string) ex: "Avenida Presidente Getúlio Vargas ss"; numero: string(string) ex: "4272"; complemento: string(string) ex: "4º Andar - Desenv"; bairro: string(string) ex: "Rebouças s"; cidade: integer ex: 10000; cep: string(string) ex: "80610040"; fone: string(string) ex: "32220888"; turnoEntrega: string(string) ex: "Manhã das 09:00 as 11:10"; dataPrevista: string(string) ex: "09/04/2019"; valorFrete: number(double) ex: 2.5; camposExtras: `ItensCamposExtrasV1` (ver reference/schemas.md); itens: `ItensPedVendaV2` (ver reference/schemas.md) }

## PedidosClienteFlexResponse

{ response: object { status, message, messages, pedidos } }

## PendFinBxReq

Pendência financeira individual a ser baixada

{ pfin_operacao: string ex: "OPR0000012345678901234567"; valorBaixa: number(double) ex: 1500.75; observacao: string ex: "Baixa parcial do título" }

## PendenciaEstoqueDto

{ operacao: string; transacao: string; status: string; dataMvto: string ex: "dd/MM/yyyy"; unidOrigem: string; unidDestino: string; prodCodigo: integer; cpesCodigo: string; cpesTipo: string; catEntidade: string; codEntidade: integer; sequencial: integer; valor: number(double); ctCompra: number(double); ctTransf: number(double); ctFiscal: number(double); ctEmpresa: number(double); ctMedio: number(double); qemb: integer; qtde: number(double); qtdeBx: number(double); transacaoBx: string; dataBaixa: string ex: "dd/MM/yyyy"; bxCompleta: string; icms: number(double); percRedBC: number(double); simbICMS: string; espeCodigo: string; dataEntrega: string ex: "dd/MM/yyyy"; dataValidade: string ex: "dd/MM/yyyy"; lastID: string; action: string }

## PendenciaFDE

Pendência financeira associada ao documento FDE

{ dataVcto: string ex: "01/01/2022"; dataEmissao: string ex: "01/01/2022"; conta: integer ex: 211001; especie: string ex: "0022"; formaPgto: string ex: "101"; localPgto: string ex: "202"; portador: string ex: "303"; historico: string ex: "1001"; moeda: string ex: "002"; vendedor: string ex: "2233"; pdv: string ex: "001"; entidade: integer ex: 18024; unidade: string ex: "001"; cnpjcpf: string ex: "07339957999"; complemento: string ex: ""; numeroDcto: string ex: ""; parcela: integer ex: 1; nparcelas: integer ex: 3; valor: number(double) ex: 150.0; juros: number(double) ex: 0.0; multa: number(double) ex: 0.0; mora: number(double) ex: 0.0; acrescimos: number(double) ex: 0.0; descontos: number(double) ex: 0.0; abatimentos: number(double) ex: 0.0; txadm: number(double) ex: 0.0; corrmonet: number(double) ex: 0.0; valorcomissao: number(double) ex: 0.0; observacao: string ex: ""; cmc7: string ex: ""; nossoNumero: string ex: ""; codigoBarras: string ex: ""; linhaDigitavel: string ex: ""; autorizador: string ex: "5"; cupom: string ex: ""; qrcodepix: string ex: "" }

## PendenciaFinanceira_V_1_0

{ codigo: number ex: 435665; transacao: string ex: "00119321815"; operacao: string ex: "001193218156"; status: string ex: "CANCELADO"; datalcto: string ex: "21/12/2022"; datamvto: string ex: "21/12/2022"; datavcto: string ex: "21/12/2022"; dataautpgto: string ex: "25/01/2025"; autorizada: string ex: "25/01/2025"; transbaixa: string; databaixa: string(nullable); pgerConta: number ex: 112106; unidCodigo: string ex: 2; espeCodigo: string ex: "0110"; fpgtCodigo: string; lpgtCodigo: string; portCodigo: string; histCodigo: string ex: "6000"; vendCodigo: string ex: "001"; pdvsCodigo: string ex: "109"; catentidade: string ex: "C"; codentidade: string ex: 12122; cnpjcpf: string ex: "631.473.240-95"; complemento: string ex: "56243001;"; numerodcto: string ex: 56243001; parcela: string ex: 1; pr: string ex: "R"; valor: number ex: 1.5; juros: number ex: 0; multa: number ex: 0; mora: number ex: 0; acrescimos: number ex: 0; descontos: number ex: 0; abatimentos: number ex: 0; txadm: number ex: 0; corrmonet: number ex: 0; valorcomissao: number ex: 5.5; mapacarga: number ex: 1; lote: number ex: 937115; usuautpgto: string ex: "103"; contacontabil: number ex: 112101; baixaparcial: number ex: 0; vinculadas: string ex: "N"; lotecnab: string ex: 0; cupom: string; nparcelas: number ex: 1 }

## PendenciaFinanceira_V_1_1

**PendenciaFinanceira_V_1_0** = object { codigo, transacao, operacao, status, datalcto, datamvto, datavcto, dataautpgto, autorizada, transbaixa, databaixa, pgerConta, unidCodigo, espeCodigo, fpgtCodigo, lpgtCodigo, portCodigo, histCodigo, vendCodigo, pdvsCodigo, catentidade, codentidade, cnpjcpf, complemento, numerodcto, parcela, pr, valor, juros, multa, mora, acrescimos, descontos, abatimentos, txadm, corrmonet, valorcomissao, mapacarga, lote, usuautpgto, contacontabil, baixaparcial, vinculadas, lotecnab, cupom, nparcelas } & { dataemissao: string(dd/MM/yyyy) ex: "21/03/2025" }

## Pendencias

{ operacao: string(string) ex: "001100002771"; transacao: string(string) ex: "00110000277"; status: string(string) ex: "PENDENTE"; dataMvto: string(string) ex: "20/05/2016"; unidadeOrigem: string(string) ex: "001"; unidadeDestino: string(string) ex: "002"; codigoProduto: number ex: 218910; codigoPes: string(string) ex: "100"; tipoPes: string(string) ex: "TC"; categoriaEntidade: string ex: "SEM_ENTIDADE"; codigoEntidade: number ex: 10006; sequencial: number ex: 1; valor: number(double) ex: 10.6; ctCompra: number(double) ex: 0.93; ctTransf: number(double) ex: 0.93; ctFiscal: number(double) ex: 0.93; ctEmpresa: number(double) ex: 0.93; ctMedio: number(double) ex: 0.93; qEmb: number ex: 1; qtde: number ex: 1; qtdeBaixada: number ex: 0; transacaoBaixa: string ex: ""; dataBaixa: string(string) ex: "19/04/2018"; bxCompleta: string ex: ""; icms: number(double) ex: 0; percRedBC: number(double) ex: 0; simbICMS: string ex: ""; codigoEspecie: string(string) ex: ""; dataEntrega: string(string) ex: "21/10/2016"; dataValidade: string ex: "19/04/2018"; ID: string ex: "1.1408761011E10" }

## PesquisaDePreco

{ items: array de object { codBarras, codConcorrente, codPesq, codPreco, codProduto, codUnidade, data, espe_codigo, marca, motSemPesq, obs, ruptura, updateCodPreco, usuario, validade, precos } }

## PesquisaDePrecoV_1_2

{ itens: array de object { codBarras, codConcorrente, codPesq, codPreco, codProduto, codUnidade, data, espe_codigo, marca, motSemPesq, obs, ruptura, updateCodPreco, usuario, validade, urlImagem, precos } }

## PontosPost

{ Pontos: object { TipoMovimento, CodigoProduto, Conta, Finalizadora, CodigoDocumento, Transacao, Valor, DataMovimento, DataVencimento, Pdv, Cupom, Quantidade } }

## PostGeracaoBoleto_V_1_0

{ operacao: string(string) ex: "001276949006"; origemVersao: string(string) ex: "1.3.1.1"; origemApp: string(string) ex: "AppTeste"; origemIdent: string(string) ex: "12" }

## PostMensagemUsuario

{ assunto: string ex: "assunto da mensagem"; texto: string ex: "texto da mensagem"; usuariosDestino: array de number ex: 1 }

## PreCadastroPostV_1_0

{ unid_codigo: string(string) ex: "001"; descricao: string(string) ex: "Teste"; complemento: string(string) ex: "Complemento teste"; marca: string(string) ex: "Marca Teste"; codBarras: string(string) ex: "213123"; descrPdvs: string(string) ex: "Teste PDV"; emb: string(string) ex: "CX"; qemb: number ex: 3; prod_Codigo: number ex: 0; codNcm: string(string) ex: ""; obs: string(string) ex: ""; balanca: string(string) ex: ""; peso: number ex: 0; pesoLiq: number ex: 0; prodFuncao: string(string) ex: ""; cest: string(string) ex: ""; codCaixa: string(string) ex: ""; lastro: number ex: 0; camadas: number ex: 0; forn_Codigo: number ex: 0; validade: number ex: 0; altura: number ex: 0; largura: number ex: 0; profundidade: number ex: 0; codProdFor: string(string) ex: "" }

## PrecoClienteV1_0

{ codigo: number ex: 1; fpgt_Codigo: string(string) ex: "001"; clie_Codigo: number(number) ex: 765245; prod_Codigo: number(number) ex: 729914; unid_Codigo: string(string) ex: "001"; prVenda: number(number) ex: 1.54 }

## PrecosClienteV1_0

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, messages, content } }

## ProdCestaBasica

{ codigoProduto: number ex: 11690; descricao: string(string) ex: "Prod Teste"; complemento: string(string) ex: ""; marca: string(string) ex: ""; qtde: number(double) ex: 5; prvenda: number(double) ex: 5.5; codigobarras: string(string) ex: "13412312" }

## ProdUnCustos_V_1_0

{ response: object { status, appVersion, messages, content } }

## ProdUnDetalhado_V_1_0

{ Codigo: integer ex: 693537; SKU: integer ex: 693537; CodigoBarras: string ex: "7896104871362"; CodigoNCM: string ex: "18063220"; Descricao: string ex: "Bar Ritter 66g Brigadeiro"; Complemento: string ex: ""; Marca: string ex: "Ritter"; Estoque: number ex: 360; Preco: number ex: 4; Grupo: string ex: "10749"; Oferta: string ex: "S"; DataOferta: string ex: "06-08-2024"; PrecoNormal: number ex: 5.26; CodigoUnidade: string ex: "001"; CodigoDepartamento: string ex: "113"; Departamento: string ex: "teste"; Ativo: boolean ex: true; CodigoTributario: string ex: "18063220"; Status: string ex: "NORMAL"; Estoque1: integer ex: 360; Estoque2: integer ex: 0; Estoque3: integer ex: 0; Estoque4: integer ex: 0; Estoque5: integer ex: 0; PrecoLista: number ex: 5.25; PrecoPDV: number ex: 5.25; PrecoPDV2: number ex: 5.25; PrecoPDV3: number ex: 5.25; PrecoPDV4: number ex: 5.25; PrecoPDV5: number ex: 5.25; PrecoPDVUnidadeMedida: number; PrecoEtiqueta: number ex: 5.26; PrecoCartaz: number ex: 3.69; PrecoVenda2: number ex: 3.69; PrecoVenda2UnidadeMedida: number ex: 3.69; PrecoVenda3: number ex: 3.69; PrecoVenda3UnidadeMedida: number ex: 3.69; PrecoVenda4: number ex: 3.69; PrecoVenda4UnidadeMedida: number ex: 3.69; PrecoVenda5: number ex: 3.69; PrecoVenda5UnidadeMedida: number ex: 3.69; FatorPr3: number ex: 3.69; FatorPr4: number ex: 3.69; FatorPr5: number ex: 3.69; AgprPreco1: number ex: 3.69; AgprPreco2: number ex: 3.69; AgprPreco3: number ex: 3.69; AgprPreco4: number ex: 3.69; AgprPreco5: number ex: 3.69; AgofPreco1: number ex: 3.69; AgofPreco2: number ex: 3.69; AgofPreco3: number ex: 3.69; AgofPreco4: number ex: 3.69; AgofPreco5: number ex: 3.69; CodEstoque: number ex: 3.69; EstoqueMinimo: number ex: 3.69; EstoqueMaximo: number ex: 3.69; VendaMediaDiaria: number ex: 3.69; Espaco: number ex: 3.69; CodigoCaixa: number ex: 3.69; CustoCompra: number ex: 2.5353; CustoEmpresa: number ex: 2.76; CustoFiscal: number ex: 1.38889; CustoMedio: number ex: 2.5353; CustoTransferencia: number ex: 2.76; CustoVenda: number ex: 27.25; SetorLoja: string ex: "J08"; SetorDeposito: string ex: ""; PrecoUnidadeMedida: number ex: 2.5; DescricaoPDV: string ex: "Bar Ritter 66g"; Bloqueado: boolean ex: false; Altura: number ex: 5; Largura: number ex: 5; Profundidade: number ex: 5; Peso: number ex: 0.075; PesoLiquido: number ex: 0.066; DescricaoEcommerce: string ex: "teste"; ComplementoEcommerce: string ex: "teste"; MarcaEcommerce: string ex: "teste"; IdEcommerce: integer ex: 0; CodBarrasAlterados: array de object { codigo, codigoBarras, numPreco, fatorEmbalagem, precoVenda, unidadeMedida, precoVendaUnidadeMedida, data }; DescricaoCliente: string; Temperatura: number ex: 0; TipoEmbalagem: string ex: "CX"; QuantidadeEmbalagem: number ex: 36; DataHoraManutencao: string ex: "04-09-2025 13:49:26"; Classe: string ex: "38"; Alterado: string ex: "S"; Etq: number ex: 1; Ctz: number ex: 1; Tecla: string ex: ""; PzRepos: number ex: 15; PzEntrega: number ex: 0; DiasSeg: number ex: 0; Validade: number ex: 0; ValMinima: number ex: 30; Marcado: string ex: "S"; PrVendaAnt: number ex: 5.26; DtPrVenda: string ex: "05-08-2024"; UsuAltPr: number ex: 939; Margem: number ex: 10; MargemMin: number ex: 0; QtdeOferta: number ex: 0; DtIniOferta: string ex: ""; DtUltComp: string ex: "19-02-2025"; PrUltComp: number ex: 2.76; QultComp: number ex: 100; UltSimbComp: string ex: "ST"; RedBCUltComp: number ex: 0; UltForn: number ex: 100781; DtCustos: string ex: "19-02-2025"; Comissao: number ex: 0; DifCusto: number ex: 0; DifVenda: number ex: 0; EtqMag: string ex: "N"; QtdeAbLoja: number ex: 0; DtAbLoja: string ex: ""; DataOfAnt: string ex: ""; PrecoOfertaAnt: number ex: 0; PrecoNormalAnt: number ex: 0; TpAltPrVenda: string ex: "F"; DifCusto1: number ex: 0; DifCusto2: number ex: 0; DifCusto3: number ex: 0; DifCusto4: number ex: 0; DifCusto5: number ex: 0; DifVenda1: number ex: 0; DifVenda2: number ex: 0; DifVenda3: number ex: 0; DifVenda4: number ex: 0; DifVenda5: number ex: 0; CtCompraAnt: number ex: 2.5353; CtMedioAnt: number ex: 2.5353; CtFiscalAnt: number ex: 1.38889; CtEmpresaAnt: number ex: 2.76; CtTransfAnt: number ex: 2.76; PrUltCompAnt: number ex: 2.76; TransCtMedio: string ex: "00127693521"; Faquisicao: string ex: ""; Extra1: string; Extra2: string; Extra3: string; Extra4: number ex: 0; Extra5: number ex: 0; Extra6: number ex: 0; Extra7: number ex: 0; Extra8: number ex: 0; Extra9: number ex: 0; Prod_Extra1: string ex: ""; Prod_Extra2: string ex: ""; Prod_Extra3: string ex: "031"; Prod_Extra4: number ex: 0; Prod_Extra5: number ex: 0; Prod_Extra6: string; Prod_Extra7: string; Prod_Extra8: number ex: 0; Prod_Extra9: number ex: 0; Extras: array de object { nome, tipo, valor }; Dataalt: string ex: "12-09-2024"; Usualt: number ex: 939; Frentes: number ex: 0; Orig_codigo: number ex: 123; PrTabela: number ex: 49.9; CreditoST: number ex: 0.90838; CodigoSim: string ex: "ABC123"; DataOfAnt2: string ex: "25-09-2025"; PrecoOfertaAnt2: number ex: 10.5; PrecoNormalAnt2: number ex: 12.3; PrNormal3: number ex: 8.75; PrNormal4: number ex: 9.99; PrNormal5: number ex: 15.4; PrecoNormalAnt3: number ex: 11.2; PrecoNormalAnt4: number ex: 13.6; PrecoNormalAnt5: number ex: 14.9; PrecoOfertaAnt3: number ex: 7.5; PrecoOfertaAnt4: number ex: 8.2; PrecoOfertaAnt5: number ex: 6.8; Margem3: number ex: 5.5; Margem4: number ex: 7.1; Margem5: number ex: 6.3; TipoAgOf: string ex: "P"; TipoAgOfAnt2: string ex: "Q"; TpTrocas: string ex: "C"; PrVdaPadrao: number ex: 19.9; CurvaABC: object { Geral, Departamento, Grupo }; PercImpostos: number ex: 23.4; PrVenda2Ant: number ex: 15.75; PrVenda2Ant2: number ex: 18.2; CodigoPreco: number ex: 9402; Descritivo: string ex: "Produto promocional"; Funcao: string ex: "Venda Direta"; Balanca: string ex: "N"; CodigoComprador: string ex: "001"; Alcada: number ex: 3; FatorEstoque: number ex: 1.25; tributacao: object { icms, ipi, pis, cofins, subTrib, controle } }

## ProdUn_V_1_0

{ Codigo: integer ex: 701904; SKU: integer ex: 701904; CodigoBarras: string ex: "0000000029452"; CodigoNCM: string ex: "08039000"; Descricao: string ex: "Morango Botesini 200g"; Complemento: string ex: ""; Marca: string ex: "Botesini"; Estoque: number ex: 121; Preco: number(double) ex: 15.99; Grupo: string ex: "11008"; Oferta: string ex: "N"; DataOferta: string ex: ""; PrecoNormal: number ex: 0; CodigoUnidade: string ex: "001"; CodigoDepartamento: string ex: "002"; Departamento: string; Ativo: boolean ex: true; CodigoTributario: string ex: "2001"; Status: string ex: "NORMAL"; Estoque1: integer ex: 360; Estoque2: integer ex: 200; Estoque3: integer ex: 10; Estoque4: integer ex: 10; Estoque5: integer ex: 20; PrecoLista: number ex: 15.99; PrecoPDV: number ex: 15.29; PrecoPDVUnidadeMedida: number ex: 76.45; PrecoPDV2: number ex: 20; PrecoPDV3: number ex: 10; PrecoPDV4: number ex: 5; PrecoPDV5: number ex: 3; PrecoEtiqueta: number ex: 15.99; PrecoCartaz: number ex: 2; PrecoVenda2: number ex: 2; PrecoVenda2UnidadeMedida: number ex: 3; PrecoVenda3: number ex: 3; PrecoVenda3UnidadeMedida: number ex: 4; PrecoVenda4: number ex: 5; PrecoVenda4UnidadeMedida: number ex: 10; PrecoVenda5: number ex: 12; PrecoVenda5UnidadeMedida: number ex: 2; FatorPr3: number ex: 0; FatorPr4: number ex: 1; FatorPr5: number ex: 2; AgprPreco1: number ex: 12.5; AgprPreco2: number ex: 12.5; AgprPreco3: number ex: "15;5"; AgprPreco4: number ex: 5.26; AgprPreco5: number ex: 3.22; AgofPreco1: number ex: 3; AgofPreco2: number ex: 8.99; AgofPreco3: number ex: 8; AgofPreco4: number ex: 7; AgofPreco5: number ex: 8; CodEstoque: integer ex: 2; EstoqueMinimo: integer ex: 100; EstoqueMaximo: integer ex: 2000; VendaMediaDiaria: number ex: 1; Espaco: integer ex: 4; CodigoCaixa: string ex: ""; CustoCompra: number ex: 4.593; CustoEmpresa: number ex: 5; CustoFiscal: number ex: 4.593; CustoMedio: number ex: 6.70996; CustoTransferencia: number ex: 5; CustoVenda: number ex: 12; SetorLoja: string ex: "SETOR"; SetorDeposito: string ex: ""; PrecoUnidadeMedida: number ex: 79.95; DescricaoPDV: string ex: "Morango Botesini 200g"; Bloqueado: boolean ex: false; Altura: number; Largura: number ex: 0; Profundidade: number ex: 0; Peso: number ex: 0.2; PesoLiquido: number ex: 0.2; DescricaoEcommerce: string ex: ""; ComplementoEcommerce: string; MarcaEcommerce: string ex: ""; IdEcommerce: integer ex: 0; CodBarrasAlterados: array de string; DescricaoCliente: string ex: ""; Temperatura: number ex: 0; TipoEmbalagem: string ex: "UN"; QuantidadeEmbalagem: integer ex: 1; DataHoraManutencao: string ex: "18-11-2024 17:16:17" }

## ProdVenda

{ codigoProduto: number ex: 242934; quantidadeUnitaria: number(double) ex: 10; valorTotal: number(double) ex: 6; oferta: string(string) ex: "NAO" }

## ProdXmlNfeV10

{ ean: string(string) ex: "7896008910143"; eanTrib: string(string) ex: "7896008910143" }

## Produto

{ Codigo: integer ex: 10162; SKU: integer ex: 10162; CodigoBarras: string(string) ex: "1050695"; CodigoNCM: string(string) ex: "18069000"; Descricao: string(string) ex: "Kinder Ovo"; Complemento: string(string) ex: ""; Marca: string(string) ex: "Dorizon"; Estoque: number(double) ex: 0; Preco: number(double) ex: 3.89; Grupo: string(string) ex: "10000"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "18-04-2018"; PrecoNormal: number(double) ex: 0; CodigoUnidade: string(string) ex: "001"; CodigoDepartamento: string(string) ex: "999"; Departamento: string(string) ex: "Geral"; Ativo: boolean ex: true; CodigoTributario: string(string) ex: "905"; TipoEmbalagem: string(string) ex: "UN"; QuantidadeEmbalagem: integer ex: 0 }

## ProdutoAlt

{ Codigo: integer ex: 10162; SKU: integer ex: 10162; CodigoBarras: string(string) ex: "1050695"; CodigoNCM: string(string) ex: "18069000"; Descricao: string(string) ex: "Kinder Ovo"; Complemento: string(string) ex: ""; Marca: string(string) ex: "Dorizon"; Estoque: number(double) ex: 0; Preco: number(double) ex: 0; Grupo: string(string) ex: "10000"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "18-04-2018"; PrecoNormal: number(double) ex: 0; CodigoUnidade: string(string) ex: "001"; CodigoDepartamento: string(string) ex: "999"; Departamento: string(string) ex: "Geral"; Ativo: boolean ex: true; CodigoTributario: string(string) ex: "905"; Estoque1: number(double) ex: 10; Estoque2: number(double) ex: 0; Estoque3: number(double) ex: 0; Estoque4: number(double) ex: 0; Estoque5: number(double) ex: 0; PrecoLista: number(double) ex: 0; PrecoPDV: number(double) ex: 3.89; PrecoPDV2: number(double) ex: 0; PrecoPDV3: number(double) ex: 0; PrecoPDV4: number(double) ex: 0; PrecoPDV5: number(double) ex: 0; PrecoEtiqueta: number(double) ex: 3.2; PrecoCartaz: number(double) ex: 0; PrecoVenda3: number(double) ex: 0; PrecoVenda4: number(double) ex: 0; PrecoVenda5: number(double) ex: 0; FatorPr3: number(double) ex: 0; FatorPr4: number(double) ex: 0; FatorPr5: number(double) ex: 0; CustoCompra: number(double) ex: 76.3639; CustoEmpresa: number(double) ex: 76.3639; CustoFiscal: number(double) ex: 76.3639; CustoMedio: number(double) ex: 76.3639; CustoTranferencia: number(double) ex: 76.3639; TipoEmbalagem: string(string) ex: "UN"; QuantidadeEmbalagem: integer ex: 0 }

## ProdutoAltSemCustos

{ Codigo: integer ex: 10162; SKU: integer ex: 10162; CodigoBarras: string(string) ex: "1050695"; CodigoNCM: string(string) ex: "18069000"; Descricao: string(string) ex: "Kinder Ovo"; Complemento: string(string) ex: ""; Marca: string(string) ex: "Dorizon"; Estoque: number(double) ex: 0; Preco: number(double) ex: 0; Grupo: string(string) ex: "10000"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "18-04-2018"; PrecoNormal: number(double) ex: 0; CodigoUnidade: string(string) ex: "001"; CodigoDepartamento: string(string) ex: "999"; Departamento: string(string) ex: "Geral"; Ativo: boolean ex: true; CodigoTributario: string(string) ex: "905"; Estoque1: number(double) ex: 10; Estoque2: number(double) ex: 0; Estoque3: number(double) ex: 0; Estoque4: number(double) ex: 0; Estoque5: number(double) ex: 0; PrecoLista: number(double) ex: 0; PrecoPDV: number(double) ex: 3.89; PrecoPDV2: number(double) ex: 0; PrecoPDV3: number(double) ex: 0; PrecoPDV4: number(double) ex: 0; PrecoPDV5: number(double) ex: 0; PrecoEtiqueta: number(double) ex: 3.2; PrecoCartaz: number(double) ex: 0; PrecoVenda3: number(double) ex: 0; PrecoVenda4: number(double) ex: 0; PrecoVenda5: number(double) ex: 0; FatorPr3: number(double) ex: 0; FatorPr4: number(double) ex: 0; FatorPr5: number(double) ex: 0; TipoEmbalagem: string(string) ex: "UN"; QuantidadeEmbalagem: integer ex: 0 }

## ProdutoAltSemCustos5

{ Codigo: integer ex: 10162; SKU: integer ex: 10162; CodigoBarras: string(string) ex: "1050695"; CodigoCaixa: string(string) ex: "020"; CodigoNCM: string(string) ex: "18069000"; Descricao: string(string) ex: "Kinder Ovo"; Complemento: string(string) ex: ""; Marca: string(string) ex: "Dorizon"; Estoque: number(double) ex: 0; Preco: number(double) ex: 0; Grupo: string(string) ex: "10000"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "18-04-2018"; PrecoNormal: number(double) ex: 0; CodigoUnidade: string(string) ex: "001"; CodigoDepartamento: string(string) ex: "999"; Departamento: string(string) ex: "Geral"; Ativo: boolean ex: true; CodigoTributario: string(string) ex: "905"; Estoque1: number(double) ex: 10; Estoque2: number(double) ex: 0; Estoque3: number(double) ex: 0; Estoque4: number(double) ex: 0; Estoque5: number(double) ex: 0; PrecoLista: number(double) ex: 0; PrecoPDV: number(double) ex: 3.89; PrecoPDV2: number(double) ex: 0; PrecoPDV3: number(double) ex: 0; PrecoPDV4: number(double) ex: 0; PrecoPDV5: number(double) ex: 0; PrecoEtiqueta: number(double) ex: 3.2; PrecoCartaz: number(double) ex: 0; PrecoVenda3: number(double) ex: 0; PrecoVenda4: number(double) ex: 0; PrecoVenda5: number(double) ex: 0; FatorPr3: number(double) ex: 0; FatorPr4: number(double) ex: 0; FatorPr5: number(double) ex: 0; TipoEmbalagem: string(string) ex: "UN"; QuantidadeEmbalagem: integer ex: 0; CodEstoque: number ex: 1; EstoqueMinimo: number(double) ex: 10; EstoqueMaximo: number(double) ex: 300; VendaMediaDiaria: number(double) ex: 15 }

## ProdutoAltSemCustosNovo

{ Codigo: integer ex: 10162; SKU: integer ex: 10162; CodigoBarras: string(string) ex: "1050695"; CodigoNCM: string(string) ex: "18069000"; Descricao: string(string) ex: "Kinder Ovo"; Complemento: string(string) ex: ""; Marca: string(string) ex: "Dorizon"; Estoque: number(double) ex: 0; Preco: number(double) ex: 0; Grupo: string(string) ex: "10000"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "18-04-2018"; PrecoNormal: number(double) ex: 0; CodigoUnidade: string(string) ex: "001"; CodigoDepartamento: string(string) ex: "999"; Departamento: string(string) ex: "Geral"; Ativo: boolean ex: true; CodigoTributario: string(string) ex: "905"; Estoque1: number(double) ex: 10; Estoque2: number(double) ex: 0; Estoque3: number(double) ex: 0; Estoque4: number(double) ex: 0; Estoque5: number(double) ex: 0; PrecoLista: number(double) ex: 0; PrecoPDV: number(double) ex: 3.89; PrecoPDV2: number(double) ex: 0; PrecoPDV3: number(double) ex: 0; PrecoPDV4: number(double) ex: 0; PrecoPDV5: number(double) ex: 0; PrecoEtiqueta: number(double) ex: 3.2; PrecoCartaz: number(double) ex: 0; PrecoVenda3: number(double) ex: 0; PrecoVenda4: number(double) ex: 0; PrecoVenda5: number(double) ex: 0; FatorPr3: number(double) ex: 0; FatorPr4: number(double) ex: 0; FatorPr5: number(double) ex: 0; TipoEmbalagem: string(string) ex: "UN"; QuantidadeEmbalagem: integer ex: 0; CodEstoque: number ex: 1; EstoqueMinimo: number(double) ex: 10; EstoqueMaximo: number(double) ex: 300; VendaMediaDiaria: number(double) ex: 15 }

## ProdutoAltV19

{ Codigo: integer ex: 508942; SKU: integer ex: 508942; CodigoBarras: string(string) ex: "7898262580827"; CodigoNCM: string(string) ex: "19049000"; Descricao: string(string) ex: "Zzsalg Naturitos 50g Queijo"; DescricaoCliente: string(string) ex: "Cliente"; Complemento: string(string) ex: ""; Marca: string(string) ex: "Naturitos"; Estoque: number(double) ex: 0; Preco: number(double) ex: 0; Grupo: string(string) ex: "21984"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "08-03-2019"; PrecoNormal: number(double) ex: 0; CodigoUnidade: string(string) ex: "004"; CodigoDepartamento: string(string) ex: "49.0"; Departamento: string(string) ex: "Mercearia Doce"; Ativo: boolean ex: true; CodigoTributario: string(string) ex: "19049000"; Estoque1: number(double) ex: 0; Estoque2: number(double) ex: 0; Estoque3: number(double) ex: 0; Estoque4: number(double) ex: 0; Estoque5: number(double) ex: 0; PrecoLista: number(double) ex: 0; PrecoPDV: number(double) ex: 0; PrecoPDV2: number(double) ex: 0; PrecoPDV3: number(double) ex: 0; PrecoPDV4: number(double) ex: 0; PrecoPDV5: number(double) ex: 0; PrecoEtiqueta: number(double) ex: 0; PrecoCartaz: number(double) ex: 0; PrecoVenda2: number(double) ex: 0; PrecoVenda3: number(double) ex: 0; PrecoVenda4: number(double) ex: 0; PrecoVenda5: number(double) ex: 0; FatorPr3: integer ex: 0; FatorPr4: integer ex: 0; FatorPr5: integer ex: 0; CodEstoque: integer ex: 0; EstoqueMinimo: number(double) ex: 0; EstoqueMaximo: number(double) ex: 0; VendaMediaDiaria: number(double) ex: 0; Espaco: integer ex: 0; CodigoCaixa: string(string) ex: ""; CustoCompra: number(double) ex: 0; CustoEmpresa: number(double) ex: 0; CustoFiscal: number(double) ex: 0; CustoMedio: number(double) ex: 0; CustoTranferencia: number(double) ex: 0; SetorLoja: string(string) ex: ""; SetorDeposito: string(string) ex: ""; PrecoUnidadeMedida: number(double) ex: 0; DescricaoPDV: string(string) ex: "Salg Naturitos 50g q"; TipoEmbalagem: string(string) ex: "UN"; QuantidadeEmbalagem: integer ex: 1; Bloqueado: boolean ex: false }

## ProdutoAltV20

{ Codigo: integer ex: 508942; SKU: integer ex: 508942; CodigoBarras: string(string) ex: "7898262580827"; CodigoNCM: string(string) ex: "19049000"; Descricao: string(string) ex: "Zzsalg Naturitos 50g Queijo"; DescricaoCliente: string(string) ex: "Cliente"; Complemento: string(string) ex: ""; Marca: string(string) ex: "Naturitos"; Estoque: number(double) ex: 0; Preco: number(double) ex: 0; Grupo: string(string) ex: "21984"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "08-03-2019"; PrecoNormal: number(double) ex: 0; CodigoUnidade: string(string) ex: "004"; CodigoDepartamento: string(string) ex: "49.0"; Departamento: string(string) ex: "Mercearia Doce"; Ativo: boolean ex: true; CodigoTributario: string(string) ex: "19049000"; Estoque1: number(double) ex: 0; Estoque2: number(double) ex: 0; Estoque3: number(double) ex: 0; Estoque4: number(double) ex: 0; Estoque5: number(double) ex: 0; PrecoLista: number(double) ex: 0; PrecoPDV: number(double) ex: 0; PrecoPDV2: number(double) ex: 0; PrecoPDV3: number(double) ex: 0; PrecoPDV4: number(double) ex: 0; PrecoPDV5: number(double) ex: 0; PrecoEtiqueta: number(double) ex: 0; PrecoCartaz: number(double) ex: 0; PrecoVenda2: number(double) ex: 0; PrecoVenda3: number(double) ex: 0; PrecoVenda4: number(double) ex: 0; PrecoVenda5: number(double) ex: 0; FatorPr3: integer ex: 0; FatorPr4: integer ex: 0; FatorPr5: integer ex: 0; CodEstoque: integer ex: 0; EstoqueMinimo: number(double) ex: 0; EstoqueMaximo: number(double) ex: 0; VendaMediaDiaria: number(double) ex: 0; Espaco: integer ex: 0; CodigoCaixa: string(string) ex: ""; CustoCompra: number(double) ex: 0; CustoEmpresa: number(double) ex: 0; CustoFiscal: number(double) ex: 0; CustoMedio: number(double) ex: 0; CustoTranferencia: number(double) ex: 0; SetorLoja: string(string) ex: ""; SetorDeposito: string(string) ex: ""; PrecoUnidadeMedida: number(double) ex: 0; DescricaoPDV: string(string) ex: "Salg Naturitos 50g q"; TipoEmbalagem: string(string) ex: "UN"; QuantidadeEmbalagem: integer ex: 1; Bloqueado: boolean ex: false }

## ProdutoAltV4

{ Codigo: integer ex: 10162; SKU: integer ex: 10162; CodigoBarras: string(string) ex: "1050695"; CodigoNCM: string(string) ex: "18069000"; Descricao: string(string) ex: "Kinder Ovo"; Complemento: string(string) ex: ""; Marca: string(string) ex: "Dorizon"; Estoque: number(double) ex: 0; Preco: number(double) ex: 0; Grupo: string(string) ex: "10000"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "18-04-2018"; PrecoNormal: number(double) ex: 0; CodigoUnidade: string(string) ex: "001"; CodigoDepartamento: string(string) ex: "999"; Departamento: string(string) ex: "Geral"; Ativo: boolean ex: true; CodigoTributario: string(string) ex: "905"; Estoque1: number(double) ex: 10; Estoque2: number(double) ex: 0; Estoque3: number(double) ex: 0; Estoque4: number(double) ex: 0; Estoque5: number(double) ex: 0; PrecoLista: number(double) ex: 0; PrecoPDV: number(double) ex: 3.89; PrecoPDV2: number(double) ex: 0; PrecoPDV3: number(double) ex: 0; PrecoPDV4: number(double) ex: 0; PrecoPDV5: number(double) ex: 0; PrecoEtiqueta: number(double) ex: 3.2; PrecoCartaz: number(double) ex: 0; PrecoVenda3: number(double) ex: 0; PrecoVenda4: number(double) ex: 0; PrecoVenda5: number(double) ex: 0; FatorPr3: number(double) ex: 0; FatorPr4: number(double) ex: 0; FatorPr5: number(double) ex: 0; CustoCompra: number(double) ex: 76.3639; CustoEmpresa: number(double) ex: 76.3639; CustoFiscal: number(double) ex: 76.3639; CustoMedio: number(double) ex: 76.3639; CustoTranferencia: number(double) ex: 76.3639; TipoEmbalagem: string(string) ex: "UN"; QuantidadeEmbalagem: integer ex: 0; CodEstoque: number ex: 1; EstoqueMinimo: number(double) ex: 10; EstoqueMaximo: number(double) ex: 300; VendaMediaDiaria: number(double) ex: 15 }

## ProdutoAltV5

{ Codigo: integer ex: 10162; SKU: integer ex: 10162; CodigoBarras: string(string) ex: "1050695"; CodigoNCM: string(string) ex: "18069000"; CodigoCaixa: string(string) ex: "020"; Descricao: string(string) ex: "Kinder Ovo"; Complemento: string(string) ex: ""; Marca: string(string) ex: "Dorizon"; Estoque: number(double) ex: 0; Preco: number(double) ex: 0; Grupo: string(string) ex: "10000"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "18-04-2018"; PrecoNormal: number(double) ex: 0; CodigoUnidade: string(string) ex: "001"; CodigoDepartamento: string(string) ex: "999"; Departamento: string(string) ex: "Geral"; Ativo: boolean ex: true; CodigoTributario: string(string) ex: "905"; Estoque1: number(double) ex: 10; Estoque2: number(double) ex: 0; Estoque3: number(double) ex: 0; Estoque4: number(double) ex: 0; Estoque5: number(double) ex: 0; PrecoLista: number(double) ex: 0; PrecoPDV: number(double) ex: 3.89; PrecoPDV2: number(double) ex: 0; PrecoPDV3: number(double) ex: 0; PrecoPDV4: number(double) ex: 0; PrecoPDV5: number(double) ex: 0; PrecoEtiqueta: number(double) ex: 3.2; PrecoCartaz: number(double) ex: 0; PrecoVenda3: number(double) ex: 0; PrecoVenda4: number(double) ex: 0; PrecoVenda5: number(double) ex: 0; FatorPr3: number(double) ex: 0; FatorPr4: number(double) ex: 0; FatorPr5: number(double) ex: 0; CustoCompra: number(double) ex: 76.3639; CustoEmpresa: number(double) ex: 76.3639; CustoFiscal: number(double) ex: 76.3639; CustoMedio: number(double) ex: 76.3639; CustoTranferencia: number(double) ex: 76.3639; TipoEmbalagem: string(string) ex: "UN"; QuantidadeEmbalagem: integer ex: 0; CodEstoque: number ex: 1; EstoqueMinimo: number(double) ex: 10; EstoqueMaximo: number(double) ex: 300; VendaMediaDiaria: number(double) ex: 15 }

## ProdutoCadastro

{ codigo: integer ex: 1015; descricao: string ex: "C Bov Picanha Fat Kg"; complemento: string ex: ""; grupoCodigo: string ex: "18102"; grupoNome: string ex: "Carnes Bovinas De Primeira"; departamentoCodigo: string ex: "018"; marca: string ex: "Açougue Bov"; classe: string ex: ""; tipo: string ex: ""; funcao: string ex: ""; codigoBarras: string ex: "0000000011273"; descricaoPDVs: string ex: "C Bov Picanha Fat Kg"; peso: number(double) ex: 1.5; pesoLiquido: number(double) ex: 1.2; embalagem: string ex: "KG"; quantidadeEmbalagem: integer ex: 1; balanca: string ex: "P"; dataCadastro: string(string) ex: "01/07/2020"; dataAlteracao: string(string) ex: "27/11/2020"; altura: integer ex: 2; largura: integer ex: 3; profundidade: integer ex: 1; lastro: integer ex: 0; camadas: integer ex: 2; fatorEmbalagem: integer ex: 0; status: string ex: "N"; codigoCaixa: string ex: ""; display: integer ex: 0; descricaoCliente: string ex: "C Bov Picanha Fat Kg"; codigoNCM: string ex: "02013000"; classificacaoFiscal: string ex: ""; descricaoEcommerce: string ex: ""; complementoEcommerce: string ex: ""; marcaEcommerce: string ex: "" }

## ProdutoCadastroDetalhe

{ codigo: integer ex: 1015; descricao: string ex: "C Bov Picanha Fat Kg"; complemento: string ex: ""; grupoCodigo: string ex: "18102"; grupoNome: string ex: "Carnes Bovinas De Primeira"; departamentoCodigo: string ex: "018"; marca: string ex: "Açougue Bov"; classe: string ex: ""; tipo: string ex: ""; funcao: string ex: ""; codigoBarras: string ex: "0000000011273"; descricaoPDVs: string ex: "C Bov Picanha Fat Kg"; peso: number(double) ex: 1.5; pesoLiquido: number(double) ex: 1.2; embalagem: string ex: "KG"; quantidadeEmbalagem: integer ex: 1; balanca: string ex: "P"; dataCadastro: string(string) ex: "01/07/2020"; dataAlteracao: string(string) ex: "27/11/2020"; altura: integer ex: 2; largura: integer ex: 3; profundidade: integer ex: 1; lastro: integer ex: 0; camadas: integer ex: 2; fatorEmbalagem: integer ex: 0; status: string ex: "N"; codigoCaixa: string ex: ""; display: integer ex: 0; descricaoCliente: string ex: "C Bov Picanha Fat Kg"; codigoNCM: string ex: "02013000"; classificacaoFiscal: string ex: ""; descricaoEcommerce: string ex: ""; complementoEcommerce: string ex: ""; marcaEcommerce: string ex: ""; tributacaoCodigo: string ex: "0201.001"; codigoEstoque: integer ex: 0; fatorEstoque: integer ex: 0; codigoPreco: integer ex: 1516; prazoReposicao: integer ex: 0; prazoEntrega: integer ex: 0; diasSeguranca: integer ex: 1; vasilhameCodigo: string ex: "0"; controlaEstoque: string ex: "S"; extra1: string ex: "SGPU"; extra2: string ex: ""; extra3: string ex: "ST"; extra4: number(double) ex: 0.0; extra5: number(double) ex: 0.0; extra6: string ex: "1708400"; extra7: string ex: ""; extra8: number(double) ex: 0.0; extra9: number(double) ex: 0.0; formaAquisicao: string ex: ""; garantiaDisponibCodigo: string ex: ""; descritivo: string ex: ""; tipoTrocas: string ex: ""; grupoPreco: string ex: ""; ativoUnidades: string ex: "175;113;042;191;190;151;120"; bloqueadoUnidades: string ex: "116;112;111;905;081"; fornecedor: integer ex: 0; codigoEX: string ex: ""; pesoMaximo: integer ex: 0; volumeMaximo: integer ex: 0; temperaturaMaxima: integer ex: 0; codigoComprador: integer ex: 0; validadeMinima: integer ex: 0; codigoSensibilidade: integer ex: 0; varPeso: integer ex: 0; codigoCentralCompras: integer ex: 0; descricaoCentralCompras: string ex: ""; sazonalidade: string ex: ""; similaridade: string ex: ""; codigoAgrupadorCompra: integer ex: 0 }

## ProdutoCadastroDetalheV2

{ codigo: number ex: 1; descricao: string(string) ex: "Molho De Tomate Quero 340g Tradicional Sc"; complemento: string(string) ex: "Sss"; grupoCodigo: string(string) ex: "15643"; grupoNome: string(string) ex: "Molho Tomate Temperado"; departamentoCodigo: string(string) ex: "047"; marca: string(string) ex: "A Definir"; classe: string(string) ex: "1"; tipo: string(string) ex: ""; funcao: string(string) ex: "VE"; codigoBarras: string(string) ex: "7896102509410"; descricaoPDVs: string(string) ex: "Molho De Tomate Quero 340g Tradicional S"; peso: number ex: 0; pesoLiquido: number ex: 0; embalagem: string(string) ex: "CX"; quantidadeEmbalagem: number ex: 1; balanca: string(string) ex: "N"; dataCadastro: string(string) ex: "03/06/2022"; dataAlteracao: string(string) ex: "19/05/2022"; altura: number ex: 0; largura: number ex: 0; profundidade: number ex: 0; lastro: number ex: 0; camadas: number ex: 0; fatorEmbalagem: number ex: 0; status: string(string) ex: "N"; codigoCaixa: string(string) ex: ""; display: number ex: 0; descricaoCliente: string(string) ex: "Molho De Tomate Quero 340g Tradicional Sc"; codigoNCM: string(string) ex: "21032010"; classificacaoFiscal: string(string) ex: ""; descricaoEcommerce: string(string) ex: ""; complementoEcommerce: string(string) ex: ""; marcaEcommerce: string(string) ex: ""; usuarioCadastro: number ex: 900; usuarioAlteracao: number ex: 957; tributacaoCodigo: string(string) ex: "0002.001"; codigoEstoque: number ex: 5; fatorEstoque: number ex: 1; codigoPreco: number ex: 1; prazoReposicao: number ex: 0; prazoEntrega: number ex: 0; diasSeguranca: number ex: 0; vasilhameCodigo: string(string) ex: ""; controlaEstoque: string(string) ex: "S"; extra1: string(string) ex: ""; extra2: string(string) ex: ""; extra3: string(string) ex: "Razão Social: Agropel Agroind Perazzoli Ltda CNPJ: 75347385000590 Endereço: Br-116 22881, 1"; extra4: number ex: 0; extra5: number ex: 0; extra6: string(string) ex: ""; extra7: string(string) ex: "extra7"; extra8: number ex: 0; extra9: number ex: 0; Extras: array de object { nome, tipo, valor }; formaAquisicao: string(string) ex: ""; garantiaDisponibCodigo: string(string) ex: ""; descritivo: string(string) ex: ""; tipoTrocas: string(string) ex: ""; grupoPreco: string(string) ex: ""; ativoUnidades: string(string) ex: "001002;"; bloqueadoUnidades: string(string) ex: ""; fornecedor: number ex: 10189; codigoEX: string(string) ex: ""; pesoMaximo: number ex: 0; volumeMaximo: number ex: 0; temperaturaMaxima: number ex: 0; codigoComprador: string(string) ex: ""; validadeMinima: number ex: 0; codigoSensibilidade: number ex: 0; varPeso: number ex: 0; codigoCentralCompras: number ex: 0; descricaoCentralCompra: string(string) ex: ""; sazonalidade: string(string) ex: ""; similaridade: string(string) ex: "001"; codigoAgrupadorCompra: number ex: 0 }

## ProdutoCadastro_V_1_3

{ codigo: integer ex: 1015; descricao: string ex: "C Bov Picanha Fat Kg"; complemento: string ex: ""; grupoCodigo: string ex: "18102"; grupoNome: string ex: "Carnes Bovinas De Primeira"; departamentoCodigo: string ex: "018"; marca: string ex: "Açougue Bov"; classe: string ex: ""; tipo: string ex: ""; funcao: string ex: ""; codigoBarras: string ex: "0000000011273"; descricaoPDVs: string ex: "C Bov Picanha Fat Kg"; peso: number(double) ex: 1.5; pesoLiquido: number(double) ex: 1.2; embalagem: string ex: "KG"; quantidadeEmbalagem: integer ex: 1; balanca: string ex: "P"; dataCadastro: string(string) ex: "01/07/2020"; dataAlteracao: string(string) ex: "27/11/2020"; altura: integer ex: 2; largura: integer ex: 3; profundidade: integer ex: 1; lastro: integer ex: 0; camadas: integer ex: 2; fatorEmbalagem: integer ex: 0; status: string ex: "N"; codigoCaixa: string ex: ""; display: integer ex: 0; descricaoCliente: string ex: "C Bov Picanha Fat Kg"; codigoNCM: string ex: "02013000"; classificacaoFiscal: string ex: ""; descricaoEcommerce: string ex: ""; complementoEcommerce: string ex: ""; marcaEcommerce: string ex: ""; codigosFornecedor: any }

## ProdutoComEstoqueV28

{ Codigo: integer ex: 100010; SKU: integer ex: 100010; CodigoBarras: string(string) ex: "7896090401222"; CodigoNCM: string(string) ex: "1042090.0"; Descricao: string(string) ex: "Desodorante"; DescricaoCliente: string(string) ex: "Cliente"; Complemento: string(string) ex: ""; Marca: string(string) ex: "Teste"; Status: string(string) ex: "NORMAL"; Preco: number(double) ex: 8.98; Estoque: number(double) ex: 8.98; Grupo: string(string) ex: "16703"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "08-03-2019"; PrecoNormal: number(double) ex: 0; CodigoUnidade: string(string) ex: "004"; CodigoDepartamento: string(string) ex: "030"; Departamento: string(string) ex: "Higiene e Beleza"; Ativo: boolean ex: true; CodigoTributario: string(string) ex: "34051000"; Estoque1: number(double) ex: 1; Estoque2: number(double) ex: 0; Estoque3: number(double) ex: 0; Estoque4: number(double) ex: 0; Estoque5: number(double) ex: 0; PrecoLista: number(double) ex: 8.98; PrecoPDV: number(double) ex: 8.98; PrecoPDV2: number(double) ex: 6.99; PrecoPDV3: number(double) ex: 6.99; PrecoPDV4: number(double) ex: 0; PrecoPDV5: number(double) ex: 0; PrecoEtiqueta: number(double) ex: 8.98; PrecoCartaz: number(double) ex: 0; PrecoVenda2: number(double) ex: 0; PrecoVenda3: number(double) ex: 6.99; PrecoVenda4: number(double) ex: 0; PrecoVenda5: number(double) ex: 0; FatorPr3: integer ex: 0; FatorPr4: integer ex: 0; FatorPr5: integer ex: 0; CodEstoque: integer ex: 0; EstoqueMinimo: number(double) ex: 0; EstoqueMaximo: number(double) ex: 0; VendaMediaDiaria: number(double) ex: 0.923; Espaco: integer ex: 0; CodigoCaixa: string(string) ex: "17896090401250"; CustoCompra: number(double) ex: 1; CustoEmpresa: number(double) ex: 4.6; CustoFiscal: number(double) ex: 4.6; CustoMedio: number(double) ex: 4.4842; CustoTranferencia: number(double) ex: 4.6; SetorLoja: string(string) ex: ""; SetorDeposito: string(string) ex: ""; PrecoUnidadeMedida: number(double) ex: 0; DescricaoPDV: string(string) ex: "Des Hydratta 165ml a"; TipoEmbalagem: string(string) ex: "CX"; QuantidadeEmbalagem: integer ex: 12; DataHoraManutencao: string(string;) ex: "21/03/2023 14:25:39.651" }

## ProdutoDeIndustrializado

{ codigoItem: number ex: 35; unidade: string(string) ex: "001"; quantComercializacao: number ex: 1.0; quantReceita: number ex: 0.175; pesoItem: number ex: 0.0; precoItem: number ex: 0.0; fase: string(string) ex: "1" }

## ProdutoDeIndustrializadoCadastro

{ codigoIndustrializado: number ex: 25; codigoItem: number ex: 35; unidade: string(string) ex: "001"; quantComercializacao: number ex: 1.0; quantReceita: number ex: 0.175; pesoItem: number ex: 0.0; precoItem: number ex: 0.0; fase: string(string) ex: "1" }

## ProdutoDeIndustrializadoEdicao_V1_2

{ cod2: number ex: 35; unidade: string(string) ex: "001"; quantComercializacao: number ex: 1.0; quantReceita: number ex: 0.175; pesoItem: number ex: 0.0; precoItem: number ex: 0.0; fase: string(string) ex: "1" }

## ProdutoDetalhadoCurvaABC

{ Geral: object { Quantidade, Valor, Lucro }; Departamento: object { Quantidade, Valor, Lucro }; Grupo: object { Quantidade, Valor, Lucro } }

## ProdutoDetalhadoCustomReleaseV29

**ProdutoDetalhadoV29** = `ProdutoDetalhadoV28` (ver reference/schemas.md) & object { AgprPreco1, AgprPreco2, AgprPreco3, AgprPreco4, AgprPreco5, AgofPreco1, AgofPreco2, AgofPreco3, AgofPreco4, AgofPreco5 } & { CustomRelease: number ex: 0 }

## ProdutoDetalhadoCustomReleaseV30

**ProdutoDetalhadoV30** = `ProdutoDetalhadoV29` (ver reference/schemas.md) & object { descricaoEcommerce, complementoEcommerce, marcaEcommerce, idEcommerce } & { CustomRelease: number ex: 0 }

## ProdutoDetalhadoCustomReleaseV31

**ProdutoDetalhadoV31** = `ProdutoDetalhadoV30` (ver reference/schemas.md) & object { codBarrasAlterados } & { CustomRelease: number ex: 0 }

## ProdutoDetalhadoCustomReleaseV32

**ProdutoDetalhadoV32** = `ProdutoDetalhadoV31` (ver reference/schemas.md) & object { PrecoPDVUnidadeMedida, PrecoVenda2UnidadeMedida, PrecoVenda3UnidadeMedida, PrecoVenda4UnidadeMedida, PrecoVenda5UnidadeMedida } & { CustomRelease: number ex: 0 }

## ProdutoDetalhadoEstoqueSemEstoqueV20

{ Codigo: integer ex: 508942; SKU: integer ex: 508942; CodigoBarras: string(string) ex: "7898262580827"; CodigoNCM: string(string) ex: "19049000"; Descricao: string(string) ex: "Zzsalg Naturitos 50g Queijo"; DescricaoCliente: string(string) ex: "Cliente"; Complemento: string(string) ex: ""; Marca: string(string) ex: "Naturitos"; Preco: number(double) ex: 0; Grupo: string(string) ex: "21984"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "08-03-2019"; PrecoNormal: number(double) ex: 0; CodigoUnidade: string(string) ex: "004"; CodigoDepartamento: string(string) ex: "49.0"; Departamento: string(string) ex: "Mercearia Doce"; Ativo: boolean ex: true; CodigoTributario: string(string) ex: "19049000"; Estoque1: number(double) ex: 0; Estoque2: number(double) ex: 0; Estoque3: number(double) ex: 0; Estoque4: number(double) ex: 0; Estoque5: number(double) ex: 0; PrecoLista: number(double) ex: 0; PrecoPDV: number(double) ex: 0; PrecoPDV2: number(double) ex: 0; PrecoPDV3: number(double) ex: 0; PrecoPDV4: number(double) ex: 0; PrecoPDV5: number(double) ex: 0; PrecoEtiqueta: number(double) ex: 0; PrecoCartaz: number(double) ex: 0; PrecoVenda2: number(double) ex: 0; PrecoVenda3: number(double) ex: 0; PrecoVenda4: number(double) ex: 0; PrecoVenda5: number(double) ex: 0; FatorPr3: integer ex: 0; FatorPr4: integer ex: 0; FatorPr5: integer ex: 0; CodEstoque: integer ex: 0; EstoqueMinimo: number(double) ex: 0; EstoqueMaximo: number(double) ex: 0; VendaMediaDiaria: number(double) ex: 0; Espaco: integer ex: 0; CodigoCaixa: string(string) ex: ""; CustoCompra: number(double) ex: 0; CustoEmpresa: number(double) ex: 0; CustoFiscal: number(double) ex: 0; CustoMedio: number(double) ex: 0; CustoTranferencia: number(double) ex: 0; SetorLoja: string(string) ex: ""; SetorDeposito: string(string) ex: ""; PrecoUnidadeMedida: number(double) ex: 0; Altura: number(integer) ex: 20; Largura: number(integer) ex: 14; Profundidade: number(integer) ex: 19; Peso: number(double) ex: 0.1; PesoLiquido: number(double) ex: 0.1; TipoEmbalagem: string(string) ex: "UN"; QuantidadeEmbalagem: integer ex: 1; Alterado: string(string) ex: "S"; Etq: integer ex: 1; Ctz: integer ex: 0; Tecla: string(string) ex: "0"; PzRepos: integer ex: 0; PzEntrega: integer ex: 0; DiasSeg: integer ex: 0; Validade: integer ex: 0; ValMinima: integer ex: 0; Marcado: string(string) ex: "N"; Bloqueado: string(string) ex: "N"; PrVendaAnt: number(double) ex: 0; DtPrVenda: string(string) ex: "08-03-2019"; UsuAltPr: integer ex: 0; Margem: number(double) ex: 25; MargemMin: number(double) ex: 10; QtdeOferta: number(double) ex: 0; DtIniOferta: string(string) ex: "08-03-2019"; DtUltComp: string(string) ex: "08-03-2019"; PrUltComp: number(double) ex: 0; QultComp: number(double) ex: 0; UltSimbComp: string(string) ex: ""; RedBCUltComp: number(double) ex: 0; UltForn: integer ex: 0; DtCustos: string(string) ex: "08-03-2019"; Comissao: number(double) ex: 1; DifCusto: number(double) ex: 0; DifVenda: number(double) ex: 0; EtqMag: string(string) ex: "N"; QtdeAbLoja: number(double) ex: 0; DtAbLoja: string(string) ex: "08-03-2019"; DataOfAnt: string(string) ex: "08-03-2019"; PrecoOfertaAnt: number(double) ex: 0; PrecoNormalAnt: number(double) ex: 0; TpAltPrVenda: string(string) ex: ""; DifCusto1: number(double) ex: 0; DifCusto2: number(double) ex: 0; DifCusto3: number(double) ex: 0; DifCusto4: number(double) ex: 0; DifCusto5: number(double) ex: 0; DifVenda1: number(double) ex: 0; DifVenda2: number(double) ex: 0; DifVenda3: number(double) ex: 0; DifVenda4: number(double) ex: 0; DifVenda5: number(double) ex: 0; CtCompraAnt: number(double) ex: 0; CtMedioAnt: number(double) ex: 0; CtFiscalAnt: number(double) ex: 0; CtEmpresaAnt: number(double) ex: 0; CtTransfAnt: number(double) ex: 0; PrUltCompAnt: number(double) ex: 0; TransCtMedio: string(string) ex: ""; Faquisicao: string(string) ex: ""; Extra1: string(string) ex: ""; Extra2: string(string) ex: ""; Extra3: string(string) ex: ""; Extra4: number(double) ex: 0; Extra5: number(double) ex: 0; Extra6: string(string) ex: ""; Extra7: string(string) ex: ""; Extra8: number(double) ex: 0; Extra9: number(double) ex: 0; Prod_Extra1: string(string) ex: "28401"; Prod_Extra2: string(string) ex: "Regra Atualizada"; Prod_Extra3: string(string) ex: "2"; Prod_Extra4: integer ex: 1; Prod_Extra5: integer ex: 0; Prod_Extra6: string(string) ex: "33072010"; Prod_Extra7: string(string) ex: "013 TESTE"; Prod_Extra8: integer ex: 0; Prod_Extra9: integer ex: 0; Dataalt: string(string) ex: "22-07-2015"; Usualt: integer ex: 40; Frentes: integer ex: 0; Orig_codigo: integer ex: 0; PrTabela: number(double) ex: 0; CreditoST: number(double) ex: 0; CodigoSim: string(string) ex: ""; DataOfAnt2: string(string) ex: "08-03-2019"; PrecoOfertaAnt2: number(double) ex: 0; PrecoNormalAnt2: number(double) ex: 0; PrNormal3: number(double) ex: 0; PrNormal4: number(double) ex: 0; PrNormal5: number(double) ex: 0; PrecoNormalAnt3: number(double) ex: 0; PrecoNormalAnt4: number(double) ex: 0; PrecoNormalAnt5: number(double) ex: 0; PrecoOfertaAnt3: number(double) ex: 0; PrecoOfertaAnt4: number(double) ex: 0; PrecoOfertaAnt5: number(double) ex: 0; Margem3: number(double) ex: 0; Margem4: number(double) ex: 0; Margem5: number(double) ex: 0; TipoAgOf: string(string) ex: ""; TipoAgOfAnt: string(string) ex: ""; TipoAgOfAnt2: string(string) ex: ""; TpTrocas: string(string) ex: ""; PrVdaPadrao: number(double) ex: 0; CurvasABC: string(string) ex: ""; PercImpostos: number(double) ex: 0; PrVenda2Ant: number(double) ex: 0; PrVenda2Ant2: number(double) ex: 0; CodigoPreco: integer ex: 1858; Descritivo: string(string) ex: ""; Funcao: string(string) ex: "EX"; CustoVenda: number(double) ex: 0 }

## ProdutoDetalhadoEstoqueSemEstoqueV21

{ Codigo: integer ex: 508942; SKU: integer ex: 508942; CodigoBarras: string(string) ex: "7898262580827"; CodigoNCM: string(string) ex: "19049000"; Descricao: string(string) ex: "Zzsalg Naturitos 50g Queijo"; DescricaoCliente: string(string) ex: "Cliente"; Complemento: string(string) ex: ""; Marca: string(string) ex: "Naturitos"; Preco: number(double) ex: 0; Grupo: string(string) ex: "21984"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "08-03-2019"; PrecoNormal: number(double) ex: 0; CodigoUnidade: string(string) ex: "004"; CodigoDepartamento: string(string) ex: "49.0"; Departamento: string(string) ex: "Mercearia Doce"; Ativo: boolean ex: true; CodigoTributario: string(string) ex: "19049000"; Estoque1: number(double) ex: 0; Estoque2: number(double) ex: 0; Estoque3: number(double) ex: 0; Estoque4: number(double) ex: 0; Estoque5: number(double) ex: 0; PrecoLista: number(double) ex: 0; PrecoPDV: number(double) ex: 0; PrecoPDV2: number(double) ex: 0; PrecoPDV3: number(double) ex: 0; PrecoPDV4: number(double) ex: 0; PrecoPDV5: number(double) ex: 0; PrecoEtiqueta: number(double) ex: 0; PrecoCartaz: number(double) ex: 0; PrecoVenda2: number(double) ex: 0; PrecoVenda3: number(double) ex: 0; PrecoVenda4: number(double) ex: 0; PrecoVenda5: number(double) ex: 0; FatorPr3: integer ex: 0; FatorPr4: integer ex: 0; FatorPr5: integer ex: 0; CodEstoque: integer ex: 0; EstoqueMinimo: number(double) ex: 0; EstoqueMaximo: number(double) ex: 0; VendaMediaDiaria: number(double) ex: 0; Espaco: integer ex: 0; CodigoCaixa: string(string) ex: ""; CustoCompra: number(double) ex: 0; CustoEmpresa: number(double) ex: 0; CustoFiscal: number(double) ex: 0; CustoMedio: number(double) ex: 0; CustoTranferencia: number(double) ex: 0; SetorLoja: string(string) ex: ""; SetorDeposito: string(string) ex: ""; PrecoUnidadeMedida: number(double) ex: 0; Altura: number(integer) ex: 20; Largura: number(integer) ex: 14; Profundidade: number(integer) ex: 19; Peso: number(double) ex: 0.1; PesoLiquido: number(double) ex: 0.1; TipoEmbalagem: string(string) ex: "UN"; QuantidadeEmbalagem: integer ex: 1; Alterado: string(string) ex: "S"; Etq: integer ex: 1; Ctz: integer ex: 0; Tecla: string(string) ex: "0"; PzRepos: integer ex: 0; PzEntrega: integer ex: 0; DiasSeg: integer ex: 0; Validade: integer ex: 0; ValMinima: integer ex: 0; Marcado: string(string) ex: "N"; Bloqueado: string(string) ex: "N"; PrVendaAnt: number(double) ex: 0; DtPrVenda: string(string) ex: "08-03-2019"; UsuAltPr: integer ex: 0; Margem: number(double) ex: 25; MargemMin: number(double) ex: 10; QtdeOferta: number(double) ex: 0; DtIniOferta: string(string) ex: "08-03-2019"; DtUltComp: string(string) ex: "08-03-2019"; PrUltComp: number(double) ex: 0; QultComp: number(double) ex: 0; UltSimbComp: string(string) ex: ""; RedBCUltComp: number(double) ex: 0; UltForn: integer ex: 0; DtCustos: string(string) ex: "08-03-2019"; Comissao: number(double) ex: 1; DifCusto: number(double) ex: 0; DifVenda: number(double) ex: 0; EtqMag: string(string) ex: "N"; QtdeAbLoja: number(double) ex: 0; DtAbLoja: string(string) ex: "08-03-2019"; DataOfAnt: string(string) ex: "08-03-2019"; PrecoOfertaAnt: number(double) ex: 0; PrecoNormalAnt: number(double) ex: 0; TpAltPrVenda: string(string) ex: ""; DifCusto1: number(double) ex: 0; DifCusto2: number(double) ex: 0; DifCusto3: number(double) ex: 0; DifCusto4: number(double) ex: 0; DifCusto5: number(double) ex: 0; DifVenda1: number(double) ex: 0; DifVenda2: number(double) ex: 0; DifVenda3: number(double) ex: 0; DifVenda4: number(double) ex: 0; DifVenda5: number(double) ex: 0; CtCompraAnt: number(double) ex: 0; CtMedioAnt: number(double) ex: 0; CtFiscalAnt: number(double) ex: 0; CtEmpresaAnt: number(double) ex: 0; CtTransfAnt: number(double) ex: 0; PrUltCompAnt: number(double) ex: 0; TransCtMedio: string(string) ex: ""; Faquisicao: string(string) ex: ""; Extra1: string(string) ex: ""; Extra2: string(string) ex: ""; Extra3: string(string) ex: ""; Extra4: number(double) ex: 0; Extra5: number(double) ex: 0; Extra6: string(string) ex: ""; Extra7: string(string) ex: ""; Extra8: number(double) ex: 0; Extra9: number(double) ex: 0; Prod_Extra1: string(string) ex: "28401"; Prod_Extra2: string(string) ex: "Regra Atualizada"; Prod_Extra3: string(string) ex: "2"; Prod_Extra4: integer ex: 1; Prod_Extra5: integer ex: 0; Prod_Extra6: string(string) ex: "33072010"; Prod_Extra7: string(string) ex: "013 TESTE"; Prod_Extra8: integer ex: 0; Prod_Extra9: integer ex: 0; Dataalt: string(string) ex: "22-07-2015"; Usualt: integer ex: 40; Frentes: integer ex: 0; Orig_codigo: integer ex: 0; PrTabela: number(double) ex: 0; CreditoST: number(double) ex: 0; CodigoSim: string(string) ex: ""; DataOfAnt2: string(string) ex: "08-03-2019"; PrecoOfertaAnt2: number(double) ex: 0; PrecoNormalAnt2: number(double) ex: 0; PrNormal3: number(double) ex: 0; PrNormal4: number(double) ex: 0; PrNormal5: number(double) ex: 0; PrecoNormalAnt3: number(double) ex: 0; PrecoNormalAnt4: number(double) ex: 0; PrecoNormalAnt5: number(double) ex: 0; PrecoOfertaAnt3: number(double) ex: 0; PrecoOfertaAnt4: number(double) ex: 0; PrecoOfertaAnt5: number(double) ex: 0; Margem3: number(double) ex: 0; Margem4: number(double) ex: 0; Margem5: number(double) ex: 0; TipoAgOf: string(string) ex: ""; TipoAgOfAnt: string(string) ex: ""; TipoAgOfAnt2: string(string) ex: ""; TpTrocas: string(string) ex: ""; PrVdaPadrao: number(double) ex: 0; CurvasABC: string(string) ex: ""; PercImpostos: number(double) ex: 0; PrVenda2Ant: number(double) ex: 0; PrVenda2Ant2: number(double) ex: 0; CodigoPreco: integer ex: 1858; Descritivo: string(string) ex: ""; Funcao: string(string) ex: "EX"; CustoVenda: number(double) ex: 0; CodigoComprador: string ex: "008" }

## ProdutoDetalhadoEstoqueV1

{ Codigo: integer ex: 508942; SKU: integer ex: 508942; CodigoBarras: string(string) ex: "7898262580827"; CodigoNCM: string(string) ex: "19049000"; Descricao: string(string) ex: "Zzsalg Naturitos 50g Queijo"; Complemento: string(string) ex: ""; Marca: string(string) ex: "Naturitos"; Estoque: number(double) ex: 0; Preco: number(double) ex: 0; Grupo: string(string) ex: "21984"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "08-03-2019"; PrecoNormal: number(double) ex: 0; CodigoUnidade: string(string) ex: "004"; CodigoDepartamento: string(string) ex: "49.0"; Departamento: string(string) ex: "Mercearia Doce"; Ativo: boolean ex: true; CodigoTributario: string(string) ex: "19049000"; Estoque1: number(double) ex: 0; Estoque2: number(double) ex: 0; Estoque3: number(double) ex: 0; Estoque4: number(double) ex: 0; Estoque5: number(double) ex: 0; PrecoLista: number(double) ex: 0; PrecoPDV: number(double) ex: 0; PrecoPDV2: number(double) ex: 0; PrecoPDV3: number(double) ex: 0; PrecoPDV4: number(double) ex: 0; PrecoPDV5: number(double) ex: 0; PrecoEtiqueta: number(double) ex: 0; PrecoCartaz: number(double) ex: 0; PrecoVenda2: number(double) ex: 0; PrecoVenda3: number(double) ex: 0; PrecoVenda4: number(double) ex: 0; PrecoVenda5: number(double) ex: 0; FatorPr3: integer ex: 0; FatorPr4: integer ex: 0; FatorPr5: integer ex: 0; CodEstoque: integer ex: 0; EstoqueMinimo: number(double) ex: 0; EstoqueMaximo: number(double) ex: 0; VendaMediaDiaria: number(double) ex: 0; Espaco: integer ex: 0; CodigoCaixa: string(string) ex: ""; CustoCompra: number(double) ex: 0; CustoEmpresa: number(double) ex: 0; CustoFiscal: number(double) ex: 0; CustoMedio: number(double) ex: 0; CustoTranferencia: number(double) ex: 0; SetorLoja: string(string) ex: ""; SetorDeposito: string(string) ex: ""; PrecoUnidadeMedida: number(double) ex: 0; Altura: number(integer) ex: 20; Largura: number(integer) ex: 14; Profundidade: number(integer) ex: 19; Peso: number(double) ex: 0.1; PesoLiquido: number(double) ex: 0.1; TipoEmbalagem: string(string) ex: "UN"; QuantidadeEmbalagem: integer ex: 1; Alterado: string(string) ex: "S"; Etq: integer ex: 1; Ctz: integer ex: 0; Tecla: string(string) ex: "0"; PzRepos: integer ex: 0; PzEntrega: integer ex: 0; DiasSeg: integer ex: 0; Validade: integer ex: 0; ValMinima: integer ex: 0; Marcado: string(string) ex: "N"; Bloqueado: string(string) ex: "N"; PrVendaAnt: number(double) ex: 0; DtPrVenda: string(string) ex: "08-03-2019"; UsuAltPr: integer ex: 0; Margem: number(double) ex: 25; MargemMin: number(double) ex: 10; QtdeOferta: number(double) ex: 0; DtIniOferta: string(string) ex: "08-03-2019"; DtUltComp: string(string) ex: "08-03-2019"; PrUltComp: number(double) ex: 0; QultComp: number(double) ex: 0; UltSimbComp: string(string) ex: ""; RedBCUltComp: number(double) ex: 0; UltForn: integer ex: 0; DtCustos: string(string) ex: "08-03-2019"; Comissao: number(double) ex: 1; DifCusto: number(double) ex: 0; DifVenda: number(double) ex: 0; EtqMag: string(string) ex: "N"; QtdeAbLoja: number(double) ex: 0; DtAbLoja: string(string) ex: "08-03-2019"; DataOfAnt: string(string) ex: "08-03-2019"; PrecoOfertaAnt: number(double) ex: 0; PrecoNormalAnt: number(double) ex: 0; TpAltPrVenda: string(string) ex: ""; DifCusto1: number(double) ex: 0; DifCusto2: number(double) ex: 0; DifCusto3: number(double) ex: 0; DifCusto4: number(double) ex: 0; DifCusto5: number(double) ex: 0; DifVenda1: number(double) ex: 0; DifVenda2: number(double) ex: 0; DifVenda3: number(double) ex: 0; DifVenda4: number(double) ex: 0; DifVenda5: number(double) ex: 0; CtCompraAnt: number(double) ex: 0; CtMedioAnt: number(double) ex: 0; CtFiscalAnt: number(double) ex: 0; CtEmpresaAnt: number(double) ex: 0; CtTransfAnt: number(double) ex: 0; PrUltCompAnt: number(double) ex: 0; TransCtMedio: string(string) ex: ""; Faquisicao: string(string) ex: ""; Extra1: string(string) ex: ""; Extra2: string(string) ex: ""; Extra3: string(string) ex: ""; Extra4: number(double) ex: 0; Extra5: number(double) ex: 0; Extra6: string(string) ex: ""; Extra7: string(string) ex: ""; Extra8: number(double) ex: 0; Extra9: number(double) ex: 0; Dataalt: string(string) ex: "22-07-2015"; Usualt: integer ex: 40; Frentes: integer ex: 0; Orig_codigo: integer ex: 0; PrTabela: number(double) ex: 0; CreditoST: number(double) ex: 0; CodigoSim: string(string) ex: ""; DataOfAnt2: string(string) ex: "08-03-2019"; PrecoOfertaAnt2: number(double) ex: 0; PrecoNormalAnt2: number(double) ex: 0; PrNormal3: number(double) ex: 0; PrNormal4: number(double) ex: 0; PrNormal5: number(double) ex: 0; PrecoNormalAnt3: number(double) ex: 0; PrecoNormalAnt4: number(double) ex: 0; PrecoNormalAnt5: number(double) ex: 0; PrecoOfertaAnt3: number(double) ex: 0; PrecoOfertaAnt4: number(double) ex: 0; PrecoOfertaAnt5: number(double) ex: 0; Margem3: number(double) ex: 0; Margem4: number(double) ex: 0; Margem5: number(double) ex: 0; TipoAgOf: string(string) ex: ""; TipoAgOfAnt: string(string) ex: ""; TipoAgOfAnt2: string(string) ex: ""; TpTrocas: string(string) ex: ""; PrVdaPadrao: number(double) ex: 0; CurvasABC: string(string) ex: ""; PercImpostos: number(double) ex: 0; PrVenda2Ant: number(double) ex: 0; PrVenda2Ant2: number(double) ex: 0; CodigoPreco: integer ex: 1858; Descritivo: string(string) ex: ""; Funcao: string(string) ex: "EX" }

## ProdutoDetalhadoEstoqueV19

{ Codigo: integer ex: 508942; SKU: integer ex: 508942; CodigoBarras: string(string) ex: "7898262580827"; CodigoNCM: string(string) ex: "19049000"; Descricao: string(string) ex: "Zzsalg Naturitos 50g Queijo"; DescricaoCliente: string(string) ex: "Cliente"; Complemento: string(string) ex: ""; Marca: string(string) ex: "Naturitos"; Estoque: number(double) ex: 0; Preco: number(double) ex: 0; Grupo: string(string) ex: "21984"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "08-03-2019"; PrecoNormal: number(double) ex: 0; CodigoUnidade: string(string) ex: "004"; CodigoDepartamento: string(string) ex: "49.0"; Departamento: string(string) ex: "Mercearia Doce"; Ativo: boolean ex: true; CodigoTributario: string(string) ex: "19049000"; Estoque1: number(double) ex: 0; Estoque2: number(double) ex: 0; Estoque3: number(double) ex: 0; Estoque4: number(double) ex: 0; Estoque5: number(double) ex: 0; PrecoLista: number(double) ex: 0; PrecoPDV: number(double) ex: 0; PrecoPDV2: number(double) ex: 0; PrecoPDV3: number(double) ex: 0; PrecoPDV4: number(double) ex: 0; PrecoPDV5: number(double) ex: 0; PrecoEtiqueta: number(double) ex: 0; PrecoCartaz: number(double) ex: 0; PrecoVenda2: number(double) ex: 0; PrecoVenda3: number(double) ex: 0; PrecoVenda4: number(double) ex: 0; PrecoVenda5: number(double) ex: 0; FatorPr3: integer ex: 0; FatorPr4: integer ex: 0; FatorPr5: integer ex: 0; CodEstoque: integer ex: 0; EstoqueMinimo: number(double) ex: 0; EstoqueMaximo: number(double) ex: 0; VendaMediaDiaria: number(double) ex: 0; Espaco: integer ex: 0; CodigoCaixa: string(string) ex: ""; CustoCompra: number(double) ex: 0; CustoEmpresa: number(double) ex: 0; CustoFiscal: number(double) ex: 0; CustoMedio: number(double) ex: 0; CustoTranferencia: number(double) ex: 0; SetorLoja: string(string) ex: ""; SetorDeposito: string(string) ex: ""; PrecoUnidadeMedida: number(double) ex: 0; Altura: number(integer) ex: 20; Largura: number(integer) ex: 14; Profundidade: number(integer) ex: 19; Peso: number(double) ex: 0.1; PesoLiquido: number(double) ex: 0.1; TipoEmbalagem: string(string) ex: "UN"; QuantidadeEmbalagem: integer ex: 1; Alterado: string(string) ex: "S"; Etq: integer ex: 1; Ctz: integer ex: 0; Tecla: string(string) ex: "0"; PzRepos: integer ex: 0; PzEntrega: integer ex: 0; DiasSeg: integer ex: 0; Validade: integer ex: 0; ValMinima: integer ex: 0; Marcado: string(string) ex: "N"; Bloqueado: string(string) ex: "N"; PrVendaAnt: number(double) ex: 0; DtPrVenda: string(string) ex: "08-03-2019"; UsuAltPr: integer ex: 0; Margem: number(double) ex: 25; MargemMin: number(double) ex: 10; QtdeOferta: number(double) ex: 0; DtIniOferta: string(string) ex: "08-03-2019"; DtUltComp: string(string) ex: "08-03-2019"; PrUltComp: number(double) ex: 0; QultComp: number(double) ex: 0; UltSimbComp: string(string) ex: ""; RedBCUltComp: number(double) ex: 0; UltForn: integer ex: 0; DtCustos: string(string) ex: "08-03-2019"; Comissao: number(double) ex: 1; DifCusto: number(double) ex: 0; DifVenda: number(double) ex: 0; EtqMag: string(string) ex: "N"; QtdeAbLoja: number(double) ex: 0; DtAbLoja: string(string) ex: "08-03-2019"; DataOfAnt: string(string) ex: "08-03-2019"; PrecoOfertaAnt: number(double) ex: 0; PrecoNormalAnt: number(double) ex: 0; TpAltPrVenda: string(string) ex: ""; DifCusto1: number(double) ex: 0; DifCusto2: number(double) ex: 0; DifCusto3: number(double) ex: 0; DifCusto4: number(double) ex: 0; DifCusto5: number(double) ex: 0; DifVenda1: number(double) ex: 0; DifVenda2: number(double) ex: 0; DifVenda3: number(double) ex: 0; DifVenda4: number(double) ex: 0; DifVenda5: number(double) ex: 0; CtCompraAnt: number(double) ex: 0; CtMedioAnt: number(double) ex: 0; CtFiscalAnt: number(double) ex: 0; CtEmpresaAnt: number(double) ex: 0; CtTransfAnt: number(double) ex: 0; PrUltCompAnt: number(double) ex: 0; TransCtMedio: string(string) ex: ""; Faquisicao: string(string) ex: ""; Extra1: string(string) ex: ""; Extra2: string(string) ex: ""; Extra3: string(string) ex: ""; Extra4: number(double) ex: 0; Extra5: number(double) ex: 0; Extra6: string(string) ex: ""; Extra7: string(string) ex: ""; Extra8: number(double) ex: 0; Extra9: number(double) ex: 0; Prod_Extra1: string(string) ex: "28401"; Prod_Extra2: string(string) ex: "Regra Atualizada"; Prod_Extra3: string(string) ex: "2"; Prod_Extra4: integer ex: 1; Prod_Extra5: integer ex: 0; Prod_Extra6: string(string) ex: "33072010"; Prod_Extra7: string(string) ex: "013 TESTE"; Prod_Extra8: integer ex: 0; Prod_Extra9: integer ex: 0; Dataalt: string(string) ex: "22-07-2015"; Usualt: integer ex: 40; Frentes: integer ex: 0; Orig_codigo: integer ex: 0; PrTabela: number(double) ex: 0; CreditoST: number(double) ex: 0; CodigoSim: string(string) ex: ""; DataOfAnt2: string(string) ex: "08-03-2019"; PrecoOfertaAnt2: number(double) ex: 0; PrecoNormalAnt2: number(double) ex: 0; PrNormal3: number(double) ex: 0; PrNormal4: number(double) ex: 0; PrNormal5: number(double) ex: 0; PrecoNormalAnt3: number(double) ex: 0; PrecoNormalAnt4: number(double) ex: 0; PrecoNormalAnt5: number(double) ex: 0; PrecoOfertaAnt3: number(double) ex: 0; PrecoOfertaAnt4: number(double) ex: 0; PrecoOfertaAnt5: number(double) ex: 0; Margem3: number(double) ex: 0; Margem4: number(double) ex: 0; Margem5: number(double) ex: 0; TipoAgOf: string(string) ex: ""; TipoAgOfAnt: string(string) ex: ""; TipoAgOfAnt2: string(string) ex: ""; TpTrocas: string(string) ex: ""; PrVdaPadrao: number(double) ex: 0; CurvasABC: string(string) ex: ""; PercImpostos: number(double) ex: 0; PrVenda2Ant: number(double) ex: 0; PrVenda2Ant2: number(double) ex: 0; CodigoPreco: integer ex: 1858; Descritivo: string(string) ex: ""; Funcao: string(string) ex: "EX" }

## ProdutoDetalhadoEstoqueV27

array de { Codigo: number ex: 21355; SKU: number ex: 21355; CodigoBarras: string(string) ex: "0000000000121"; CodigoNCM: string(string) ex: "08011100"; Descricao: string(string) ex: "Coco Seco - Kg"; Complemento: string(string) ex: ""; Marca: string(string) ex: "A Definir"; Estoque: number ex: 0; Preco: number ex: 3; Grupo: string(string) ex: "10000"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "01-06-2022"; PrecoNormal: number ex: 3; CodigoUnidade: string(string) ex: "001"; CodigoDepartamento: string(string) ex: "999"; Departamento: string(string) ex: "Importação"; Ativo: string(string) ex: true; CodigoTributario: string(string) ex: "99999"; Estoque1: number ex: 0; Estoque2: number ex: 0; Estoque3: number ex: 0; Estoque4: number ex: 0; Estoque5: number ex: 0; PrecoLista: number ex: 0; PrecoPDV: number ex: 3; PrecoPDV2: number ex: 0; PrecoPDV3: number ex: 0; PrecoPDV4: number ex: 0; PrecoPDV5: number ex: 0; PrecoEtiqueta: number ex: 3; PrecoCartaz: number ex: 3; PrecoVenda2: number ex: 0; PrecoVenda3: number ex: 0; PrecoVenda4: number ex: 0; PrecoVenda5: number ex: 0; FatorPr3: number ex: 0; FatorPr4: number ex: 0; FatorPr5: number ex: 0; CodEstoque: number ex: 0; EstoqueMinimo: number ex: 0; EstoqueMaximo: number ex: 0; VendaMediaDiaria: number ex: 0; Espaco: number ex: 0; CodigoCaixa: string(string) ex: ""; CustoCompra: number ex: 2; CustoEmpresa: number ex: 2; CustoFiscal: number ex: 2; CustoMedio: number ex: 2; CustoTranferencia: number ex: 2; SetorLoja: string(string) ex: ""; SetorDeposito: string(string) ex: ""; PrecoUnidadeMedida: number ex: 0; DescricaoPDV: string(string) ex: "Coco Seco - Kg"; Bloqueado: string(string) ex: "N"; Altura: number ex: 0; Largura: number ex: 0; Profundidade: number ex: 0; Peso: number ex: 0; PesoLiquido: number ex: 0; DescricaoCliente: string(string) ex: "Coco Seco - Kg"; Temperatura: number ex: 0; TipoEmbalagem: string(string) ex: "UN"; QuantidadeEmbalagem: number ex: 1; Alterado: string(string) ex: "N"; Etq: number ex: 1; Ctz: number ex: 1; Tecla: string(string) ex: ""; PzRepos: number ex: 0; PzEntrega: number ex: 0; DiasSeg: number ex: 0; Validade: number ex: 0; ValMinima: number ex: 0; Marcado: string(string) ex: "N"; PrVendaAnt: number ex: 3; DtPrVenda: string(string) ex: "22-09-2017"; UsuAltPr: number ex: 936; Margem: number ex: 0; MargemMin: number ex: 0; QtdeOferta: number ex: 0; DtIniOferta: string(string) ex: "01-06-2022"; DtUltComp: string(string) ex: "25-10-2012"; PrUltComp: number ex: 0; QultComp: number ex: 0; UltSimbComp: string(string) ex: ""; RedBCUltComp: number ex: 0; UltForn: number ex: 1481; DtCustos: string(string) ex: "01-06-2022"; Comissao: number ex: 0; DifCusto: number ex: 0; DifVenda: number ex: 0; EtqMag: string(string) ex: "N"; QtdeAbLoja: number ex: 0; DtAbLoja: string(string) ex: "01-06-2022"; DataOfAnt: string(string) ex: "01-06-2022"; PrecoOfertaAnt: number ex: 3; PrecoNormalAnt: number ex: 3; TpAltPrVenda: string(string) ex: "0"; DifCusto1: number ex: 0; DifCusto2: number ex: 0; DifCusto3: number ex: 0; DifCusto4: number ex: 0; DifCusto5: number ex: 0; DifVenda1: number ex: 0; DifVenda2: number ex: 0; DifVenda3: number ex: 0; DifVenda4: number ex: 0; DifVenda5: number ex: 0; CtCompraAnt: number ex: 2; CtMedioAnt: number ex: 2; CtFiscalAnt: number ex: 1481; CtEmpresaAnt: number ex: 1481; CtTransfAnt: number ex: 1481; PrUltCompAnt: number ex: 1481; TransCtMedio: string(string) ex: ""; Faquisicao: string(string) ex: ""; Extra1: string(string) ex: ""; Extra2: string(string) ex: "abc"; Extra3: string(string) ex: ""; Extra4: number ex: 12; Extra5: number ex: 200720; Extra6: number ex: 0; Extra7: number ex: 0; Extra8: number ex: 0; Extra9: number ex: 0; Prod_Extra1: string(string) ex: ""; Prod_Extra2: string(string) ex: ""; Prod_Extra3: string(string) ex: "Endereço: Santa Marta 0, 1"; Prod_Extra4: number ex: 0; Prod_Extra5: number ex: 0; Prod_Extra6: string(string) ex: ""; Prod_Extra7: string(string) ex: "extra7"; Prod_Extra8: number ex: 0; Prod_Extra9: number ex: 0; Extras: array de object { nome, tipo, valor }; Dataalt: string(string) ex: "28-01-2022"; Usualt: number ex: 936; Frentes: number ex: 0; Orig_codigo: number ex: 0; PrTabela: number ex: 0; CreditoST: number ex: 0; CodigoSim: string(string) ex: ""; DataOfAnt2: string(string) ex: "01-06-2022"; PrecoOfertaAnt2: number ex: 0; PrecoNormalAnt2: number ex: 0; PrNormal3: number ex: 0; PrNormal4: number ex: 0; PrNormal5: number ex: 0; PrecoNormalAnt3: number ex: 0; PrecoNormalAnt4: number ex: 0; PrecoNormalAnt5: number ex: 0; PrecoOfertaAnt3: number ex: 0; PrecoOfertaAnt4: number ex: 0; PrecoOfertaAnt5: number ex: 0; Margem3: number ex: 0; Margem4: number ex: 0; Margem5: number ex: 0; TipoAgOf: string(string) ex: ""; TipoAgOfAnt: string(string) ex: ""; TipoAgOfAnt2: string(string) ex: ""; TpTrocas: string(string) ex: ""; PrVdaPadrao: number ex: 0; CurvasABC: object { Geral, Departamento, Grupo }; PercImpostos: number ex: 0; PrVenda2Ant: number ex: 0; PrVenda2Ant2: number ex: 0; CodigoPreco: number ex: 1; Descritivo: string(string) ex: ""; Funcao: string(string) ex: ""; Balanca: string(string) ex: "P"; CustoVenda: number ex: 0; CodigoComprador: string(string) ex: ""; Alcada: number ex: 0; FatorEstoque: number ex: 0; tributacao: object { icms, ipi, pis, cofins, icms_st, controle } }

## ProdutoDetalhadoEstoqueV27Array

array de **ProdutoDetalhadoEstoqueV27** = array de object { Codigo, SKU, CodigoBarras, CodigoNCM, Descricao, Complemento, Marca, Estoque, Preco, Grupo, Oferta, DataOferta, PrecoNormal, CodigoUnidade, CodigoDepartamento, Departamento, Ativo, CodigoTributario, Estoque1, Estoque2, Estoque3, Estoque4, Estoque5, PrecoLista, PrecoPDV, PrecoPDV2, PrecoPDV3, PrecoPDV4, PrecoPDV5, PrecoEtiqueta, PrecoCartaz, PrecoVenda2, PrecoVenda3, PrecoVenda4, PrecoVenda5, FatorPr3, FatorPr4, FatorPr5, CodEstoque, EstoqueMinimo, EstoqueMaximo, VendaMediaDiaria, Espaco, CodigoCaixa, CustoCompra, CustoEmpresa, CustoFiscal, CustoMedio, CustoTranferencia, SetorLoja, SetorDeposito, PrecoUnidadeMedida, DescricaoPDV, Bloqueado, Altura, Largura, Profundidade, Peso, PesoLiquido, DescricaoCliente, Temperatura, TipoEmbalagem, QuantidadeEmbalagem, Alterado, Etq, Ctz, Tecla, PzRepos, PzEntrega, DiasSeg, Validade, ValMinima, Marcado, PrVendaAnt, DtPrVenda, UsuAltPr, Margem, MargemMin, QtdeOferta, DtIniOferta, DtUltComp, PrUltComp, QultComp, UltSimbComp, RedBCUltComp, UltForn, DtCustos, Comissao, DifCusto, DifVenda, EtqMag, QtdeAbLoja, DtAbLoja, DataOfAnt, PrecoOfertaAnt, PrecoNormalAnt, TpAltPrVenda, DifCusto1, DifCusto2, DifCusto3, DifCusto4, DifCusto5, DifVenda1, DifVenda2, DifVenda3, DifVenda4, DifVenda5, CtCompraAnt, CtMedioAnt, CtFiscalAnt, CtEmpresaAnt, CtTransfAnt, PrUltCompAnt, TransCtMedio, Faquisicao, Extra1, Extra2, Extra3, Extra4, Extra5, Extra6, Extra7, Extra8, Extra9, Prod_Extra1, Prod_Extra2, Prod_Extra3, Prod_Extra4, Prod_Extra5, Prod_Extra6, Prod_Extra7, Prod_Extra8, Prod_Extra9, Extras, Dataalt, Usualt, Frentes, Orig_codigo, PrTabela, CreditoST, CodigoSim, DataOfAnt2, PrecoOfertaAnt2, PrecoNormalAnt2, PrNormal3, PrNormal4, PrNormal5, PrecoNormalAnt3, PrecoNormalAnt4, PrecoNormalAnt5, PrecoOfertaAnt3, PrecoOfertaAnt4, PrecoOfertaAnt5, Margem3, Margem4, Margem5, TipoAgOf, TipoAgOfAnt, TipoAgOfAnt2, TpTrocas, PrVdaPadrao, CurvasABC, PercImpostos, PrVenda2Ant, PrVenda2Ant2, CodigoPreco, Descritivo, Funcao, Balanca, CustoVenda, CodigoComprador, Alcada, FatorEstoque, tributacao }

## ProdutoDetalhadoEstoqueV28

{ Codigo: number ex: 21355; SKU: number ex: 21355; CodigoBarras: string(string) ex: "0000000000121"; CodigoNCM: string(string) ex: "08011100"; Descricao: string(string) ex: "Coco Seco - Kg"; Complemento: string(string) ex: ""; Marca: string(string) ex: "A Definir"; Status: string(string) ex: "NORMAL"; Estoque: number ex: 0; Preco: number ex: 3; Grupo: string(string) ex: "10000"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "01-06-2022"; PrecoNormal: number ex: 3; CodigoUnidade: string(string) ex: "001"; CodigoDepartamento: string(string) ex: "999"; Departamento: string(string) ex: "Importação"; Ativo: string(string) ex: true; CodigoTributario: string(string) ex: "99999"; Estoque1: number ex: 0; Estoque2: number ex: 0; Estoque3: number ex: 0; Estoque4: number ex: 0; Estoque5: number ex: 0; PrecoLista: number ex: 0; PrecoPDV: number ex: 3; PrecoPDV3: number ex: 0; PrecoPDV2: number ex: 0; PrecoPDV4: number ex: 0; PrecoPDV5: number ex: 0; PrecoEtiqueta: number ex: 3; PrecoCartaz: number ex: 3; PrecoVenda2: number ex: 0; PrecoVenda3: number ex: 0; PrecoVenda4: number ex: 0; PrecoVenda5: number ex: 0; FatorPr3: number ex: 0; FatorPr4: number ex: 0; FatorPr5: number ex: 0; CodEstoque: number ex: 0; EstoqueMinimo: number ex: 0; EstoqueMaximo: number ex: 0; VendaMediaDiaria: number ex: 0; Espaco: number ex: 0; CodigoCaixa: string(string) ex: ""; CustoCompra: number ex: 2; CustoEmpresa: number ex: 2; CustoFiscal: number ex: 2; CustoMedio: number ex: 2; CustoTranferencia: number ex: 2; SetorLoja: string(string) ex: ""; SetorDeposito: string(string) ex: ""; PrecoUnidadeMedida: number ex: 0; DescricaoPDV: string(string) ex: "Coco Seco - Kg"; Bloqueado: string(string) ex: "N"; Altura: number ex: 0; Largura: number ex: 0; Profundidade: number ex: 0; Peso: number ex: 0; PesoLiquido: number ex: 0; DescricaoCliente: string(string) ex: "Coco Seco - Kg"; Temperatura: number ex: 0; TipoEmbalagem: string(string) ex: "UN"; QuantidadeEmbalagem: number ex: 1; Alterado: string(string) ex: "N"; Etq: number ex: 1; Ctz: number ex: 1; Tecla: string(string) ex: ""; PzRepos: number ex: 0; PzEntrega: number ex: 0; DiasSeg: number ex: 0; Validade: number ex: 0; ValMinima: number ex: 0; Marcado: string(string) ex: "N"; PrVendaAnt: number ex: 3; DtPrVenda: string(string) ex: "22-09-2017"; UsuAltPr: number ex: 936; Margem: number ex: 0; MargemMin: number ex: 0; QtdeOferta: number ex: 0; DtIniOferta: string(string) ex: "01-06-2022"; DtUltComp: string(string) ex: "25-10-2012"; PrUltComp: number ex: 0; QultComp: number ex: 0; UltSimbComp: string(string) ex: ""; RedBCUltComp: number ex: 0; UltForn: number ex: 1481; DtCustos: string(string) ex: "01-06-2022"; Comissao: number ex: 0; DifCusto: number ex: 0; DifVenda: number ex: 0; EtqMag: string(string) ex: "N"; QtdeAbLoja: number ex: 0; DtAbLoja: string(string) ex: "01-06-2022"; DataOfAnt: string(string) ex: "01-06-2022"; PrecoOfertaAnt: number ex: 3; PrecoNormalAnt: number ex: 3; TpAltPrVenda: string(string) ex: "0"; DifCusto1: number ex: 0; DifCusto2: number ex: 0; DifCusto3: number ex: 0; DifCusto4: number ex: 0; DifCusto5: number ex: 0; DifVenda1: number ex: 0; DifVenda2: number ex: 0; DifVenda3: number ex: 0; DifVenda4: number ex: 0; DifVenda5: number ex: 0; CtCompraAnt: number ex: 2; CtMedioAnt: number ex: 2; CtFiscalAnt: number ex: 1481; CtEmpresaAnt: number ex: 1481; CtTransfAnt: number ex: 1481; PrUltCompAnt: number ex: 1481; TransCtMedio: string(string) ex: ""; Faquisicao: string(string) ex: ""; Extra1: string(string) ex: ""; Extra2: string(string) ex: "abc"; Extra3: string(string) ex: ""; Extra4: number ex: 12; Extra5: number ex: 200720; Extra6: number ex: 0; Extra7: number ex: 0; Extra8: number ex: 0; Extra9: number ex: 0; Prod_Extra1: string(string) ex: ""; Prod_Extra2: string(string) ex: ""; Prod_Extra3: string(string) ex: "Endereço: Santa Marta 0, 1"; Prod_Extra4: number ex: 0; Prod_Extra5: number ex: 0; Prod_Extra6: string(string) ex: ""; Prod_Extra7: string(string) ex: "extra7"; Prod_Extra8: number ex: 0; Prod_Extra9: number ex: 0; Extras: array de object { nome, tipo, valor }; Dataalt: string(string) ex: "28-01-2022"; Usualt: number ex: 936; Frentes: number ex: 0; Orig_codigo: number ex: 0; PrTabela: number ex: 0; CreditoST: number ex: 0; CodigoSim: string(string) ex: ""; DataOfAnt2: string(string) ex: "01-06-2022"; PrecoOfertaAnt2: number ex: 0; PrecoNormalAnt2: number ex: 0; PrNormal3: number ex: 0; PrNormal4: number ex: 0; PrNormal5: number ex: 0; PrecoNormalAnt3: number ex: 0; PrecoNormalAnt4: number ex: 0; PrecoNormalAnt5: number ex: 0; PrecoOfertaAnt3: number ex: 0; PrecoOfertaAnt4: number ex: 0; PrecoOfertaAnt5: number ex: 0; Margem3: number ex: 0; Margem4: number ex: 0; Margem5: number ex: 0; TipoAgOf: string(string) ex: ""; TipoAgOfAnt: string(string) ex: ""; TipoAgOfAnt2: string(string) ex: ""; TpTrocas: string(string) ex: ""; PrVdaPadrao: number ex: 0; CurvasABC: object { Geral, Departamento, Grupo }; PercImpostos: number ex: 0; PrVenda2Ant: number ex: 0; PrVenda2Ant2: number ex: 0; CodigoPreco: number ex: 1; Descritivo: string(string) ex: ""; Funcao: string(string) ex: ""; Balanca: string(string) ex: "P"; CustoVenda: number ex: 0; CodigoComprador: string(string) ex: ""; Alcada: number ex: 0; FatorEstoque: number ex: 0; tributacao: object { icms, ipi, pis, cofins, icms_st, controle }; DataHoraManutencao: string(string;) ex: "21/03/2023 14:25:39.651" }

## ProdutoDetalhadoEstoqueV28Array

array de **ProdutoDetalhadoEstoqueV28** = object { Codigo, SKU, CodigoBarras, CodigoNCM, Descricao, Complemento, Marca, Status, Estoque, Preco, Grupo, Oferta, DataOferta, PrecoNormal, CodigoUnidade, CodigoDepartamento, Departamento, Ativo, CodigoTributario, Estoque1, Estoque2, Estoque3, Estoque4, Estoque5, PrecoLista, PrecoPDV, PrecoPDV3, PrecoPDV2, PrecoPDV4, PrecoPDV5, PrecoEtiqueta, PrecoCartaz, PrecoVenda2, PrecoVenda3, PrecoVenda4, PrecoVenda5, FatorPr3, FatorPr4, FatorPr5, CodEstoque, EstoqueMinimo, EstoqueMaximo, VendaMediaDiaria, Espaco, CodigoCaixa, CustoCompra, CustoEmpresa, CustoFiscal, CustoMedio, CustoTranferencia, SetorLoja, SetorDeposito, PrecoUnidadeMedida, DescricaoPDV, Bloqueado, Altura, Largura, Profundidade, Peso, PesoLiquido, DescricaoCliente, Temperatura, TipoEmbalagem, QuantidadeEmbalagem, Alterado, Etq, Ctz, Tecla, PzRepos, PzEntrega, DiasSeg, Validade, ValMinima, Marcado, PrVendaAnt, DtPrVenda, UsuAltPr, Margem, MargemMin, QtdeOferta, DtIniOferta, DtUltComp, PrUltComp, QultComp, UltSimbComp, RedBCUltComp, UltForn, DtCustos, Comissao, DifCusto, DifVenda, EtqMag, QtdeAbLoja, DtAbLoja, DataOfAnt, PrecoOfertaAnt, PrecoNormalAnt, TpAltPrVenda, DifCusto1, DifCusto2, DifCusto3, DifCusto4, DifCusto5, DifVenda1, DifVenda2, DifVenda3, DifVenda4, DifVenda5, CtCompraAnt, CtMedioAnt, CtFiscalAnt, CtEmpresaAnt, CtTransfAnt, PrUltCompAnt, TransCtMedio, Faquisicao, Extra1, Extra2, Extra3, Extra4, Extra5, Extra6, Extra7, Extra8, Extra9, Prod_Extra1, Prod_Extra2, Prod_Extra3, Prod_Extra4, Prod_Extra5, Prod_Extra6, Prod_Extra7, Prod_Extra8, Prod_Extra9, Extras, Dataalt, Usualt, Frentes, Orig_codigo, PrTabela, CreditoST, CodigoSim, DataOfAnt2, PrecoOfertaAnt2, PrecoNormalAnt2, PrNormal3, PrNormal4, PrNormal5, PrecoNormalAnt3, PrecoNormalAnt4, PrecoNormalAnt5, PrecoOfertaAnt3, PrecoOfertaAnt4, PrecoOfertaAnt5, Margem3, Margem4, Margem5, TipoAgOf, TipoAgOfAnt, TipoAgOfAnt2, TpTrocas, PrVdaPadrao, CurvasABC, PercImpostos, PrVenda2Ant, PrVenda2Ant2, CodigoPreco, Descritivo, Funcao, Balanca, CustoVenda, CodigoComprador, Alcada, FatorEstoque, tributacao, DataHoraManutencao }

## ProdutoDetalhadoEstoqueV29

**ProdutoDetalhadoEstoqueV28** = object { Codigo, SKU, CodigoBarras, CodigoNCM, Descricao, Complemento, Marca, Status, Estoque, Preco, Grupo, Oferta, DataOferta, PrecoNormal, CodigoUnidade, CodigoDepartamento, Departamento, Ativo, CodigoTributario, Estoque1, Estoque2, Estoque3, Estoque4, Estoque5, PrecoLista, PrecoPDV, PrecoPDV3, PrecoPDV2, PrecoPDV4, PrecoPDV5, PrecoEtiqueta, PrecoCartaz, PrecoVenda2, PrecoVenda3, PrecoVenda4, PrecoVenda5, FatorPr3, FatorPr4, FatorPr5, CodEstoque, EstoqueMinimo, EstoqueMaximo, VendaMediaDiaria, Espaco, CodigoCaixa, CustoCompra, CustoEmpresa, CustoFiscal, CustoMedio, CustoTranferencia, SetorLoja, SetorDeposito, PrecoUnidadeMedida, DescricaoPDV, Bloqueado, Altura, Largura, Profundidade, Peso, PesoLiquido, DescricaoCliente, Temperatura, TipoEmbalagem, QuantidadeEmbalagem, Alterado, Etq, Ctz, Tecla, PzRepos, PzEntrega, DiasSeg, Validade, ValMinima, Marcado, PrVendaAnt, DtPrVenda, UsuAltPr, Margem, MargemMin, QtdeOferta, DtIniOferta, DtUltComp, PrUltComp, QultComp, UltSimbComp, RedBCUltComp, UltForn, DtCustos, Comissao, DifCusto, DifVenda, EtqMag, QtdeAbLoja, DtAbLoja, DataOfAnt, PrecoOfertaAnt, PrecoNormalAnt, TpAltPrVenda, DifCusto1, DifCusto2, DifCusto3, DifCusto4, DifCusto5, DifVenda1, DifVenda2, DifVenda3, DifVenda4, DifVenda5, CtCompraAnt, CtMedioAnt, CtFiscalAnt, CtEmpresaAnt, CtTransfAnt, PrUltCompAnt, TransCtMedio, Faquisicao, Extra1, Extra2, Extra3, Extra4, Extra5, Extra6, Extra7, Extra8, Extra9, Prod_Extra1, Prod_Extra2, Prod_Extra3, Prod_Extra4, Prod_Extra5, Prod_Extra6, Prod_Extra7, Prod_Extra8, Prod_Extra9, Extras, Dataalt, Usualt, Frentes, Orig_codigo, PrTabela, CreditoST, CodigoSim, DataOfAnt2, PrecoOfertaAnt2, PrecoNormalAnt2, PrNormal3, PrNormal4, PrNormal5, PrecoNormalAnt3, PrecoNormalAnt4, PrecoNormalAnt5, PrecoOfertaAnt3, PrecoOfertaAnt4, PrecoOfertaAnt5, Margem3, Margem4, Margem5, TipoAgOf, TipoAgOfAnt, TipoAgOfAnt2, TpTrocas, PrVdaPadrao, CurvasABC, PercImpostos, PrVenda2Ant, PrVenda2Ant2, CodigoPreco, Descritivo, Funcao, Balanca, CustoVenda, CodigoComprador, Alcada, FatorEstoque, tributacao, DataHoraManutencao } & { PrecoPDV2: number ex: 0; AgofPreco1: number ex: 0; AgofPreco2: number ex: 0; AgofPreco3: number ex: 0; AgofPreco4: number ex: 0; AgofPreco5: number ex: 0 }

## ProdutoDetalhadoEstoqueV29Array

array de **ProdutoDetalhadoEstoqueV29** = `ProdutoDetalhadoEstoqueV28` (ver reference/schemas.md) & object { PrecoPDV2, AgofPreco1, AgofPreco2, AgofPreco3, AgofPreco4, AgofPreco5 }

## ProdutoDetalhadoEstoqueV30

**ProdutoDetalhadoEstoqueV29** = `ProdutoDetalhadoEstoqueV28` (ver reference/schemas.md) & object { PrecoPDV2, AgofPreco1, AgofPreco2, AgofPreco3, AgofPreco4, AgofPreco5 } & { descricaoEcommerce: string ex: ""; complementoEcommerce: string ex: ""; marcaEcommerce: string ex: ""; idEcommerce: number ex: 0 }

## ProdutoDetalhadoEstoqueV30Array

array de **ProdutoDetalhadoEstoqueV30** = `ProdutoDetalhadoEstoqueV29` (ver reference/schemas.md) & object { descricaoEcommerce, complementoEcommerce, marcaEcommerce, idEcommerce }

## ProdutoDetalhadoEstoqueV31

**ProdutoDetalhadoEstoqueV30** = `ProdutoDetalhadoEstoqueV29` (ver reference/schemas.md) & object { descricaoEcommerce, complementoEcommerce, marcaEcommerce, idEcommerce } & { codBarrasAlterados: array de object { codigo, codigoBarras, numPreco, fatorEmbalagem, precoVenda, unidadeMedida, precoVendaUnidadeMedida, data } }

## ProdutoDetalhadoEstoqueV31Array

array de **ProdutoDetalhadoEstoqueV31** = `ProdutoDetalhadoEstoqueV30` (ver reference/schemas.md) & object { codBarrasAlterados }

## ProdutoDetalhadoEstoqueV32

**ProdutoDetalhadoEstoqueV31** = `ProdutoDetalhadoEstoqueV30` (ver reference/schemas.md) & object { codBarrasAlterados } & { PrecoPDVUnidadeMedida: number ex: 2.55; PrecoVenda2UnidadeMedida: number ex: 2.12; PrecoVenda3UnidadeMedida: number ex: 3.52; PrecoVenda4UnidadeMedida: number ex: 4.23; PrecoVenda5UnidadeMedida: number ex: 5.64 }

## ProdutoDetalhadoEstoqueV32Array

array de **ProdutoDetalhadoEstoqueV32** = `ProdutoDetalhadoEstoqueV31` (ver reference/schemas.md) & object { PrecoPDVUnidadeMedida, PrecoVenda2UnidadeMedida, PrecoVenda3UnidadeMedida, PrecoVenda4UnidadeMedida, PrecoVenda5UnidadeMedida }

## ProdutoDetalhadoV27

{ Codigo: number ex: 21355; SKU: number ex: 21355; CodigoBarras: string(string) ex: "0000000000121"; CodigoNCM: string(string) ex: "08011100"; Descricao: string(string) ex: "Coco Seco - Kg"; Complemento: string(string) ex: ""; Marca: string(string) ex: "A Definir"; Preco: number ex: 3; Grupo: string(string) ex: "10000"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "01-06-2022"; PrecoNormal: number ex: 3; CodigoUnidade: string(string) ex: "001"; CodigoDepartamento: string(string) ex: "999"; Departamento: string(string) ex: "Importação"; Ativo: string(string) ex: true; CodigoTributario: string(string) ex: "99999"; Estoque1: number ex: 0; Estoque2: number ex: 0; Estoque3: number ex: 0; Estoque4: number ex: 0; Estoque5: number ex: 0; PrecoLista: number ex: 0; PrecoPDV: number ex: 3; PrecoPDV2: number ex: 0; PrecoPDV3: number ex: 0; PrecoPDV4: number ex: 0; PrecoPDV5: number ex: 0; PrecoEtiqueta: number ex: 3; PrecoCartaz: number ex: 3; PrecoVenda2: number ex: 0; PrecoVenda3: number ex: 0; PrecoVenda4: number ex: 0; PrecoVenda5: number ex: 0; FatorPr3: number ex: 0; FatorPr4: number ex: 0; FatorPr5: number ex: 0; CodEstoque: number ex: 0; EstoqueMinimo: number ex: 0; EstoqueMaximo: number ex: 0; VendaMediaDiaria: number ex: 0; Espaco: number ex: 0; CodigoCaixa: string(string) ex: ""; CustoCompra: number ex: 2; CustoEmpresa: number ex: 2; CustoFiscal: number ex: 2; CustoMedio: number ex: 2; CustoTranferencia: number ex: 2; CustoVenda: number ex: 2; SetorLoja: string(string) ex: ""; SetorDeposito: string(string) ex: ""; PrecoUnidadeMedida: number ex: 0; DescricaoPDV: string(string) ex: "Coco Seco - Kg"; Bloqueado: string(string) ex: "N"; Altura: number ex: 0; Largura: number ex: 0; Profundidade: number ex: 0; Peso: number ex: 0; PesoLiquido: number ex: 0; DescricaoCliente: string(string) ex: "Coco Seco - Kg"; Temperatura: number ex: 0; TipoEmbalagem: string(string) ex: "UN"; QuantidadeEmbalagem: number ex: 1; Alterado: string(string) ex: "N"; Etq: number ex: 1; Ctz: number ex: 1; Tecla: string(string) ex: ""; PzRepos: number ex: 0; PzEntrega: number ex: 0; DiasSeg: number ex: 0; Validade: number ex: 0; ValMinima: number ex: 0; Marcado: string(string) ex: "N"; PrVendaAnt: number ex: 3; DtPrVenda: string(string) ex: "22-09-2017"; UsuAltPr: number ex: 936; Margem: number ex: 0; MargemMin: number ex: 0; QtdeOferta: number ex: 0; DtIniOferta: string(string) ex: "01-06-2022"; DtUltComp: string(string) ex: "25-10-2012"; PrUltComp: number ex: 0; QultComp: number ex: 0; UltSimbComp: string(string) ex: ""; RedBCUltComp: number ex: 0; UltForn: number ex: 1481; DtCustos: string(string) ex: "01-06-2022"; Comissao: number ex: 0; DifCusto: number ex: 0; DifVenda: number ex: 0; EtqMag: string(string) ex: "N"; QtdeAbLoja: number ex: 0; DtAbLoja: string(string) ex: "01-06-2022"; DataOfAnt: string(string) ex: "01-06-2022"; PrecoOfertaAnt: number ex: 3; PrecoNormalAnt: number ex: 3; TpAltPrVenda: string(string) ex: "0"; DifCusto1: number ex: 0; DifCusto2: number ex: 0; DifCusto3: number ex: 0; DifCusto4: number ex: 0; DifCusto5: number ex: 0; DifVenda1: number ex: 0; DifVenda2: number ex: 0; DifVenda3: number ex: 0; DifVenda4: number ex: 0; DifVenda5: number ex: 0; CtCompraAnt: number ex: 2; CtMedioAnt: number ex: 2; CtFiscalAnt: number ex: 1481; CtEmpresaAnt: number ex: 1481; CtTransfAnt: number ex: 1481; PrUltCompAnt: number ex: 1481; TransCtMedio: string(string) ex: ""; Faquisicao: string(string) ex: ""; Extra1: string(string) ex: ""; Extra2: string(string) ex: "abc"; Extra3: string(string) ex: ""; Extra4: number ex: 12; Extra5: number ex: 200720; Extra6: number ex: 0; Extra7: number ex: 0; Extra8: number ex: 0; Extra9: number ex: 0; Prod_Extra1: string(string) ex: ""; Prod_Extra2: string(string) ex: ""; Prod_Extra3: string(string) ex: "Endereço: Santa Marta 0, 1"; Prod_Extra4: number ex: 0; Prod_Extra5: number ex: 0; Prod_Extra6: string(string) ex: ""; Prod_Extra7: string(string) ex: "extra7"; Prod_Extra8: number ex: 0; Prod_Extra9: number ex: 0; Extras: array de object { nome, tipo, valor }; Dataalt: string(string) ex: "28-01-2022"; Usualt: number ex: 936; Frentes: number ex: 0; Orig_codigo: number ex: 0; PrTabela: number ex: 0; CreditoST: number ex: 0; CodigoSim: string(string) ex: ""; DataOfAnt2: string(string) ex: "01-06-2022"; PrecoOfertaAnt2: number ex: 0; PrecoNormalAnt2: number ex: 0; PrNormal3: number ex: 0; PrNormal4: number ex: 0; PrNormal5: number ex: 0; PrecoNormalAnt3: number ex: 0; PrecoNormalAnt4: number ex: 0; PrecoNormalAnt5: number ex: 0; PrecoOfertaAnt3: number ex: 0; PrecoOfertaAnt4: number ex: 0; PrecoOfertaAnt5: number ex: 0; Margem3: number ex: 0; Margem4: number ex: 0; Margem5: number ex: 0; TipoAgOf: string(string) ex: ""; TipoAgOfAnt: string(string) ex: ""; TipoAgOfAnt2: string(string) ex: ""; TpTrocas: string(string) ex: ""; PrVdaPadrao: number ex: 0; CurvasABC: `ProdutoDetalhadoCurvaABC` (ver reference/schemas.md); PercImpostos: number ex: 0; PrVenda2Ant: number ex: 0; PrVenda2Ant2: number ex: 0; CodigoPreco: number ex: 1; Descritivo: string(string) ex: ""; Funcao: string(string) ex: ""; Balanca: string(string) ex: "P"; CodigoComprador: string(string) ex: ""; Alcada: number(number) ex: 10; FatorEstoque: number(number) ex: 1; tributacao: object { icms, ipi, pis, cofins, icms_st, controle } }

## ProdutoDetalhadoV28

{ Codigo: number ex: 21355; SKU: number ex: 21355; CodigoBarras: string(string) ex: "0000000000121"; CodigoNCM: string(string) ex: "08011100"; Descricao: string(string) ex: "Coco Seco - Kg"; Complemento: string(string) ex: ""; Marca: string(string) ex: "A Definir"; Status: string(string) ex: "NORMAL"; Preco: number ex: 3; Grupo: string(string) ex: "10000"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "01-06-2022"; PrecoNormal: number ex: 3; CodigoUnidade: string(string) ex: "001"; CodigoDepartamento: string(string) ex: "999"; Departamento: string(string) ex: "Importação"; Ativo: string(string) ex: true; CodigoTributario: string(string) ex: "99999"; Estoque1: number ex: 0; Estoque2: number ex: 0; Estoque3: number ex: 0; Estoque4: number ex: 0; Estoque5: number ex: 0; PrecoLista: number ex: 0; PrecoPDV: number ex: 3; PrecoPDV2: number ex: 0; PrecoPDV3: number ex: 0; PrecoPDV4: number ex: 0; PrecoPDV5: number ex: 0; PrecoEtiqueta: number ex: 3; PrecoCartaz: number ex: 3; PrecoVenda2: number ex: 0; PrecoVenda3: number ex: 0; PrecoVenda4: number ex: 0; PrecoVenda5: number ex: 0; FatorPr3: number ex: 0; FatorPr4: number ex: 0; FatorPr5: number ex: 0; CodEstoque: number ex: 0; EstoqueMinimo: number ex: 0; EstoqueMaximo: number ex: 0; VendaMediaDiaria: number ex: 0; Espaco: number ex: 0; CodigoCaixa: string(string) ex: ""; CustoCompra: number ex: 2; CustoEmpresa: number ex: 2; CustoFiscal: number ex: 2; CustoMedio: number ex: 2; CustoTranferencia: number ex: 2; CustoVenda: number ex: 2; SetorLoja: string(string) ex: ""; SetorDeposito: string(string) ex: ""; PrecoUnidadeMedida: number ex: 0; DescricaoPDV: string(string) ex: "Coco Seco - Kg"; Bloqueado: string(string) ex: "N"; Altura: number ex: 0; Largura: number ex: 0; Profundidade: number ex: 0; Peso: number ex: 0; PesoLiquido: number ex: 0; DescricaoCliente: string(string) ex: "Coco Seco - Kg"; Temperatura: number ex: 0; TipoEmbalagem: string(string) ex: "UN"; QuantidadeEmbalagem: number ex: 1; Alterado: string(string) ex: "N"; Etq: number ex: 1; Ctz: number ex: 1; Tecla: string(string) ex: ""; PzRepos: number ex: 0; PzEntrega: number ex: 0; DiasSeg: number ex: 0; Validade: number ex: 0; ValMinima: number ex: 0; Marcado: string(string) ex: "N"; PrVendaAnt: number ex: 3; DtPrVenda: string(string) ex: "22-09-2017"; UsuAltPr: number ex: 936; Margem: number ex: 0; MargemMin: number ex: 0; QtdeOferta: number ex: 0; DtIniOferta: string(string) ex: "01-06-2022"; DtUltComp: string(string) ex: "25-10-2012"; PrUltComp: number ex: 0; QultComp: number ex: 0; UltSimbComp: string(string) ex: ""; RedBCUltComp: number ex: 0; UltForn: number ex: 1481; DtCustos: string(string) ex: "01-06-2022"; Comissao: number ex: 0; DifCusto: number ex: 0; DifVenda: number ex: 0; EtqMag: string(string) ex: "N"; QtdeAbLoja: number ex: 0; DtAbLoja: string(string) ex: "01-06-2022"; DataOfAnt: string(string) ex: "01-06-2022"; PrecoOfertaAnt: number ex: 3; PrecoNormalAnt: number ex: 3; TpAltPrVenda: string(string) ex: "0"; DifCusto1: number ex: 0; DifCusto2: number ex: 0; DifCusto3: number ex: 0; DifCusto4: number ex: 0; DifCusto5: number ex: 0; DifVenda1: number ex: 0; DifVenda2: number ex: 0; DifVenda3: number ex: 0; DifVenda4: number ex: 0; DifVenda5: number ex: 0; CtCompraAnt: number ex: 2; CtMedioAnt: number ex: 2; CtFiscalAnt: number ex: 1481; CtEmpresaAnt: number ex: 1481; CtTransfAnt: number ex: 1481; PrUltCompAnt: number ex: 1481; TransCtMedio: string(string) ex: ""; Faquisicao: string(string) ex: ""; Extra1: string(string) ex: ""; Extra2: string(string) ex: "abc"; Extra3: string(string) ex: ""; Extra4: number ex: 12; Extra5: number ex: 200720; Extra6: number ex: 0; Extra7: number ex: 0; Extra8: number ex: 0; Extra9: number ex: 0; Prod_Extra1: string(string) ex: ""; Prod_Extra2: string(string) ex: ""; Prod_Extra3: string(string) ex: "Endereço: Santa Marta 0, 1"; Prod_Extra4: number ex: 0; Prod_Extra5: number ex: 0; Prod_Extra6: string(string) ex: ""; Prod_Extra7: string(string) ex: "extra7"; Prod_Extra8: number ex: 0; Prod_Extra9: number ex: 0; Extras: array de object { nome, tipo, valor }; Dataalt: string(string) ex: "28-01-2022"; Usualt: number ex: 936; Frentes: number ex: 0; Orig_codigo: number ex: 0; PrTabela: number ex: 0; CreditoST: number ex: 0; CodigoSim: string(string) ex: ""; DataOfAnt2: string(string) ex: "01-06-2022"; PrecoOfertaAnt2: number ex: 0; PrecoNormalAnt2: number ex: 0; PrNormal3: number ex: 0; PrNormal4: number ex: 0; PrNormal5: number ex: 0; PrecoNormalAnt3: number ex: 0; PrecoNormalAnt4: number ex: 0; PrecoNormalAnt5: number ex: 0; PrecoOfertaAnt3: number ex: 0; PrecoOfertaAnt4: number ex: 0; PrecoOfertaAnt5: number ex: 0; Margem3: number ex: 0; Margem4: number ex: 0; Margem5: number ex: 0; TipoAgOf: string(string) ex: ""; TipoAgOfAnt: string(string) ex: ""; TipoAgOfAnt2: string(string) ex: ""; TpTrocas: string(string) ex: ""; PrVdaPadrao: number ex: 0; CurvasABC: `ProdutoDetalhadoCurvaABC` (ver reference/schemas.md); PercImpostos: number ex: 0; PrVenda2Ant: number ex: 0; PrVenda2Ant2: number ex: 0; CodigoPreco: number ex: 1; Descritivo: string(string) ex: ""; Funcao: string(string) ex: ""; Balanca: string(string) ex: "P"; CodigoComprador: string(string) ex: ""; Alcada: number(number) ex: 10; FatorEstoque: number(number) ex: 1; tributacao: object { icms, ipi, pis, cofins, icms_st, controle }; DataHoraManutencao: string ex: "21/08/2023 08:20:54.215" }

## ProdutoDetalhadoV29

**ProdutoDetalhadoV28** = object { Codigo, SKU, CodigoBarras, CodigoNCM, Descricao, Complemento, Marca, Status, Preco, Grupo, Oferta, DataOferta, PrecoNormal, CodigoUnidade, CodigoDepartamento, Departamento, Ativo, CodigoTributario, Estoque1, Estoque2, Estoque3, Estoque4, Estoque5, PrecoLista, PrecoPDV, PrecoPDV2, PrecoPDV3, PrecoPDV4, PrecoPDV5, PrecoEtiqueta, PrecoCartaz, PrecoVenda2, PrecoVenda3, PrecoVenda4, PrecoVenda5, FatorPr3, FatorPr4, FatorPr5, CodEstoque, EstoqueMinimo, EstoqueMaximo, VendaMediaDiaria, Espaco, CodigoCaixa, CustoCompra, CustoEmpresa, CustoFiscal, CustoMedio, CustoTranferencia, CustoVenda, SetorLoja, SetorDeposito, PrecoUnidadeMedida, DescricaoPDV, Bloqueado, Altura, Largura, Profundidade, Peso, PesoLiquido, DescricaoCliente, Temperatura, TipoEmbalagem, QuantidadeEmbalagem, Alterado, Etq, Ctz, Tecla, PzRepos, PzEntrega, DiasSeg, Validade, ValMinima, Marcado, PrVendaAnt, DtPrVenda, UsuAltPr, Margem, MargemMin, QtdeOferta, DtIniOferta, DtUltComp, PrUltComp, QultComp, UltSimbComp, RedBCUltComp, UltForn, DtCustos, Comissao, DifCusto, DifVenda, EtqMag, QtdeAbLoja, DtAbLoja, DataOfAnt, PrecoOfertaAnt, PrecoNormalAnt, TpAltPrVenda, DifCusto1, DifCusto2, DifCusto3, DifCusto4, DifCusto5, DifVenda1, DifVenda2, DifVenda3, DifVenda4, DifVenda5, CtCompraAnt, CtMedioAnt, CtFiscalAnt, CtEmpresaAnt, CtTransfAnt, PrUltCompAnt, TransCtMedio, Faquisicao, Extra1, Extra2, Extra3, Extra4, Extra5, Extra6, Extra7, Extra8, Extra9, Prod_Extra1, Prod_Extra2, Prod_Extra3, Prod_Extra4, Prod_Extra5, Prod_Extra6, Prod_Extra7, Prod_Extra8, Prod_Extra9, Extras, Dataalt, Usualt, Frentes, Orig_codigo, PrTabela, CreditoST, CodigoSim, DataOfAnt2, PrecoOfertaAnt2, PrecoNormalAnt2, PrNormal3, PrNormal4, PrNormal5, PrecoNormalAnt3, PrecoNormalAnt4, PrecoNormalAnt5, PrecoOfertaAnt3, PrecoOfertaAnt4, PrecoOfertaAnt5, Margem3, Margem4, Margem5, TipoAgOf, TipoAgOfAnt, TipoAgOfAnt2, TpTrocas, PrVdaPadrao, CurvasABC, PercImpostos, PrVenda2Ant, PrVenda2Ant2, CodigoPreco, Descritivo, Funcao, Balanca, CodigoComprador, Alcada, FatorEstoque, tributacao, DataHoraManutencao } & { AgprPreco1: number ex: 0; AgprPreco2: number ex: 0; AgprPreco3: number ex: 0; AgprPreco4: number ex: 0; AgprPreco5: number ex: 0; AgofPreco1: number ex: 0; AgofPreco2: number ex: 0; AgofPreco3: number ex: 0; AgofPreco4: number ex: 0; AgofPreco5: number ex: 0 }

## ProdutoDetalhadoV30

**ProdutoDetalhadoV29** = `ProdutoDetalhadoV28` (ver reference/schemas.md) & object { AgprPreco1, AgprPreco2, AgprPreco3, AgprPreco4, AgprPreco5, AgofPreco1, AgofPreco2, AgofPreco3, AgofPreco4, AgofPreco5 } & { descricaoEcommerce: string ex: ""; complementoEcommerce: string ex: ""; marcaEcommerce: string ex: ""; idEcommerce: number ex: 0 }

## ProdutoDetalhadoV31

**ProdutoDetalhadoV30** = `ProdutoDetalhadoV29` (ver reference/schemas.md) & object { descricaoEcommerce, complementoEcommerce, marcaEcommerce, idEcommerce } & { codBarrasAlterados: array de object { codigo, codigoBarras, numPreco, fatorEmbalagem, precoVenda, unidadeMedida, data, precoVendaUnidadeMedida } }

## ProdutoDetalhadoV32

**ProdutoDetalhadoV31** = `ProdutoDetalhadoV30` (ver reference/schemas.md) & object { codBarrasAlterados } & { PrecoPDVUnidadeMedida: number ex: 2.55; PrecoVenda2UnidadeMedida: number ex: 2.12; PrecoVenda3UnidadeMedida: number ex: 3.52; PrecoVenda4UnidadeMedida: number ex: 4.23; PrecoVenda5UnidadeMedida: number ex: 5.64 }

## ProdutoExcluidosV10

array de { codigoProduto: integer ex: 11231; codigoBarras: string ex: "7891109146590"; status: string ex: "C"; dataExclusao: string ex: "18/03/2020"; usuarioExclusao: integer ex: 900 }

## ProdutoFornecedorResponse_V_1_0

{ response: object { status, messages, codigosFornecedor } }

## ProdutoFornecedorResponse_V_1_1

{ response: object { status, appVersion, messages, content } }

## ProdutoMarcadoPut_V1

{ marcado: string ex: "S" }

## ProdutoPreCadastroV1_1

{ unid_codigo: string(string) ex: "001"; status: string(string) ex: ""; descricao: string(string) ex: "Teste"; complemento: string(string) ex: "Complemento teste"; marca: string(string) ex: "Marca Teste"; codBarras: string(string) ex: "213123"; descrPdvs: string(string) ex: "TEste PDV"; emb: string(string) ex: "CX"; qemb: number ex: 3; prod_Codigo: number ex: 0; dtCadastro: string(string) ex: "04/05/2023"; horaCadastro: string(string) ex: ""; dtLiberacao: string(string) ex: "04/05/2023"; horaLiberacao: string(string) ex: ""; codNcm: string(string) ex: ""; obs: string(string) ex: ""; balanca: string(string) ex: "S"; peso: number ex: 0; pesoLiq: number ex: 0; prodFuncao: string(string) ex: ""; cest: string(string) ex: ""; codCaixa: string(string) ex: ""; lastro: number ex: 0; camadas: number ex: 0; forn_Codigo: number ex: 0; validade: number ex: 0; altura: number ex: 0; largura: number ex: 0; profundidade: number ex: 0; codProdFor: string(string) ex: ""; tiposTroca: string(string) ex: "N,S,L"; grupo: string(string) ex: ""; departamento: string(string) ex: ""; formaAquisicao: string(string) ex: "CD" }

## ProdutoV1

{ Codigo: integer ex: 10162; SKU: integer ex: 10162; CodigoBarras: string(string) ex: "1050695"; CodigoNCM: string(string) ex: "18069000"; Descricao: string(string) ex: "Kinder Ovo"; Complemento: string(string) ex: ""; Marca: string(string) ex: "Dorizon"; Estoque: number(double) ex: 0; Preco: number(double) ex: 3.89; Grupo: string(string) ex: "10000"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "18-04-2018"; PrecoNormal: number(double) ex: 0; CodigoUnidade: string(string) ex: "001"; CodigoDepartamento: string(string) ex: "999"; Departamento: string(string) ex: "Geral"; Ativo: boolean ex: true; CodigoTributario: string(string) ex: "905"; TipoEmbalagem: string(string) ex: "UN"; QuantidadeEmbalagem: integer ex: 0; CodEstoque: number ex: 1; EstoqueMinimo: number(double) ex: 10; EstoqueMaximo: number(double) ex: 300; VendaMediaDiaria: number(double) ex: 15 }

## ProdutoV27

{ Codigo: integer ex: 100010; SKU: integer ex: 100010; CodigoBarras: string(string) ex: "7896090401222"; CodigoNCM: string(string) ex: "1042090.0"; Descricao: string(string) ex: "Desodorante"; DescricaoCliente: string(string) ex: "Cliente"; Complemento: string(string) ex: ""; Marca: string(string) ex: "Teste"; Preco: number(double) ex: 8.98; Grupo: string(string) ex: "16703"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "08-03-2019"; PrecoNormal: number(double) ex: 0; CodigoUnidade: string(string) ex: "004"; CodigoDepartamento: string(string) ex: "030"; Departamento: string(string) ex: "Higiene e Beleza"; Ativo: boolean ex: true; CodigoTributario: string(string) ex: "34051000"; Estoque1: number(double) ex: 1; Estoque2: number(double) ex: 0; Estoque3: number(double) ex: 0; Estoque4: number(double) ex: 0; Estoque5: number(double) ex: 0; PrecoLista: number(double) ex: 8.98; PrecoPDV: number(double) ex: 8.98; PrecoPDV2: number(double) ex: 5.99; PrecoPDV3: number(double) ex: 6.99; PrecoPDV4: number(double) ex: 0; PrecoPDV5: number(double) ex: 0; PrecoEtiqueta: number(double) ex: 8.98; PrecoCartaz: number(double) ex: 0; PrecoVenda2: number(double) ex: 0; PrecoVenda3: number(double) ex: 6.99; PrecoVenda4: number(double) ex: 0; PrecoVenda5: number(double) ex: 0; FatorPr3: integer ex: 0; FatorPr4: integer ex: 0; FatorPr5: integer ex: 0; CodEstoque: integer ex: 0; EstoqueMinimo: number(double) ex: 0; EstoqueMaximo: number(double) ex: 0; VendaMediaDiaria: number(double) ex: 0.923; Espaco: integer ex: 0; CodigoCaixa: string(string) ex: "17896090401250"; CustoCompra: number(double) ex: 1; CustoEmpresa: number(double) ex: 4.6; CustoFiscal: number(double) ex: 4.6; CustoMedio: number(double) ex: 4.4842; CustoTranferencia: number(double) ex: 4.6; SetorLoja: string(string) ex: ""; SetorDeposito: string(string) ex: ""; PrecoUnidadeMedida: number(double) ex: 0; DescricaoPDV: string(string) ex: "Des Hydratta 165ml a"; TipoEmbalagem: string(string) ex: "CX"; QuantidadeEmbalagem: integer ex: 12 }

## ProdutoV28

{ Codigo: integer ex: 100010; SKU: integer ex: 100010; CodigoBarras: string(string) ex: "7896090401222"; CodigoNCM: string(string) ex: "1042090.0"; Descricao: string(string) ex: "Desodorante"; DescricaoCliente: string(string) ex: "Cliente"; Complemento: string(string) ex: ""; Marca: string(string) ex: "Teste"; Status: string(string) ex: "NORMAL"; Preco: number(double) ex: 8.98; Grupo: string(string) ex: "16703"; Oferta: string(string) ex: "N"; DataOferta: string(string) ex: "08-03-2019"; PrecoNormal: number(double) ex: 0; CodigoUnidade: string(string) ex: "004"; CodigoDepartamento: string(string) ex: "030"; Departamento: string(string) ex: "Higiene e Beleza"; Ativo: boolean ex: true; CodigoTributario: string(string) ex: "34051000"; Estoque1: number(double) ex: 1; Estoque2: number(double) ex: 0; Estoque3: number(double) ex: 0; Estoque4: number(double) ex: 0; Estoque5: number(double) ex: 0; PrecoLista: number(double) ex: 8.98; PrecoPDV: number(double) ex: 8.98; PrecoPDV2: number(double) ex: 6.99; PrecoPDV3: number(double) ex: 6.99; PrecoPDV4: number(double) ex: 0; PrecoPDV5: number(double) ex: 0; PrecoEtiqueta: number(double) ex: 8.98; PrecoCartaz: number(double) ex: 0; PrecoVenda2: number(double) ex: 0; PrecoVenda3: number(double) ex: 6.99; PrecoVenda4: number(double) ex: 0; PrecoVenda5: number(double) ex: 0; FatorPr3: integer ex: 0; FatorPr4: integer ex: 0; FatorPr5: integer ex: 0; CodEstoque: integer ex: 0; EstoqueMinimo: number(double) ex: 0; EstoqueMaximo: number(double) ex: 0; VendaMediaDiaria: number(double) ex: 0.923; Espaco: integer ex: 0; CodigoCaixa: string(string) ex: "17896090401250"; CustoCompra: number(double) ex: 1; CustoEmpresa: number(double) ex: 4.6; CustoFiscal: number(double) ex: 4.6; CustoMedio: number(double) ex: 4.4842; CustoTranferencia: number(double) ex: 4.6; SetorLoja: string(string) ex: ""; SetorDeposito: string(string) ex: ""; PrecoUnidadeMedida: number(double) ex: 0; DescricaoPDV: string(string) ex: "Des Hydratta 165ml a"; TipoEmbalagem: string(string) ex: "CX"; QuantidadeEmbalagem: integer ex: 12; DataHoraManutencao: string(string;) ex: "21/03/2023 14:25:39.651" }

## ProdutosAgendaV1

{ Codigo: integer ex: 218973; PrecoOferta: number(double) ex: 1; Custo: number(double) ex: 2.33; CodigoPreco: boolean ex: true; Observacao: string(string) ex: ""; PrecoOferta2: number(double) ex: 0; PrecoOferta3: number(double) ex: 0; PrecoOferta4: number(double) ex: 0; PrecoOferta5: number(double) ex: 0; DataInicio: string(string) ex: "15/03/2019"; DataFim: string(string) ex: "15/03/2019"; Quantidade: integer ex: 0; OfertaDiasSemana: string(string) ex: ""; Divulgacao: string(string) ex: ""; PrecoNormal: number(double) ex: 2.48 }

## ProdutosAgenda_V1.2

{ Codigo: integer ex: 218973; PrecoOferta: number(double) ex: 1; Custo: number(double) ex: 2.33; codigoPreco: array de number; Observacao: string(string) ex: ""; PrecoOferta2: number(double) ex: 0; PrecoOferta3: number(double) ex: 0; PrecoOferta4: number(double) ex: 0; PrecoOferta5: number(double) ex: 0; DataInicio: string(string) ex: "15/03/2019"; DataFim: string(string) ex: "15/03/2019"; Quantidade: integer ex: 0; OfertaDiasSemana: string(string) ex: ""; Divulgacao: string(string) ex: ""; PrecoNormal: number(double) ex: 2.48 }

## ProdutosEstoqueDisponivel

array de { codigo: number ex: 100001; estoque: number ex: 25.0 }

## ProdutosFornecedorRes

{ response: object { status, messages, produtos } }

## ProdutosFornecedorRes_V_1_3

{ response: object { status, messages, produtos } }

## ProgramaPreco

{ codigoProduto: integer ex: 100010; codigoPreco: string ex: 10222; status: string(string) ex: "PRECO_PREVISTO"; codigoAgenda: string(string) ex: "0003"; precoAlteracao: string(string) ex: "1"; uf: string(string) ex: "PR"; dataInicial: string(string) ex: "21/12/2018"; dataFinal: string(string) ex: "22/12/2018"; horaInicial: string(string) ex: "23"; horaFinal: string(string) ex: "23"; precoVenda: number(double) ex: 5; dataLancamento: string(string) ex: "21/12/2018"; prioridade: string(string) ex: "1"; oferta: string(string) ex: "S"; descricaoCliente: string ex: "Descrição do cliente"; qtdeMaximaCliente: integer ex: 10; fatorPreco: integer ex: 0; observacao: string(string) ex: "Observação" }

## PromotorEfetivCadastro

{ fornecedores: array de any; codigo: number ex: 10005; nome: string(string) ex: "Teste marcos"; obs: string(string) ex: "obs teste"; fone: string(string) ex: "425435843"; email: string(string) ex: "afg@af.cdas"; status: string(string); dtvenccad: string(string) ex: "01/01/2026"; supervisornome: string(string) ex: "matheus"; supervisorfone: string(string) ex: "1241515"; supervisoremail: string(string) ex: "asfg@aiksgfhi.sdgs"; cpf: string(string) ex: "544352143"; fonecel: string(string) ex: "5136513"; supervisorfonecel: string(string) ex: ""; contatoalt: string(string) ex: ""; supervisorcontatoalt: string(string) ex: ""; ufexprg: string(string) ex: "pr"; rg: string(string) ex: "1453132132"; dtnasc: string(string) ex: "01/01/2000"; dtcad: string(string); release: number ex: 5 }

## RecMercVencimentoValidade_V_1_0

{ response: object { status, messages, content } }

## RecMerc_V_1_0

{ response: object { status, messages, content } }

## RefDocumentoFDE

Documento referenciado por um documento FDE. Pode ser de dois tipos distintos:
- Tipo "F" (Fiscal): Use RefDocumentoFDEFiscal
- Tipo "P" (Processo): Use RefDocumentoFDEProcesso

object

## RefDocumentoFDEFiscal

Referência a um documento fiscal (Tipo F)

{ tipoReferencia: string ex: "F"; dataEmissao: string ex: "01/01/2022"; catEntidade: number ex: "F"; codEntidade: number ex: "100006"; modeloDcto: string ex: "55"; serieDcto: string ex: "1"; numeroDcto: string ex: "1064"; chaveDfe: string ex: "12345678901234567890123456789012345678901244"; totalDcto: number(double) ex: 150.0; indTipoOperacao: string ex: "0"; indEmitente: string ex: "1" }

## RefDocumentoFDEProcesso

Referência a um processo judicial (Tipo P)

{ tipoReferencia: string ex: "P"; numeroDcto: string ex: "123"; processoOrigem: string ex: "3"; processoDescricao: string ex: "Remoção do ICMS da Base de PIS e COFINS"; processoSecao: string ex: "05"; processoVara: string ex: "02"; processoTipo: string ex: "J"; processoNatureza: string ex: "01" }

## RegistrarOcorrenciaMovFinResponse

{ response: object { status, appVersion, messages, content } }

## RegraNegocioResponse

{ response: object { status, messages, regra } }

## RegraNegocioResponse_V1

{ response: object { status, messages, regra } }

## ReqInsertTributacao_V_1_0

**Tributacao_V_1_0** = object { codigo, descricao, unidades, ufOrigem, ufDestino, mvtos, caracTrib, simbologia, servico, codNF, codPDV, origemMerc, icms, ipi, iss, pis, cofins, redBCICMS, bcSubTrib, subTrib, controle, tribPISCofins, redBCST, icmsAnt, simbCredito, icmsCritica, redBCCritica, comportamento, subtribEnt, complemento1, complemento2, complemento3, complemento4, complemento5, cstPis, cstIPI, natPISCof, data, dtIVal, dtFVal, cstAlternativa, icmsDestino, percFCP, redBcDestino, infAdicional, fcpAliq, fcpRedBC, fcpStAliq, fcpSTAliqEnt, simbFCP, fcpCritica, fcpRedBCCritica, codBenef, codMotRest, codMotCompl, icmsIvaAjustado, release, motDesonICMS, redBcPisCofins }

## RequestBaixacontroleEntregasPendentesV1_0

{ transacao: string ex: "00127691685"; entregador: string ex: ""; quilometragem: integer ex: 1500; observacao: string ex: "Entrega finalizade"; dataHora: string(date-time) ex: "2026-03-20T14:30:00" }

## RequestCadastroProdutosIndustrializados

{ codigo: number ex: 100577; descricao: string(string) ex: "Osso Bovino Desossa Dianteiro Kg"; tipo: string(string) ex: "IC"; unidade: string(string) ex: "000"; rendimento: number ex: 1.0; pesoTotal: number ex: 0.0; precoTotal: number ex: 0.0; dataCusto: string(string) ex: "28/02/2020"; comportamento: string(string) ex: ""; fase: number ex: 0; tempoProducao: string(string) ex: ""; observacao: string(string) ex: ""; quantidadeMinimaProduzir: number ex: 0.0; quantidadeProduzir: number ex: 0.0; quantidadeMultiplaProduzir: number ex: 0.0; baseProducao: string(string) ex: ""; tempoAntecedencia: number ex: 0; tempoProducaoHomensHora: number ex: 0; prioridadeProducao: number ex: 0; tempoPreparo: number ex: 0; estoqueSeguranca: number ex: 0.0; baixaEstoqueMateriaPrima: string(string) ex: ""; fatorProducao: number ex: 0.0; AgrupamentoUnidadesValidas: string(string) ex: ""; departamento: string(string) ex: "037"; itens: array de `ProdutoDeIndustrializado` (ver reference/schemas.md) }

## RequestCadastroProdutosIndustrializados_V1_2

{ codigo: number ex: 100577; descricao: string(string) ex: "Osso Bovino Desossa Dianteiro Kg"; tipo: string(string) ex: "IC"; unidade: string(string) ex: "000"; rendimento: number ex: 1.0; pesoTotal: number ex: 0.0; precoTotal: number ex: 0.0; dataCusto: string(string) ex: "28/02/2020"; comportamento: string(string) ex: ""; fase: number ex: 0; tempoProducao: string(string) ex: ""; observacao: string(string) ex: ""; quantidadeMinimaProduzir: number ex: 0.0; quantidadeProduzir: number ex: 0.0; quantidadeMultiplaProduzir: number ex: 0.0; baseProducao: string(string) ex: ""; tempoAntecedencia: number ex: 0; tempoProducaoHomensHora: number ex: 0; prioridadeProducao: number ex: 0; tempoPreparo: number ex: 0; estoqueSeguranca: number ex: 0.0; baixaEstoqueMateriaPrima: string(string) ex: ""; fatorProducao: number ex: 0.0; AgrupamentoUnidadesValidas: string(string) ex: ""; departamento: string(string) ex: "037"; itens: array de `ProdutoDeIndustrializadoCadastro` (ver reference/schemas.md) }

## RequestMarcaAuditoriaDocV_1_0

{ transacao: string(string) ex: "00111708150"; operacao: string(string) ex: "001117081501"; usuarioErp: number ex: 10000; observacao: string(string) ex: "teste marcação auditoria" }

## RequestMarcaAuditoriaDocV_1_1

**RequestMarcaAuditoriaDocV_1_0** = object { transacao, operacao, usuarioErp, observacao } & { origemApp: string(string) ex: "nome sistema consumidor da API"; origemVersao: string(string) ex: "5.0.2.013"; origemIdent: string(string) ex: "1"; pendenciasAutorizar: array de object { operacao, dataAutorizacao } }

## Request_Contratos_BaixarRegra_V_1_0

{ id: string ex: "1_2"; dataHora: string ex: "01/01/2024 12:00:00"; nomeResponsavel: string ex: "Jose Silva" }

## Request_Descontos_Incluir_V_1_0

{ webService: string ex: "S"; codBarra: string ex: 7893000436992; valorMin: number ex: 0; valorMinCupom: number ex: 0; percentual: number ex: 1; unidades: string ex: 2; dataInicial: string ex: "08/11/2021"; dataFinal: string ex: "01/01/2035"; descricao: string ex: "Promoção Item: 31933 (F)"; preco: number ex: 0; finValidas: string; finInvalidas: string; qtdMaxima: number ex: 0; qtdMinima: number ex: 0; valorMaxDesconto: number ex: 0; fatorDiv: number ex: 0; qtdFatorDiv: number ex: 0; fatorDivSub: number ex: 0; tipoCliente: string; tipoClienteCrm: string ex: "F"; tipoDesconto: string ex: "I"; utilPreco2: string ex: "N"; igrPrecoDif: string ex: "N"; prodOferta: string ex: "N"; grupos: string; marcas: string; rcrCodigo: number ex: 0; valorDesconto: number ex: 0; produtoSbt: string; qtdFatorDivSbt: number ex: 0; produtoOfVId: string; codBarrasVld: string; gruposVld: string; codIntoOferta: string ex: "Y101"; codAgof: string; permedicao: string; titulo: string; linha1: string; linha2: string ex: "tTt"; linha3: string; rgFixa: string; qtdMaxImaVld: number ex: 0; qtdMaxImaCli: number ex: 0; horaInicial: string; horaFinal: string; itensPartVlrMin: string; gruposInvalidos: string; dataHoraManutencao: string ex: "09/04/2024 07:52:55" }

## Request_PackVirtual_V_1_0

{ dataInicial: string ex: "01/01/2024"; dataFinal: string ex: "31/12/2024"; unidCodigo: string ex: "001"; prodCodigo: number ex: 0; prvenda: number ex: 4.79; quantidade: number ex: 0; tipo: string ex: "E"; unidades: string ex: "002"; descritivo: string; desconto: number ex: 0; alteracao: string(nullable) ex: "N"; qtdLimite: number ex: 0; produtos: string ex: "0"; tiposCli: string; valorUnitCli: number ex: 0; codintOferta: string; tiposCliCrm: string; webService: string; tipoRegra: string; permaCresFc: string ex: "n"; finValidas: string; binsValidos: string; diasSemana: string ex: "sao separados por ';'"; tiposCliZoombox: string; descricao: string(nullable); detalhes: array de object { prodCodigo, quantidade, produtos } }

## Request_XmlNfe_Gravar_V_4_0

{ conteudo: string ex: "H4sIAAAAAAAA/5VUXY+iMBT9Kw3v2oLiV66dsIoJmwgO4r4j1JFEqIuVMfvr97bF3czMviwP3I+eezi"; chave: string ex: "35260112345678000199550010000012341000012348"; unidade: string ex: "001"; transacao: string ex: "" }

## ResProcFDE

Resultado do processamento do documento FDE no ERP.

{ codResposta: integer ex: 200; descricaoResposta: string ex: "Existem inconsistências no documento, verifique as ocorrências"; transacao: string ex: "00116924969"; ocorrencias: array de `OcorrenciaFDE` (ver reference/schemas.md) }

## RespClientesv2_0

{ codigo: integer ex: 727564; nome: string ex: "Alexandre Basso Preti"; razaoSocial: string ex: "Alexandre Basso Preti"; tipos: string ex: "M"; cnpjCpf: string ex: "01743488947"; rgIe: string ex: ""; dtExpRG: string(dd/mm/yyyy); orgExpRG: string ex: ""; ufExpRG: string ex: "PR"; sexo: string ex: "M"; dadosResidenciais: object { endereco, numero, complemento, bairro, cidade, uf, cep, fone }; dadosComerciais: object { endereco, numero, complemento, bairro, cidade, uf, cep, fone, foneCel }; foneCel: string ex: ""; dtNasc: string(dd/mm/yyyy) ex: "20/10/1974"; naturalidade: string ex: ""; classe: string ex: "564"; email: string ex: "alexpreti@gmail.com"; emailCorr: string ex: ""; endCorr: string ex: ""; empresa: string ex: ""; funcao: string ex: ""; ramal: integer ex: 0; estadoCivil: string ex: "CASADO"; profissao: string ex: ""; escolaridade: string ex: "N"; contaContabil: integer ex: 112101; contaGerencial: integer ex: 112101; contribuinte: string ex: ""; dataCadastro: string(dd/mm/yyyy); ramoAtividade: string ex: ""; fpgt_codigo: string ex: ""; camposExtras: object; caractrib: string ex: "F" }

## RespPedCompraDevolucaoLV10

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages } }

## RespRecMercInserirV11

{ response: object { status, message, messages, transacao } }

## ResponseAgendaFornecedores_V_1_0

{ response: object { status, messages, content } }

## ResponseCadClientesLastId_v1.9

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, message, messages, clientes } }

## ResponseCadClientes_v1.6

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, message, messages, clientes } }

## ResponseCadClientes_v1.7

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, message, messages, clientes } }

## ResponseCadClientes_v1.8

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, message, messages, clientes } }

## ResponseCadClientes_v2.0

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, AppVersion, message, messages, content } }

## ResponseCadClientesv3

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, message, messages, clientes } }

## ResponseCadClientesv4

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, message, messages, clientes } }

## ResponseCadTabEmb_V_1_0

{ response: object { status, messages, content } }

## ResponseContentMovDctosTransacaoPendFin

Resposta bem-sucedida da API, contendo os dados do conteúdo solicitado

{ appVersion: string ex: "2.0.75"; pages: integer; content: any }

## ResponseControleEntregasPendentes

{ response: object { status, appVersion, messages, content } }

## ResponseCriacaoDocumentoFDE

Response da criação de um documento FDE via POST

{ response: object { status, messages, numeroRecibo, resProc } }

## ResponseDadosClienteV3

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, message, messages, cliente } }

## ResponseDadosClienteV4

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, message, messages, cliente } }

## ResponseDadosClienteV5

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, messages, cliente } }

## ResponseDigitalizacaoDocumentosV_1_0

{ response: object { status, appVersion, messages, content } }

## ResponseDocumentosConfigPES

Se nenhuma espécie válida inicial e final, como também espécie de produto inicial e final não for informada, 
o endpoint vai carregar todas as espécies apenas no atributo 'especiesValidas' e o atributo 'especiesProdutos' 
retornará null e as espécies válidas para o produto devem ser as contidas no atributo 'especiesValidas'.

{ response: object { status, appVersion, messages, content } }

## ResponseError_V_1_0

{ error: string(string) ex: "Dados inconsistentes" }

## ResponseFdeLancamentos1_0

{ response: object { status, messages, content } }

## ResponseFdeLancamentos1_1

{ response: object { status, messages, content } }

## ResponseGetQuantPendPedVenda

{ response: object { status, messages, quantidade } }

## ResponseHistorico

{ codigo: string(string) ex: "0001"; descricao: string(string) ex: "Vr. nota fiscal "; complemento: string(string) ex: "No. :#001; Fornecedor.: #006" }

## ResponseHistoricov1

{ response: object { status, messages, content } }

## ResponseInsertTributacao_V_1_0

{ response: object { status, message, messages, content } }

## ResponseMarcaAuditoriaDocV_1_0

{ response: object { status, messages, content } }

## ResponsePadrao

{ status: string ex: "ok"; appVersion: string ex: "4.0.2.106"; messages: `messagesV2` (ver reference/schemas.md) }

## ResponsePendenciasFinanceiras_V_1_0

{ response: object { status, messages, content } }

## ResponsePendenciasFinanceiras_V_1_1

{ response: object { status, messages, content } }

## ResponsePontosCliente

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { Status, Message, Messages, Extrato } }

## ResponseProdUnDetalhado_V_1_0

{ response: object { status, appVersion, messages, content } }

## ResponseProdUn_V_1_0

{ response: object { status, appVersion, messages, content } }

## ResponseProgramacaoPrecosReleaseV_1_0

Quando o atributo **status** do objeto **response** for igual a **"ok"**, a requisição foi processada com sucesso.

Caso contrário, ocorreu algum erro durante o processamento e a lista **messages** conterá as mensagens de erro ou alerta correspondentes.

{ response: object { status, appVersion, messages, content } }

## ResponseRotas_V_1_0

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, content } }

## ResponseTabFornV1_0

{ response: object { status, messages, content } }

## ResponseTribHashesConsultaReciboOk_V_1_0

{ response: object { status, messages, content } }

## ResponseTribHashesConsultaReciboPartial_V_1_0

{ response: object { status, messages, content } }

## ResponseTribHashesInconsistentes_V_1_0

{ response: object { status, messages, content } }

## ResponseTribLastExec_V_1_0

{ response: object { status, messages, content } }

## ResponseTribRelease_V_1_0

{ response: object { status, messages, content } }

## ResponseUltimaEntradaEAQ_V_1_0

{ response: object { status, appVersion, messages, content } }

## ResponseUpdateFornecedorV1_0

{ response: object { status, messages } }

## ResponseUpdateSituacaoFornecedorV1_0

{ response: object { status, messages } }

## Response_Contratos_BaixarRegra_V_1_0

{ content: string ex: "Regra do contrato atualizada" }

## Response_Contratos_Regras_V_1_0

{ response: object { status, messages, content } }

## Response_Descontos_Incluir_V_1_0

{ content: string ex: "Desconto incluído" }

## Response_Descontos_Listar_V_1_0

{ response: object { status, messages, content } }

## Response_DocumentoConfigCCV_V_4_0

{ appVersion: string ex: "5.0.7.112"; content: `DocumentoConfigCCV_V_4_0` (ver reference/schemas.md) }

## Response_Documentos_Relatorio_Transacao_V_1_0

{ response: object { status, appVersion, messages, content } }

## Response_Forbidden

Resposta devolvida por qualquer rota quando o usuário autenticado não possui a permissão exigida pelo endpoint.
O atributo 'requiredPermission' acompanha as negativas do controle de permissão de endpoint; nas demais negativas de acesso (regras de LGPD, bloqueio por força bruta e validações de negócio) apenas 'error' é devolvido.

{ error: string ex: "Não Autorizado"; requiredPermission: object { httpMethod, endpoint, enableAnyOf } }

## Response_PackVirtual_Listar_V_1_0

{ response: object { status, messages, content } }

## Response_PackVirtual_Post_V_1_0

{ response: object { status, appVersion, messages, content } }

## Response_Pedidos_ListaPedidos_V_1_3

{ response: object { status, messages, pedidos } }

## Response_PontosExposicao_ListarPontos_Unidade_Data_V_1_0

{ response: object { status, message, messages, Agendas } }

## Response_PontosExposicao_ListarPontos_Unidade_LastId_V_1_0

{ response: object { status, message, messages, PontosExposicao } }

## Response_XmlNfe_Gravar_V_4_0

{ chave: string ex: "35260112345678000199550010000012341000012348"; unidade: string ex: "001"; operacao: string [INSERIDO, ATUALIZADO, JA_EXISTENTE]; entSai: string ex: "E"; catEntidade: string ex: "F"; codEntidade: integer ex: 42 }

## RespostaAutenticacao_V_1_1

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, token, tokenExpiration, expiresIn } }

## RespostaBaixaCancelada

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, transacao } }

## RespostaCadastroCidade

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, messages, content } }

## RespostaCarregamento

{ response: object { status, messages, carregamento } }

## RespostaCarregamentos

{ response: object { status, messages, carregamentos } }

## RespostaComprador

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, comprador } }

## RespostaComprador_V_1_2

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, messages, content } }

## RespostaConsultaProdutoIndustrializado

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, produto } }

## RespostaConsultaProdutoIndustrializados_V1_2

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, produto } }

## RespostaConsultaProdutoIndustrializados_V1_3

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, messages, content } }

## RespostaConsultaProdutoReceitaIndustrializado

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, produto } }

## RespostaConsultaProdutoReceitaIndustrializadoV_1_2

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, messages, content } }

## RespostaConsultaProdutosIndustrializados

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, produtos } }

## RespostaConsultaProdutosIndustrializados_V1_2

{ response: object { status, messages, produtos } }

## RespostaConsultaProdutosIndustrializados_V1_3

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, messages, content } }

## RespostaConsultaTodosProdutosReceitaIndustrializado

{ response: object { status, messages, produtos } }

## RespostaConsultaTodosProdutosReceitaIndustrializadoV_1_2

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, messages, content } }

## RespostaConsultaTransportadores

{ response: object { status, appVersion, messages, content } }

## RespostaConsultaTransportadoresV1

{ response: object { status, appVersion, messages, content } }

## RespostaControleEntrega

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, transacao } }

## RespostaDepartamentos

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, messages, content } }

## RespostaEditProdutoV_1_0

{ response: object { status, messages } }

## RespostaErroPadrao

{ response: object { status, messages } }

## RespostaExclusaoItem_SemMessage

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages } }

## RespostaFdeCancelados

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, cancelamentos } }

## RespostaFinalizadoras_V_1_0

{ response: object { status, messages, finalizadoras } }

## RespostaFuncionario

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, messages, content } }

## RespostaFuncionario_V_1_0

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, funcionario } }

## RespostaFuncionarios

{ response: object { status, messages, funcionarios } }

## RespostaFuncionarios_V_1_0

{ response: object { status, messages, content } }

## RespostaGetAuditoriaEstoque

{ response: object { status, messages, auditorias } }

## RespostaGetAuditoriaEstoque_V_1_3

{ response: object { status, messages, content } }

## RespostaGetConcorrentes

{ response: object { status, messages, concorrentes } }

## RespostaGetConcorrentesV1_1

{ response: object { status, messages, concorrentes } }

## RespostaIndustrializadoDeletado

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, messages, content } }

## RespostaListaDeFuncionarios

{ response: object { status, appVersion, messages, content } }

## RespostaListaDeVendedores

{ response: object { status, appVersion, messages, content } }

## RespostaListarBiometrias_V_1_0

{ response: object { status, messages, biometrias } }

## RespostaMovFinalizadoras_V_1_0

{ response: object { status, messages, movimentos } }

## RespostaMovFormaVdaPDV_V_1_0

{ response: object { status, messages, movimentos } }

## RespostaMovFormaVdaPDV_V_1_1

{ response: object { status, messages, movimentos } }

## RespostaMovPesquisa

{ response: object { status, messages, pesquisas } }

## RespostaMovPesquisaItem_1_1

{ codigoProduto: number ex: 89761; codigoConcorrente: number ex: 5; data: string(string) ex: "19/06/2017"; preco: number ex: 5; PrecoOferta: number ex: 0; codigUnidade: string(string) ex: "002"; marca: string(string) ex: "Feel Good"; validade: string(string) ex: "26/06/2017"; codBarras: string(string) ex: "7898192031895"; codigoEspecie: string(string) ex: ""; oferta: string(string) ex: "N"; tipoOferta: string(string) ex: ""; ruptura: string(string) ex: "N"; motivoSemPesquisa: string(string) ex: ""; observacao: string(string) ex: ""; tipoPreco: string(string) ex: "1"; fatorPreco: number ex: 0 }

## RespostaMovPesquisaItem_1_2

array de **RespostaMovPesquisaItem_1_1** = object { codigoProduto, codigoConcorrente, data, preco, PrecoOferta, codigUnidade, marca, validade, codBarras, codigoEspecie, oferta, tipoOferta, ruptura, motivoSemPesquisa, observacao, tipoPreco, fatorPreco } & { urlImagem: string(string) ex: "https://portaldocliente.rpinfo.com.br/images/login.png" }

## RespostaMovPesquisaPrecoItem_V_1_0

{ codProduto: number ex: 100099; codConcorrente: number ex: 7; nomeConcorrente: string ex: "Cidade Canção"; codUnidade: string ex: "001"; data: string ex: "29/03/2016"; valor: number(double) ex: 13.89; oferta: string ex: "N"; ruptura: string ex: "N"; obs: string ex: ""; tpPreco: string ex: "1"; precoOf: number(double) ex: 0; marca: string ex: "Xxxx"; validade: string ex: ""; codBarras: string ex: "7896183900762"; motSemPesq: string ex: ""; fatorPreco: number(double) ex: 1; updateCodPreco: string ex: ""; codPreco: number ex: 0; usuario: number ex: 0; urlImagem: string ex: "" }

## RespostaMovPesquisaPreco_V_1_0

{ response: object { status, appVersion, messages, content } }

## RespostaMovPesquisa_V_1_2

{ response: object { status, messages, pesquisas } }

## RespostaPadrao

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages } }

## RespostaPadrao_SemMessage

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages } }

## RespostaPadrao_SemMessageV2

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages } }

## RespostaPadrao_SemMessageV3

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, messages, content } }

## RespostaPesquisaDePreco

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages } }

## RespostaPostAuditoriaEstoqueV1_1

{ response: object { status, messages, criticas } }

## RespostaPostAuditoriaEstoqueV1_3

{ response: object { status, messages, content } }

## RespostaPostFuncionarioV1

{ response: object { status, messages, codigo } }

## RespostaPostFuncionarioV1_2

{ response: object { status, appVersion, messages, content } }

## RespostaPostMensagemUsuario

{ status: string ex: "ok"; appVersion: string ex: "4.0.0.165"; messages: array de object { message }; content: string ex: "Mensagem inserida com sucesso" }

## RespostaProdPesquisa

{ response: object { status, message, messages, pagination, prodPesquisa } }

## RespostaProdutoDeletado

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, messages, content } }

## RespostaSaldoContas_V_1_0

{ response: object { status, messages, content } }

## RespostaUnMedida

{ response: object { status, message, messages, preco } }

## RespostaUpdateStatusControleEntrega

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages } }

## RespostaXmlChave

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, XmlNfe } }

## RespostaXmlChaveProdutosV10

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, prods } }

## RespostaXmlChaveV11

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, XmlNfe } }

## RespostaXmlDataUnid

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, chaves } }

## RespostaXmlDataUnidV11

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, chaves } }

## ResquestBaixaEntregaV1_1

{ transacao: string ex: "00127691685"; Entregador: string ex: "123"; quilometragem: integer ex: 1050; observacao: string ex: "Entrega finalizada com sucesso"; dataHora: string(date-time) ex: "2026-03-24T10:30:00" }

## ResquestListaDeFuncionarios

{ codigo: integer ex: 91276; nome: string ex: "João da Silva"; unidade: string ex: "001"; nascimento: string ex: "03/03/1900"; endereco: string ex: "Rua Luis Garcia"; enderecoNumero: string ex: "129"; enderecoComplemento: string ex: ""; bairro: string ex: "Pq Independencia"; codigoMunicipio: integer ex: 4593; cep: string ex: "80230030"; nomeMae: string ex: "Maria De Lourdes De Proencio"; nomePai: string ex: "Paulo Alves De Proencio"; telefone: string ex: ""; estadoCivil: string ex: "2"; sexo: string ex: "F"; cor: string ex: "2"; deficiente: string ex: "N"; rg: string ex: "5637152"; rgUf: string ex: "SC"; rgExpedicao: string ex: "SPSC"; rgData: string ex: ""; cpf: string ex: "11625761600"; pis: string ex: "16195505391"; documentoMilitar: string ex: ""; tipoDocumentoMilitar: string ex: ""; eleitor: string ex: "91662710604"; zonaEleitoral: integer ex: 68; secaoEleitoral: integer ex: 0; carteiraProfissional: string ex: "6371912"; serieCarteiraProfissional: string ex: "0010"; ufCarteiraProfissional: string ex: "SC"; admissao: string ex: "06/02/2014"; demissao: string ex: ""; salarioBase: number ex: 0; codigoFgts: string ex: "112202"; valeTransporte: string ex: "N"; banco: string ex: ""; agencia: string ex: ""; digitoAgencia: string ex: ""; contaCorrente: string ex: ""; digitoConta: string ex: ""; titularConta: string ex: ""; nroCartaoMagnetico: string ex: ""; tipo: string ex: ""; situacao: string ex: "05"; senha: string ex: "2403224"; limiteConvenio: number ex: 10; codigoPDV: string ex: "0000000111102"; acumuladoChequeDiario: number ex: 0; acumuladoChequeDiario01: number ex: 0; acumuladoChequeDiario02: number ex: 0; acumuladoChequeDiario03: number ex: 0; acumuladoChequeDiario04: number ex: 0; acumuladoChequeDiario05: number ex: 0; acumuladoChequeDiario06: number ex: 0; acumuladoValorDiario: number ex: 0; ultimaOperacaoPdv: string ex: ""; limiteCheque: number ex: 0; foneEmergencia: string ex: ""; celular: string ex: ""; codigoUsuario: integer ex: 0; comissao: number ex: 0; funcao: string ex: "OPC"; unidadeFechamentoPDV: string ex: ""; observacao: string ex: ""; usuarioInclusao: integer ex: 999; dataCadastro: string ex: "02/03/2022"; email: string ex: ""; limiteDiario: string ex: "N"; centroCusto: string ex: ""; municipio: string ex: "Medianeira"; municipioUf: string ex: "PR"; escolaridade: string ex: ""; dataAlteracao: string ex: ""; usuarioAlteracao: integer ex: 0; horarioEntrada: string ex: ""; horarioSaida: string ex: ""; tipos: string ex: ""; dataHoraManutencao: string ex: "08/10/2022 16:05:45.215" }

## ResquestListaDeVendedores

{ codigo: string(string) ex: "001"; nome: string(string) ex: "Josimar Dos Santos"; comissao: number ex: 0; comissind: number ex: 0; unid_codigo: string(string) ex: "002"; supe_codigo: string(string) ex: ""; meta01: number ex: 0; meta02: number ex: 0; meta03: number ex: 0; meta04: number ex: 0; meta05: number ex: 0; meta06: number ex: 0; meta07: number ex: 0; meta08: number ex: 0; meta09: number ex: 0; meta10: number ex: 0; meta11: number ex: 0; meta12: number ex: 0; adicprvda: number ex: 0; uf: string(string) ex: "PR"; verba: number ex: 0; usadoVerba: number ex: 0; comportamento: string(string) ex: ""; func_codigo: number ex: 1507; contaComissao: number ex: 0; email: string(string) ex: "ger.pernambuco@musamar.com.br"; codFrente: number ex: 0; situacao: string(string) ex: "N"; unidadesmvto: string(string) }

## RetornoVerbas_Contratos_V_1_0

{ response: object { status, messages, verbas } }

## RetornoVerbas_Produtos_V_1_0

{ response: object { status, messages, verbas_Produtos } }

## RetornoVerbas_fornecedores_V_1_0

{ response: object { status, messages, verbas_Fornecedor } }

## RetornoVerbas_fornecedores_pagto_V_1_0

{ verbas: array de object { cod_verba, dt_pagamento_acordo, vlr_recebido, tipo_recebimento_acordo, parcela } }

## RetornoVerbas_produtos_pagto_V_1_0

{ response: object { status, message, messages, verbas_produtos_pagto } }

## Retorno_ConsultaNegociacoes_V_1_0

{ response: object { status, messages, negociacoes } }

## Retorno_ConsultaNegociacoes_V_1_1

{ response: object { status, appVersion, messages, content } }

## Retorno_ConsultaReciboNLQ_V_1_0

{ response: object { status, messages, resProc } }

## Retorno_Contratos_Variaveis_V_1_0

{ response: object { status, messages, variaveis } }

## Retorno_GeracaoBoleto_V_1_0

{ response: object { status, appVersion, messages, content } }

## Retorno_LocalPagamento_V_1_0

{ response: object { status, appVersion, messages, content } }

## Retorno_PostGeracaoBoleto_V_1_0

{ response: object { status, appVersion, messages, content } }

## Retorno_PostNLQ_V_1_0

{ response: object { status, messages, recibo } }

## Retorno_PostNLQ_V_1_1

{ response: object { status, appVersion, messages, content } }

## Retorno_reenviarMensageriaKafka_V_1_0

{ response: object { status, messages, content } }

## Rota_V_1_0

{ codigo: string ex: "001"; descricao: string ex: "Rota 001"; percFrete: number(number) ex: 0.0; valFrete: number(number) ex: 0.0; distancia: number(number) ex: 0.0; custoMedioKm: number(number) ex: 0.0; ufPercorridas: string ex: "PR;MG;SC"; endConfReab: string ex: ""; extra1: number(number) ex: 0.0; extra2: number(number) ex: 0.0 }

## SnapShotProduto

{ codigo: number ex: 10162; custoMedio: number(double) ex: 76.3639; custoCompra: number(double) ex: 76.3639; precoPDV: number(double) ex: 3.89; estoque: number(double) ex: 0 }

## SnapShotProdutoResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, produtos } }

## SnapShotProdutos

{ codigo: number ex: 10162; custoMedio: number(double) ex: 76.3639; custoCompra: number(double) ex: 76.3639; precoPDV: number(double) ex: 3.89; estoque: number(double) ex: 0 }

## SnapShotProdutosResponse

{ response: object { status, message, messages, produtos } }

## SnapshotDailyResponse

{ response: object { status, messages, estoques } }

## StatusProcessamentoPedido

{ dataProcessamento: string ex: "13/04/2018"; horaProcessamento: string ex: ""; codigo: number ex: 9; data: string ex: "13/04/2018"; clie_codigo: number ex: 1; fpgt_codigo: string ex: "001"; vend_codigo: string ex: "103"; dataBaseVencimento: string ex: "13/04/2018"; especie: number ex: 1; observacao: string ex: "observações"; NumeroPedido: number ex: 0; NumeroCupom: string ex: ""; CodigoPdv: string; UnidadePdv: string; Status: string ex: "Pendente"; itens: `ItensPedido` (ver reference/schemas.md) }

## StatusProcessamentoPedidoDeprecated

{ dataProcessamento: string ex: "13/04/2018"; horaProcessamento: string ex: ""; codigo: number ex: 9; data: string ex: "13/04/2018"; clie_codigo: number ex: 1; fpgt_codigo: string ex: "001"; vend_codigo: string ex: "103"; dataBaseVencimento: string ex: "13/04/2018"; especie: number ex: 1; observacao: string ex: "observações"; NumeroPedido: number ex: 0; NumeroCupom: string ex: ""; CodigoPdv: string; UnidadePdv: string; Status: string ex: "Pendente" }

## StatusProcessamentoPedidoResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, pedido } }

## StatusProcessamentoPedidoResponseDeprecated

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, pedido } }

## StatusProcessamentoPedidoResponsev2

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, pedido } }

## StatusProcessamentoPedidoResponsev3

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, pedido } }

## StatusProcessamentoPedidoResponsev4

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, pedido } }

## StatusProcessamentoPedidov2

{ dataProcessamento: string ex: "13/04/2018"; horaProcessamento: string ex: ""; codigo: number ex: 9; data: string ex: "13/04/2018"; clie_codigo: number ex: 1; fpgt_codigo: string ex: "001"; vend_codigo: string ex: "103"; dataBaseVencimento: string ex: "13/04/2018"; especie: number ex: 1; observacao: string ex: "observações"; NumeroPedido: number ex: 0; NumeroCupom: string ex: ""; CodigoPdv: string; UnidadePdv: string; Status: string ex: "Pendente"; itens: `ItensPedido` (ver reference/schemas.md) }

## StatusProcessamentoPedidov3

{ dataProcessamento: string ex: "13/04/2018"; horaProcessamento: string ex: ""; codigo: number ex: 9; data: string ex: "13/04/2018"; clie_codigo: number ex: 1; fpgt_codigo: string ex: "001"; vend_codigo: string ex: "103"; dataBaseVencimento: string ex: "13/04/2018"; especie: number ex: 1; observacao: string ex: "observações"; NumeroPedido: number ex: 0; NumeroCupom: string ex: ""; CodigoPdv: string; UnidadePdv: string; idNfe: string ex: "41190100000000000000550010000002331105508640"; Status: string ex: "Pendente"; itens: `ItensPedido` (ver reference/schemas.md) }

## StatusProcessamentoPedidov4

{ dataProcessamento: string ex: "13/04/2018"; horaProcessamento: string ex: ""; codigo: number ex: 9; data: string ex: "13/04/2018"; clie_codigo: number ex: 1; fpgt_codigo: string ex: "001"; vend_codigo: string ex: "103"; dataBaseVencimento: string ex: "13/04/2018"; especie: number ex: 1; observacao: string ex: "observações"; NumeroPedido: number ex: 0; NumeroCupom: string ex: ""; CodigoPdv: string; UnidadePdv: string; unidadeRetirada: string ex: "002"; idNfe: string ex: ""; Status: string ex: "Pendente"; itens: `ItensPedido` (ver reference/schemas.md) }

## SubContaFDE

Subconta associada a uma contrapartida

{ unidade: string ex: "001"; subConta: string ex: "001"; regra: string ex: "01"; valor: number(double) ex: 10.0; dc: string ex: "D" }

## SugestDia

Sugestão

{ codigoProduto: number ex: 10154; sugestaoDia: number ex: 10 }

## SugestDiaResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, Sugestao } }

## TabForn_V_1_0

{ data: string(string) ex: "16/01/2018"; status: string(string) ex: "N"; fornCodigo: number ex: 157040; prodCodigo: number ex: 886688; tpEmb: string(string) ex: "E"; qemb: number ex: 12; preco: number ex: 34; desc: number ex: 0; bonif: number ex: 0; ipi: number ex: 0; vlIpi: number ex: 0; st: number ex: 0; frete: number ex: 0; tribCodigo: string(string) ex: "20019000"; usuaCodigo: number ex: 107; unidCodigo: string(string) ex: "000"; vlAcresFin: number ex: 0; verba: number ex: 0; cstIcms: string(string); fcpst: number ex: 0; fpgtCodigo: string(string) ex: "028"; release: number ex: 2 }

## TransfProdResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, maxCod, transferencias } }

## Transferencia

Transferencia

array de { transacao: string ex: "00110041550"; operacao: string ex: "001100415501"; data: string ex: "01/02/2015"; unidade: string ex: "00000000000000"; numero: string ex: ""; id: string ex: "1"; itens: `ItensTransfProd` (ver reference/schemas.md) }

## TribRelease_V_1_0

array de { release: number ex: 523326; codigo: string(string) ex: "04012010.51"; controle: string(string) ex: "811285"; descricao: string(string) ex: "Regra em Ambiente Produção"; unidades: string(string) ex: "001;002;003"; ufOrigem: string(string) ex: "AC;AL;AM;AP;BA;CE;DF;ES;EX;GO;MA;MG;MS;MT;PA;PB;PE;PI;RJ;RN;RO;RR;RS;SC;SE;SP;TO"; ufDestino: string(string) ex: "PR"; mvtos: string(string) ex: "EBR;ETE"; caractTrib: string(string) ex: "I"; simb: string(string) ex: "ST"; servico: string(string) ex: "N"; codNF: string(string) ex: "410"; codPDV: string(string) ex: "03"; origMerc: string(string) ex: ""; icms: number ex: 0; ipi: number ex: 0; iss: number ex: 0; pis: number ex: 0; cofins: number ex: 0; redBC: number ex: 0; bcSubTrib: number ex: 14; icmsSubTrib: number ex: 18; tribPisCofins: string(string) ex: "N"; redBCST: number ex: 0; icmsAnt: number ex: 0; simbCredito: string(string) ex: ""; icmsCritica: number ex: 12; redBCCritica: number ex: 0; comportamento: string(string) ex: "AJ"; icmsSubTribEnt: number ex: 12; complemento1: string(string) ex: ""; complemento2: string(string) ex: ""; complemento3: string(string) ex: ""; complemento4: string(string) ex: ""; complemento5: string(string) ex: ""; cstPis: string(string) ex: "98"; cstIPI: string(string) ex: ""; natPISCof: string(string) ex: ""; data: string(string) ex: "07/03/2023"; dtIVal: string(string) ex: "01/01/2000"; dtFVal: string(string) ex: "12/03/2023"; cstCredito: string(string) ex: ""; icmsDestino: number ex: 0; percFCP: number ex: 0; redBcDestino: number ex: 0; infAdicional: string(string) ex: ""; fcpAliq: number ex: 0; fcpRedBC: number ex: 0; fcpSTAliq: number ex: 0; fcpSTAliqEnt: number ex: 0; simbFCP: string(string) ex: ""; fcpCritica: number ex: 0; fcpRedBCCritica: number ex: 0; codBenef: string(string) ex: ""; codMotRest: string(string) ex: ""; codMotCompl: string(string) ex: ""; icmsIvaAjustado: number ex: 0; motDesonICMS: number ex: 0; redBcPisCofins: number ex: 0 }

## Tributacao_V_1_0

{ codigo: string(string) ex: ""; descricao: string(string) ex: ""; unidades: string(string) ex: ""; ufOrigem: string(string) ex: ""; ufDestino: string(string) ex: ""; mvtos: string(string) ex: ""; caracTrib: string(string) ex: ""; simbologia: string(string) ex: ""; servico: string(string) ex: ""; codNF: string(string) ex: ""; codPDV: string(string) ex: ""; origemMerc: string(string) ex: ""; icms: number(number) ex: 0.0; ipi: number(number) ex: 0.0; iss: number(number) ex: 0.0; pis: number(number) ex: 0.0; cofins: number(number) ex: 0.0; redBCICMS: number(number) ex: 0.0; bcSubTrib: number(number) ex: 0.0; subTrib: number(number) ex: 0.0; controle: string(string) ex: ""; tribPISCofins: string(string) ex: ""; redBCST: number(number) ex: 0.0; icmsAnt: number(number) ex: 0.0; simbCredito: string(string) ex: ""; icmsCritica: number(number) ex: 0.0; redBCCritica: number(number) ex: 0.0; comportamento: string(string) ex: ""; subtribEnt: number(number) ex: 0.0; complemento1: string(string) ex: ""; complemento2: string(string) ex: ""; complemento3: string(string) ex: ""; complemento4: string(string) ex: ""; complemento5: string(string) ex: ""; cstPis: string(string) ex: ""; cstIPI: string(string) ex: ""; natPISCof: string(string) ex: ""; data: string(string) ex: ""; dtIVal: string(string) ex: ""; dtFVal: string(string) ex: ""; cstAlternativa: string(string) ex: ""; icmsDestino: number(number) ex: 0.0; percFCP: number(number) ex: 0.0; redBcDestino: number(number) ex: 0.0; infAdicional: string(string) ex: ""; fcpAliq: number(number) ex: 0.0; fcpRedBC: string(string) ex: ""; fcpStAliq: number(number) ex: 0.0; fcpSTAliqEnt: number(number) ex: ""; simbFCP: string(string) ex: ""; fcpCritica: number(number) ex: 0.0; fcpRedBCCritica: number(number) ex: 0.0; codBenef: string(string) ex: ""; codMotRest: string(string) ex: ""; codMotCompl: string(string) ex: ""; icmsIvaAjustado: number(number) ex: 0.0; release: string(string) ex: ""; motDesonICMS: string(string) ex: ""; redBcPisCofins: number(number) ex: 0.0 }

## UltimaVendaDResponse_V_1_0

{ response: object { status, messages, content } }

## UnidadeResponseV_1_4

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, unidade } }

## UnidadeResponseV_1_5

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, unidade } }

## UnidadeResponseV_1_6

{ response: object { status, appVersion, messages, content } }

## UnidadeV_1_4

{ Codigo: string(string) ex: "001"; Nome: string(string) ex: "Matriz - Empresa Demonstração Ltda"; RazaoSocial: string(string) ex: "Matriz - Empresa Demonstração Ltda"; CNPJ: string(string) ex: "00000000000000"; InscEstadual: string(string) ex: ""; InscMunicipal: string(string) ex: ""; Endereco: string(string) ex: ""; Numero: string(string) ex: ""; Complemento: string(string) ex: ""; Bairro: string(string) ex: ""; CEP: string(string) ex: ""; CaixaPostal: string(string) ex: ""; Municipio: string(string) ex: "Curitiba"; UF: string(string) ex: "PR"; Fone: string(string) ex: ""; Email: string(string) ex: ""; IdentAtividade: string(string) ex: "SM - Supermercado | AT - Atacado | CD - Centro de distribuição | AD - Administração | ID - Indústria | AC - Atacado e centro de distribuição | OU - Outra | TR - Transportes | FA - Farmácia | PT - Posto"; NomeReduzido: string(string) ex: "Sup. Teste"; MetrosQuadrados: number(number) ex: "Area da loja em metros quadrados"; AreaVenda: number(number) ex: "Area de venda da loja em metros quadrados"; NumFuncionarios: number(number) ex: "Número de funcionários da loja"; NumeroPDVs: number(number) ex: "Número de Checkouts da loja"; Empresa: string(string) ex: "01" }

## UnidadeV_1_5

{ Codigo: string(string) ex: "001"; Nome: string(string) ex: "Matriz - Empresa Demonstração Ltda"; RazaoSocial: string(string) ex: "Matriz - Empresa Demonstração Ltda"; CNPJ: string(string) ex: "00000000000000"; InscEstadual: string(string) ex: ""; InscMunicipal: string(string) ex: ""; Endereco: string(string) ex: ""; Numero: string(string) ex: ""; Complemento: string(string) ex: ""; Bairro: string(string) ex: ""; CEP: string(string) ex: ""; CaixaPostal: string(string) ex: ""; Municipio: string(string) ex: "Curitiba"; UF: string(string) ex: "PR"; Fone: string(string) ex: ""; Email: string(string) ex: ""; IdentAtividade: string(string) ex: "SM - Supermercado | AT - Atacado | CD - Centro de distribuição | AD - Administração | ID - Indústria | AC - Atacado e centro de distribuição | OU - Outra | TR - Transportes | FA - Farmácia | PT - Posto"; NomeReduzido: string(string) ex: "Sup. Teste"; MetrosQuadrados: number(number) ex: "Area da loja em metros quadrados"; AreaVenda: number(number) ex: "Area de venda da loja em metros quadrados"; NumFuncionarios: number(number) ex: "Número de funcionários da loja"; NumeroPDVs: number(number) ex: "Número de Checkouts da loja"; Empresa: string(string) ex: "01"; Cidade: number(number) ex: 154; Latitude: number(number) ex: -25.4601554; Longitude: number(number) ex: -49.213212 }

## UnidadeV_1_6

{ Codigo: string(string) ex: "001"; Nome: string(string) ex: "Matriz - Empresa Demonstração Ltda"; RazaoSocial: string(string) ex: "Matriz - Empresa Demonstração Ltda"; CNPJ: string(string) ex: "00000000000000"; InscEstadual: string(string) ex: ""; InscMunicipal: string(string) ex: ""; Endereco: string(string) ex: ""; Numero: string(string) ex: ""; Complemento: string(string) ex: ""; Bairro: string(string) ex: ""; CEP: string(string) ex: ""; CaixaPostal: string(string) ex: ""; Municipio: string(string) ex: "Curitiba"; UF: string(string) ex: "PR"; Fone: string(string) ex: ""; Email: string(string) ex: ""; IdentAtividade: string(string) ex: "SM - Supermercado | AT - Atacado | CD - Centro de distribuição | AD - Administração | ID - Indústria | AC - Atacado e centro de distribuição | OU - Outra | TR - Transportes | FA - Farmácia | PT - Posto"; NomeReduzido: string(string) ex: "Sup. Teste"; MetrosQuadrados: number(number) ex: "Area da loja em metros quadrados"; AreaVenda: number(number) ex: "Area de venda da loja em metros quadrados"; NumFuncionarios: number(number) ex: "Número de funcionários da loja"; NumeroPDVs: number(number) ex: "Número de Checkouts da loja"; Empresa: string(string) ex: "01"; Cidade: number(number) ex: 154; Latitude: number(number) ex: -25.4601554; Longitude: number(number) ex: -49.213212 }

## UnidadesResponseV_1_6

{ response: object { status, appVersion, messages, content } }

## UnidadesSimplificadasResponseV_1_0

{ response: object { status, appVersion, messages, content } }

## UnidadesV_1_6

{ Codigo: string(string) ex: "001"; Nome: string(string) ex: "Matriz - Empresa Demonstração Ltda"; RazaoSocial: string(string) ex: "Matriz - Empresa Demonstração Ltda"; CNPJ: string(string) ex: "00000000000000"; InscEstadual: string(string) ex: ""; InscMunicipal: string(string) ex: ""; Endereco: string(string) ex: ""; Numero: string(string) ex: ""; Complemento: string(string) ex: ""; Bairro: string(string) ex: ""; CEP: string(string) ex: ""; CaixaPostal: string(string) ex: ""; Municipio: string(string) ex: "Curitiba"; UF: string(string) ex: "PR"; Fone: string(string) ex: ""; Email: string(string) ex: ""; IdentAtividade: string(string) ex: "SM - Supermercado | AT - Atacado | CD - Centro de distribuição | AD - Administração | ID - Indústria | AC - Atacado e centro de distribuição | OU - Outra | TR - Transportes | FA - Farmácia | PT - Posto"; NomeReduzido: string(string) ex: "Sup. Teste"; MetrosQuadrados: number(number) ex: "Area da loja em metros quadrados"; AreaVenda: number(number) ex: "Area de venda da loja em metros quadrados"; NumFuncionarios: number(number) ex: "Número de funcionários da loja"; NumeroPDVs: number(number) ex: "Número de Checkouts da loja"; Empresa: string(string) ex: "01"; Cidade: number(number) ex: 154; Latitude: number(number) ex: -25.4601554; Longitude: number(number) ex: -49.213212 }

## UpdateFornecedorV1_0

{ obsPedidos: string(string) ex: "Observações para pedidos" }

## UpdateGrupoResponse

{ response: object { status, messages } }

## UpdateGrupoResponseV1_1

{ response: object { status, appVersion, messages, content } }

## UpdateSituacaoFornecedorV1_0

{ situacao: string(string) ex: "valores possíveis = IMPEDIDO, AUTORIZACAO, NORMAL" }

## UpdateSituacaoFornecedorV1_1

{ situacao: string(string) ex: "valores possíveis = IMPEDIDO, AUTORIZACAO, NORMAL"; codigoBloqueio: number(number) ex: 0 }

## Usuario

{ Codigo: number ex: 100; Nome: string(string) ex: "Rp Info"; Grupo: string(string) ex: "Suporte"; CodigoGrupo: string(string) ex: "100"; CodigoVendedor: string(string) ex: "2135" }

## UsuarioAcessosErp_V_1_0

{ imprEtqPrVendTipo1: boolean ex: true; imprEtqPrVendTipo2: boolean ex: true; imprEtqPrVendTipo3: boolean ex: true; imprEtqPrVendTipo4: boolean ex: true; imprEtqPrVendTipo5: boolean ex: true; imprEtqPrVendTipo6: boolean ex: true }

## UsuarioDeprecated

{ Codigo: number ex: 100; Nome: string(string) ex: "Rp Info"; Grupo: string(string) ex: "Suporte"; CodigoGrupo: string(string) ex: "100" }

## UsuarioDetalhado

{ Codigo: number ex: 100; Nome: string(string) ex: "Rp Info"; Grupo: string(string) ex: "Suporte"; CodigoGrupo: string(string) ex: "100"; CodigoVendedor: string(string) ex: "2135"; UnidadesMovimento: string(string) ex: "001;002;003;004;100"; Ativo: string(string) ex: "S"; Bloqueado: string(string) ex: "N"; DptosEscopoProd: string(string) ex: ""; Comp_Codigo: string(string) ex: ""; ObjetosAcessados: string(string) ex: ""; OutrosAcessos: string(string) ex: ""; Documentos: `UsuarioDetalhadoDocumentos` (ver reference/schemas.md) }

## UsuarioDetalhadoDocumentos

array de { Codigo: string(string) ex: "2025"; Descricao: string(string) ex: "Despesas C/ Seguros Prediais"; Tipo: string(string) ex: "FDE" }

## UsuarioExterno

{ Codigo: number ex: 100; Nome: string(string) ex: "Teste"; UsuarioERP: number ex: 100; Comportamentos: string(string) ex: ""; Acessos: string(string) ex: "CT;WS;TF"; AcessosWS: string(string) ex: "" }

## UsuarioExterno_V_1_2

{ Codigo: number ex: 100; Nome: string(string) ex: "Teste"; UsuarioERP: number ex: 100; Comportamentos: string(string) ex: ""; Acessos: string(string) ex: "CT;WS;TF"; AcessosWS: string(string) ex: ""; permissoes: object { FlexMobile.Recebimento, FlexMobile.Recebimento.incluirNota, FlexMobile.Recebimento.incluirLote, FlexMobile.Recebimento.excluirLote, FlexMobile.Recebimento.excluirNota, FlexMobile.Recebimento.desvincularUsuario, FlexMobile.ConsultaProdutos, FlexMobile.ConsultaProdutos.marcarExportacaoPDV, FlexMobile.ConsultaProdutos.marcarExportacaoCotacao, FlexMobile.ConsultaProdutos.visualizarPrecos, FlexMobile.ConsultaProdutos.visualizarEstoques, FlexMobile.ConsultaProdutos.visualizarUltimaCompra, FlexMobile.ConsultaProdutos.visualizarCustos, FlexMobile.ConsultaProdutos.visualizarVendas, FlexMobile.ConsultaProdutos.imprimirEtiquetas, FlexMobile.AuditoriaEstoques, FlexMobile.AutorizacaoLancamentos, FlexMobile.ConsultaProdutos.alertarEtqPendImpressao, FlexMobile.ConsultaPatrimonio, FlexMobile.ProdutosMarcados.TarefaAuditoriaEstoque } }

## UsuarioExterno_V_1_3

**UsuarioExterno_V_1_2** = object { Codigo, Nome, UsuarioERP, Comportamentos, Acessos, AcessosWS, permissoes } & { acessosErp: `UsuarioAcessosErp_V_1_0` (ver reference/schemas.md) }

## Usuarios

{ Codigo: number ex: 100; Nome: string(string) ex: "Rp Info"; Grupo: string(string) ex: "Suporte"; CodigoGrupo: string(string) ex: "100"; CodigoVendedor: string(string) ex: "2135" }

## UsuariosDeprecated

{ Codigo: number ex: 100; Nome: string(string) ex: "Rp Info"; Grupo: string(string) ex: "Suporte"; CodigoGrupo: string(string) ex: "100" }

## V_1_3_pendest_incluir

{ Inclusoes: object { dataMovimento, dataEntrega, unidadeOrigem, unidadeDestino, tipoPendencia, codigoPendencia, especie, codigoDocumento, categoriaParticipante, participante, observacao, pendencias }; Baixas: object { pendencias } }

## V_1_4_pendest_incluir

{ Inclusoes: object { dataMovimento, dataEntrega, unidadeOrigem, unidadeDestino, tipoPendencia, codigoPendencia, especie, codigoDocumento, categoriaParticipante, participante, observacao, pendencias } }

## V_1_5_pendest_incluir

{ Inclusoes: object { dataMovimento, dataEntrega, unidadeOrigem, unidadeDestino, tipoPendencia, codigoPendencia, especie, codigoDocumento, categoriaParticipante, participante, observacao, pendencias }; Baixas: object { pendencias } }

## V_1_6_pendest_incluir

{ Inclusoes: object { dataMovimento, dataEntrega, unidadeOrigem, unidadeDestino, tipoPendencia, codigoPendencia, especie, codigoDocumento, categoriaParticipante, participante, observacao, pendencias }; Baixas: object { pendencias } }

## VdaDetResponse

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, movimentos } }

## VendasResponse_V_1_0

{ response: object { status, messages, content } }

## XmlMessages

array de { message: string ex: "Requisição processada com sucesso" }

## XmlNfe

O Atributo "conteudo" está no formato de compacatação GZIP, e codificado em BASE64.

{ chave: string(string) ex: "41190129884092000110550010000407811068816470"; conteudo: string(string) ex: "" }

## XmlNfeV11

O Atributo "conteudo" está no formato de compacatação GZIP, e codificado em BASE64.

{ chave: string(string) ex: "41190129884092000110550010000407811068816470"; tpEvento: string(string) ex: "210200"; justificativa: string(string) ex: ""; status: string(string) ex: "AUTORIZADA"; conteudo: string(string) ex: "" }

## alterados_dthrmanutencao_V_1_0

{ response: object { status, messages, content } }

## bens_V_1_0

{ response: object { status, messages, content } }

## bens_V_1_1

{ response: object { status, appVersion, messages, content } }

## bens_update_req_V_1_0

{ descricao: string ex: ""; complemento: string ex: ""; funcao: string ex: ""; gbenCodigo: number ex: 100; numeroserie: string ex: ""; plaqueta: string ex: ""; codigoncm: string ex: ""; ccstRateio: string ex: ""; marca: string ex: ""; identutil: string ex: ""; vctogarantia: string ex: "12/01/2023"; corretor: string ex: ""; vlsegurado: string ex: ""; franquia: string ex: ""; vigsegi: string ex: ""; vigsegf: string ex: ""; apoliceseg: string ex: ""; codresponsavel: string ex: ""; peso: string ex: ""; observacao: string ex: "" }

## bens_update_res_V_1_0

{ response: object { status, messages, content } }

## biometriasReqBody

{ codEntidade: number ex: 1; categoriaEntidade: string(string) ex: "CLIENTE"; dedo: string(string) ex: "MAO_ESQUERDA_INDICADOR"; equipamento: string(string) ex: "MDBTECHMAG_FS_FTR"; biometria: string(string) }

## biometriasReqBodyArray

array de **biometriasReqBody** = object { codEntidade, categoriaEntidade, dedo, equipamento, biometria }

## biometriasRes

{ response: object { status, messages } }

## bodyMetaProd_V1

{ data: string(string) ex: "25/06/2022"; cnpjUnidade: string(string) ex: "76387901000140"; departamento: string(string) ex: "0"; grupo: string(string) ex: "0"; vendas: number ex: 20000; lucros: number ex: 0; estoques: number ex: 0; giro: number ex: 0; percentCmv: number ex: 5; margemContrib: number ex: 0; compras: number ex: 20000; perdas: number ex: 0; verbas: number ex: 0; verbasLiq: number ex: 0; devolucoes: number ex: 0; faltas: number ex: 0; percentLucros: number ex: 0; sobras: number ex: 0 }

## bodyMetaProd_V1_1

**bodyMetaProd_V1** = object { data, cnpjUnidade, departamento, grupo, vendas, lucros, estoques, giro, percentCmv, margemContrib, compras, perdas, verbas, verbasLiq, devolucoes, faltas, percentLucros, sobras } & { tipo: string(string) ex: "Dia"; produto: number ex: 12345678; tipoInformacao: string(string) ex: "Valor" }

## bodyMetasProd_V1

{ metas: array de `bodyMetaProd_V1` (ver reference/schemas.md) }

## bodyMetasProd_V1_1

{ metas: array de `bodyMetaProd_V1_1` (ver reference/schemas.md) }

## cadastroCidade

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, messages, content } }

## cadastroCidadeV1

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, municipios } }

## cadastroCidadeV2

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, messages, content } }

## cadastroMunicipio

{ codigo: number ex: 1; codigoIBGE: number ex: 4107108; descricao: string(string) ex: "Curitiba"; uf: string(string) ex: "PR" }

## cadastroMunicipiosV1

array de { codigo: number ex: 1; descricao: string(string) ex: "Curitiba"; uf: string(string) ex: "PR" }

## cadastroMunicipiosV2

array de { codigo: number ex: 1; codigoIBGE: number ex: 4107108; descricao: string(string) ex: "Curitiba"; uf: string(string) ex: "PR" }

## carregamento

{ numero: number ex: 399; status: string(string) ex: "B"; unidade: string(string) ex: "003"; rota: string(string) ex: "011"; dataMovimento: string(string) ex: "10/06/2019"; relatorio: string(string) ex: ""; pesoPaletes: number ex: 1200; volumePaletes: number ex: 2; kmInicial: number ex: 0; kmFinal: number ex: 0; distancia: number ex: 0; custoTransporte: number ex: 0; custoKm: number ex: 0; totalProdutos: number ex: 0; despesasAdicionais: number ex: 0; custoTotal: number ex: 0; transportador: string(string) ex: ""; quantidadePaletes: number ex: 1; quantidadePedidos: number ex: 1; pesoProdutos: number ex: 300; volumeProdutos: number ex: 0; descricao: string(string) ex: ""; placa: string(string) ex: ""; distanciaPrevista: number ex: 100; custoKmPrevisto: number ex: 3; custoTotalPrevisto: number ex: 350; valorTotalPrevisto: number ex: 588; margemPrevista: number ex: 60; lucroTotalPrevisto: number ex: 355; volumeTotalPrevisto: number ex: 0; pesoTotalPrevisto: number ex: 300; usuarioSimulacao: number ex: 0; documentoUsadoSimulacao: string(string) ex: ""; outrosCarretamentos: string(string) ex: ""; doca: number ex: 0; dataSaida: string(string) ex: "11/06/2019"; dataChegada: string(string) ex: "24/03/2022"; usuarioSaida: number ex: 900; usuarioChegada: number ex: 0; usuarioAutorizador: number ex: 0; lacres: string(string) ex: ""; statusTransporte: string(string) ex: "1"; justificativa: string(string) ex: ""; etiquetas: string(string) ex: ""; etiquetasCaixas: string(string) ex: ""; observacao: string(string) ex: ""; motorista: number ex: 0; ajudante: number ex: 0; processadosEstoque: string(string) ex: ""; preseparacao: string(string) ex: "N"; liberadoFaturamento: string(string) ex: ""; espe_codigo: string(string) ex: "0011"; dataPrevista: string(string) ex: "10/06/2019" }

## carregamentos

array de **carregamento** = object { numero, status, unidade, rota, dataMovimento, relatorio, pesoPaletes, volumePaletes, kmInicial, kmFinal, distancia, custoTransporte, custoKm, totalProdutos, despesasAdicionais, custoTotal, transportador, quantidadePaletes, quantidadePedidos, pesoProdutos, volumeProdutos, descricao, placa, distanciaPrevista, custoKmPrevisto, custoTotalPrevisto, valorTotalPrevisto, margemPrevista, lucroTotalPrevisto, volumeTotalPrevisto, pesoTotalPrevisto, usuarioSimulacao, documentoUsadoSimulacao, outrosCarretamentos, doca, dataSaida, dataChegada, usuarioSaida, usuarioChegada, usuarioAutorizador, lacres, statusTransporte, justificativa, etiquetas, etiquetasCaixas, observacao, motorista, ajudante, processadosEstoque, preseparacao, liberadoFaturamento, espe_codigo, dataPrevista }

## chaveXml

{ chave: string(string) ex: "41190129884092000110550010000407811068816470" }

## chaveXmlV11

{ chave: string(string) ex: "41190129884092000110550010000407811068816470"; tpEvento: string(string) ex: "210200"; justificativa: string(string) ex: "" }

## codigoCidade

{ codigo: number ex: 9 }

## dadosComerciais

{ endereco: string(string) ex: "Marcio Rafael"; numero: string(string) ex: "198"; complemento: string(string) ex: "Casa"; bairro: string(string) ex: "São Rafael"; cidade: integer ex: 273; uf: string(string) ex: "PR"; cep: string(string) ex: "87160000"; fone: string(string) ex: "4498651504"; foneCel: string(string) ex: "4498651504" }

## dadosResidenciais

{ endereco: string(string) ex: "Marcio Rafael"; numero: string(string) ex: "198"; complemento: string(string) ex: "Casa"; bairro: string(string) ex: "São Rafael"; cidade: integer ex: 273; uf: string(string) ex: "PR"; cep: string(string) ex: "87160000"; fone: string(string) ex: "4498651504" }

## depesasServicosV1

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, appVersion, messages, content } }

## erros

{ message_1: string ex: "erro 1"; message_2: string ex: "erro 2" }

## financeiro_centrodecustos_V_1_1

{ response: object { status, message, messages, centroDeCustos } }

## fornecedor_V_1_3

{ codigo: number ex: 13269; nome: string(string) ex: "Bella Janela Cortinas"; razaoSocial: string(string) ex: "Bella Janela Cortinas"; cnpj: string(string) ex: "72344591000125"; inscricaoEstadual: string(string) ex: "252696654"; codigoVinc: number ex: 0; situacao: string(string) ex: "I"; marcas: string(string) ex: ""; dataCadastro: string(string) ex: "24/07/2013"; dataAlteracao: string(string) ex: "16/11/2017"; status: string(string) ex: "N"; tipos: string(string) ex: ""; uf: string(string) ex: "SC"; contribPrev: string(string) ex: "S" }

## fornecedor_V_1_4

{ codigo: number ex: 13269; nome: string(string) ex: "Bella Janela Cortinas"; razaoSocial: string(string) ex: "Bella Janela Cortinas"; cnpj: string(string) ex: "72344591000125"; inscricaoEstadual: string(string) ex: "252696654"; codigoVinc: number ex: 0; situacao: string(string) ex: "I"; marcas: string(string) ex: ""; dataCadastro: string(string) ex: "24/07/2013"; dataAlteracao: string(string) ex: "16/11/2017"; status: string(string) ex: "N"; tipos: string(string) ex: ""; uf: string(string) ex: "SC"; contribPrev: string(string) ex: "S"; endereco: object { cep, logradouro, numero, bairro, complemento, cidade } }

## funcionario

{ codigo: number ex: 91276; nome: string(string) ex: "João da Silva"; unidade: string(string) ex: "001"; nascimento: string(string) ex: "03/03/1900"; endereco: string(string) ex: "Rua Luis Garcia"; enderecoNumero: string(string) ex: "129"; enderecoComplemento: string(string) ex: ""; bairro: string(string) ex: "Pq Independencia"; codigoMunicipio: number ex: 4593; cep: string(string) ex: "80230030"; nomeMae: string(string) ex: "Maria De Lourdes De Proencio"; nomePai: string(string) ex: "Paulo Alves De Proencio"; telefone: string(string) ex: ""; estadoCivil: string(string) ex: "2"; sexo: string(string) ex: "F"; cor: string(string) ex: "2"; deficiente: string(string) ex: "N"; rg: string(string) ex: "5637152"; rgUf: string(string) ex: "SC"; rgExpedicao: string(string) ex: "SPSC"; rgData: string(string) ex: ""; cpf: string(string) ex: "11625761600"; pis: string(string) ex: "16195505391"; documentoMilitar: string(string) ex: ""; tipoDocumentoMilitar: string(string) ex: ""; eleitor: string(string) ex: "91662710604"; zonaEleitoral: number ex: 68; secaoEleitoral: number ex: 0; carteiraProfissional: string(string) ex: "6371912"; serieCarteiraProfissional: string(string) ex: "0010"; ufCarteiraProfissional: string(string) ex: "SC"; admissao: string(string) ex: "06/02/2014"; demissao: string(string) ex: ""; salarioBase: number ex: 0; codigoFgts: string(string) ex: "112202"; valeTransporte: string(string) ex: "N"; banco: string(string) ex: ""; agencia: string(string) ex: ""; digitoAgencia: string(string) ex: ""; contaCorrente: string(string) ex: ""; digitoConta: string(string) ex: ""; titularConta: string(string) ex: ""; nroCartaoMagnetico: string(string) ex: ""; tipo: string(string) ex: ""; situacao: string(string) ex: "05"; senha: string(string) ex: "2403224"; limiteConvenio: number ex: 10; codigoPDV: string(string) ex: "0000000111102"; acumuladoChequeDiario: number ex: 0; acumuladoChequeDiario01: number ex: 0; acumuladoChequeDiario02: number ex: 0; acumuladoChequeDiario03: number ex: 0; acumuladoChequeDiario04: number ex: 0; acumuladoChequeDiario05: number ex: 0; acumuladoChequeDiario06: number ex: 0; acumuladoValorDiario: number ex: 0; ultimaOperacaoPdv: string(string) ex: ""; limiteCheque: number ex: 0; foneEmergencia: string(string) ex: ""; celular: string(string) ex: ""; codigoUsuario: number ex: 0; comissao: number ex: 0; funcao: string(string) ex: "OPC"; unidadeFechamentoPDV: string(string) ex: ""; observacao: string(string) ex: ""; usuarioInclusao: number ex: 999; dataCadastro: string(string) ex: "02/03/2022"; email: string(string) ex: ""; limiteDiario: string(string) ex: "N"; centroCusto: string(string) ex: ""; municipio: string(string) ex: "Medianeira"; municipioUf: string(string) ex: "PR"; escolaridade: string(string) ex: ""; dataAlteracao: string(string) ex: ""; usuarioAlteracao: number ex: 0; horarioEntrada: string(string) ex: ""; horarioSaida: string(string) ex: ""; tipos: string(string) ex: ""; dataHoraManutencao: string(string) ex: "08/10/2022 16:05:45.215" }

## funcionarioInsert

{ codigo: number(numer) ex: 1; nome: string(string) ex: "João da Silva"; unidade: string(string) ex: "001"; nascimento: string(string) ex: "03/03/1995"; endereco: string(string) ex: "Rua João Barros"; enderecoNumero: string(string) ex: "129"; enderecoComplemento: string(string) ex: ""; bairro: string(string) ex: "Pq Independencia"; codigoMunicipio: number ex: 4593; cep: string(string) ex: "80230030"; nomeMae: string(string) ex: "Maria De Lourdes De Proencio"; nomePai: string(string) ex: "Paulo Alves De Proencio"; telefone: string(string) ex: ""; estadoCivil: string(string) ex: "2"; sexo: string(string) ex: "F"; cor: string(string) ex: "2"; deficiente: string(string) ex: "N"; rg: string(string) ex: "5637152"; rgUf: string(string) ex: "SC"; rgExpedicao: string(string) ex: "SPSC"; rgData: string(string) ex: ""; cpf: string(string) ex: "11624865200"; pis: string(string) ex: "16195505391"; documentoMilitar: string(string) ex: ""; tipoDocumentoMilitar: string(string) ex: ""; eleitor: string(string) ex: "91662710604"; zonaEleitoral: number ex: 68; secaoEleitoral: number ex: 0; carteiraProfissional: string(string) ex: "6371912"; serieCarteiraProfissional: string(string) ex: "0010"; ufCarteiraProfissional: string(string) ex: "SC"; admissao: string(string) ex: "06/02/2014"; demissao: string(string) ex: ""; salarioBase: number ex: 960; codigoFgts: string(string) ex: "112202"; valeTransporte: string(string) ex: "N"; banco: string(string) ex: ""; agencia: string(string) ex: ""; digitoAgencia: string(string) ex: ""; contaCorrente: string(string) ex: ""; digitoConta: string(string) ex: ""; titularConta: string(string) ex: ""; nroCartaoMagnetico: string(string) ex: ""; tipo: string(string); situacao: string(string) ex: "05"; senha: string(string) ex: "2403224"; limiteConvenio: number ex: 10; codigoPDV: string(string) ex: "0000000111102"; acumuladoChequeDiario: number ex: 0; acumuladoChequeDiario01: number ex: 0; acumuladoChequeDiario02: number ex: 0; acumuladoChequeDiario03: number ex: 0; acumuladoChequeDiario04: number ex: 0; acumuladoChequeDiario05: number ex: 0; acumuladoChequeDiario06: number ex: 0; acumuladoValorDiario: number ex: 0; ultimaOperacaoPdv: string(string) ex: ""; limiteCheque: number ex: 0; foneEmergencia: string(string); celular: string(string) ex: ""; codigoUsuario: number ex: 0; comissao: number ex: 0; funcao: string(string) ex: "OPC"; unidadeFechamentoPDV: string(string) ex: ""; observacao: string(string) ex: ""; email: string(string) ex: ""; limiteDiario: string(string) ex: "N"; centroCusto: string(string); escolaridade: string(string); horarioEntrada: string(string); horarioSaida: string(string); tipos: string(string) }

## funcionario_V_1_0

{ codigo: number ex: 91276; nome: string(string) ex: "João da Silva"; unidade: string(string) ex: "001"; nascimento: string(string) ex: "03/03/1900"; endereco: string(string) ex: "Rua Luis Garcia"; enderecoNumero: string(string) ex: "129"; enderecoComplemento: string(string) ex: ""; bairro: string(string) ex: "Pq Independencia"; codigoMunicipio: number ex: 4593; cep: string(string) ex: "80230030"; nomeMae: string(string) ex: "Maria De Lourdes De Proencio"; nomePai: string(string) ex: "Paulo Alves De Proencio"; telefone: string(string) ex: ""; estadoCivil: string(string) ex: "2"; sexo: string(string) ex: "F"; cor: string(string) ex: "2"; deficiente: string(string) ex: "N"; rg: string(string) ex: "5637152"; rgUf: string(string) ex: "SC"; rgExpedicao: string(string) ex: "SPSC"; rgData: string(string) ex: ""; cpf: string(string) ex: "11625761600"; pis: string(string) ex: "16195505391"; documentoMilitar: string(string) ex: ""; tipoDocumentoMilitar: string(string) ex: ""; eleitor: string(string) ex: "91662710604"; zonaEleitoral: number ex: 68; secaoEleitoral: number ex: 0; carteiraProfissional: string(string) ex: "6371912"; serieCarteiraProfissional: string(string) ex: "0010"; ufCarteiraProfissional: string(string) ex: "SC"; admissao: string(string) ex: "06/02/2014"; demissao: string(string) ex: ""; salarioBase: number ex: 0; codigoFgts: string(string) ex: "112202"; valeTransporte: string(string) ex: "N"; banco: string(string) ex: ""; agencia: string(string) ex: ""; digitoAgencia: string(string) ex: ""; contaCorrente: string(string) ex: ""; digitoConta: string(string) ex: ""; titularConta: string(string) ex: ""; nroCartaoMagnetico: string(string) ex: ""; tipo: string(string) ex: ""; situacao: string(string) ex: "05"; senha: string(string) ex: "2403224"; limiteConvenio: number ex: 10; codigoPDV: string(string) ex: "0000000111102"; acumuladoChequeDiario: number ex: 0; acumuladoChequeDiario01: number ex: 0; acumuladoChequeDiario02: number ex: 0; acumuladoChequeDiario03: number ex: 0; acumuladoChequeDiario04: number ex: 0; acumuladoChequeDiario05: number ex: 0; acumuladoChequeDiario06: number ex: 0; acumuladoValorDiario: number ex: 0; ultimaOperacaoPdv: string(string) ex: ""; limiteCheque: number ex: 0; foneEmergencia: string(string) ex: ""; celular: string(string) ex: ""; codigoUsuario: number ex: 0; comissao: number ex: 0; funcao: string(string) ex: "OPC"; unidadeFechamentoPDV: string(string) ex: ""; observacao: string(string) ex: ""; usuarioInclusao: number ex: 999; dataCadastro: string(string) ex: "02/03/2022"; email: string(string) ex: ""; limiteDiario: string(string) ex: "N"; centroCusto: string(string) ex: ""; municipio: string(string) ex: "Medianeira"; municipioUf: string(string) ex: "PR"; escolaridade: string(string) ex: ""; dataAlteracao: string(string) ex: ""; usuarioAlteracao: number ex: 0; horarioEntrada: string(string) ex: ""; horarioSaida: string(string) ex: ""; tipos: string(string) ex: "" }

## getClassVipCommerce

{ response: object { status, messages, classes } }

## getClassVipCommerce_V_1_1

{ response: object { status, appVersion, messages, content } }

## getMetasProd_V1

{ response: object { status, messages, metas } }

## getMetasProd_V1_1

{ response: object { status, messages, metas } }

## getPendenciasFinanceirasBaixadasResponse

{ response: object { status, appVersion, messages, content } }

## imageBensDEL_res_V1_0

{ response: object { status, appVersion, messages, content } }

## imageBensGET_res_V1_0

{ response: object { status, appVersion, messages, content } }

## imageBensPOST_res_V1_0

{ response: object { status, appVersion, messages, content } }

## imageBensPUT_res_V1_0

{ response: object { status, appVersion, messages, content } }

## imageBens_req_V1_0

{ codigoBem: number ex: 100; fileName: string ex: "Example.jpg"; descricao: string ex: ""; codigoGrupo: number ex: 1; data: string ex: "*base64*" }

## itemPendenciaFinanceira

{ entidade: string(string) ex: "15695"; transacao: string(string) ex: "01313399199"; operacao: string(string) ex: "013133991997"; pger_conta: number ex: 211101; status: string(string) ex: "NORMAL"; numeroDcto: string(string) ex: "295074"; parcela: string(string) ex: "1"; pr: string(string) ex: "P"; valor: number ex: 793.3; juros: number ex: 0.0; multa: number ex: 0.0; mora: number ex: 0.0; acrescimos: number ex: 0.0; abatimentos: number ex: 0.0; descontos: number ex: 0.0; corrMonet: number ex: 0.0; txAdm: number ex: 0.0; baixaParcial: number ex: 0.0; dataMovimento: string(string) ex: "31/12/2019"; dataBaixa: string(string) ex: "02/09/2021"; dataVencimento: string(string) ex: "13/02/2020" }

## itemPendenciaFinanceira_V_1_2

{ entidade: string(string) ex: "15695"; transacao: string(string) ex: "01313399199"; operacao: string(string) ex: "013133991997"; pger_conta: number ex: 211101; status: string(string) ex: "NORMAL"; numeroDcto: string(string) ex: "295074"; parcela: string(string) ex: "1"; pr: string(string) ex: "P"; valor: number ex: 793.3; juros: number ex: 0.0; multa: number ex: 0.0; mora: number ex: 0.0; acrescimos: number ex: 0.0; abatimentos: number ex: 0.0; descontos: number ex: 0.0; corrMonet: number ex: 0.0; txAdm: number ex: 0.0; baixaParcial: number ex: 0.0; dataMovimento: string(string) ex: "31/12/2019"; dataBaixa: string(string) ex: "02/09/2021"; dataVencimento: string(string) ex: "13/02/2020"; dataLancamento: string(string) ex: "13/02/2020"; complemento: string ex: ""; formaPagamento: string ex: ""; numeroParcelas: number ex: 1; unidade: string ex: "001" }

## itemPendenciaFinanceira_V_1_3

{ entidade: string(string) ex: "15695"; transacao: string(string) ex: "01313399199"; operacao: string(string) ex: "013133991997"; pger_conta: number ex: 211101; status: string(string) ex: "NORMAL"; numeroDcto: string(string) ex: "295074"; parcela: string(string) ex: "1"; pr: string(string) ex: "P"; valor: number ex: 793.3; juros: number ex: 0.0; multa: number ex: 0.0; mora: number ex: 0.0; acrescimos: number ex: 0.0; abatimentos: number ex: 0.0; descontos: number ex: 0.0; corrMonet: number ex: 0.0; txAdm: number ex: 0.0; baixaParcial: number ex: 0.0; dataMovimento: string(string) ex: "31/12/2019"; dataBaixa: string(string) ex: "02/09/2021"; dataVencimento: string(string) ex: "13/02/2020"; dataLancamento: string(string) ex: "13/02/2020"; complemento: string ex: ""; formaPagamento: string ex: ""; numeroParcelas: number ex: 1; unidade: string ex: "001"; localPagamento: string ex: "001"; portador: string ex: "900"; loteCNAB: string ex: "99990"; codigoPdv: string ex: "001"; cupom: string ex: "0064812" }

## itemPendenciaFinanceira_V_1_4

{ entidade: string(string) ex: "15695"; transacao: string(string) ex: "01313399199"; operacao: string(string) ex: "013133991997"; pger_conta: number ex: 211101; status: string(string) ex: "NORMAL"; numeroDcto: string(string) ex: "295074"; parcela: string(string) ex: "1"; pr: string(string) ex: "P"; valor: number ex: 793.3; juros: number ex: 0.0; multa: number ex: 0.0; mora: number ex: 0.0; acrescimos: number ex: 0.0; abatimentos: number ex: 0.0; descontos: number ex: 0.0; corrMonet: number ex: 0.0; txAdm: number ex: 0.0; baixaParcial: number ex: 0.0; dataMovimento: string(string) ex: "31/12/2019"; dataBaixa: string(string) ex: "02/09/2021"; transacaoBaixa: string ex: "00115603190"; dataVencimento: string(string) ex: "13/02/2020"; dataLancamento: string(string) ex: "13/02/2020"; complemento: string ex: ""; formaPagamento: string ex: ""; numeroParcelas: number ex: 1; unidade: string ex: "001"; localPagamento: string ex: "001"; portador: string ex: "900"; loteCNAB: string ex: "99990"; codigoPdv: string ex: "001"; cupom: string ex: "0064812" }

## itemPendenciaFinanceira_V_1_5

{ entidade: string(string) ex: "15695"; transacao: string(string) ex: "01313399199"; operacao: string(string) ex: "013133991997"; pger_conta: number ex: 211101; status: string(string) ex: "NORMAL"; numeroDcto: string(string) ex: "295074"; parcela: string(string) ex: "1"; pr: string(string) ex: "P"; valor: number ex: 793.3; juros: number ex: 0.0; multa: number ex: 0.0; mora: number ex: 0.0; acrescimos: number ex: 0.0; abatimentos: number ex: 0.0; descontos: number ex: 0.0; corrMonet: number ex: 0.0; txAdm: number ex: 0.0; baixaParcial: number ex: 0.0; dataMovimento: string(string) ex: "31/12/2019"; dataBaixa: string(string) ex: "02/09/2021"; transacaoBaixa: string ex: "00115603190"; codDocumentoBaixa: number ex: 3503; dataVencimento: string(string) ex: "13/02/2020"; dataLancamento: string(string) ex: "13/02/2020"; complemento: string ex: ""; formaPagamento: string ex: ""; numeroParcelas: number ex: 1; unidade: string ex: "001"; localPagamento: string ex: "001"; portador: string ex: "900"; loteCNAB: string ex: "99990"; codigoPdv: string ex: "001"; cupom: string ex: "0064812" }

## itemPendenciaFinanceira_V_1_6

{ entidade: string(string) ex: "15695"; transacao: string(string) ex: "01313399199"; operacao: string(string) ex: "013133991997"; pger_conta: number ex: 211101; status: string(string) ex: "NORMAL"; numeroDcto: string(string) ex: "295074"; parcela: string(string) ex: "1"; pr: string(string) ex: "P"; valor: number ex: 793.3; juros: number ex: 0.0; multa: number ex: 0.0; mora: number ex: 0.0; acrescimos: number ex: 0.0; abatimentos: number ex: 0.0; descontos: number ex: 0.0; corrMonet: number ex: 0.0; txAdm: number ex: 0.0; baixaParcial: number ex: 0.0; dataMovimento: string(string) ex: "31/12/2019"; dataBaixa: string(string) ex: "02/09/2021"; transacaoBaixa: string ex: "00115603190"; codDocumentoBaixa: number ex: 3503; dataVencimento: string(string) ex: "13/02/2020"; dataLancamento: string(string) ex: "13/02/2020"; complemento: string ex: ""; formaPagamento: string ex: ""; numeroParcelas: number ex: 1; unidade: string ex: "001"; localPagamento: string ex: "001"; portador: string ex: "900"; loteCNAB: string ex: "99990"; codigoPdv: string ex: "001"; cupom: string ex: "0064812"; mapaCarga: number ex: 2; dataAutPgto: string ex: "27/01/2025"; autorizada: string ex: "27/01/2025"; espe_codigo: string ex: "3021"; hist_codigo: string ex: "6000"; vend_codigo: string ex: "001"; catentidade: string ex: "N"; cnpjcpf: string ex: "033.868.940-03"; valorComissao: number ex: 5.55; lote: number ex: 30661; transBaixa: string ex: "010109391739"; databaixa: string ex: "25/01/2025"; usuautpgto: string ex: "111"; contacontabil: number ex: 112301; vinculadas: string ex: "N" }

## listaCodigoPendencia

{ codigo: string ex: "000"; descricao: string ex: ""; bxparcial: string ex: ""; sugcompra: string ex: ""; tipo: string ex: ""; pzelim: number(integer) ex: 0; pzelimbx: number(integer) ex: 0; comportamento: string ex: "" }

## listaFormasPagamentoResponse

{ response: object { status, message, messages, formasPagamento } }

## listaFormasPagamentoResponse_V_1_1

{ response: object { status, messages, formasPagamento } }

## listaFormasPagamentoResponse_V_1_2

{ response: object { status, messages, formasPagamento } }

## listaFornecedoresResponse

{ response: object { status, message, messages, fornecedores } }

## listaPendenciasFinanceirasFornecedorResponse

{ response: object { status, messages, pendencias } }

## listaPendenciasFinanceirasFornecedorResponse_V_1_1

{ response: object { status, messages, pendecias } }

## listaPendenciasFinanceirasFornecedorResponse_V_1_2

{ response: object { status, messages, pendencias } }

## listaPendenciasFinanceirasFornecedorResponse_V_1_3

{ response: object { status, messages, pendencias } }

## listaPendenciasFinanceirasFornecedorResponse_V_1_4

{ response: object { status, messages, pendencias } }

## listaPendenciasFinanceirasFornecedorResponse_V_1_5

{ response: object { status, messages, pendencias } }

## listaPendenciasFinanceirasFornecedorResponse_V_1_6

{ response: object { status, messages, pendencias } }

## messages

array de { message: string ex: "Requisição processada com sucesso" }

## messagesAgendas

array de { message: string ex: "Dados carregados com sucesso" }

## messagesCadastroCidade

array de { message: string ex: "Cidade salva com sucesso" }

## messagesCompradores

array de { message: string ex: "Dados carregados com sucesso" }

## messagesControleEntrega

array de { message: string ex: "Controle de entrega gravado com sucesso" }

## messagesDeleteItem

array de { message: string ex: "Item excluído com sucesso" }

## messagesMovProd

array de { message: string ex: "Dados processados com sucesso" }

## messagesPedidoCompra

array de { message: string ex: "Dados processados com sucesso" }

## messagesPesquisaDePreco

array de { message: string ex: "Dados gravados com sucesso" }

## messagesProgramaPreco

array de { message: string ex: "Dados carregados com sucesso" }

## messagesUpdateStatusControleEntrega

array de { message: string ex: "Status do Controle de entrega atualizado com sucesso" }

## messagesUsuario

array de { message: string ex: "Dados carregados" }

## messagesV2

array de { message: string ex: "Dados processados com sucesso" }

## messagesV3

array de { message: string ex: "Requisição processada com sucesso" }

## messagesproc

array de { message: string ex: "processado com sucesso" }

## metasProdSucess

{ response: object { status, messages } }

## metasProdV1_0

{ data: string(string) ex: "29/06/2022"; unidade: string(string) ex: "001"; departamento: string(string) ex: "000"; grupo: string(string) ex: "00000"; vendas: number ex: 215309; lucros: number ex: 0; estoques: number ex: 0; giro: number ex: 0; usuario: number ex: 999; percentCmv: number ex: 0; margemContrib: number ex: 51674; compras: number ex: 172247; perdas: number ex: 0; verbas: number ex: 0; verbasLiq: number ex: 0; devolucoes: number ex: 0; faltas: number ex: 0; percentLucros: number ex: 0; sobras: number ex: 0 }

## metasProdV1_1

**metasProdV1_0** = object { data, unidade, departamento, grupo, vendas, lucros, estoques, giro, usuario, percentCmv, margemContrib, compras, perdas, verbas, verbasLiq, devolucoes, faltas, percentLucros, sobras } & { produto: number ex: 0; tipo: string(strings) ex: "Mes"; agrupamento: string(string) ex: "Deptos"; tipoInformacao: string(string) ex: "Valor" }

## responseFornecedor_V_1_3

{ response: object { status, messages, fornecedor } }

## responseFornecedor_V_1_4

{ response: object { status, messages, fornecedor } }

## responseFornecedor_V_1_5

{ response: object { status, messages, fornecedores } }

## response_v1.0_ativos

{ response: object { status, appVersion, messages, content } }

## response_v1.0_cenarios_preco_produtos

{ response: object { status, appVersion, messages, content } }

## response_v1.0_classes

{ response: object { status, appVersion, messages, content } }

## response_v1.0_curvasABC

{ response: object { status, appVersion, messages, content } }

## response_v1.0_marcas

{ response: object { status, appVersion, messages, content } }

## response_v1.0_produtosFornecedores

{ response: object { status, appVersion, messages, content } }

## response_v1.0_produtounidade_ofertas

{ status: string; appVersion: string; messages: array de object { message }; content: array de object { codigoProduto, nomeProduto, marca, precoAnterior, precoAtual, preco2, preco3, preco4, preco5, codigoBarras, codigosAlternativos, caminhoImagem } }

## response_v1.0_setores

{ response: object { status, appVersion, messages, content } }

## response_v1.0_setoresdeposito

{ response: object { status, appVersion, messages, content } }

## response_v1.0_tipos

{ response: object { status, appVersion, messages, content } }

## tiposFornec

array de { codigo: string(string) ex: "PA"; descricao: string(string) ex: "Parceiros" }

## v1_0_patrimonial_auditar_requestBody

{ data: string ex: "21/01/2025"; unidade: string ex: 1; auditorias: array de object { id, codigo, qtde, centroCustos, acumular, identificador } }

## v1_0_patrimonial_auditar_response

{ response: object { status, appVersion, messages, content } }

## v1_0_produtounidade_codigo_unidade_cnpjOrCodigo_requestbody

{ setor: string; setorDep: string; etq: number ex: 0; ctz: number ex: 0; tecla: string; espaco: number ex: 0; pzRepos: number ex: 0; pzEntrega: number ex: 0; diasSeg: number ex: 0; validade: number ex: 0; valMinima: number ex: 0; marcado: string ex: "S ou N"; bloqueado: string ex: "S ou N"; margem: number ex: 0; margemMin: number ex: 0; comissao: number ex: 0; difCusto: number ex: 0; difVenda: number ex: 0; emb: string; qEmb: number ex: 0; etqMag: string; tpAltPrVenda: string; difCusto1: number ex: 0; difCusto2: number ex: 0; difCusto3: number ex: 0; difCusto4: number ex: 0; difCusto5: number ex: 0; difVenda1: number ex: 0; difVenda2: number ex: 0; difVenda3: number ex: 0; difVenda4: number ex: 0; difVenda5: number ex: 0; fAquisicao: string; frentes: number ex: 0; codigoSim: string; margem3: number ex: 0; margem4: number ex: 0; margem5: number ex: 0; etiquetas: string; sensCodigo: number ex: 0; estAbastMin: number ex: 0; compCodigo: string; vmd: number ex: 0; extra1: string; extra2: string; extra3: string; extra4: number ex: 0; extra5: number ex: 0; extra6: number ex: 0; extra7: number ex: 0; extra8: number ex: 0; extra9: number ex: 0; extra10: string; extra11: string; extra12: string; extra13: string; extra14: string; extra15: string; extra16: string; extra17: string; extra18: string; extra19: string; extra20: string; extra21: string; extra22: string; extra23: string; extra24: string; extra25: string; extra26: string; extra27: string; extra28: string; extra29: string; extra30: string; extra31: string; extra32: string; extra33: string; extra34: string; extra35: string; extra36: string; extra37: string; extra38: string; extra39: string; extra40: string; extra41: string; extra42: string; extra43: string; extra44: string; extra45: string; extra46: string; extra47: string; extra48: string; extra49: string; extra50: string; extra51: string; extra52: string; extra53: string; extra54: string; extra55: string; extra56: string; extra57: string; extra58: string; extra59: string; extra60: string; extra61: string; extra62: string; extra63: string; extra64: string; extra65: string; extra66: string; extra67: string; extra68: string; extra69: string; extra70: string; extra71: string; extra72: string; extra73: string; extra74: string; extra75: string; extra76: string; extra77: string; extra78: string; extra79: string; extra80: string; extra81: string; extra82: string; extra83: string; extra84: string; extra85: string; extra86: string; extra87: string; extra88: string; extra89: string; extra90: string; extra91: string; extra92: string; extra93: string; extra94: string; extra95: string; extra96: string; extra97: string; extra98: string; extra99: string; eraseExtras: array de any }

## v1_0_produtounidade_codigo_unidade_cnpjOrCodigo_response

{ response: object { status, appVersion, messages, content } }

## vdonlineLUndPdv

array de { codigo: string(string) ex: "201"; unidade: string(string) ex: "001" }

## vdonlineLVdPdv

array de { unidade: string(string) ex: "001"; cupom: string(string) ex: "000001"; codigoPDV: string(string) ex: "201"; dataMovimento: string(string) ex: "03/02/2020"; itens: `vdonlineLVdPdvItems` (ver reference/schemas.md) }

## vdonlineLVdPdvItems

array de { unidade: string(string) ex: "001"; cupom: string(string) ex: "000001"; codigoBarras: string(string) ex: ""; codigoProduto: number ex: 10111; codigoPDV: string(string) ex: "201"; dataMovimento: string(string) ex: "03/02/2020"; hora: string(string) ex: "163801"; status: string(string) ex: "N"; quantidade: number ex: 6; valor: number ex: 2; desconto: number ex: 0; tipoRegistro: string(string) ex: "IT" }

## vdonlineLVdPdvItems_V_1_1

array de { unidade: string(string) ex: "001"; cupom: string(string) ex: "000001"; codigoBarras: string(string) ex: ""; codigoProduto: number ex: 10111; codigoPDV: string(string) ex: "201"; dataMovimento: string(string) ex: "03/02/2020"; hora: string(string) ex: "163801"; status: string(string) ex: "N"; quantidade: number ex: 6; valor: number ex: 2; desconto: number ex: 0; tipoRegistro: string(string) ex: "IT"; icmsValor: number ex: 0.0; pisValor: number ex: 0.0; cofinsValor: number ex: 0.0; fcpValor: number ex: 0.0; custoEntrada: number ex: 0.0; custoSaida: number ex: 0.0 }

## vdonlineLVdPdvItems_V_1_2

array de { unidade: string(string) ex: "001"; cupom: string(string) ex: "000001"; codigoBarras: string(string) ex: ""; codigoProduto: number ex: 10111; codigoPDV: string(string) ex: "201"; dataMovimento: string(string) ex: "03/02/2020"; hora: string(string) ex: "163801"; status: string(string) ex: "N"; quantidade: number ex: 6; valor: number ex: 2; desconto: number ex: 0; tipoRegistro: string(string) ex: "IT"; icmsValor: number ex: 0.0; pisValor: number ex: 0.0; cofinsValor: number ex: 0.0; fcpValor: number ex: 0.0; custoEntrada: number ex: 0.0; custoSaida: number ex: 0.0; operador: string ex: "01" }

## vdonlineLVdPdvItems_V_1_3

array de { unidade: string(string) ex: "001"; cupom: string(string) ex: "000001"; codigoBarras: string(string) ex: ""; codigoProduto: number ex: 10111; codigoPDV: string(string) ex: "201"; dataMovimento: string(string) ex: "03/02/2020"; hora: string(string) ex: "163801"; status: string(string) ex: "N"; quantidade: number ex: 6; valor: number ex: 2; desconto: number ex: 0; tipoRegistro: string(string) ex: "IT"; icmsValor: number ex: 0.0; pisValor: number ex: 0.0; cofinsValor: number ex: 0.0; fcpValor: number ex: 0.0; custoEntrada: number ex: 0.0; custoSaida: number ex: 0.0; operador: string ex: "01"; sequencial: number ex: 102; cupomReferenciado: string ex: "100002"; codigoAgenda: number ex: 10 }

## vdonlineLVdPdvItems_V_1_5

array de { codigoBarras: string(string) ex: ""; codigoProduto: number ex: 10111; hora: string(string) ex: "163801"; status: string(string) ex: "N"; quantidade: number ex: 6; valor: number ex: 2; desconto: number ex: 0; tipoRegistro: string(string) ex: "IT"; icmsValor: number ex: 0.0; pisValor: number ex: 0.0; cofinsValor: number ex: 0.0; fcpValor: number ex: 0.0; custoEntrada: number ex: 0.0; custoSaida: number ex: 0.0; operador: string ex: "01"; sequencial: number ex: 102; cupomReferenciado: string ex: "100002"; codigoAgenda: number ex: 10; acrescimo: number ex: 0; imcsBc: number ex: 0; icmsAliq: number ex: 0; pisBc: number ex: 0; pisAliq: number ex: 0; cofinsBc: number ex: 0; cofinsAliq: number ex: 0; fcpBc: number ex: 0; fcpAliq: number ex: 0; cfop: string(string) ex: ""; icmsCST: string(string) ex: ""; pisCST: string(string) ex: ""; cofinsCST: string(string) ex: "" }

## vdonlineLVdPdv_V_1_1

array de { unidade: string(string) ex: "001"; cupom: string(string) ex: "000001"; codigoPDV: string(string) ex: "201"; dataMovimento: string(string) ex: "03/02/2020"; itens: `vdonlineLVdPdvItems_V_1_1` (ver reference/schemas.md) }

## vdonlineLVdPdv_V_1_2

array de { unidade: string(string) ex: "001"; cupom: string(string) ex: "000001"; codigoPDV: string(string) ex: "201"; dataMovimento: string(string) ex: "03/02/2020"; itens: `vdonlineLVdPdvItems_V_1_2` (ver reference/schemas.md) }

## vdonlineLVdPdv_V_1_3

array de { unidade: string(string) ex: "001"; cupom: string(string) ex: "000001"; codigoPDV: string(string) ex: "201"; dataMovimento: string(string) ex: "03/02/2020"; itens: `vdonlineLVdPdvItems_V_1_3` (ver reference/schemas.md) }

## vdonlineLVdPdv_V_1_4

array de { unidade: string(string) ex: "001"; cupom: string(string) ex: "000001"; codigoPDV: string(string) ex: "201"; dataMovimento: string(string) ex: "03/02/2020"; cnpjCpf: string ex: "99999999999"; cnpjCpfCrm: string ex: "99999999999"; itens: `vdonlineLVdPdvItems_V_1_3` (ver reference/schemas.md) }

## vdonlineLVdPdv_V_1_5

array de { codigo: integer ex: "1001"; unidade: string(string) ex: "001"; cupom: string(string) ex: "000001"; codigoPDV: string(string) ex: "201"; dataMovimento: string(string) ex: "03/02/2020"; cnpjCpf: string ex: "99999999999"; cnpjCpfCrm: string ex: "99999999999"; cupomRef: string ex: "000002"; itens: `vdonlineLVdPdvItems_V_1_5` (ver reference/schemas.md) }

## vdonlineUndPdv

{ response: object { status, message, messages, pdvs } }

## vdonlineVdPdv

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, pdvs } }

## vdonlineVdPdvFi_V_1_3

{ response: object { status, messages, vendasOnlineFi } }

## vdonlineVdPdv_V_1_1

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, pdvs } }

## vdonlineVdPdv_V_1_2

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, pdvs } }

## vdonlineVdPdv_V_1_3

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, pdvs } }

## vdonlineVdPdv_V_1_4

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, message, messages, pdvs } }

## vdonlineVdPdv_V_1_5

Quando o atributo "status" do objeto "response" for igual a "ok" ocorreu tudo bem na execução do método, caso contrário ocorreu algum erro, e deve ser avaliado o atributo "messages"
que é uma lista de problemas ou alertas de processamento.

{ response: object { status, messages, cupons } }
