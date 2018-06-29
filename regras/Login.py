from linguagens_programacao.modelo.dao import UsuarioDAO
from linguagens_programacao.modelo.Usuario import Usuario

def login(userName, userPass):
    try:
        usuario = UsuarioDAO.login(userName, userPass)
        if (usuario != None):
            Usuario.usuarioLogado = usuario
            return 1
        else:
            return 0

    except :
        print("Login inválido")
        return 0



