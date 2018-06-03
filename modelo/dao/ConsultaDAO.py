from linguagens_programacao.conexoes.Conector import connect
from linguagens_programacao.modelo.Consulta import Consulta
from linguagens_programacao.modelo.dao import UsuarioDAO, PacienteDAO

def inserir(consulta):
    cnx = connect()
    cursor = cnx.cursor()

    sql_insert = ("INSERT INTO consulta (Paciente_idPaciente, Usuario_id, dt_registro, dt_consulta, valor) VALUES (%s, %s, %s, %s, %s)")
    data_insert = (consulta.getPaciente().getId(), consulta.getUsuarioRegistro().getId(), consulta.dt_registro, consulta.dt_consulta, consulta.valor)

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

    query = ("SELECT idConsulta, Paciente_idPaciente, Usuario_id, dt_registro, dt_consulta, valor FROM consulta WHERE idConsulta = %s and 0 = %s")


    cursor.execute(query, (id, 0))

    consulta = None
    for (idConsulta, Paciente_idPaciente, Usuario_id, dt_registro, dt_consulta, valor) in cursor:
        consulta = Consulta(idConsulta, PacienteDAO.buscar(Paciente_idPaciente), UsuarioDAO.buscar(Usuario_id), dt_registro, dt_consulta, valor)

    cursor.close()
    cnx.close()
    return consulta


def buscarTodos():
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT idConsulta, Paciente_idPaciente, Usuario_id, dt_registro, dt_consulta, valor FROM consulta")


    cursor.execute(query)

    consultas = []
    for (idConsulta, Paciente_idPaciente, Usuario_id, dt_registro, dt_consulta, valor) in cursor:
        consulta = Consulta(idConsulta, PacienteDAO.buscar(Paciente_idPaciente), UsuarioDAO.buscar(Usuario_id), dt_registro, dt_consulta, valor)

    cursor.close()
    cnx.close()
    return consultas


def relatorioGanhos(dt_inicio, dt_fim, valor):
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT idConsulta, Paciente_idPaciente, Usuario_id, dt_registro, dt_consulta, valor FROM consulta WHERE dt_consulta between %s and %s AND valor = %s")

    cursor.execute(query, (dt_inicio, dt_fim, valor))

    consultas = []
    for (idConsulta, Paciente_idPaciente, Usuario_id, dt_registro, dt_consulta, valor) in cursor:
        consulta = Consulta(idConsulta, PacienteDAO.buscar(Paciente_idPaciente), UsuarioDAO.buscar(Usuario_id),
                            dt_registro, dt_consulta, valor)

    cursor.close()
    cnx.close()
    return consultas

def folhaPagamento(dt_inicio, dt_fim, usuaario):
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT idConsulta, Paciente_idPaciente, Usuario_id, dt_registro, dt_consulta, valor FROM consulta WHERE dt_consulta between %s and %s AND Usuario_id = %s")

    cursor.execute(query, (dt_inicio, dt_fim, usuaario.getID()))

    consultas = []
    for (idConsulta, Paciente_idPaciente, Usuario_id, dt_registro, dt_consulta, valor) in cursor:
        consulta = Consulta(idConsulta, PacienteDAO.buscar(Paciente_idPaciente), UsuarioDAO.buscar(Usuario_id),
                            dt_registro, dt_consulta, valor)

    cursor.close()
    cnx.close()
    return consultas













