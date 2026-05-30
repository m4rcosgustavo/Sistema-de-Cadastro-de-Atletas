from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3


app = Flask(__name__)
app.secret_key = 'chave_secreta_para_sessao'

def get_db():
    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS atletas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            esporte TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

# Banco de dados fake
# usuarios = {}
lista_atletas = []  
proximo_id = 1

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

        conn = get_db()
        cursor = conn.cursor()

        # Verifica se já existe
        cursor.execute(
            "SELECT * FROM usuarios WHERE nome = ?",
            (nome,)
        )

        usuario_existente = cursor.fetchone()

        if usuario_existente:
            conn.close()
            return render_template(
                'cadastro.html',
                erro='Usuário já cadastrado.'
            )

        # Salva usuário
        cursor.execute(
            "INSERT INTO usuarios (nome, senha) VALUES (?, ?)",
            (nome, senha)
        )

        conn.commit()
        conn.close()

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

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM usuarios WHERE nome = ? AND senha = ?",
            (nome, senha)
        )

        usuario = cursor.fetchone()

        conn.close()

        if usuario:
            session['usuario'] = nome
            return redirect(url_for('atletas'))

        return render_template(
            'login.html',
            erro='Credenciais inválidas!'
        )

    return render_template('login.html')


@app.route('/logout')
def logout():

    # Remove usuario da sessao
    session.pop('usuario', None)
    # Limpa completamente a sessao
    session.clear()

    return redirect(url_for('index'))

# ========== CRUD ATLETAS ==========
@app.route('/atletas')
def atletas():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    busca = request.args.get('busca', '').strip()

    conn = get_db()
    cursor = conn.cursor()

    if busca:
        cursor.execute(
            "SELECT * FROM atletas WHERE nome LIKE ?",
            ('%' + busca + '%',)
        )
    else:
        cursor.execute("SELECT * FROM atletas")

    atletas_filtrados = cursor.fetchall()

    conn.close()

    return render_template(
        'atletas.html',
        atletas=atletas_filtrados,
        busca=busca
    )

# Rota parametrizada - mostrar detalhes
@app.route('/atleta/<int:id>')
def detalhe_atleta(id):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    atleta = next((a for a in lista_atletas if a['id'] == id), None)
    if atleta:
        return render_template('atleta_detalhe.html', atleta=atleta)
    return 'Atleta não encontrado', 404

# Salvar (CREATE)
@app.route('/add', methods=['GET', 'POST'])
def add_atleta():

    if 'usuario' not in session:
        return redirect(url_for('login')

)

    if request.method == 'POST':

        nome = request.form['nome']
        idade = request.form['idade']
        esporte = request.form['esporte']

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO atletas
            (nome, idade, esporte)
            VALUES (?, ?, ?)
            """,
            (nome, idade, esporte)
        )

        conn.commit()
        conn.close()

        return redirect(url_for('atletas'))

    return render_template(
        'form_atleta.html',
        atleta=None
    )

# Editar (UPDATE) - rota parametrizada
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_atleta(id):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    atleta = next((a for a in lista_atletas if a['id'] == id), None)  # ← mudado
    if not atleta:
        return 'Atleta não encontrado', 404
    
    if request.method == 'POST':
        atleta['nome'] = request.form['nome']
        atleta['idade'] = int(request.form['idade'])
        atleta['esporte'] = request.form['esporte']
        return redirect(url_for('atletas'))
    
    return render_template('form_atleta.html', atleta=atleta)

# Remover (DELETE) - rota parametrizada
@app.route('/delete/<int:id>')
def delete_atleta(id):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    global lista_atletas  # ← mudado
    lista_atletas = [a for a in lista_atletas if a['id'] != id]  # ← mudado
    return redirect(url_for('atletas'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)