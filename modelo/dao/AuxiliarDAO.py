from linguagens_programacao.conexoes.Conector import connect
from linguagens_programacao.modelo.Auxiliar import Auxiliar
from linguagens_programacao.modelo.dao import UsuarioDAO

def inserir(auxiliar):
    cnx = connect()
    cursor = cnx.cursor()

    sql_insert = ("INSERT INTO auxiliar (funcao, usuario_id) VALUES (%s, %s)")
    data_insert = (auxiliar.especielizacao, auxiliar.usuario.getId())

    cursor.execute(sql_insert, data_insert)
    auxiliar.id = cursor.lastrowid
    cnx.commit()

    cursor.close()
    cnx.close()
    return auxiliar.id

def delete(id):
    cnx = connect()
    cursor = cnx.cursor()

    sql_delete = ("DELETE FROM auxiliar WHERE id = %s")
    data_delete = (id,)

    cursor.execute(sql_delete, data_delete)
    cnx.commit()

    cursor.close()
    cnx.close()

def buscar(id):
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT funcao, usuario_id FROM auxiliar WHERE usuario_id = %s and 0 = %s")


    cursor.execute(query, (id, 0))

    auxiliar = None
    for (funcao, usuario_id) in cursor:
        auxiliar = Auxiliar(funcao, UsuarioDAO.buscar(usuario_id))

    cursor.close()
    cnx.close()
    return auxiliar


def buscarTodos():
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT  funcao, usuario_id FROM auxiliar")


    cursor.execute(query)

    auxiliars = []
    for (funcao, usuario_id) in cursor:
        auxiliar = Auxiliar(funcao, UsuarioDAO.buscar(usuario_id))

    cursor.close()
    cnx.close()
    return auxiliars













