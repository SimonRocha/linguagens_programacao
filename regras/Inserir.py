from linguagens_programacao.modelo import Paciente, Administrador, Auxiliar, Atendente, Medico, Consulta
from linguagens_programacao.modelo.dao import PacienteDAO, AdministradorDAO, AuxiliarDAO, AtendenteDAO, ConsultaDAO, MedicoDAO

def inserirPaciente(nome, documento, dt_nascimento, dt_entrada):
    p = Paciente(999, nome, documento, dt_nascimento, dt_entrada)

    p = PacienteDAO.inserir(p)

    if (p != None):
        return 1
    else:
        return 0


def inserirAdministrador(login, senha, tipo, nome, documento):
    p = Administrador(999, login, senha, tipo, nome, documento)

    p = AdministradorDAO.inserir(p)

    if (p != None):
        return 1
    else:
        return 0


def inserirAuxiliar(login, senha, tipo, nome, documento, funcao):
    p = Auxiliar(999, login, senha, tipo, nome, documento, funcao)

    p = AuxiliarDAO.inserir(p)

    if (p != None):
        return 1
    else:
        return 0


def inserirAtendente(login, senha, tipo, nome, documento):
    p = Atendente(999, login, senha, tipo, nome, documento)

    p = AtendenteDAO.inserir(p)

    if (p != None):
        return 1
    else:
        return 0


def inserirMedico(login, senha, tipo, nome, documento, especializacao):
    p = Medico(999, login, senha, tipo, nome, documento, especializacao)

    p = MedicoDAO.inserir(p)

    if (p != None):
        return 1
    else:
        return 0


def inserirConsulta(nome,  usuarioRegistro, medico, paciente, auxiliares, dt_registro, dt_consulta, status):
    p = Consulta(999, nome,  usuarioRegistro, medico, paciente, auxiliares, dt_registro, dt_consulta, status)

    p = ConsultaDAO.inserir(p)

    if (p != None):
        return 1
    else:
        return 0