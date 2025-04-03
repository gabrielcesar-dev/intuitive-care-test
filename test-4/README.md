# Teste Técnico 4 - Intuitive Care

Este projeto é parte do teste técnico para a Intuitive Care. Ele consiste em desenvolver uma interface web utilizando **Vue.js** que interaja com um servidor em **Python** para realizar buscas em uma lista de cadastros de operadoras.

## Objetivo

Criar uma aplicação que permita:

1. Realizar buscas textuais em uma lista de cadastros de operadoras.
2. Retornar os registros mais relevantes.
3. Demonstrar o funcionamento da API utilizando uma coleção no **Postman**.

## Estrutura do Projeto

O projeto está dividido em duas partes principais:

- **Backend**: Desenvolvido em Python com Django, responsável por processar as buscas e fornecer os dados via API.
- **Frontend**: Desenvolvido em Vue.js, responsável por consumir a API e exibir os resultados.

## Tarefas

### Tarefas de Preparação

- Utilizar o arquivo CSV fornecido no item 3.2 do teste para carregar os dados no backend.

### Tarefas de Código

1. Criar um servidor com uma rota que realiza buscas textuais na lista de cadastros de operadoras.
2. Retornar os registros mais relevantes com base na busca.
3. Elaborar uma coleção no Postman para demonstrar os resultados da API.

## Configuração do Projeto

### Backend

1. Acesse o diretório `backend` e siga as instruções no arquivo [README.md](./backend/README.md) para configurar o servidor.

### Frontend

1. Acesse o diretório `frontend` e siga as instruções no arquivo [README.md](./frontend/README.md) para configurar a interface web.

### Postman

1. Importe a coleção Postman fornecida no diretório `postman_collection` para testar os endpoints da API.

## Como Usar

1. Certifique-se de que o backend está rodando em [http://localhost:8000](http://localhost:8000).
2. Inicie o frontend e acesse a aplicação em [http://localhost:5173](http://localhost:5173).
3. Utilize a interface web para realizar buscas textuais.
4. Para testar diretamente a API, utilize a coleção Postman.

## Observações

- Certifique-se de que o arquivo CSV está no formato correto antes de carregá-lo no backend.
- Atualize as configurações de produção, como `DEBUG` e `ALLOWED_HOSTS`, antes de implantar o projeto.

## Autor

- **Gabriel Cesar**

## Licença

Este projeto está licenciado sob a Licença MIT.
