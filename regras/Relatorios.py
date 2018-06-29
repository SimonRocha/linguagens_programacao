from linguagens_programacao.modelo import Usuario, Administrador, Atendente, Auxiliar, Consulta
from linguagens_programacao.modelo.dao import UsuarioDAO, ConsultaDAO

usuarioADM = lambda tipo : tipo == 0
usuarioMedico = lambda tipo : tipo == 2
usuarioAtendente = lambda tipo : tipo == 4

def relatorioGanhosMedicoValor(dt_inicio, dt_fim, medico, valor):
    consultas = ConsultaDAO.buscarTodos()

    consultas = list(filter(lambda consulta: usuarioADM(Usuario.usuarioLogado.getTipo()) and consulta.getMedico().getId() == medico and valor == consulta.getValor(), consultas))
    return consultas

def ganhosMedicoValor(dt_inicio, dt_fim, medico, valor):
    consultas = ConsultaDAO.buscarTodosData(dt_inicio, dt_fim)

    consultas = list(filter(lambda consulta: usuarioADM(Usuario.usuarioLogado.getTipo()) and consulta.getMedico().getId() == medico and valor == consulta.getValor(), consultas))
    valorTotal = sum(c.getValor() for c in consultas)

    return valorTotal

def relatorioGanhosMedico(dt_inicio, dt_fim, medico):
    consultas = ConsultaDAO.buscarTodosData(dt_inicio, dt_fim)

    consultas = list(filter(lambda consulta: usuarioADM(Usuario.usuarioLogado.getTipo()) and consulta.getMedico().getId() == medico, consultas))
    return consultas

def ganhosMedico(dt_inicio, dt_fim, medico):
    consultas = ConsultaDAO.buscarTodosData(dt_inicio, dt_fim)

    consultas = list(filter(lambda consulta: usuarioADM(Usuario.usuarioLogado.getTipo()) and consulta.getMedico().getId() == medico, consultas))
    valorTotal = sum(c.getValor() for c in consultas)

    return valorTotal

def ganhosDoPeriodo(dt_inicio, dt_fim):
    consultas = ConsultaDAO.buscarTodosData(dt_inicio, dt_fim)
    valorTotal = sum(c.getValor() for c in consultas)

    return valorTotal

def folhaPagamento(dt_inicio, dt_fim):
    consultas = ConsultaDAO.buscarTodosData(dt_inicio, dt_fim)

    consultas = list(
        filter(lambda consulta: (usuarioMedico(Usuario.usuarioLogado.getTipo())) and consulta.getMedico().getId() == Usuario.usuarioLogado.getTipo(),
               consultas))
    valorTotal = sum(c.getValor() for c in consultas)

    return valorTotal


