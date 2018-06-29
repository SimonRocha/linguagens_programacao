from linguagens_programacao.conexoes.Conector import connect
from linguagens_programacao.modelo import Auxiliar
from linguagens_programacao.modelo.Auxiliar import Auxiliar
from linguagens_programacao.modelo.dao import UsuarioDAO

createAuxiliar = lambda lista: Auxiliar(UsuarioDAO.buscar(lista[0][0]).getId(), UsuarioDAO.buscar(lista[0][0]).getLogin(), UsuarioDAO.buscar(lista[0][0]).getSenha(), UsuarioDAO.buscar(lista[0][0]).getTipo(), UsuarioDAO.buscar(lista[0][0]).getNome(), UsuarioDAO.buscar(lista[0][0]).getDocumento(), lista[0][1])
createAuxiliarT = lambda lista: Auxiliar(UsuarioDAO.buscar(lista[0]).getId(), UsuarioDAO.buscar(lista[0]).getLogin(), UsuarioDAO.buscar(lista[0]).getSenha(), UsuarioDAO.buscar(lista[0]).getTipo(), UsuarioDAO.buscar(lista[0]).getNome(), UsuarioDAO.buscar(lista[0]).getDocumento(), lista[1])


def inserir(auxiliar):
    cnx = connect()
    cursor = cnx.cursor()

    p = UsuarioDAO.inserir(auxiliar)

    sql_insert = ("INSERT INTO auxiliar (funcao, usuario_id) VALUES (%s, %s)")
    data_insert = (auxiliar.getFuncao(), p)

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

    query = ("SELECT usuario_id, funcao FROM auxiliar WHERE usuario_id = %s and 0 = %s")


    cursor.execute(query, (id, 0))

    result = cursor.fetchall()
    auxiliar = createAuxiliar([x for x in result])

    cursor.close()
    cnx.close()
    return auxiliar


def buscarTodos():
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT  usuario_id, funcao FROM auxiliar")

    cursor.execute(query)

    result = cursor.fetchall()

    auxiliares = []
    for x in result:
        auxiliares.append(createAuxiliarT(x))

    cursor.close()
    cnx.close()
    return auxiliares






