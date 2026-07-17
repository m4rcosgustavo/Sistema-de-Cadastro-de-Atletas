from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = 'chave_secreta_para_sessao'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

from models import db, User, Atleta

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = "Faça login para acessar esta página."
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

# ========== AUTENTICAÇÃO ==========
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':

        nome = request.form['nome'].strip()
        senha = request.form['senha'].strip()

        # Campos vazios
        if not nome or not senha:
            return render_template(
                'cadastro.html',
                erro='Preencha todos os campos.'
            )

        # Tamanho mínimo do nome
        if len(nome) < 3:
            return render_template(
                'cadastro.html',
                erro='O nome deve ter pelo menos 3 caracteres.'
            )

        # Tamanho mínimo da senha
        if len(senha) < 3:
            return render_template(
                'cadastro.html',
                erro='A senha deve ter pelo menos 3 caracteres.'
            )

        usuario_existente = User.query.filter_by(nome=nome).first()

        if usuario_existente:
            return render_template(
                'cadastro.html',
                erro='Usuário já cadastrado.'
            )

        # Salva usuário
        senha_hash = generate_password_hash(senha)

        novo_usuario = User(
            nome=nome,
            senha=senha_hash
        )

        db.session.add(novo_usuario)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('cadastro.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        nome = request.form['nome'].strip()
        senha = request.form['senha'].strip()

        # Verifica campos vazios
        if not nome or not senha:
            return render_template(
                'login.html',
                erro='Preencha todos os campos.'
            )

        usuario = User.query.filter_by(nome=nome).first()

        if usuario and check_password_hash(usuario.senha, senha):
            login_user(usuario)
            return redirect(url_for('atletas'))

        return render_template(
            'login.html',
            erro='Credenciais inválidas!'
        )

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():

    logout_user()

    return redirect(url_for('index'))

# ========== CRUD ATLETAS ==========
@app.route('/atletas')
@login_required
def atletas():

    busca = request.args.get("busca", "").strip()

    if busca:
        atletas_filtrados = Atleta.query.filter(
            Atleta.nome.like(f"%{busca}%")
        ).all()
    else:
        atletas_filtrados = Atleta.query.all()

    return render_template(
        "atletas.html",
        atletas=atletas_filtrados,
        busca=busca
    )

@app.route('/atleta/<int:id>')
@login_required
def detalhe_atleta(id):

    atleta = Atleta.query.get_or_404(id)

    return render_template(
        'atleta_detalhe.html',
        atleta=atleta
    )

# Salvar (CREATE)
@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_atleta():

    if request.method == 'POST':

        novo_atleta = Atleta(
            nome=request.form['nome'],
            idade=request.form['idade'],
            esporte=request.form['esporte']
        )

        db.session.add(novo_atleta)
        db.session.commit()

        return redirect(url_for('atletas'))

    return render_template(
        'form_atleta.html',
        atleta=None
    )

# Editar (UPDATE) - rota parametrizada
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_atleta(id):

    atleta = Atleta.query.get_or_404(id)

    if request.method == 'POST':

        atleta.nome = request.form['nome']
        atleta.idade = request.form['idade']
        atleta.esporte = request.form['esporte']

        db.session.commit()

        return redirect(url_for('atletas'))

    return render_template(
        'form_atleta.html',
        atleta=atleta
    )

@app.route('/delete/<int:id>')
@login_required
def delete_atleta(id):

    atleta = Atleta.query.get_or_404(id)

    db.session.delete(atleta)
    db.session.commit()

    return redirect(url_for('atletas'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
