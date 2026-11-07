# Schema do banco `erp` (somente leitura, mapeado automaticamente)

91 tabela(s) e 0 view(s) no schema `public`. Gerado por `scripts/mapear_banco.py`. Contagem de linhas é estimativa (`pg_class.reltuples`, não `COUNT(*)` — evita sobrecarregar o banco com full scan). Nenhuma linha de dado real foi lida — só metadado de schema (`information_schema`/`pg_catalog`).

| Tabela | ~Linhas |
|---|---|
| [attributesml](#attributesml) | 0 |
| [auditwms](#auditwms) | 0 |
| [caractprod](#caractprod) | 0 |
| [congeventos](#congeventos) | 0 |
| [congeventosvinc](#congeventosvinc) | 0 |
| [conglomerados](#conglomerados) | 0 |
| [congplano](#congplano) | 0 |
| [congplanovinc](#congplanovinc) | 0 |
| [congposicao](#congposicao) | 0 |
| [congregelim](#congregelim) | 0 |
| [congregelimcontrap](#congregelimcontrap) | 0 |
| [deparaautorizadores](#deparaautorizadores) | 0 |
| [entcontager](#entcontager) | 445 |
| [etiqcpaletes](#etiqcpaletes) | 0 |
| [etiqdpaletes](#etiqdpaletes) | 0 |
| [filestorage](#filestorage) | 0 |
| [impressoraswms](#impressoraswms) | 0 |
| [lotetarefaws](#lotetarefaws) | 8 |
| [movdivergmonit](#movdivergmonit) | 22387 |
| [pickdinwms](#pickdinwms) | 0 |
| [presprodcadastro](#presprodcadastro) | 0 |
| [presprodcoleta](#presprodcoleta) | 0 |
| [regcompllancprodd](#regcompllancprodd) | 0 |
| [reglancprodd0120](#reglancprodd0120) | 0 |
| [reglancprodd0121](#reglancprodd0121) | 0 |
| [reglancprodd0122](#reglancprodd0122) | 0 |
| [reglancprodd0123](#reglancprodd0123) | 0 |
| [reglancprodd0124](#reglancprodd0124) | 0 |
| [reglancprodd0220](#reglancprodd0220) | 0 |
| [reglancprodd0221](#reglancprodd0221) | 0 |
| [reglancprodd0222](#reglancprodd0222) | 0 |
| [reglancprodd0223](#reglancprodd0223) | 0 |
| [reglancprodd0224](#reglancprodd0224) | 0 |
| [reglancprodd0320](#reglancprodd0320) | 0 |
| [reglancprodd0321](#reglancprodd0321) | 0 |
| [reglancprodd0322](#reglancprodd0322) | 0 |
| [reglancprodd0323](#reglancprodd0323) | 0 |
| [reglancprodd0324](#reglancprodd0324) | 0 |
| [reglancprodd0420](#reglancprodd0420) | 0 |
| [reglancprodd0421](#reglancprodd0421) | 0 |
| [reglancprodd0422](#reglancprodd0422) | 0 |
| [reglancprodd0423](#reglancprodd0423) | 0 |
| [reglancprodd0424](#reglancprodd0424) | 0 |
| [reglancprodd0520](#reglancprodd0520) | 0 |
| [reglancprodd0521](#reglancprodd0521) | 0 |
| [reglancprodd0522](#reglancprodd0522) | 0 |
| [reglancprodd0523](#reglancprodd0523) | 0 |
| [reglancprodd0524](#reglancprodd0524) | 0 |
| [reglancprodd0620](#reglancprodd0620) | 0 |
| [reglancprodd0621](#reglancprodd0621) | 0 |
| [reglancprodd0622](#reglancprodd0622) | 0 |
| [reglancprodd0623](#reglancprodd0623) | 0 |
| [reglancprodd0624](#reglancprodd0624) | 0 |
| [reglancprodd0720](#reglancprodd0720) | 0 |
| [reglancprodd0721](#reglancprodd0721) | 0 |
| [reglancprodd0722](#reglancprodd0722) | 0 |
| [reglancprodd0723](#reglancprodd0723) | 0 |
| [reglancprodd0724](#reglancprodd0724) | 0 |
| [reglancprodd0820](#reglancprodd0820) | 0 |
| [reglancprodd0821](#reglancprodd0821) | 0 |
| [reglancprodd0822](#reglancprodd0822) | 0 |
| [reglancprodd0823](#reglancprodd0823) | 0 |
| [reglancprodd0824](#reglancprodd0824) | 0 |
| [reglancprodd0920](#reglancprodd0920) | 0 |
| [reglancprodd0921](#reglancprodd0921) | 0 |
| [reglancprodd0922](#reglancprodd0922) | 0 |
| [reglancprodd0923](#reglancprodd0923) | 0 |
| [reglancprodd0924](#reglancprodd0924) | 0 |
| [reglancprodd1020](#reglancprodd1020) | 0 |
| [reglancprodd1021](#reglancprodd1021) | 0 |
| [reglancprodd1022](#reglancprodd1022) | 0 |
| [reglancprodd1023](#reglancprodd1023) | 0 |
| [reglancprodd1024](#reglancprodd1024) | 0 |
| [reglancprodd1120](#reglancprodd1120) | 0 |
| [reglancprodd1121](#reglancprodd1121) | 0 |
| [reglancprodd1122](#reglancprodd1122) | 0 |
| [reglancprodd1123](#reglancprodd1123) | 0 |
| [reglancprodd1124](#reglancprodd1124) | 0 |
| [reglancprodd1220](#reglancprodd1220) | 0 |
| [reglancprodd1221](#reglancprodd1221) | 0 |
| [reglancprodd1222](#reglancprodd1222) | 0 |
| [reglancprodd1223](#reglancprodd1223) | 0 |
| [reglancprodd1224](#reglancprodd1224) | 0 |
| [regrascontabfde](#regrascontabfde) | 0 |
| [regraslctofde](#regraslctofde) | 0 |
| [regrastxpix](#regrastxpix) | 0 |
| [shippcadastro](#shippcadastro) | 0 |
| [shipplog](#shipplog) | 0 |
| [tarefasetq](#tarefasetq) | 0 |
| [tribanuncioml](#tribanuncioml) | 0 |
| [ususenhashist](#ususenhashist) | 220 |

## Detalhe por tabela

### `attributesml` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| atml_codigo | numeric(8,0) | não |  |  |  |
| atml_caml_codigo | numeric(8,0) | não |  |  |  |
| atml_anml_codigo | numeric(8,0) | não |  |  |  |
| atml_id | character varying(60) | não |  |  |  |
| atml_name | character varying(80) | não |  |  |  |
| atml_value | character varying(80) | sim |  |  |  |
| atml_attribute_group_id | character varying(20) | sim |  |  |  |
| atml_attribute_group_name | character varying(20) | sim |  |  |  |

### `auditwms` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| audw_opew_codigo | numeric(8,0) | sim |  |  |  |
| audw_unid_codigo | character varying(3) | sim |  |  |  |
| audw_setores | character varying(400) | sim |  |  |  |
| audw_zonas | character varying(400) | sim |  |  |  |
| audw_ruas | character varying(400) | sim |  |  |  |
| audw_niveis | character varying(20) | sim |  |  |  |
| audw_auditar | character varying(1) | sim |  |  |  |
| audw_reauditar | character varying(1) | sim |  |  |  |
| audw_ativo | character varying(1) | sim |  |  |  |

### `caractprod` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| carp_codigo | character varying(4) | sim |  |  |  |
| carp_descricao | character varying(50) | sim |  |  |  |

### `congeventos` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| cnev_cong_codigo | character varying(2) | não |  |  |  |
| cnev_codigo | numeric(10,0) | não |  |  |  |
| cnev_status | character varying(1) | não |  |  |  |
| cnev_empr_codigo | character varying(2) | não |  |  |  |
| cnev_data | date | não |  |  |  |
| cnev_tipo | character varying(1) | não |  |  |  |

### `congeventosvinc` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| cevv_codigo | numeric(10,0) | não |  |  |  |
| cevv_empr_codigo | character varying(2) | não |  |  |  |
| cevv_condicao | character varying(1) | não |  |  |  |
| cevv_percempresa | numeric(7,4) | sim |  |  |  |
| cevv_status | character varying(1) | não |  |  |  |

### `conglomerados` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| cong_codigo | character varying(2) | não |  |  |  |
| cong_nome | character varying(60) | sim |  |  |  |

### `congplano` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| copc_conta | numeric(8,0) | não |  |  |  |
| copc_classificacao | character varying(20) | não |  |  |  |
| copc_descricao | character varying(100) | não |  |  |  |
| copc_tipo | character varying(2) | não |  |  |  |
| copc_natureza | character varying(2) | sim |  |  |  |
| copc_cong_codigo | character varying(2) | não |  |  |  |

### `congplanovinc` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| copv_cong_codigo | character varying(2) | não |  |  |  |
| copv_copc_conta | numeric(8,0) | não |  |  |  |
| copv_empr_codigo | character varying(2) | não |  |  |  |
| copv_pcon_conta | numeric(8,0) | não |  |  |  |

### `congposicao` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| cnpo_cong_codigo | character varying(2) | não |  |  |  |
| cnpo_dataref | date | não |  |  |  |
| cnpo_empr_codigo | character varying(2) | não |  |  |  |
| cnpo_percpartemp | numeric(7,4) | sim |  |  |  |
| cnpo_percconsolidado | numeric(7,4) | sim |  |  |  |

### `congregelim` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| crel_cong_codigo | character varying(2) | não |  |  |  |
| crel_codigo | numeric(10,0) | não |  |  |  |
| crel_status | character varying(1) | não |  |  |  |
| crel_dataref | date | não |  |  |  |
| crel_empr_codigo | character varying(2) | não |  |  |  |
| crel_valor | numeric(12,2) | não |  |  |  |
| crel_dc | character varying(1) | não |  |  |  |

### `congregelimcontrap` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| crep_crel_codigo | numeric(10,0) | não |  |  |  |
| crep_empr_codigo | character varying(2) | não |  |  |  |
| crep_copc_conta | numeric(8,0) | não |  |  |  |
| crep_valor | numeric(12,2) | não |  |  |  |
| crep_dc | character varying(1) | não |  |  |  |
| crep_status | character varying(1) | não |  |  |  |

### `deparaautorizadores` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| dpat_codigo | numeric(7,0) | não |  |  |  |
| dpat_tef | character varying(20) | não |  |  |  |
| dpat_autt_codigo | numeric(3,0) | não |  |  |  |
| dpat_codigodepara | character varying(500) | sim |  |  |  |

### `entcontager` (~445 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| ecge_codentidade | numeric(8,0) | não |  |  |  |
| ecge_pger_conta | numeric(8,0) | não |  |  |  |
| ecge_fpgt_codigo | character varying(3) | sim |  |  |  |
| ecge_lpgt_codigo | character varying(3) | sim |  |  |  |
| ecge_portadores | character varying(300) | sim |  |  |  |
| ecge_espe_codigo | character varying(4) | sim |  |  |  |
| ecge_unidades | character varying(200) | sim |  |  |  |
| ecge_formaspgto | character varying(200) | sim |  |  |  |
| ecge_locaispgto | character varying(200) | sim |  |  |  |
| ecge_port_codigo | character varying(3) | sim |  |  |  |
| ecge_especies | character varying(200) | sim |  |  |  |

### `etiqcpaletes` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| etcp_etiqueta | character varying(13) | sim |  |  |  |
| etcp_pcar_numero | character varying(9) | sim |  |  |  |
| etcp_unid_codigo | character varying(3) | sim |  |  |  |
| etcp_unid_wms | character varying(3) | sim |  |  |  |
| etcp_rota_codigo | character varying(3) | sim |  |  |  |
| etcp_data | date | sim |  |  |  |
| etcp_hora | character varying(8) | sim |  |  |  |
| etcp_tran_codigo | character varying(5) | sim |  |  |  |
| etcp_status | character varying(1) | sim |  |  |  |
| etcp_usua_codigo | numeric(5,0) | sim |  |  |  |
| etcp_avulsa | character varying(1) | sim |  |  |  |
| etcp_peso | numeric(10,0) | sim |  |  |  |
| etcp_volume | numeric(10,3) | sim |  |  |  |
| etcp_viaw_numero | numeric(8,0) | sim |  |  |  |
| etcp_unid_destino | character varying(3) | sim |  |  |  |
| etcp_nrocaixas | numeric(4,0) | sim |  |  |  |
| etcp_dcto | character varying(1000) | sim |  |  |  |

### `etiqdpaletes` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| etdp_etiqueta | character varying(13) | sim |  |  |  |
| etdp_carregamento | numeric(10,0) | sim |  |  |  |
| etdp_palete | numeric(4,0) | sim |  |  |  |
| etdp_data | date | sim |  |  |  |
| etdp_hora | character varying(8) | sim |  |  |  |
| etdp_status | character varying(1) | sim |  |  |  |
| etdp_tarefa | character varying(9) | sim |  |  |  |

### `filestorage` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| fsto_codigo | numeric(15,0) | não |  |  |  |
| fsto_datacriacao | timestamp without time zone | não |  |  |  |
| fsto_datamodificacao | timestamp without time zone | sim |  |  |  |
| fsto_extensaoarquivo | character varying(10) | não |  |  |  |
| fsto_nomearquivo | character varying(400) | não |  |  |  |
| fsto_signature | character varying(100) | não |  |  |  |
| fsto_status | character varying(1) | não |  |  |  |
| fsto_storageid | character varying(100) | não |  |  |  |
| fsto_ufor_codigo | numeric(12,0) | não |  |  |  |
| fsto_url | character varying(3000) | não |  |  |  |

### `impressoraswms` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| impw_unid_codigo | character varying(3) | sim |  |  |  |
| impw_etiq_codigo | numeric(6,0) | não |  |  |  |
| impw_etiq_tipo | character varying(2) | sim |  |  |  |
| impw_nome | character varying(100) | não |  |  |  |
| impw_caminho | character varying(200) | sim |  |  |  |
| impw_descricao | character varying(60) | sim |  |  |  |
| impw_tipo | character varying(2) | não |  |  |  |
| impr_endereco | character varying(20) | não |  |  |  |
| impr_porta | character varying(5) | não |  |  |  |
| impw_endereco | character varying(20) | não |  |  |  |
| impw_porta | character varying(5) | não |  |  |  |

### `lotetarefaws` (~8 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| ltws_codigo | numeric(15,0) | não |  |  |  |
| ltws_datacriacao | timestamp without time zone | não |  |  |  |
| ltws_ufor_codigo | numeric(12,0) | não |  |  |  |
| ltws_status | character varying(1) | não |  |  |  |
| ltws_resposta | text | não |  |  |  |

### `movdivergmonit` (~22387 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| modv_dcto_tipo | character varying(3) | sim |  |  |  |
| modv_dcto_codigo | character varying(4) | sim |  |  |  |
| modv_status | character varying(1) | sim |  |  |  |
| modv_statusret | character varying(2) | sim |  |  |  |
| modv_datahora | timestamp without time zone | sim |  |  |  |
| modv_unid_codigo | character varying(3) | sim |  |  |  |
| modv_catentidade | character varying(1) | sim |  |  |  |
| modv_codentidade | numeric(8,0) | sim |  |  |  |
| modv_codusu | numeric(5,0) | sim |  |  |  |
| modv_nomeusu | character varying(30) | sim |  |  |  |
| modv_codusuaut | numeric(5,0) | sim |  |  |  |
| modv_codusumonit | numeric(5,0) | sim |  |  |  |
| modv_datahoramonit | timestamp without time zone | sim |  |  |  |
| modv_numped | numeric(18,0) | sim |  |  |  |
| modv_numnf | numeric(10,0) | sim |  |  |  |
| modv_comp_codigo | character varying(3) | sim |  |  |  |
| modv_prod_codigo | numeric(8,0) | sim |  |  |  |
| modv_tpdiverg | character varying(2) | sim |  |  |  |
| modv_diverg | character varying(200) | sim |  |  |  |
| modv_msgret | character varying(200) | sim |  |  |  |
| modv_datahoraaut | timestamp without time zone | sim |  |  |  |
| modv_origem | character varying(20) | sim |  |  |  |
| modv_tarefa | character varying(20) | sim |  |  |  |
| modv_idsnfe | character varying(4000) | sim |  |  |  |
| modv_codigo | numeric(10,0) | sim |  |  |  |
| modv_idnfe | character varying(44) | sim |  |  |  |
| modv_observacao | character varying(200) | sim |  |  |  |
| modv_qtdefis | numeric(12,3) | sim |  |  |  |
| modv_qtdemov | numeric(12,3) | sim |  |  |  |
| modv_contag1 | numeric(12,3) | sim |  |  |  |
| modv_contag2 | numeric(12,3) | sim |  |  |  |
| modv_contag3 | numeric(12,3) | sim |  |  |  |
| modv_contag4 | numeric(12,3) | sim |  |  |  |
| modv_contag5 | numeric(12,3) | sim |  |  |  |
| modv_numnfsdevolver | character varying(200) | sim |  |  |  |
| modv_custoxml | numeric(12,3) | sim |  |  |  |
| modv_custoped | numeric(12,3) | sim |  |  |  |
| modv_identificador | character varying(30) | sim |  |  |  |

### `pickdinwms` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| picd_codigo | numeric(5,0) | sim |  |  |  |
| picd_unid_codigo | character varying(3) | sim |  |  |  |
| picd_grupos | character varying(800) | sim |  |  |  |
| picd_enderecoi | character varying(9) | sim |  |  |  |
| picd_enderecof | character varying(9) | sim |  |  |  |
| picd_capacidade | numeric(12,3) | sim |  |  |  |
| picd_minimo | numeric(12,3) | sim |  |  |  |
| picd_status | character varying(1) | sim |  |  |  |

### `presprodcadastro` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| ppcd_cnpj | character varying(14) | não |  |  |  |
| ppcd_codigo | numeric(8,0) | não |  |  |  |
| ppcd_descricao | character varying(100) | não |  |  |  |
| ppcd_complemento | character varying(40) | sim |  |  |  |
| ppcd_marca | character varying(30) | sim |  |  |  |
| ppcd_codbarras | character varying(13) | não |  |  |  |

### `presprodcoleta` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| ppcl_cnpj | character varying(14) | não |  |  |  |
| ppcl_codbarras | character varying(14) | não |  |  |  |

### `regcompllancprodd` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rclp_operacao | character varying(22) | não |  |  |  |
| rclp_transacao | character varying(16) | não |  |  |  |
| rclp_sequencial | numeric(8,0) | não |  |  |  |
| rclp_isscodmunfg | character varying(7) | sim |  |  |  |
| rclp_isscodlistaserv | character varying(5) | sim |  |  |  |
| rclp_issdeducaovalor | numeric(12,2) | sim |  |  |  |
| rclp_issoutretvalor | numeric(12,2) | sim |  |  |  |
| rclp_issdescincondvalor | numeric(12,2) | sim |  |  |  |
| rclp_issdesccondvalor | numeric(12,2) | sim |  |  |  |
| rclp_issretvalor | numeric(12,2) | sim |  |  |  |
| rclp_issindexigencia | character varying(1) | sim |  |  |  |
| rclp_isscodservmun | character varying(20) | sim |  |  |  |
| rclp_isscodmunincid | character varying(7) | sim |  |  |  |
| rclp_isscodpais | character varying(4) | sim |  |  |  |
| rclp_issprocessonumero | character varying(30) | sim |  |  |  |
| rclp_issindincentivo | character varying(1) | sim |  |  |  |
| rclp_infadprod | character varying(500) | sim |  |  |  |

### `reglancprodd0120` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | não |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0121` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0122` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0123` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0124` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0220` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | não |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0221` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0222` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0223` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0224` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0320` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | não |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0321` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0322` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0323` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0324` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0420` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | não |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0421` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0422` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0423` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0424` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0520` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | não |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0521` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0522` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0523` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0524` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0620` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | não |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0621` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0622` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0623` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0624` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0720` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | não |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0721` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0722` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0723` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0724` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0820` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | não |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0821` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0822` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0823` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0824` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0920` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | não |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0921` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0922` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0923` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd0924` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd1020` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | não |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd1021` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd1022` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd1023` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd1024` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd1120` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | não |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd1121` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd1122` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd1123` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd1124` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd1220` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | não |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd1221` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd1222` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd1223` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `reglancprodd1224` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlpd_operacao | character varying(22) | não |  |  |  |
| rlpd_transacao | character varying(16) | não |  |  |  |
| rlpd_unid_codigo | character varying(3) | não |  |  |  |
| rlpd_datamvto | date | não |  |  |  |
| rlpd_status | character varying(1) | não |  |  |  |
| rlpd_sequencial | numeric(8,0) | não |  |  |  |
| rlpd_prod_codigo | numeric(8,0) | sim |  |  |  |
| rlpd_mprd_sequencial | numeric(8,0) | sim |  |  |  |
| rlpd_codigoitem | character varying(60) | sim |  |  |  |
| rlpd_codigoncm | character varying(10) | sim |  |  |  |
| rlpd_cfop | character varying(4) | sim |  |  |  |
| rlpd_cest | character varying(7) | sim |  |  |  |
| rlpd_benefcodigo | character varying(10) | sim |  |  |  |
| rlpd_extipi | character varying(3) | sim |  |  |  |
| rlpd_embcom | character varying(6) | sim |  |  |  |
| rlpd_embtrib | character varying(6) | sim |  |  |  |
| rlpd_qtdecom | numeric(15,4) | sim |  |  |  |
| rlpd_qtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_valor | numeric(12,2) | sim |  |  |  |
| rlpd_fretevalor | numeric(12,2) | sim |  |  |  |
| rlpd_segurovalor | numeric(12,2) | sim |  |  |  |
| rlpd_descvalor | numeric(12,2) | sim |  |  |  |
| rlpd_despacvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmscst | character varying(3) | sim |  |  |  |
| rlpd_icmsmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmspercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsvalorop | numeric(12,2) | sim |  |  |  |
| rlpd_icmspercdif | numeric(7,4) | sim |  |  |  |
| rlpd_icmsvalordif | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsdesonmot | numeric(2,0) | sim |  |  |  |
| rlpd_icmsstmodbc | character varying(1) | sim |  |  |  |
| rlpd_icmsstpercmva | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstpercredbc | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_icmsstretvalorsub | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetredbc | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetbc | numeric(12,2) | sim |  |  |  |
| rlpd_icmsstefetaliq | numeric(7,3) | sim |  |  |  |
| rlpd_icmsstefetvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstvalor | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretbc | numeric(12,2) | sim |  |  |  |
| rlpd_fcpstretaliq | numeric(7,4) | sim |  |  |  |
| rlpd_fcpstretvalor | numeric(12,2) | sim |  |  |  |
| rlpd_ipicst | character varying(2) | sim |  |  |  |
| rlpd_ipiindcalculo | character varying(1) | sim |  |  |  |
| rlpd_ipibc | numeric(12,2) | sim |  |  |  |
| rlpd_ipialiq | numeric(7,4) | sim |  |  |  |
| rlpd_ipiqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalorun | numeric(15,4) | sim |  |  |  |
| rlpd_ipivalor | numeric(12,2) | sim |  |  |  |
| rlpd_piscst | character varying(2) | sim |  |  |  |
| rlpd_pisbc | numeric(12,2) | sim |  |  |  |
| rlpd_pisaliq | numeric(7,4) | sim |  |  |  |
| rlpd_pisqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_pisvalor | numeric(12,2) | sim |  |  |  |
| rlpd_cofinscst | character varying(2) | sim |  |  |  |
| rlpd_cofinsbc | numeric(12,2) | sim |  |  |  |
| rlpd_cofinsaliq | numeric(7,4) | sim |  |  |  |
| rlpd_cofinsqtdetrib | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalorun | numeric(15,4) | sim |  |  |  |
| rlpd_cofinsvalor | numeric(12,2) | sim |  |  |  |
| rlpd_issbc | numeric(12,2) | sim |  |  |  |
| rlpd_issaliq | numeric(7,4) | sim |  |  |  |
| rlpd_issvalor | numeric(12,2) | sim |  |  |  |
| rlpd_devolst | numeric(12,2) | sim |  |  |  |
| rlpd_devolfcpst | numeric(12,2) | sim |  |  |  |
| rlpd_devolipi | numeric(12,2) | sim |  |  |  |
| rlpd_devolperc | numeric(6,3) | sim |  |  |  |
| rlpd_inddadosadic | character varying(1) | sim |  |  |  |

### `regrascontabfde` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rcfd_codigo | numeric(8,0) | não |  |  |  |
| rcfd_dcto_codigo | character varying(4) | não |  |  |  |
| rcfd_condgrupos | character varying(4000) | sim |  |  |  |
| rcfd_conddptos | character varying(2000) | sim |  |  |  |
| rcfd_condclasse | text | sim |  |  |  |
| rcfd_condprod | text | sim |  |  |  |
| rcfd_pger_conta | numeric(8,0) | não |  |  |  |

### `regraslctofde` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rlfd_classificacao | character varying(31) | não |  |  |  |
| rlfd_variavel | character varying(2) | não |  |  |  |
| rlfd_avaltipo | character varying(1) | não |  |  |  |
| rlfd_avalvalor | character varying(500) | não |  |  |  |
| rlfd_dcto_codigo | character varying(4) | sim |  |  |  |

### `regrastxpix` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| rpix_codigo | numeric(8,0) | não |  |  |  |
| rpix_pger_conta | numeric(8,0) | não |  |  |  |
| rpix_vlmin | numeric(10,2) | sim |  |  |  |
| rpix_vlmax | numeric(10,2) | sim |  |  |  |
| rpix_unidades | character varying(500) | sim |  |  |  |
| rpix_vp | character varying(1) | não |  |  |  |
| rpix_vlperc | numeric(10,5) | sim |  |  |  |

### `shippcadastro` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| shpc_unid_codigo | character varying(3) | sim |  |  |  |
| shpc_tipo | character varying(1) | não |  |  |  |
| shpc_codigo | numeric(8,0) | não |  |  |  |
| shpc_preco | numeric(15,5) | sim |  |  |  |
| shpc_descricao | character varying(100) | não |  |  |  |

### `shipplog` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| shpl_unid_codigo | character varying(3) | não |  |  |  |
| shpl_tipo | character varying(1) | não |  |  |  |
| shpl_codigo | numeric(8,0) | não |  |  |  |
| shpl_httpcode | character varying(3) | não |  |  |  |
| shpl_dadosenvio | text | não |  |  |  |
| shpl_dadosretorno | text | não |  |  |  |
| shpl_status | character varying(1) | não |  |  |  |

### `tarefasetq` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| tetq_numero | character varying(9) | sim |  |  |  |
| tetq_tipo | character varying(2) | sim |  |  |  |
| tetq_codigo | numeric(3,0) | sim |  |  |  |
| tetq_texto | character varying(2000) | sim |  |  |  |

### `tribanuncioml` (~0 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| taml_codigo | numeric(8,0) | não |  |  |  |
| taml_anml_codigo | numeric(8,0) | não |  |  |  |
| taml_trib_controle | character varying(6) | sim |  |  |  |
| taml_trib_release | numeric(8,0) | sim |  |  |  |

### `ususenhashist` (~220 linhas)

| Coluna | Tipo | Nulo? | Default | PK | FK |
|---|---|---|---|---|---|
| ushi_codigo | numeric(9,0) | não |  |  |  |
| ushi_tipo | numeric(3,0) | não |  |  |  |
| ushi_usua_codigo | numeric(5,0) | não |  |  |  |
| ushi_data | timestamp without time zone | sim |  |  |  |
| ushi_hashsenha | character varying(100) | sim |  |  |  |
| ushi_saltsenha | character varying(50) | sim |  |  |  |
