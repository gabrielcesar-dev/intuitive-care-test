# Teste de Banco de Dados - Intuitive Care

## Visão Geral

Este projeto foi desenvolvido como parte de um teste técnico para processar e analisar dados fornecidos pela **ANS (Agência Nacional de Saúde Suplementar)**. O objetivo principal é importar, estruturar e consultar dados relacionados às operadoras de saúde e suas demonstrações contábeis.

---

## Funcionalidades

- **Criação de Estrutura de Banco de Dados**:
  - Tabelas para armazenar informações das operadoras e suas demonstrações contábeis.
  - Índices para otimizar consultas frequentes.

- **Importação de Dados**:
  - Importa dados de arquivos CSV para as tabelas do banco de dados.
  - Valida e filtra registros antes de inseri-los na tabela final.

- **Consultas SQL**:
  - Identifica as 10 operadoras com maiores despesas em categorias específicas, tanto trimestralmente quanto anualmente.

---

## Pré-requisitos

Certifique-se de ter os seguintes itens instalados no seu sistema:

- **PostgreSQL** versão 10.0 ou superior.
- Acesso ao terminal ou ferramenta de gerenciamento de banco de dados compatível com PostgreSQL.
- Arquivos CSV baixados dos links fornecidos na seção "Tarefas de Preparação."

---

## Tarefas de Preparação

1. **Baixar Arquivos**:
   - Baixe os arquivos dos últimos 2 anos do repositório público:  
     [Demonstrativos Contábeis](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/)
   - Baixe os dados cadastrais das operadoras ativas no formato CSV:  
     [Operadoras Ativas](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/)

---

## Tarefas de Código

1. **Estruturar Tabelas**:
   - Utilize o script `schema.sql` para criar as tabelas necessárias para armazenar os dados dos arquivos CSV.

2. **Importar Dados**:
   - Utilize o script `import.sql` para importar o conteúdo dos arquivos preparados, garantindo o encoding correto.

3. **Consultas Analíticas**:
   - Utilize o script `queries.sql` para responder às seguintes perguntas:
     - Quais as 10 operadoras com maiores despesas em "EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE MÉDICO HOSPITALAR" no último trimestre?
     - Quais as 10 operadoras com maiores despesas nessa categoria no último ano?

---

## Estrutura do Projeto

```
test-3/
├── schema.sql       # Script para criação das tabelas e índices do banco de dados
├── import.sql       # Script para importar os dados dos arquivos CSV
├── queries.sql      # Script para executar as consultas analíticas
├── input/           # Diretório contendo os arquivos CSV de entrada
│   ├── Relatorio_cadop.csv  # Dados cadastrais das operadoras
│   ├── 1T2023.csv           # Demonstrativos contábeis do 1º trimestre de 2023
│   ├── 2T2023.csv           # Demonstrativos contábeis do 2º trimestre de 2023
│   ├── 3T2023.csv           # Demonstrativos contábeis do 3º trimestre de 2023
│   ├── 4T2023.csv           # Demonstrativos contábeis do 4º trimestre de 2023
│   ├── 1T2024.csv           # Demonstrativos contábeis do 1º trimestre de 2024
│   ├── 2T2024.csv           # Demonstrativos contábeis do 2º trimestre de 2024
│   ├── 3T2024.csv           # Demonstrativos contábeis do 3º trimestre de 2024
│   └── 4T2024.csv           # Demonstrativos contábeis do 4º trimestre de 2024
└── README.md        # Documentação do projeto
```

---

## Uso

### Passos

1. Certifique-se de que o PostgreSQL está instalado e em execução no seu sistema.
2. Crie um banco de dados para o projeto:

   ```sql
   CREATE DATABASE intuitive_care;
   ```

3. Execute o script `schema.sql` para criar as tabelas e índices:

   ```bash
   psql -d intuitive_care -f schema.sql
   ```

4. Importe os dados utilizando o script `import.sql`:

   ```bash
   psql -d intuitive_care -f import.sql
   ```

5. Execute as consultas analíticas utilizando o script `queries.sql`:

   ```bash
   psql -d intuitive_care -f queries.sql
   ```

---

## Notas

1. **Formato Internacional**:
   - Os arquivos CSV já estão convertidos para o padrão internacional, utilizando ponto como separador decimal. Não é necessário realizar nenhuma conversão adicional.

2. **Uso de Tabela Temporária**:
   - Durante a importação, é utilizada uma tabela temporária (`tmp_demonstracoes_contabeis`) para lidar com inconsistências nos dados. Apenas os registros válidos (com `reg_ans` correspondente na tabela `operadoras`) são inseridos na tabela final.

---

## Licença

Este script está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

---

## Autor

### Gabriel Cesar Silvino Xavier

Sinta-se à vontade para entrar em contato para dúvidas ou feedback!
