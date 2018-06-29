from linguagens_programacao.conexoes.Conector import connect
from linguagens_programacao.modelo.Consulta import Consulta
from linguagens_programacao.modelo.dao import UsuarioDAO, PacienteDAO, MedicoDAO

createConsulta = lambda lista: Consulta(lista[0][0], UsuarioDAO.buscar(lista[0][1]), MedicoDAO.buscar(lista[0][2]), PacienteDAO.buscar(lista[0][3]), "", lista[0][4], lista[0][5], lista[0][6], lista[0][7])
createConsultaT = lambda v: Consulta(v[0], UsuarioDAO.buscar(v[1]), MedicoDAO.buscar(v[2]), PacienteDAO.buscar(v[3]), "", v[4], v[5], v[6], v[7])


def inserir(consulta):
    cnx = connect()
    cursor = cnx.cursor()

    sql_insert = ("INSERT INTO consulta (Paciente_idPaciente, Usuario_id, dt_registro, dt_consulta, valor, id_medico, status) VALUES (%s, %s, %s, %s, %s, %s, %s)")
    data_insert = (consulta.getPaciente().getId(), consulta.getUsuarioRegistro().getId(), consulta.getDt_registro(), consulta.getDt_consulta(), consulta.getValor(), consulta.getMedico().getId(), consulta.getStatus())

    cursor.execute(sql_insert, data_insert)
    consulta.id = cursor.lastrowid
    cnx.commit()

    cursor.close()
    cnx.close()
    return consulta.id

def delete(id):
    cnx = connect()
    cursor = cnx.cursor()

    sql_delete = ("DELETE FROM consulta WHERE id = %s")
    data_delete = (id,)

    cursor.execute(sql_delete, data_delete)
    cnx.commit()

    cursor.close()
    cnx.close()

def buscar(id):
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT idConsulta, Usuario_id, id_medico, Paciente_idPaciente, dt_registro, dt_consulta, status, valor FROM consulta WHERE idConsulta = %s and 0 = %s")

    cursor.execute(query, (id, 0))

    result = cursor.fetchall()
    consulta = createConsulta([x for x in result])

    cnx.close()
    return consulta


def buscarTodos():
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT idConsulta, Usuario_id, id_medico, Paciente_idPaciente, dt_registro, dt_consulta, status, valor FROM consulta")


    cursor.execute(query)

    result = cursor.fetchall()

    consultas = []
    for x in result:
        consultas.append(createConsultaT(x))

    cursor.close()
    cnx.close()
    return consultas

def buscarTodosData(dt_inicio, dt_fim):
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT idConsulta, Usuario_id, id_medico, Paciente_idPaciente, dt_registro, dt_consulta, status, valor FROM consulta WHERE dt_consulta between %s and %s")

    cursor.execute(query, (dt_inicio, dt_fim))

    result = cursor.fetchall()

    consultas = []
    for x in result:
        consultas.append(createConsultaT(x))

    cursor.close()
    cnx.close()
    return consultas














