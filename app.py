from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_sessao'

# Banco de dados fake
usuarios = {}
lista_atletas = []  # ← Mudei de "atletas" para "lista_atletas"
proximo_id = 1

@app.route('/')
def index():
    return render_template('index.html')

# ========== AUTENTICAÇÃO ==========
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        if nome not in usuarios:
            usuarios[nome] = senha
            return redirect(url_for('login'))
        return 'Usuário já existe!'
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        if usuarios.get(nome) == senha:
            session['usuario'] = nome
            return redirect(url_for('atletas'))
        return 'Credenciais inválidas!'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))

# ========== CRUD ATLETAS ==========
@app.route('/atletas')
def atletas():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    # String de consulta (filtro)
    busca = request.args.get('busca', '')
    if busca:
        atletas_filtrados = [a for a in lista_atletas if busca.lower() in a['nome'].lower()]
    else:
        atletas_filtrados = lista_atletas
    
    return render_template('atletas.html', atletas=atletas_filtrados, busca=busca)

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
        return redirect(url_for('login'))
    
    global proximo_id
    if request.method == 'POST':
        atleta = {
            'id': proximo_id,
            'nome': request.form['nome'],
            'idade': int(request.form['idade']),
            'esporte': request.form['esporte']
        }
        lista_atletas.append(atleta)  # ← mudado para lista_atletas
        proximo_id += 1
        return redirect(url_for('atletas'))
    return render_template('form_atleta.html', atleta=None)

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
    app.run(debug=True)