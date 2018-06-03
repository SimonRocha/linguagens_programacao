from linguagens_programacao.conexoes.Conector import connect
from linguagens_programacao.modelo.Paciente import Paciente

def inserir(paciente):
    cnx = connect()
    cursor = cnx.cursor()

    sql_insert = ("INSERT INTO paciente (nome, documento, dt_nascimento, dt_entrada) VALUES (%s, %s, %s)")
    data_insert = (paciente.nome, paciente.documento, paciente.dt_nascimento, paciente.dt_entrada )

    cursor.execute(sql_insert, data_insert)
    paciente.id = cursor.lastrowid
    cnx.commit()

    cursor.close()
    cnx.close()
    return paciente.id

def delete(id):
    cnx = connect()
    cursor = cnx.cursor()

    sql_delete = ("DELETE FROM paciente WHERE id = %s")
    data_delete = (id,)

    cursor.execute(sql_delete, data_delete)
    cnx.commit()

    cursor.close()
    cnx.close()

def buscar(id):
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT idPaciente, nome, documento, dt_nascimento, dt_entrada FROM paciente WHERE id = %s and 0 = %s")


    cursor.execute(query, (id, 0))

    paciente = None
    for (idPaciente, nome, documento, dt_nascimento, dt_entrada) in cursor:
        paciente = Paciente(idPaciente, nome, documento, dt_nascimento, dt_entrada)

    cursor.close()
    cnx.close()
    return paciente


def buscarTodos():
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT idPaciente, nome, documento, dt_nascimento, dt_entrada FROM paciente")


    cursor.execute(query)

    pacientes = []
    for (idPaciente, nome, documento, dt_nascimento, dt_entrada) in cursor:
        pacientes.append(Paciente(idPaciente, nome, documento, dt_nascimento, dt_entrada))

    cursor.close()
    cnx.close()
    return pacientes













