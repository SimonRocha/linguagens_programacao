from linguagens_programacao.modelo import Paciente, Administrador, Auxiliar, Atendente, Medico, Consulta
from linguagens_programacao.modelo.dao import PacienteDAO, AdministradorDAO, AuxiliarDAO, AtendenteDAO, ConsultaDAO, MedicoDAO

def removerPaciente(id):
    p = PacienteDAO.delete(id)

    if (p != None):
        return 1
    else:
        return 0

def removerAdministrador(id):
    p = AdministradorDAO.delete(id)

    if (p != None):
        return 1
    else:
        return 0

def removerAuxiliar(id):
    p = AuxiliarDAO.delete(id)

    if (p != None):
        return 1
    else:
        return 0

def removerAtendente(id):
    p = AtendenteDAO.delete(id)

    if (p != None):
        return 1
    else:
        return 0

def removerMedico(id):
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