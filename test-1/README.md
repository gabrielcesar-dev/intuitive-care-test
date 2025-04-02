# Script de Web Scraping da ANS

## Visão Geral

Este script foi desenvolvido para realizar web scraping no site da **ANS (Agência Nacional de Saúde Suplementar)**, com o objetivo de baixar arquivos PDF específicos (Anexos I e II) e compactá-los em um único arquivo ZIP.

---

## Funcionalidades

- Acessa o site da ANS: [Atualização do Rol de Procedimentos](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos).
- Busca e baixa os arquivos PDF especificados (Anexos I e II).
- Compacta os arquivos baixados em um único arquivo ZIP.

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
- `requests`
- `beautifulsoup4`
- `logging`

---

## Estrutura do Projeto

```
test-1/
├── main.py          # Script de web scraping
├── web_scraping.log # Arquivo de log do web scraping
├── downloads/       # Diretório para os arquivos baixados (criado automaticamente)
└── README.md        # Documentação do script de web scraping
```

---

## Uso

### Passos:
1. Navegue até o diretório `test-1`:
   ```bash
   cd test-1
   ```
2. Execute o script:
   ```bash
   python main.py
   ```
3. Os PDFs baixados serão salvos no diretório `downloads/`, e o arquivo ZIP será criado no mesmo diretório.

### Saída:
- PDFs baixados: `downloads/Anexo_I.pdf`, `downloads/Anexo_II.pdf`
- Arquivo ZIP compactado: `downloads/anexos.zip`

---

## Logs

O script gera um arquivo de log detalhado (`web_scraping.log`) para acompanhar o processo de execução. Este log inclui informações sobre operações bem-sucedidas, avisos e erros.

---

## Tratamento de Erros

O script inclui tratamento robusto de erros para lidar com:
- Problemas de rede durante o web scraping.
- Dados ausentes ou malformados no site.
- Erros de entrada/saída de arquivos durante os downloads e compactações.

Em caso de erros, mensagens detalhadas são registradas no log, e exceções são levantadas para garantir transparência.

---

## Personalização

- **URL Base**: Atualize a variável `base_url` no arquivo `main.py` para realizar scraping em outra página.
- **Nomes Alvo**: Modifique a lista `target_names` para buscar por nomes de arquivos diferentes.

---

## Licença

Este script está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

---

## Autor

**Gabriel Cesar Silvino Xavier**

Sinta-se à vontade para entrar em contato para dúvidas ou feedback!
