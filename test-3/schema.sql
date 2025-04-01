-- Tabela para dados de registro das operadoras
create table operadoras (
   registro_ans              varchar(20) primary key,
   cnpj                      varchar(20),
   razao_social              text,
   nome_fantasia             text,
   modalidade                varchar(100),
   logradouro                text,
   numero                    varchar(20),
   complemento               text,
   bairro                    text,
   cidade                    varchar(100),
   uf                        varchar(2),
   cep                       varchar(10),
   ddd                       varchar(5),
   telefone                  varchar(20),
   fax                       varchar(20),
   endereco_eletronico       text,
   representante             text,
   cargo_representante       text,
   regiao_de_comercializacao integer,
   data_registro_ans         date
);

-- Tabela para dados contábeis
create table demonstracoes_contabeis (
   id                serial primary key,
   data              date,
   reg_ans           varchar(20),
   cd_conta_contabil varchar(20),
   descricao         text,
   vl_saldo_inicial  numeric(15,2),
   vl_saldo_final    numeric(15,2),
   foreign key ( reg_ans ) references operadoras ( registro_ans )
);

-- Criação de índices para melhorar o desempenho das buscas
-- Índice para acelerar buscas pelo campo 'reg_ans', utilizado em junções entre as tabelas 'demonstracoes_contabeis' e 'operadoras'
create index idx_reg_ans on
   demonstracoes_contabeis (
      reg_ans
   );

-- Índice para acelerar buscas pelo campo 'data', utilizado em filtros por intervalo de datas, como em consultas trimestrais ou anuais
create index idx_data on
   demonstracoes_contabeis (
      data
   );

-- Índice para acelerar buscas pelo campo 'descricao', utilizado em filtros por categorias específicas de despesas
create index idx_descricao on
   demonstracoes_contabeis (
      descricao
   );
