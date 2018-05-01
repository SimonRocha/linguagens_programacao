from linguagens_programacao.modelo.Usuario import Usuario

class Administrador(Usuario):

    def __init__(self, id, login, senha, tipo, nome, documento):
        super().__init__( id, login, senha, tipo, nome, documento)


