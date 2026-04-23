from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = '123'

usuarios = []
tarefas = []
id_counter = 1

# ---------------- HOME ----------------
@app.route('/')
def index():
    return render_template('index.html')


# ---------------- CADASTRO ----------------
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        user = request.form['user']
        senha = request.form['senha']

        usuarios.append({'user': user, 'senha': senha})
        return redirect('/login')

    return render_template('cadastro.html')


# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        senha = request.form['senha']

        for u in usuarios:
            if u['user'] == user and u['senha'] == senha:
                session['user'] = user
                return redirect('/dashboard')

    return render_template('login.html')


# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')

    filtro = request.args.get('filtro')

    if filtro:
        lista = [t for t in tarefas if filtro.lower() in t['titulo'].lower()]
    else:
        lista = tarefas

    return render_template('dashboard.html', tarefas=lista)


# ---------------- CRIAR ----------------
@app.route('/criar', methods=['GET', 'POST'])
def criar():
    global id_counter

    if request.method == 'POST':
        titulo = request.form['titulo']

        tarefas.append({
            'id': id_counter,
            'titulo': titulo
        })

        id_counter += 1
        return redirect('/dashboard')

    return render_template('criar_item.html')


# ---------------- EDITAR ----------------
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    for t in tarefas:
        if t['id'] == id:
            if request.method == 'POST':
                t['titulo'] = request.form['titulo']
                return redirect('/dashboard')

            return render_template('editar_item.html', tarefa=t)


# ---------------- DELETAR ----------------
@app.route('/deletar/<int:id>')
def deletar(id):
    global tarefas
    tarefas = [t for t in tarefas if t['id'] != id]
    return redirect('/dashboard')


if __name__ == '__main__':
    app.run(debug=True)