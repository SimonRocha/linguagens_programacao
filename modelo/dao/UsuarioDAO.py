from conexao.Conector import connect
from linguagens_programacao.modelo.Usuario import Usuario

def login(login, senha):
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT id, login, senha, tipo FROM usuario WHERE login = %s and senha = %s")


    cursor.execute(query, (login, senha))

    usuario = None
    for (id, login, senha, tipo) in cursor:
        usuario = Usuario(id, login, senha, tipo)

    cursor.close()
    cnx.close()
    return usuario

def inserir(usuario):
    cnx = connect()
    cursor = cnx.cursor()

    sql_insert = ("INSERT INTO usuario (login, senha, tipo) VALUES (%s, %s, %s)")
    data_insert = (usuario.login, usuario.senha, usuario.tipo)

    cursor.execute(sql_insert, data_insert)
    usuario.id = cursor.lastrowid
    cnx.commit()

    cursor.close()
    cnx.close()
    return usuario.id

def delete(id):
    cnx = connect()
    cursor = cnx.cursor()

    sql_delete = ("DELETE FROM usuario WHERE id = %s")
    data_delete = (id,)

    cursor.execute(sql_delete, data_delete)
    cnx.commit()

    cursor.close()
    cnx.close()

def buscar(id):
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT id, login, senha, tipo FROM usuario WHERE id = %s and 0 = %s")


    cursor.execute(query, (id, 0))

    usuario = None
    for (id, login, senha, tipo) in cursor:
        usuario = Usuario(id, login, senha, tipo)

    cursor.close()
    cnx.close()
    return usuario


def buscarTodos():
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT id, login, senha, tipo FROM usuario")


    cursor.execute(query)

    usuarios = []
    for (id, login, senha, tipo) in cursor:
        usuarios.append(Usuario(id, login, senha, tipo))

    cursor.close()
    cnx.close()
    return usuarios













