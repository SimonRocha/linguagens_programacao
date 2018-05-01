from linguagens_programacao.modelo import Paciente, Administrador, Auxiliar, Atendente, Medico, Consulta
from linguagens_programacao.modelo.dao import PacienteDAO, AdministradorDAO, AuxiliarDAO, AtendenteDAO, ConsultaDAO, MedicoDAO, UsuarioDAO

def listarTodosPaciente():
    todos = PacienteDAO.buscarTodos()

    if (todos != None):
        return todos
    else:
        return 0


def listarTodosAdministrador():
    todos = AdministradorDAO.buscarTodos()

    if (todos != None):
        return todos
    else:
        return 0


def listarTodosAuxiliar():
    todos = AuxiliarDAO.buscarTodos()

    if (todos != None):
        return todos
    else:
        return 0


def listarTodosAtendente():
    todos = AtendenteDAO.buscarTodos()

    if (todos != None):
        return todos
    else:
        return 0


def listarTodosConsulta():
    todos = ConsultaDAO.buscarTodos()

    if (todos != None):
        return todos
    else:
        return 0


def listarTodosMedico():
    todos = MedicoDAO.buscarTodos()

    if (todos != None):
        return todos
    else:
        return 0


def listarTodosUsuario():
    todos = UsuarioDAO.buscarTodos()

    if (todos != None):
        return todos
    else:
        return 0

def buscarPaciente(id):
    um = PacienteDAO.buscar(id)

    if (um != None):
        return um
    else:
        return 0

def buscarAdministrador(id):
    um = AdministradorDAO.buscar(id)

    if (um != None):
        return um
    else:
        return 0

def buscarAuxiliar(id):
    um = AuxiliarDAO.buscar(id)

    if (um != None):
        return um
    else:
        return 0

def buscarAtendente(id):
    um = AtendenteDAO.buscar(id)

    if (um != None):
        return um
    else:
        return 0

def buscarConsulta(id):
    um = ConsultaDAO.buscar(id)

    if (um != None):
        return um
    else:
        return 0

def buscarMedico(id):
    um = MedicoDAO.buscar(id)

    if (um != None):
        return um
    else:
        return 0