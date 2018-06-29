from linguagens_programacao.conexoes.Conector import connect
from linguagens_programacao.modelo.Paciente import Paciente

createPaciente = lambda lista: Paciente(lista[0][0], lista[0][1], lista[0][2], lista[0][3], lista[0][4])
createPacienteT = lambda lista: Paciente(lista[0], lista[1], lista[2], lista[3], lista[4])

def inserir(paciente):
    cnx = connect()
    cursor = cnx.cursor()

    sql_insert = ("INSERT INTO paciente (nome, documento, dt_nascimento, dt_entrada) VALUES (%s, %s, %s, %s)")
    data_insert = (paciente.getNome(), paciente.getDocumento(), paciente.getDt_nascimento(), paciente.getDt_entrada())

    cursor.execute(sql_insert, data_insert)
    paciente.id = cursor.lastrowid
    cnx.commit()

    cursor.close()
    cnx.close()
    return paciente

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

    query = ("SELECT idPaciente, nome, documento, dt_nascimento, dt_entrada FROM paciente WHERE idPaciente = %s and 0 = %s")

    cursor.execute(query, (id, 0))

    result = cursor.fetchall()
    paciente = createPaciente([x for x in result])

    cursor.close()
    cnx.close()
    return paciente


def buscarTodos():
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT idPaciente, nome, documento, dt_nascimento, dt_entrada FROM paciente")

    cursor.execute(query)
    result = cursor.fetchall()

    pacientes = []
    print(result)
    for x in result:
        pacientes.append(createPacienteT(x))

    cursor.close()
    cnx.close()
    return pacientes














