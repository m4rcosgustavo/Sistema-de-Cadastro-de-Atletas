# Sistema de Cadastro de Atletas

## 1. Introdução

O Sistema de Cadastro de Atletas é uma aplicação web desenvolvida com Flask que permite realizar o gerenciamento de atletas por meio de um ambiente simples, intuitivo e seguro.

Nesta versão do projeto, foram implementados recursos de autenticação de usuários, persistência de dados utilizando SQLite com SQLAlchemy, controle de sessões através do Flask-Login e um sistema completo de gerenciamento de atletas (CRUD).

O sistema permite que apenas usuários autenticados possam acessar as funcionalidades internas da aplicação, garantindo maior segurança aos dados cadastrados.

---

# 2. Equipe

- Marcos Gustavo
- Heloísa Pereira
- Jullyane Sandra
- Maria Luiza

---

# 3. Objetivo Geral

Desenvolver uma aplicação web utilizando Flask, SQLAlchemy e Flask-Login para realizar o cadastro e gerenciamento de atletas, aplicando os principais conceitos estudados durante a disciplina de Desenvolvimento Web.

---

# 4. Objetivos Específicos

- Desenvolver autenticação de usuários;
- Implementar login e logout;
- Controlar sessões utilizando Flask-Login;
- Persistir informações em banco de dados SQLite;
- Desenvolver operações de CRUD;
- Aplicar templates utilizando herança;
- Utilizar rotas GET e POST;
- Implementar busca utilizando Query String;
- Utilizar rotas parametrizadas;
- Organizar o projeto seguindo boas práticas.

---

# 5. Problema Abordado

Em diversos ambientes esportivos, como escolas, academias e projetos sociais, o cadastro de atletas ainda é realizado de forma manual ou utilizando planilhas eletrônicas.

Esse tipo de gerenciamento dificulta a organização das informações, aumenta a possibilidade de erros e torna o processo de consulta e atualização dos dados mais lento.

Diante desse cenário, foi desenvolvido um sistema web que permite centralizar o cadastro dos atletas em uma única plataforma, facilitando o gerenciamento das informações.

---

# 6. Justificativa

A criação deste sistema busca oferecer uma solução simples, organizada e segura para o gerenciamento de atletas.

Além de resolver um problema real, o projeto permitiu colocar em prática diversos conteúdos estudados durante a disciplina, como desenvolvimento web com Flask, banco de dados relacionais, autenticação de usuários, arquitetura MVC, utilização de ORM através do SQLAlchemy e organização de aplicações web.

---

# 7. Tecnologias Utilizadas

- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- SQLAlchemy
- SQLite
- HTML5
- CSS3
- Jinja2
- Werkzeug

---

# 8. Estrutura do Projeto

