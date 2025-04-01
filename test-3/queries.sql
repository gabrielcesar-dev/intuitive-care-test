-- Consulta 1: As 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre
-- O último trimestre seria o Q4 2024 (4T2024)
SELECT o.razao_social, o.registro_ans, SUM(dc.vl_saldo_final) as total_despesas
FROM demonstracoes_contabeis dc
JOIN operadoras o ON dc.reg_ans = o.registro_ans
WHERE dc.descricao LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS%DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
  AND dc.data BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY o.razao_social, o.registro_ans
ORDER BY total_despesas DESC
LIMIT 10;

-- Consulta 2: As 10 operadoras com maiores despesas na mesma categoria no último ano
-- O último ano seria todo o ano de 2024 (todos os 4 trimestres)
SELECT o.razao_social, o.registro_ans, SUM(dc.vl_saldo_final) as total_despesas
FROM demonstracoes_contabeis dc
JOIN operadoras o ON dc.reg_ans = o.registro_ans
WHERE dc.descricao LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS%DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
  AND dc.data BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY o.razao_social, o.registro_ans
ORDER BY total_despesas DESC
LIMIT 10;