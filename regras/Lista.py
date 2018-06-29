from linguagens_programacao.modelo import Paciente, Administrador, Auxiliar, Atendente, Medico, Consulta
from linguagens_programacao.modelo.dao import PacienteDAO, AdministradorDAO, AuxiliarDAO, AtendenteDAO, ConsultaDAO, MedicoDAO, UsuarioDAO

def listarTodosPaciente():
    todos = PacienteDAO.buscarTodos()

    if (todos != None):
        return todos
    else:
        return 0

def listarTodosPacienteNome(nome):
    todos = PacienteDAO.buscarTodos()

    filtrados = list(filter(lambda paciente: paciente.getPaciente().getNome() == nome, todos))
    return filtrados

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


def listarTodasConsultasPacienteId(id_paciente):
    todos = ConsultaDAO.buscarTodos()

    filtrados = list(filter(lambda consulta: consulta.getPaciente().getId() == id_paciente, todos))
    return filtrados

def listarTodasConsultasPacienteNome(nome):
    todos = ConsultaDAO.buscarTodos()

    filtrados = list(filter(lambda consulta: consulta.getPaciente().getNome() == nome, todos))
    return filtrados

def listarTodasConsultasMedicoId(id):
    todos = ConsultaDAO.buscarTodos()

    filtrados = list(filter(lambda consulta: consulta.getMedico().getId() == id, todos))
    return filtrados

def listarTodasConsultasMedicoNome(nome):
    todos = ConsultaDAO.buscarTodos()

    filtrados = list(filter(lambda consulta: consulta.getMedico().getNome() == nome, todos))
    return filtrados


def listarTodasConsultasUsuarioId(id):
    todos = ConsultaDAO.buscarTodos()

    filtrados = list(filter(lambda consulta: consulta.getUsuarioRegistro().getId() == id, todos))
    return filtrados

def listarTodasConsultasUsuarioNome(nome):
    todos = ConsultaDAO.buscarTodos()

    filtrados = list(filter(lambda consulta: consulta.getUsuarioRegistro().getNome() == nome, todos))
    return filtrados


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
