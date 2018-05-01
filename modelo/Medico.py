from linguagens_programacao.modelo.Usuario import Usuario

class Medico(Usuario):

    def __init__(self, id, login, senha, tipo, nome, documento, especializacao):
        super().__init__( id, login, senha, tipo, nome, documento)
        self.__especializacao = especializacao

    def getEspecializaca(self):
        return self.__especializacao

    def setEspecializaca(self, id_valor):
       self.__especializacao = id_valor

