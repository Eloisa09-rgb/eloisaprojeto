from flask import *
import dao

app = Flask(__name__)


@app.route('/')
def pagina_inicial():
    return render_template('index.html')

@app.route('/adicionar_usuario')
def page_adicionar_usuario():
    return render_template('adicionarusuario.html')

@app.route('/listarlivros')
def listar_livros():
    return render_template('listarlivros.html')

@app.route('/adicionarusuario', methods=['POST'])
def adicionar_usuario():
    login = request.form.get('login')
    senha = request.form.get('senha')
    nome = request.form.get('nome')

    if dao.inserirusuario(login, senha, nome):
        return render_template('index.html', msg='Usuário cadastrado com sucesso')
    else:
        return render_template('index.html', msg='Erro ao inserir usuário')


@app.route('/login', methods=['POST'])
def login():
    login = request.form.get('login')
    senha = request.form.get('senha')

    resultado = dao.verificarlogin(login, senha, dao.conectardb())

    if len(resultado) > 0:
        return render_template('homeuser.html', user=resultado[0][1])
    else:
        msg = 'Senha ou login incorretos'
        return render_template('index.html', msglogin=msg)


@app.route('/page_add_livro')
def mostrar_page_add():
    return render_template('adicionarlivro.html')


@app.route('/cadastrarlivro')
def mostrar_pag_cadstrolivro():
    return render_template('adicionarlivro.html')

@app.route ('/adicionarlivro', methods=['POST'])
def cadastrarlivro():
    nome = request.form.get('nome')
    codigo = request.form.get('codigo')
    disponivel = request.form.get('disponivel')

    if dao.adicionarlivro( nome, codigo, disponivel):
        return render_template('index.html', msg='Livro cadastrado com sucesso')
    else:
        return render_template('index.html', msg='Erro ao inserir Livro')



app.run(debug=True)