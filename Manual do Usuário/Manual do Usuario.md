### Manual do Usuário

Bem-vindo ao Manual do Usuário para a Aplicação de Gerenciamento de Livros.

Este manual fornecerá instruções sobre como instalar as dependências necessárias, executar a aplicação e utilizar suas principais funcionalidades.

---

## Instalação do Python e Bibliotecas Necessárias

### Passo 1: Instalar o Python

1. **Baixar o Instalador do Python**:
   - Acesse o [site oficial do Python](https://www.python.org/downloads/).
   - Baixe e execute o instalador Python, seguindo as instruções específicas para seu sistema operacional.

2. **Adicionar Python ao PATH**:
   - Durante a instalação, certifique-se de selecionar a opção **"Add Python to PATH"**.
   - Isso permite que o Python seja executado facilmente a partir da linha de comando.

3. **Verificar a Instalação**:
   - Abra o terminal (Prompt de Comando no Windows ou Terminal no macOS/Linux).
   - Digite `python --version` para verificar se o Python foi instalado corretamente.

### Passo 2: Configuração do Ambiente Virtual

1. **Criar um Ambiente Virtual**:
   - Navegue até o diretório raiz do projeto onde o arquivo `README.md` está localizado.
   - Execute o comando para criar um ambiente virtual:
     - No Windows: `python -m venv venv`
     - No macOS/Linux: `python3 -m venv venv`

2. **Ativar o Ambiente Virtual**:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### Passo 3: Instalar as Dependências do Projeto

1. **Instalar Flask**:
   - Com o ambiente virtual ativado, instale o Flask executando o seguinte comando no terminal:
     ```bash
     pip install Flask
     ```

2. **Verificar a Instalação**:
   - Execute `pip freeze` para listar todas as bibliotecas instaladas.
   - Certifique-se de que `Flask` está listado entre as dependências.

---

## Executando a Aplicação

1. **Navegar até o Diretório do Projeto**:
   - No terminal, navegue até o diretório onde o arquivo `README.md` está localizado.

2. **Ativar o Ambiente Virtual**:
   - Se ainda não estiver ativado, ative o ambiente virtual usando o comando apropriado para seu sistema operacional.

3. **Iniciar o Servidor Flask**:
   - Execute o seguinte comando para iniciar o servidor Flask:
     ```bash
     python FlaskApp/app.py
     ```
   - O servidor irá iniciar e você verá mensagens indicando que a aplicação está sendo executada.

4. **Acessar a Aplicação no Navegador**:
   - Abra um navegador web (como Chrome, Firefox, ou Safari).
   - Digite `http://localhost:5000` na barra de endereços para acessar a aplicação.

---

## Utilizando a Aplicação

Agora que a aplicação está em execução, você pode utilizar as seguintes funcionalidades:

- **Adicionar Livros**:
  - Clique em "Adicionar Livro" no menu principal.
  - Preencha o formulário com as informações do livro e clique em "Salvar".

- **Visualizar Livros**:
  - Clique em "Visualizar Livros" para ver todos os livros cadastrados.
  - Você poderá ver detalhes de cada livro e realizar ações como editar, excluir, emprestar ou reservar.

- **Editar Livros**:
  - Na página de visualização de livros, clique em "Editar" ao lado do livro desejado.
  - Faça as alterações necessárias no formulário e clique em "Salvar".

- **Excluir Livros**:
  - Na página de visualização de livros, clique em "Excluir" ao lado do livro que deseja remover.

- **Emprestar Livros**:
  - Na página de visualização de livros, clique em "Emprestar" ao lado do livro desejado.
  - Insira o nome do emprestador e confirme a operação.

- **Reservar Livros**:
  - Na página de visualização de livros, clique em "Reservar" ao lado do livro desejado.
  - Insira seu nome como reservante e confirme a reserva.

- **Encerrar Empréstimo de Livros**:
  - Na página de visualização de livros, clique em "Encerrar Empréstimo" ao lado do livro emprestado.
  - Confirme para encerrar o empréstimo do livro.

---

Este projeto foi desenvolvido por Leônidas Serra e Jhones Sousa para a disciplina de Paradigmas de Programação ministrada pela Profa. Dra. Alana de Araujo Oliveira.

Siga estas instruções para instalar, executar e utilizar a aplicação de gerenciamento de livros de forma eficiente. Em caso de dúvidas ou problemas, consulte a documentação do Python, do Flask ou entre em contato com o suporte técnico.


