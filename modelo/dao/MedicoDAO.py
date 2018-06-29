from linguagens_programacao.conexoes.Conector import connect
from linguagens_programacao.modelo.Medico import Medico
from linguagens_programacao.modelo.dao import UsuarioDAO

createMedico = lambda lista: Medico(UsuarioDAO.buscar(lista[0][0]).getId(), UsuarioDAO.buscar(lista[0][0]).getLogin(), UsuarioDAO.buscar(lista[0][0]).getSenha(), UsuarioDAO.buscar(lista[0][0]).getTipo(), UsuarioDAO.buscar(lista[0][0]).getNome(), UsuarioDAO.buscar(lista[0][0]).getDocumento(), lista[0][1])
createMedicoT = lambda lista: Medico(UsuarioDAO.buscar(lista[0]).getId(), UsuarioDAO.buscar(lista[0]).getLogin(), UsuarioDAO.buscar(lista[0]).getSenha(), UsuarioDAO.buscar(lista[0]).getTipo(), UsuarioDAO.buscar(lista[0]).getNome(), UsuarioDAO.buscar(lista[0]).getDocumento(), lista[1])

def inserir(medico):
    cnx = connect()
    cursor = cnx.cursor()

    id = UsuarioDAO.inserir(medico)

    sql_insert = ("INSERT INTO medico (especializacao, usuario_id) VALUES (%s, %s)")
    data_insert = (medico.getEspecializaca(), id)

    cursor.execute(sql_insert, data_insert)
    medico.id = cursor.lastrowid
    cnx.commit()

    cursor.close()
    cnx.close()
    return medico.id


def delete(id):
    cnx = connect()
    cursor = cnx.cursor()

    sql_delete = ("DELETE FROM medico WHERE id = %s")
    data_delete = (id,)

    cursor.execute(sql_delete, data_delete)
    cnx.commit()

    cursor.close()
    cnx.close()

def buscar(id):
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT usuario_id, especializacao FROM medico WHERE usuario_id = %s and 0 = %s")

    cursor.execute(query, (id, 0))

    result = cursor.fetchall()
    medico = createMedico([x for x in result])

    cursor.close()
    cnx.close()
    return medico

def buscarTodos():
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT usuario_id, especializacao FROM medico")

    cursor.execute(query)

    result = cursor.fetchall()

    medicos = []
    print(result)
    for x in result:
        medicos.append(createMedicoT(x))

    cursor.close()
    cnx.close()
    return medicos












