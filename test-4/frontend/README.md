# Frontend - Teste de Nivelamento | Intuitive Care

Este é o frontend do projeto de teste de nivelamento da Intuitive Care. Ele foi desenvolvido utilizando **Vue 3**, **TypeScript** e **Vite** como ferramentas principais.

## Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

- **Node.js** (versão 18 ou superior)
- **pnpm** (gerenciador de pacotes)

## Instalação

1. Acesse o diretório do projeto:
   ```bash
   cd frontend
   ```

2. Instale as dependências:
   - Usando **pnpm**:
     ```bash
     pnpm install
     ```
   - Usando **npm**:
     ```bash
     npm install
     ```

## Scripts Disponíveis

- Usando **pnpm**:
  - `pnpm dev`: Inicia o servidor de desenvolvimento.
  - `pnpm build`: Compila o projeto para produção.
  - `pnpm preview`: Visualiza a aplicação compilada.

- Usando **npm**:
  - `npm run dev`: Inicia o servidor de desenvolvimento.
  - `npm run build`: Compila o projeto para produção.
  - `npm run preview`: Visualiza a aplicação compilada.

## Estrutura do Projeto

- **`src/`**: Contém o código-fonte do projeto.
  - **`components/`**: Componentes Vue reutilizáveis.
  - **`App.vue`**: Componente raiz da aplicação.
  - **`main.ts`**: Ponto de entrada principal.
- **`public/`**: Arquivos estáticos.
- **`vite.config.ts`**: Configuração do Vite.
- **`tsconfig.app.json`**: Configuração do TypeScript.

## Funcionalidades

- Busca de operadoras de saúde com paginação.
- Exibição de resultados em uma tabela responsiva.
- Mensagens de status para carregamento e erros de conexão.

## Tecnologias Utilizadas

- **Vue 3**: Framework JavaScript para construção de interfaces de usuário.
- **TypeScript**: Superset do JavaScript que adiciona tipagem estática.
- **Vite**: Ferramenta de build rápida e moderna.
- **Bootstrap**: Framework CSS para estilização.

## Como Usar

1. Inicie o servidor de desenvolvimento:
   ```bash
   pnpm dev
   ```

2. Acesse a aplicação no navegador em: [http://localhost:5173](http://localhost:5173).

3. Certifique-se de que o backend está rodando em [http://localhost:8000](http://localhost:8000) para que a busca funcione corretamente.

## Observações

- Caso o backend não esteja disponível, uma mensagem de erro será exibida.
- O frontend utiliza **axios** para realizar requisições HTTP.

## Autor

- **Gabriel Cesar**

## Licença

Este projeto está licenciado sob a Licença MIT.
