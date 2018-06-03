from linguagens_programacao.modelo import Paciente, Administrador, Auxiliar, Atendente, Medico, Consulta, Usuario
from linguagens_programacao.modelo.dao import PacienteDAO, AdministradorDAO, AuxiliarDAO, AtendenteDAO, ConsultaDAO, MedicoDAO

def removerPaciente(id):
    if (isinstance(Usuario.usuarioLogado, Administrador)):
        p = PacienteDAO.delete(id)

        if (p != None):
            return 1
        else:
            return 0

def removerAdministrador(id):
    if (isinstance(Usuario.usuarioLogado, Administrador)):
        p = AdministradorDAO.delete(id)

        if (p != None):
            return 1
        else:
            return 0

def removerAuxiliar(id):
    if (isinstance(Usuario.usuarioLogado, Administrador)):
        p = AuxiliarDAO.delete(id)

        if (p != None):
            return 1
        else:
            return 0

def removerAtendente(id):
    if (isinstance(Usuario.usuarioLogado, Administrador)):
        p = AtendenteDAO.delete(id)

        if (p != None):
            return 1
        else:
            return 0

def removerMedico(id):
    if (isinstance(Usuario.usuarioLogado, Administrador)):
        p = ConsultaDAO.delete(id)

        if (p != None):
            return 1
        else:
            return 0

def removerConsulta(id):
    p = MedicoDAO.delete(id)

    if (p != None):
        return 1
    else:
        return 0