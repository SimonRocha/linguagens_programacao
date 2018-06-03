from linguagens_programacao.modelo import Usuario, Administrador, Atendente, Auxiliar, Consulta
from linguagens_programacao.modelo.dao import UsuarioDAO, ConsultaDAO

def relatorioGanhos(dt_inicio, dt_fim, medico, valor):
    if (isinstance(Usuario.usuarioLogado, Administrador)):
        return ConsultaDAO.relatorioGanhos(dt_inicio, dt_fim, medico, valor)

def folhaPagamento(dt_inicio, dt_fim):
    if (isinstance(Usuario.usuarioLogado, Administrador) == 0):
        return ConsultaDAO.folhaPagamento(dt_inicio, dt_fim, Usuario.usuarioLogado)



