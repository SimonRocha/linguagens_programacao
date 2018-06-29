from linguagens_programacao.conexoes.Conector import connect
from linguagens_programacao.modelo.Usuario import Usuario

createUsuario = lambda lista: Usuario(lista[0][0], lista[0][1], lista[0][2], lista[0][3], lista[0][4], lista[0][5])
createUsuarioT = lambda lista: Usuario(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5])

def login(login, senha):
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT id, login, senha, tipo, nome, documento FROM usuario WHERE login = %s and senha = %s")

    cursor.execute(query, (login, senha))

    result = cursor.fetchall()
    usuario = createUsuario([x for x in result])

    cursor.close()
    cnx.close()
    return usuario


def inserir(usuario):
    cnx = connect()
    cursor = cnx.cursor()

    sql_insert = ("INSERT INTO usuario (login, senha, tipo, nome, documento ) VALUES (%s, %s, %s, %s, %s)")
    data_insert = (usuario.getLogin(), usuario.getSenha(), usuario.getTipo(), usuario.getNome(), usuario.getDocumento())

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

    query = ("SELECT id, login, senha, tipo, nome, documento  FROM usuario WHERE id = %s and 0 = %s")

    cursor.execute(query, (id, 0))

    result = cursor.fetchall()
    usuario = createUsuario([x for x in result])

    cursor.close()
    cnx.close()
    return usuario

def buscarTodos():
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT  id, login, senha, tipo, nome, documento FROM usuario")
    cursor.execute(query)

    result = cursor.fetchall()

    usuarios = []
    print(result)
    for x in result:
        usuarios.append(createUsuarioT(x))

    cursor.close()
    cnx.close()
    return usuarios


















