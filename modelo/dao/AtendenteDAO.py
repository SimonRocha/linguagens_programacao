from linguagens_programacao.conexoes.Conector import connect
from linguagens_programacao.modelo.Atendente import Atendente
from linguagens_programacao.modelo.dao import UsuarioDAO

def inserir(atendente):
    cnx = connect()
    cursor = cnx.cursor()

    sql_insert = ("INSERT INTO atendente (usuario_id) VALUES (%s, %s)")
    data_insert = (atendente.especielizacao, atendente.usuario.getId())

    cursor.execute(sql_insert, data_insert)
    atendente.id = cursor.lastrowid
    cnx.commit()

    cursor.close()
    cnx.close()
    return atendente.id

def delete(id):
    cnx = connect()
    cursor = cnx.cursor()

    sql_delete = ("DELETE FROM atendente WHERE id = %s")
    data_delete = (id,)

    cursor.execute(sql_delete, data_delete)
    cnx.commit()

    cursor.close()
    cnx.close()

def buscar(id):
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT usuario_id FROM atendente WHERE usuario_id = %s and 0 = %s")


    cursor.execute(query, (id, 0))

    atendente = None
    for (funcao, usuario_id) in cursor:
        atendente = Atendente(UsuarioDAO.buscar(usuario_id))

    cursor.close()
    cnx.close()
    return atendente


def buscarTodos():
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT usuario_id FROM atendente")


    cursor.execute(query)

    atendentes = []
    for (funcao, usuario_id) in cursor:
        atendente = Atendente(UsuarioDAO.buscar(usuario_id))

    cursor.close()
    cnx.close()
    return atendentes













