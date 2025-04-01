-- Importa os dados das operadoras
\copy operadoras FROM 'input/Relatorio_cadop.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';

-- Cria a tabela temporária para armazenar os dados das demonstrações contábeis
-- A tabela temporária é necessária porque alguns registros podem não ter uma operadora correspondente na tabela 'operadoras'.
-- Isso permite validar e filtrar os dados antes de inseri-los na tabela final.
DROP TABLE IF EXISTS tmp_demonstracoes_contabeis;
CREATE TEMP TABLE tmp_demonstracoes_contabeis (
    id                serial primary key,
    data              date,
    reg_ans           varchar(20),
    cd_conta_contabil varchar(20),
    descricao         text,
    vl_saldo_inicial  numeric(15,2),
    vl_saldo_final    numeric(15,2)
);

-- Importa todos os arquivos para a tabela temporária
\copy tmp_demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'input/1T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\copy tmp_demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'input/2T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\copy tmp_demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'input/3T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\copy tmp_demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'input/4T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\copy tmp_demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'input/1T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\copy tmp_demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'input/2T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\copy tmp_demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'input/3T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\copy tmp_demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'input/4T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';

-- Insere na tabela final somente os registros válidos (com reg_ans existente em operadoras)
INSERT INTO demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
SELECT t.data, t.reg_ans, t.cd_conta_contabil, t.descricao, t.vl_saldo_inicial, t.vl_saldo_final
FROM tmp_demonstracoes_contabeis t
WHERE t.reg_ans IN (SELECT registro_ans FROM operadoras);

-- Exclui a tabela temporária, se desejado
DROP TABLE tmp_demonstracoes_contabeis;
