# Backend do Projeto Operadoras

Este é o backend do Projeto Operadoras, uma aplicação baseada em Django projetada para gerenciar e buscar dados de operadoras. Ele fornece APIs para carregar dados de operadoras a partir de um arquivo CSV e buscar operadoras com base em vários critérios.

## Funcionalidades

- **Carregar Dados CSV**: Carregar dados de operadoras de um arquivo CSV para o banco de dados.
- **Buscar Operadoras**: Buscar operadoras usando vários campos, como `registro_ans`, `cnpj`, `razao_social` e outros.
- **API REST**: Construída com Django REST Framework para fácil integração com frontend ou outros serviços.

## Requisitos

- Python 3.8+
- Django 5.1
- Django REST Framework
- Pandas
- SQLite (banco de dados padrão)

## Instruções de Configuração

1. **Criar um Ambiente Virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

2. **Instalar Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Aplicar Migrações**:
   ```bash
   python manage.py migrate
   ```

4. **Executar o Servidor de Desenvolvimento**:
   ```bash
   python manage.py runserver
   ```

5. **Acessar a API**:
   - Carregar Dados CSV: `POST /operators/load-data/`
   - Buscar Operadoras: `GET /operators/search/?q=<query>`

## Configuração

- **Caminho do Arquivo CSV**: Coloque o arquivo CSV chamado `operators_data.csv` no diretório raiz do projeto.
- **CORS**: O CORS está habilitado para todas as origens. Atualize `CORS_ALLOW_ALL_ORIGINS` em `settings.py` para produção.

## Endpoints da API

### 1. Carregar Dados CSV
- **URL**: `/api/operators/load-data/`
- **Método**: `POST`
- **Descrição**: Carrega dados de operadoras de um arquivo CSV para o banco de dados.

### 2. Buscar Operadoras
- **URL**: `/api/operators/search/`
- **Método**: `GET`
- **Parâmetro de Consulta**: `q` - Termo de busca.
- **Descrição**: Busca operadoras com base no termo fornecido.

## Estrutura do Projeto

- `operators_project/`: Pasta principal do projeto Django.
- `operators_api/`: Contém a lógica da API, incluindo views, models e URLs.
- `db.sqlite3`: Arquivo de banco de dados SQLite padrão.
- `manage.py`: Script de gerenciamento do Django.

## Observações

- Certifique-se de que o arquivo CSV segue o formato esperado com os nomes de colunas apropriados.
- Para produção, atualize as configurações `DEBUG` e `ALLOWED_HOSTS` em `settings.py`.
- **Nota**: O arquivo `operators_data.csv` já foi carregado para o banco de dados SQLite, e ambos estão disponíveis no diretório do projeto.

## Autor

- **Gabriel Cesar**

## Licença

Este projeto está licenciado sob a Licença MIT.
