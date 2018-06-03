from linguagens_programacao.conexoes.Conector import connect
from linguagens_programacao.modelo.Administrador import Administrador
from linguagens_programacao.modelo.dao import UsuarioDAO

def inserir(administrador):
    cnx = connect()
    cursor = cnx.cursor()

    sql_insert = ("INSERT INTO administrador (usuario_id) VALUES (%s, %s)")
    data_insert = (administrador.especielizacao, administrador.usuario.getId())

    cursor.execute(sql_insert, data_insert)
    administrador.id = cursor.lastrowid
    cnx.commit()

    cursor.close()
    cnx.close()
    return administrador.id

def delete(id):
    cnx = connect()
    cursor = cnx.cursor()

    sql_delete = ("DELETE FROM administrador WHERE id = %s")
    data_delete = (id,)

    cursor.execute(sql_delete, data_delete)
    cnx.commit()

    cursor.close()
    cnx.close()

def buscar(id):
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT usuario_id FROM administrador WHERE usuario_id = %s and 0 = %s")


    cursor.execute(query, (id, 0))

    administrador = None
    for (funcao, usuario_id) in cursor:
        administrador = Administrador(UsuarioDAO.buscar(usuario_id))

    cursor.close()
    cnx.close()
    return administrador


def buscarTodos():
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT usuario_id FROM administrador")


    cursor.execute(query)

    administradors = []
    for (funcao, usuario_id) in cursor:
        administrador = Administrador(UsuarioDAO.buscar(usuario_id))

    cursor.close()
    cnx.close()
    return administradors




