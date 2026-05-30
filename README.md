# Sistema de Cadastro de Atletas (Flask + SQLite3)

## 1. Introdução

Este projeto consiste na continuação do Projeto 1 da disciplina de Desenvolvimento Web com Flask.

Nesta segunda versão, a aplicação foi aprimorada com a implementação de persistência de dados utilizando SQLite3 e autenticação de usuários através de sessões Flask, tornando o sistema mais seguro e funcional.

A aplicação tem como objetivo auxiliar no cadastro e gerenciamento de atletas, permitindo que usuários autenticados realizem operações completas de CRUD (Create, Read, Update e Delete).

---

## 2. Objetivo Geral

Desenvolver uma aplicação web funcional utilizando Flask, SQLite3 e sessões de usuário, aplicando os principais conceitos de desenvolvimento web estudados durante a disciplina.

---

## 3. Objetivos Específicos

- Implementar autenticação de usuários com login e logout;
- Utilizar sessões para controle de acesso;
- Persistir dados utilizando banco de dados SQLite3;
- Desenvolver CRUD completo para gerenciamento de atletas;
- Utilizar templates com herança;
- Aplicar métodos HTTP GET e POST;
- Utilizar rotas parametrizadas e query strings;
- Organizar o projeto seguindo boas práticas de desenvolvimento.

---

## 4. Problema Abordado

Em ambientes esportivos, escolares ou recreativos, muitas vezes não existe um sistema simples para armazenar informações de atletas de forma organizada e acessível.

O uso de planilhas ou registros manuais pode dificultar a atualização, consulta e manutenção dessas informações.

---

## 5. Justificativa

O sistema foi desenvolvido para facilitar o gerenciamento de atletas por meio de uma aplicação web simples, intuitiva e acessível.

Além de solucionar um problema real, o projeto contribui para a prática dos conceitos de desenvolvimento web, banco de dados e autenticação de usuários.

---

## 6. Tecnologias Utilizadas

- Python
- Flask
- SQLite3
- HTML5
- CSS3

---

## 7. Estrutura do Projeto

```text
Sistema-de-Cadastro-de-Atletas-Profissionais-e-Iniciantes/
│
├── app.py
├── banco.db
├── README.md
│
├── static/
│   ├── style.css
│   ├── logo.png
│   └── atletas.jpg
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── cadastro.html
│   ├── atletas.html
│   ├── atleta_detalhe.html
│   └── form_atleta.html
│
├── env/
└── __pycache__/

```
## 8. Banco de Dados SQLite3

O sistema utiliza SQLite3 para armazenamento persistente das informações.

### Tabela de Usuários

Campos:

- id
- nome
- senha

### Tabela de Atletas

Campos:

- id
- nome
- idade
- esporte

O banco é inicializado automaticamente através da função `init_db()`, responsável pela criação das tabelas caso ainda não existam.

---

## 9. Sistema de Sessões

O projeto utiliza sessões Flask para controlar a autenticação dos usuários.

### Funcionalidades

- Login de usuários;
- Criação de sessão após autenticação;
- Restrição de acesso às páginas internas;
- Logout com encerramento da sessão;
- Redirecionamento de usuários não autenticados.

---

## 10. Funcionalidades do Sistema

### Cadastro de Usuários

Permite que novos usuários criem uma conta para acessar o sistema.

### Login e Logout

Usuários cadastrados podem acessar o sistema através de autenticação.

### Gerenciamento de Atletas

A aplicação permite:

- Cadastrar atletas;
- Visualizar atletas cadastrados;
- Consultar detalhes de um atleta;
- Editar informações;
- Excluir registros.

### Busca de Atletas

O sistema possui filtro de busca utilizando query string.

Exemplo:

```text
/atletas?busca=joao
```
## 11. Rotas da Aplicação

| Rota           | Método   | Descrição            |
| -------------- | -------- | -------------------- |
| `/`            | GET      | Página inicial       |
| `/cadastro`    | GET/POST | Cadastro de usuários |
| `/login`       | GET/POST | Login                |
| `/logout`      | GET      | Logout               |
| `/atletas`     | GET      | Listagem de atletas  |
| `/atleta/<id>` | GET      | Detalhes do atleta   |
| `/add`         | GET/POST | Cadastro de atleta   |
| `/edit/<id>`   | GET/POST | Edição de atleta     |
| `/delete/<id>` | GET      | Remoção de atleta    |

