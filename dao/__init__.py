import psycopg2  # Certifique-se de ter o psycopg2 instalado
import logging

#para acessar o banco de dados, eu preciso de uma conexao.
#provê conexao com o banco de dados

def conectardb():
    con = psycopg2.connect(
        host='dpg-cumfc4aj1k6c73aljd60-a.oregon-postgres.render.com',
        database='livro_ppf1',
        user='livro_ppf1_user',
        password='3DHq3GOoM8R2OQMMjdd1FDuJ2Ww29qbu'
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
def adicionarusuario(login, senha, nome, conexao):
    #método para conectar o banco de dados, retornando a conexao com o BD
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

def adicionarlivro(titulo, autor, editora, login):
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO livros (titulo, autor, editora, login) VALUES ('{titulo}', '{autor}' , '{editora}', '{login}')"
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






