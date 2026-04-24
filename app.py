from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_sessao'

# Simulação de banco de dados
usuarios = {}
atletas = []
proximo_id = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        if nome not in usuarios:
            usuarios[nome] = senha
            return redirect(url_for('login'))
        else:
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
        else:
            return 'Credenciais inválidas!'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))

@app.route('/atletas')
def atletas():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    # ✅ STRING DE CONSULTA (filtro por nome)
    busca = request.args.get('busca', '')
    if busca:
        atletas_filtrados = [a for a in atletas if busca.lower() in a['nome'].lower()]
    else:
        atletas_filtrados = atletas

    return render_template('atletas.html', atletas=atletas_filtrados, busca=busca)

# ✅ ROTA PARAMETRIZADA PARA DETALHES
@app.route('/atleta/<int:id>')
def detalhe_atleta(id):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    atleta = next((a for a in atletas if a['id'] == id), None)
    if atleta:
        return render_template('atleta_detalhe.html', atleta=atleta)
    return 'Atleta não encontrado', 404

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
        atletas.append(atleta)
        proximo_id += 1
        return redirect(url_for('atletas'))
    return render_template('form_atleta.html', atleta=None)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_atleta(id):
    if 'usuario' not in session:
        return redirect(url_for('login'))

    atleta = next((a for a in atletas if a['id'] == id), None)
    if not atleta:
        return 'Atleta não encontrado', 404

    if request.method == 'POST':
        atleta['nome'] = request.form['nome']
        atleta['idade'] = int(request.form['idade'])
        atleta['esporte'] = request.form['esporte']
        return redirect(url_for('atletas'))

    return render_template('form_atleta.html', atleta=atleta)

@app.route('/delete/<int:id>')
def delete_atleta(id):
    if 'usuario' not in session:
        return redirect(url_for('login'))

    global atletas
    atletas = [a for a in atletas if a['id'] != id]
    return redirect(url_for('atletas'))

if __name__ == '__main__':
    app.run(debug=True)