---

## 12. Requisitos Atendidos

* Rotas Flask
* Redirecionamentos
* Templates com herança
* Arquivos estáticos
* Métodos GET e POST
* Query Strings
* Rotas parametrizadas
* Cadastro de usuários
* Login e Logout
* Sessões Flask
* Banco de Dados SQLite3
* CRUD completo
* Controle de acesso por autenticação

---

## 13. Como Executar o Projeto

### Clonar o repositório

```bash
git clone https://github.com/seu-usuario/Sistema-de-Cadastro-de-Atletas-Profissionais-e-Iniciantes
```

### Entrar na pasta

```bash
cd Sistema-de-Cadastro-de-Atletas-Profissionais-e-Iniciantes
```

### Ativar ambiente virtual

```bash
env\Scripts\activate
```

### Executar aplicação

```bash
python app.py
```

A aplicação estará disponível em:

```text
http://127.0.0.1:5000
```

---

## 14. Integrantes

* Marcos Gustavo
* Heloisa Pereira
* Jullyane Sandra
* Maria Luiza

---

## 15. Divisão de Responsabilidades da Equipe

### Marcos Gustavo – Banco de Dados SQLite3

Responsável pela implementação da estrutura de banco de dados da aplicação.

Atividades desenvolvidas:

- Adição da biblioteca `sqlite3` ao projeto;
- Criação do arquivo `banco.db`;
- Implementação da função `get_db()` para conexão com o banco de dados;
- Implementação da função `init_db()` para inicialização automática do banco;
- Criação da tabela `usuarios`;
- Criação da tabela `atletas`;
- Testes de criação e funcionamento do banco de dados.
- Além da implementação da estrutura inicial do banco de dados, também realizou a revisão final da aplicação, testes de integração entre os módulos e validação dos requisitos obrigatórios do projeto.

Principais funcionalidades implementadas:

- Persistência de dados utilizando SQLite3;
- Criação automática das tabelas do sistema;
- Estruturação do banco de dados para usuários e atletas;
- Integração inicial do banco de dados com a aplicação Flask;
- Preparação da base para armazenamento permanente das informações.

### Jullyane Sandra – Sistema de Usuários

Responsável pela implementação e gerenciamento do cadastro de usuários da aplicação.

Atividades desenvolvidas:

- Alteração do sistema de cadastro para armazenamento utilizando SQLite3;
- Implementação de validação dos campos obrigatórios;
- Prevenção de cadastros duplicados;
- Exibição de mensagens de erro para o usuário;
- Realização de testes no processo de cadastro.

Principais funcionalidades implementadas:

- Cadastro de novos usuários;
- Validação de dados informados;
- Armazenamento persistente no banco de dados;
- Controle de integridade dos registros cadastrados.

### Maria Luiza – Login e Sessões

Responsável pela implementação do sistema de autenticação e controle de acesso da aplicação.

Atividades desenvolvidas:

- Implementação do login utilizando dados armazenados no SQLite3;
- Verificação de usuário e senha durante a autenticação;
- Criação e gerenciamento de sessões com Flask;
- Implementação da funcionalidade de logout;
- Proteção das rotas restritas do sistema;
- Redirecionamento de usuários não autenticados para a página de login.

Principais funcionalidades implementadas:

- Autenticação de usuários;
- Controle de acesso por sessão;
- Encerramento seguro da sessão (logout);
- Restrição de acesso às páginas internas;
- Validação de credenciais armazenadas no banco de dados.

### Heloisa Pereira – CRUD dos Atletas

Responsável pela implementação e adaptação do sistema de gerenciamento de atletas utilizando SQLite3.

Atividades desenvolvidas:

- Implementação do cadastro de atletas utilizando comandos `INSERT`;
- Implementação da listagem de atletas utilizando consultas `SELECT`;
- Implementação da edição de atletas utilizando comandos `UPDATE`;
- Implementação da exclusão de atletas utilizando comandos `DELETE`;
- Ajuste do sistema de busca por nome utilizando query strings;
- Realização de testes para validação do CRUD completo.

Principais funcionalidades implementadas:

- Cadastro de novos atletas;
- Visualização dos atletas cadastrados;
- Consulta de detalhes dos atletas;
- Atualização de informações dos registros;
- Remoção de atletas do sistema;
- Integração do CRUD com o banco de dados SQLite3.


