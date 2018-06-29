
class Usuario(object):

    def __init__(self, id, login, senha, tipo, nome, documento):
        self.__id = id
        self.__login = login
        self.__senha = senha
        self.__nome = nome
        self.__documento = documento
        self.__tipo = tipo

    def getId(self):
        return self.__id

    def setId(self, id_valor):
        self.__id = id_valor

    def getNome(self):
        return self.__nome

    def setNome(self, id_valor):
        self.__nome = id_valor

    def getDocumento(self):
        return self.__documento

    def setDocumento(self, id_valor):
        self.__documento = id_valor

    def getLogin(self):
        return self.__login

    def setLogin(self, login_valor):
        self.__login = login_valor

    def getSenha(self):
        return self.__senha

    def setSenha(self, senha_valor):
        self.__senha = senha_valor

    def getTipo(self):
        return self.__tipo

    def setTipo(self, tipo_valor):
        self.__tipo = tipo_valor


usuarioLogado = Usuario(2, "sims", "simss", 2, "zimon", "asdasdea")











