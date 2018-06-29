class Consulta(object):

    def __init__(self, id, usuarioRegistro, medico, paciente, auxiliares, dt_registro, dt_consulta, status, valor):
        self.__id = id
        self.__usuarioRegistro = usuarioRegistro
        self.__medico = medico
        self.__paciente = paciente
        self.__auxiliares = auxiliares
        self.__dt_registro = dt_registro
        self.__dt_consulta = dt_consulta
        self.__status = status
        self.__valor = valor


    def getId(self):
        return self.__id

    def setId(self, id_valor):
        self.__id = id_valor

    def getMedico(self):
        return self.__medico

    def setMedico(self, id_valor):
        self.__medico = id_valor

    def getUsuarioRegistro(self):
        return self.__usuarioRegistro

    def setUsuarioRegistro(self, id_valor):
        self.__usuarioRegistro = id_valor

    def getPaciente(self):
        return self.__paciente

    def setPaciente(self, id_valor):
        self.__paciente = id_valor

    def getAuxiliares(self):
        return self.__auxiliares

    def setAuxiliares(self, id_valor):
        self.__auxiliares = id_valor

    def getDt_registro(self):
        return self.__dt_registro

    def setDt_registro(self, id_valor):
        self.__dt_registro = id_valor

    def getDt_consulta(self):
        return self.__dt_consulta

    def setDt_consulta(self, id_valor):
        self.__dt_consulta = id_valor

    def getStatus(self):
        return self.__status

    def setStatus(self, id_valor):
        self.__status = id_valor

    def getValor(self):
        return self.__valor

    def setValor(self, id_valor):
        self.__valor = id_valor