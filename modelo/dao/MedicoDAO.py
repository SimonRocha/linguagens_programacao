from linguagens_programacao.conexoes.Conector import connect
from linguagens_programacao.modelo.Medico import Medico
from linguagens_programacao.modelo.dao import UsuarioDAO

def inserir(medico):
    cnx = connect()
    cursor = cnx.cursor()

    sql_insert = ("INSERT INTO medico (especializacao, usuario_id) VALUES (%s, %s)")
    data_insert = (medico.especielizacao, medico.usuario.getId())

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

    query = ("SELECT especializacao, usuario_id FROM medico WHERE usuario_id = %s and 0 = %s")


    cursor.execute(query, (id, 0))

    medico = None
    for (especializacao, usuario_id) in cursor:
        medico = Medico(especializacao, UsuarioDAO.buscar(usuario_id))

    cursor.close()
    cnx.close()
    return medico


def buscarTodos():
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT  especializacao, usuario_id FROM medico")


    cursor.execute(query)

    medicos = []
    for (especializacao, usuario_id) in cursor:
        medico = Medico(especializacao, UsuarioDAO.buscar(usuario_id))

    cursor.close()
    cnx.close()
    return medicos













