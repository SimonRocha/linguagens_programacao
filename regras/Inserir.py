from linguagens_programacao.modelo import Paciente, Administrador, Auxiliar, Atendente, Medico, Consulta, Usuario
from linguagens_programacao.modelo.Paciente import Paciente
from linguagens_programacao.modelo.Administrador import Administrador
from linguagens_programacao.modelo.Auxiliar import Auxiliar
from linguagens_programacao.modelo.Atendente import Atendente
from linguagens_programacao.modelo.Medico import Medico
from linguagens_programacao.modelo.Consulta import Consulta
from linguagens_programacao.modelo.Usuario import Usuario
from linguagens_programacao.modelo.dao import  AdministradorDAO, AuxiliarDAO, AtendenteDAO, ConsultaDAO

from linguagens_programacao.modelo.dao import UsuarioDAO, PacienteDAO, MedicoDAO

usuarioADM = lambda tipo : tipo == 0
usuarioAtendente = lambda tipo : tipo == 4
inserirLambda = lambda insertT, tipoUser, obj: insertT(obj) if (usuarioADM(tipoUser)) else print("Você não é administrador")
inserirLambdaFree = lambda insertT, obj: insertT(obj)

def inserirPaciente(nome, documento, dt_nascimento, dt_entrada):

        p = inserirLambda(PacienteDAO.inserir, Usuario.usuarioLogado.getTipo(), Paciente(999, nome, documento, dt_nascimento, dt_entrada))

        if (p != None):
            return p
        else:
            return 0



def inserirAdministrador(login, senha, tipo, nome, documento):
        p = inserirLambda(AdministradorDAO.inserir, Usuario.usuarioLogado.getTipo(),
                          Administrador(999, login, senha, tipo, nome, documento))

        if (p != None):
            return p
        else:
            return 0


def inserirAuxiliar(login, senha, tipo, nome, documento, funcao):
    p = inserirLambda(AuxiliarDAO.inserir, Usuario.usuarioLogado.getTipo(),
                      Auxiliar(999, login, senha, tipo, nome, documento, funcao))

    if (p != None):
        return p
    else:
        return 0



def inserirAtendente(login, senha, tipo, nome, documento):
    p = inserirLambda(AtendenteDAO.inserir, Usuario.usuarioLogado.getTipo(),
                      Atendente(999, login, senha, tipo, nome, documento))

    if (p != None):
        return p
    else:
        return 0

def inserirMedico(login, senha, tipo, nome, documento, especializacao):
    p = inserirLambda(MedicoDAO.inserir, Usuario.usuarioLogado.getTipo(),
                      Medico(999, login, senha, tipo, nome, documento, especializacao))

    if (p != None):
        return p
    else:
        return 0


def inserirConsulta(nome,  usuarioRegistro, medico, paciente, auxiliares, dt_registro, dt_consulta, status, valor):
    p = inserirLambdaFree(ConsultaDAO.inserir,
                      Consulta(999, usuarioRegistro, medico, paciente, auxiliares, dt_registro, dt_consulta, status, valor))

    if (p != None):
        return p
    else:
        return 0
