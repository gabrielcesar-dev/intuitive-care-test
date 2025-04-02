# Teste de Transformação de Dados

## Visão Geral

Este script foi desenvolvido para realizar a transformação de dados extraídos de um arquivo PDF fornecido pela **ANS (Agência Nacional de Saúde Suplementar)**. O objetivo é processar as tabelas contidas no PDF e gerar um arquivo estruturado e compactado.

---

## Funcionalidades

- Extrai os dados da tabela **Rol de Procedimentos e Eventos em Saúde** do PDF (Anexo I do teste 1), processando todas as páginas.
- Salva os dados extraídos em um arquivo CSV estruturado.
- Compacta o arquivo CSV gerado em um arquivo ZIP denominado `Teste_{seu_nome}.zip`.
- Substitui as abreviações das colunas:
  - `OD` → **Seg. Odontológica**
  - `AMB` → **Seg. Ambulatorial**

---

## Pré-requisitos

Certifique-se de ter os seguintes itens instalados no seu sistema:
- Python 3.8 ou superior
- `pip` (gerenciador de pacotes do Python)

Instale as bibliotecas Python necessárias executando:
```bash
pip install -r requirements.txt
```

### Bibliotecas Necessárias
- `pandas`
- `pdfplumber`
- `logging`

---

## Estrutura do Projeto

```
test-2/
├── main.py          # Script principal de transformação de dados
├── data-transform.log # Arquivo de log do processo de transformação
├── output/          # Diretório para os arquivos gerados (criado automaticamente)
└── README.md        # Documentação do script de transformação de dados
```

---

## Uso

### Passos:
1. Navegue até o diretório `test-2`:
   ```bash
   cd test-2
   ```
2. Coloque o arquivo PDF `Anexo_I.pdf` no mesmo diretório do script `main.py`.
3. Execute o script:
   ```bash
   python main.py
   ```
4. Os dados extraídos serão salvos no diretório `output/`, e o arquivo ZIP será criado no mesmo diretório.

### Saída:
- Arquivo CSV gerado: `output/Teste_{seu_nome}.csv`
- Arquivo ZIP compactado: `output/Teste_{seu_nome}.zip`

---

## Logs

O script gera um arquivo de log detalhado (`data-transform.log`) para acompanhar o processo de execução. Este log inclui informações sobre operações bem-sucedidas, avisos e erros.

---

## Tratamento de Erros

O script inclui tratamento robusto de erros para lidar com:
- Problemas na leitura do arquivo PDF.
- Dados ausentes ou malformados nas tabelas extraídas.
- Erros de entrada/saída de arquivos durante a geração do CSV e compactação.

Em caso de erros, mensagens detalhadas são registradas no log, e exceções são levantadas para garantir transparência.

---

## Personalização

- **Nome do Arquivo de Saída**: Atualize o parâmetro `output_filename` no script `main.py` para personalizar o nome dos arquivos gerados.
- **Diretório de Saída**: Modifique o parâmetro `output_dir` para alterar o local onde os arquivos serão salvos.

---

## Licença

Este script está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

---

## Autor

**Gabriel Cesar Silvino Xavier**

Sinta-se à vontade para entrar em contato para dúvidas ou feedback!