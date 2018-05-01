from linguagens_programacao.modelo.Usuario import Usuario

class Auxiliar(Usuario):

    def __init__(self, id, login, senha, tipo, nome, documento, funcao):
        super().__init__( id, login, senha, tipo, nome, documento)
        self.__funcao = funcao

        def getFuncao(self):
            return self.__funcao

        def setFuncao(self, id_valor):
            self.__funcao = id_valor


