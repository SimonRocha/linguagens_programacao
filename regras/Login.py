from linguagens_programacao.modelo.dao import UsuarioDAO
from linguagens_programacao.modelo.Usuario import Usuario

def login(userName, userPass):
    usuario = login(userName, userPass)
    if (usuario != None):
        Usuario.usuarioLogado = usuario
        return 1
    else:
        return 0



