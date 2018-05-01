from linguagens_programacao.modelo import Paciente, Administrador, Auxiliar, Atendente, Medico, Consulta
from linguagens_programacao.modelo.dao import PacienteDAO, AdministradorDAO, AuxiliarDAO, AtendenteDAO, ConsultaDAO, MedicoDAO

def editarPaciente(id, nome, documento, dt_nascimento, dt_entrada):
    p = Paciente(id, nome, documento, dt_nascimento, dt_entrada)

    p = PacienteDAO.editar(p)

    if (p != None):
        return 1
    else:
        return 0


def editarAdministrador(id, login, senha, tipo, nome, documento):
    p = Administrador(id, login, senha, tipo, nome, documento)

    p = AdministradorDAO.editar(p)

    if (p != None):
        return 1
    else:
        return 0


def editarAuxiliar(id,login, senha, tipo, nome, documento, funcao):
    p = Auxiliar(id, login, senha, tipo, nome, documento, funcao)

    p = AuxiliarDAO.editar(p)

    if (p != None):
        return 1
    else:
        return 0


def editarAtendente(id,login, senha, tipo, nome, documento):
    p = Atendente(id, login, senha, tipo, nome, documento)

    p = AtendenteDAO.editar(p)

    if (p != None):
        return 1
    else:
        return 0


def editarMedico(id,login, senha, tipo, nome, documento, especializacao):
    p = Medico(id, login, senha, tipo, nome, documento, especializacao)

    p = MedicoDAO.editar(p)

    if (p != None):
        return 1
    else:
        return 0


def editarConsulta(id, nome,  usuarioRegistro, medico, paciente, auxiliares, dt_registro, dt_consulta, status):
    p = Consulta(id, nome,  usuarioRegistro, medico, paciente, auxiliares, dt_registro, dt_consulta, status)

    p = ConsultaDAO.editar(p)

    if (p != None):
        return 1
    else:
        return 0