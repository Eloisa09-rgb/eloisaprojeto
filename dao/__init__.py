import psycopg2  # Certifique-se de ter o psycopg2 instalado
import logging

#para acessar o banco de dados, eu preciso de uma conexao.
#provê conexao com o banco de dados

def conectardb():
    con = psycopg2.connect(
        host='dpg-cu2lq6pu0jms73apljc0-a.oregon-postgres.render.com',
        database='livro_ggm9',
        user='livro_ggm9_user',
        password='mTCebfzldtYm6WgS6xnR3HvfkeFoeTtZ'
    )
    return con

#verifica no banco de dados se existe um usuário com matrícula e a senha
#informadas por parâmetro
def verificarlogin(login, senha, conexao):

    cur = conexao.cursor()
    cur.execute(f"SELECT login, nome FROM usuarios WHERE login = '{login}' AND senha = '{senha}'")
    recset = cur.fetchall()
    cur.close()
    conexao.close()

    return recset

 #inserir usuario
def adicionarusuario(login, senha, nome):
    #método para conectar o banco de dados, retornando a conexao com o BD
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO usuarios (login, senha, nome) VALUES ('{login}', '{senha}', '{nome}')"
        cur.execute(sql)
    except psycopg2.Error:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito

def listarpessoas():
    conexao = conectardb()

    cur = conexao.cursor()
    cur.execute(f"SELECT * FROM usuarios")
    recset = cur.fetchall()
    conexao.close()

    return recset

def listarlivros(login):
    conexao = conectardb()

    cur = conexao.cursor()
    cur.execute(f"SELECT * FROM livros where login = '{login}'")
    recset = cur.fetchall()
    conexao.close()

    return recset

def adicionarlivro(titulo, autor, editora):
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO livros (titulo, autor, editora) VALUES ('{titulo}', '{autor}' , '{editora}')"
        cur.execute(sql)
    except psycopg2.Error as e:
        print(f"Erro ao adicionar livro: {e}")
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True


    conexao.close()
    return exito
import psycopg2  # Certifique-se de ter o psycopg2 instalado
import logging

# Configurar logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')






