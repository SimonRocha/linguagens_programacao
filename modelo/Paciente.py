class Paciente(object):

    def __init__(self, id, nome, documento, dt_nascimento, dt_entrada):
        self.__id = id
        self.__nome = nome
        self.__documento = documento
        self.__dt_nascimento = dt_nascimento
        self.__dt_entrada = dt_entrada

    def getId(self):
        return self.__id

    def setId(self, id_valor):
        self.__id = id_valor

    def getNome(self):
        return self.__id

    def setNome(self, id_valor):
        self.__id = id_valor

    def getDocumento(self):
        return self.__id

    def setDocumento(self, id_valor):
        self.__id = id_valor

    def getDt_nascimento(self):
        return self.__dt_nascimento

    def setDt_nascimento(self, id_valor):
        self.__dt_nascimento = id_valor


    def getDt_entrada(self):
        return self.__dt_entrada

    def setDt_entrada(self, id_valor):
        self.__dt_entrada = id_valor

