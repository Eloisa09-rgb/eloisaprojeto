from flask import *
import dao
from dao import conectardb

app = Flask(__name__)

app.secret_key = 'khgGH4J32G4J'

@app.route('/')
def pagina_inicial():
    return render_template('index.html')

@app.route('/adicionar_usuario')
def page_adicionar_usuario():
    return render_template('adicionarusuario.html')

@app.route('/listar_livros')
def listar_livros():
    livros = dao.listarlivros(session['login'])
    print(livros)
    return render_template('listarlivros.html', lista=livros)


@app.route('/adicionarusuario', methods=['POST'])
def adicionarusuario():
    login = request.form.get('login')
    senha = request.form.get('senha')
    nome = request.form.get('nome')

    if dao.adicionarusuario(login, senha, nome, dao.conectardb()):
        return render_template('index.html', msg='Usuário cadastrado com sucesso')
    else:
        return render_template('index.html', msg='Erro ao inserir usuário')



@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'GET' and 'login' in session:
        return render_template('homeuser.html', user=session['nome'])

    login = request.form.get('login')
    senha = request.form.get('senha')

    resultado = dao.verificarlogin(login, senha, dao.conectardb())

    if len(resultado) > 0:
        session['login'] = login
        session['nome'] = resultado[0][1]
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
def adicionarlivro():
    titulo = request.form.get('titulo')
    autor = request.form.get('autor')
    editora = request.form.get('editora')
    login = session['login']

    if dao.adicionarlivro( titulo, autor, editora, login):
        return render_template('adicionarlivro.html', msg='Livro cadastrado com sucesso')
    else:
        return render_template('adicionarlivro.html', msg='Erro ao inserir Livro')


if __name__ == '__main__':

 app.run(debug=True)
