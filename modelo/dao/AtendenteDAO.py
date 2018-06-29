from linguagens_programacao.conexoes.Conector import connect
from linguagens_programacao.modelo.Atendente import Atendente
from linguagens_programacao.modelo.dao import UsuarioDAO

createAtendente = lambda lista: Atendente(UsuarioDAO.buscar(lista[0][0]).getId(), UsuarioDAO.buscar(lista[0][0]).getLogin(), UsuarioDAO.buscar(lista[0][0]).getSenha(), UsuarioDAO.buscar(lista[0][0]).getTipo(), UsuarioDAO.buscar(lista[0][0]).getNome(), UsuarioDAO.buscar(lista[0][0]).getDocumento())
createAtendenteT = lambda lista: Atendente(UsuarioDAO.buscar(lista[0]).getId(), UsuarioDAO.buscar(lista[0]).getLogin(), UsuarioDAO.buscar(lista[0]).getSenha(), UsuarioDAO.buscar(lista[0]).getTipo(), UsuarioDAO.buscar(lista[0]).getNome(), UsuarioDAO.buscar(lista[0]).getDocumento())


def inserir(atendente):
    cnx = connect()
    cursor = cnx.cursor()

    p = UsuarioDAO.inserir(atendente)

    sql_insert = ("INSERT INTO atendente (usuario_id) VALUES (%s)")
    data_insert = (p,)

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

    result = cursor.fetchall()
    atendente = createAtendente([x for x in result])

    cursor.close()
    cnx.close()
    return atendente



def buscarTodos():
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT usuario_id FROM atendente")


    cursor.execute(query)

    result = cursor.fetchall()

    atendentes = []
    for x in result:
        atendentes.append(createAtendenteT(x))

    cursor.close()
    cnx.close()
    return atendentes