```text
Sistema-de-Cadastro-de-Atletas/

│
├── app.py
├── models.py
├── banco.db
├── requirements.txt
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

---

# 9. Banco de Dados

O projeto utiliza SQLite juntamente com SQLAlchemy para persistência das informações.

Foram implementadas as seguintes tabelas:

## Usuários

- id
- nome
- senha

A senha é armazenada de forma criptografada utilizando o Werkzeug.

## Atletas

- id
- nome
- idade
- esporte

## Esportes

- id
- nome

As tabelas são criadas automaticamente através do método:

```python
db.create_all()
```

quando a aplicação é iniciada.

---

# 10. Sistema de Autenticação

O sistema utiliza Flask-Login para controlar a autenticação dos usuários.

As principais funcionalidades implementadas foram:

- Cadastro de usuários;
- Login;
- Logout;
- Controle de sessões;
- Proteção das rotas utilizando `@login_required`;
- Redirecionamento automático para login quando necessário;
- Armazenamento seguro das senhas utilizando hash.

---

# 11. Funcionalidades

## Cadastro de usuários

Permite criar novos usuários para utilização do sistema.

---

## Login

Permite autenticar usuários cadastrados.

---

## Logout

Finaliza a sessão do usuário.

---

## Cadastro de atletas

Permite adicionar novos atletas.

---

## Listagem

Exibe todos os atletas cadastrados.

---

## Busca

Permite pesquisar atletas pelo nome utilizando Query String.

Exemplo:

```
/atletas?busca=joao
```

---

## Detalhes

Visualiza todas as informações de um atleta.

---

## Edição

Permite alterar os dados cadastrados.

---

## Exclusão

Remove atletas do banco de dados.

---

# 12. Rotas

| Rota | Método | Descrição |
|------|---------|-----------|
| / | GET | Página inicial |
| /cadastro | GET/POST | Cadastro de usuários |
| /login | GET/POST | Login |
| /logout | GET | Logout |
| /atletas | GET | Lista atletas |
| /atleta/<id> | GET | Detalhes do atleta |
| /add | GET/POST | Novo atleta |
| /edit/<id> | GET/POST | Editar atleta |
| /delete/<id> | GET | Excluir atleta |

---

# 13. Requisitos Atendidos

- Flask
- Templates com herança
- HTML
- CSS
- SQLAlchemy
- SQLite
- Flask-Login
- CRUD completo
- Login
- Logout
- Controle de sessões
- Banco de dados
- Query Strings
- Rotas parametrizadas
- Métodos GET
- Métodos POST
- Proteção das rotas
- Hash de senha
- Interface responsiva

---

# 14. Principais Problemas Técnicos Encontrados

Durante o desenvolvimento do projeto foram encontrados alguns desafios técnicos.

O primeiro foi a migração da aplicação que utilizava SQLite puro para SQLAlchemy. Essa alteração exigiu mudanças na forma de realizar consultas, inserções, atualizações e exclusões no banco de dados, tornando o código mais organizado e de fácil manutenção.

Outro desafio foi a implementação da autenticação de usuários. Para solucionar esse problema foi utilizada a biblioteca Flask-Login, responsável pelo gerenciamento das sessões e proteção das rotas da aplicação.

Também foi necessário implementar a criptografia das senhas dos usuários utilizando as funções `generate_password_hash()` e `check_password_hash()` da biblioteca Werkzeug, garantindo maior segurança ao sistema.

Por fim, houve a reorganização da estrutura do projeto, separando os modelos de banco de dados em um arquivo específico (`models.py`), tornando a aplicação mais organizada e próxima das boas práticas de desenvolvimento.

---

# 15. Como Executar

## Clonar o projeto

```bash
git clone https://github.com/seu-repositorio.git
```

## Entrar na pasta

```bash
cd Sistema-de-Cadastro-de-Atletas
```

## Criar ambiente virtual

```bash
python -m venv env
```

## Ativar ambiente

Windows

```bash
env\Scripts\activate
```

Linux

```bash
source env/bin/activate
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Executar

```bash
python app.py
```

O sistema ficará disponível em:

```
http://127.0.0.1:5000
```

---

# 16. Divisão das Responsabilidades

## Marcos Gustavo — Banco de Dados

- Modelagem do banco de dados;
- Configuração do SQLAlchemy;
- Criação das tabelas;
- Estruturação dos modelos;
- Testes da persistência dos dados.

---

## Jullyane Sandra — Cadastro de Usuários

- Cadastro de usuários;
- Validação dos campos;
- Verificação de usuários duplicados;
- Mensagens de erro;
- Testes do cadastro.

---

## Maria Luiza — Login e Controle de Sessões

- Implementação do Flask-Login;
- Login;
- Logout;
- Proteção das rotas;
- Criptografia das senhas utilizando Werkzeug;
- Controle das sessões dos usuários.

---

## Heloísa Pereira — CRUD de Atletas

- Cadastro;
- Listagem;
- Busca;
- Visualização dos detalhes;
- Edição;
- Exclusão dos atletas;
- Testes do CRUD completo.

---

# 17. Considerações Finais

O projeto permitiu aplicar na prática os principais conceitos estudados durante a disciplina de Desenvolvimento Web, envolvendo desenvolvimento com Flask, banco de dados relacionais, autenticação de usuários, controle de sessões, organização de código e utilização de ORM através do SQLAlchemy.

O resultado foi uma aplicação funcional, organizada, segura e preparada para futuras melhorias, como relacionamentos entre tabelas, cadastro de modalidades esportivas, upload de imagens dos atletas e diferentes níveis de permissão de usuários.
