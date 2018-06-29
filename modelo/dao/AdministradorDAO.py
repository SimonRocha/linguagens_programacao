from linguagens_programacao.conexoes.Conector import connect
from linguagens_programacao.modelo.Administrador import Administrador
from linguagens_programacao.modelo.dao import UsuarioDAO

createAdministrador = lambda lista: Administrador(UsuarioDAO.buscar(lista[0][0]).getId(), UsuarioDAO.buscar(lista[0][0]).getLogin(), UsuarioDAO.buscar(lista[0][0]).getSenha(), UsuarioDAO.buscar(lista[0][0]).getTipo(), UsuarioDAO.buscar(lista[0][0]).getNome(), UsuarioDAO.buscar(lista[0][0]).getDocumento())
createAdministradorT = lambda lista: Administrador(UsuarioDAO.buscar(lista[0]).getId(), UsuarioDAO.buscar(lista[0]).getLogin(), UsuarioDAO.buscar(lista[0]).getSenha(), UsuarioDAO.buscar(lista[0]).getTipo(), UsuarioDAO.buscar(lista[0]).getNome(), UsuarioDAO.buscar(lista[0]).getDocumento())


def inserir(administrador):
    cnx = connect()
    cursor = cnx.cursor()

    p = UsuarioDAO.inserir(administrador)

    sql_insert = ("INSERT INTO administrador (usuario_id) VALUES (%s)")
    data_insert = (p,)

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

    result = cursor.fetchall()
    administrador = createAdministrador([x for x in result])

    cursor.close()
    cnx.close()
    return administrador


def buscarTodos():
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT usuario_id FROM administrador")


    cursor.execute(query)

    result = cursor.fetchall()
    administradores = []
    for x in result:
        administradores.append(createAdministradorT(x))

    cursor.close()
    cnx.close()
    return administradores



