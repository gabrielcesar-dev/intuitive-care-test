-- Importa dados do arquivo CSV das operadoras - o arquivo se chama Relatorio_cadop.csv no diretório de entrada
COPY operadoras
FROM '/input/Relatorio_cadop.csv' 
DELIMITER ';' 
CSV HEADER
ENCODING 'UTF8';

-- Função para importar todos os arquivos de demonstrações trimestrais de 2023 e 2024
DO $$
DECLARE
    years TEXT[] := ARRAY['2023', '2024'];
    quarters TEXT[] := ARRAY['1T', '2T', '3T', '4T'];
    file_path TEXT;
    year_val TEXT;
    quarter_val TEXT;
BEGIN
    FOREACH year_val IN ARRAY years
    LOOP
        FOREACH quarter_val IN ARRAY quarters
        LOOP
            file_path := '/input/' || quarter_val || year_val || '.csv';
            
            EXECUTE format('
                COPY demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
                FROM %L 
                DELIMITER %L 
                CSV HEADER
                ENCODING %L',
                file_path, ';', 'UTF8'
            );
            
            RAISE NOTICE 'Arquivo importado: %', file_path;
        END LOOP;
    END LOOP;
END $$;