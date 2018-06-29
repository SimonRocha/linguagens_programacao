from linguagens_programacao.regras import Inserir
from linguagens_programacao.regras import Login
from linguagens_programacao.regras import Lista
from linguagens_programacao.regras import Relatorios
from linguagens_programacao.modelo.Usuario import Usuario
import os
import datetime


from pprint import pprint


clear = lambda: os.system('cls')


Usuario.usuarioLogado = Usuario(2, "sims", "simss", 0, "zimon", "asdasdea")

print("Olá bem vindo ao ambiente de testes, digite login e senha, caso você não tenha sido cadastrado criaremos seu usuário")
login = input("Digite o login")
senha = input("Difite a senha")
clear()

meuUser = 0
while meuUser == 0:
    if (Login.login(login, senha)):
        print("login efetuado com sucesso")
        meuUser = 1
    else:
        print("Vamos criar este usuário para você, ele terá permissão de admninistrador ja que estamos apenas testando")
        nome = input("Digite o nome")
        documento = input("Digite o documento de identificação")
        meuUser = Inserir.inserirAdministrador(login, senha, 0, nome, documento)
        print("Parabéns, agora você é o administrador!")

opcao = 9
while (opcao != 999):
    print("         1- Adicionar Médico")
    print("         2- Adicionar Auxiliar")
    print("         3- Adicionar Atendente")
    print("         4- Listar Médicos")
    print("         5- Listar Atendentes")
    print("         6- Listar Consultas")
    print("         7- Relatorios")
    print("         8- Adicionar Consulta")
    print("         999- Sair")

    opcao = int(input("Digite a opção desejada"))

    if opcao == 1:
        print("Digite os dados do médico")
        login = input("Login para o usuário")
        senha = input("Senha do usuário")
        tipo = 2
        nome = input("Nome")
        documento = input("Documento")
        especializacao = input("Especialização")

        Inserir.inserirMedico(login, senha, tipo, nome, documento, especializacao)
        print("Médico inserido com sucesso")
    elif opcao == 2:
        print("Digite os dados do auxiliar")
        login = input("Login para o usuário")
        senha = input("Senha do usuário")
        tipo = 3
        nome = input("Nome")
        documento = input("Documento")
        funcao = input("Funcao")

        Inserir.inserirAuxiliar(login, senha, tipo, nome, documento, funcao)
        print("Auxiliar inserido com sucesso")
    elif opcao == 3:
        print("Digite os dados do atendente")
        login = input("Login para o usuário")
        senha = input("Senha do usuário")
        tipo = 4
        nome = input("Nome")
        documento = input("Documento")

        Inserir.inserirAtendente(login, senha, tipo, nome, documento)
        print("Auxiliar inserido com sucesso")
    elif opcao == 4:
        print("Listando os médicos")
        print("----Nome---------------Esp.--------------------------------")

        for m in Lista.listarTodosMedico():
            print(m.getNome() + '   --- ' + m.getEspecializaca())
    elif opcao == 5:
        print("Listando os atendentes")
        print("----Nome-----------------------------------------------")

        for m in Lista.listarTodosAtendente():
            print(m.getNome())

    elif opcao == 6:
        print("     Filtrar por: 1- Médico 2- Paciente 3- Usuario 4- Todas")
        opcao = int(input("     Selecione"))

        if (opcao == 4):
            print("Listando as consultas")
            print("-----Medico--Paciente--Usuario--Valor--Dt. Registro--Dt. Consulta---")

            for m in Lista.listarTodosConsulta():
                pprint(vars(m))

        if (opcao == 3):
            nome = input("Digite o nome do usuario")
            print("Listando as consultas")
            print("-----Medico--Paciente--Usuario--Valor--Dt. Registro--Dt. Consulta---")

            for m in Lista.listarTodasConsultasUsuarioNome(nome):
                pprint(vars(m))

        if (opcao == 2):
            nome = input("Digite o nome do paciente")
            print("Listando as consultas")
            print("-----Medico--Paciente--Usuario--Valor--Dt. Registro--Dt. Consulta---")

            for m in Lista.listarTodasConsultasPacienteNome(nome):
                pprint(vars(m))

        if (opcao == 1):
            nome = input("Digite o nome do médico")
            print("Listando as consultas")
            print("-----Medico--Paciente--Usuario--Valor--Dt. Registro--Dt. Consulta---")

            for m in Lista.listarTodasConsultasMedicoNome(nome):
                pprint(vars(m))

    elif opcao == 7:
        print("     Qual relatorio deseja: 1- Por Médico 2- Ganhos do Período 3- Folha de pagamento ")
        opcao = int(input("     Digite a opção desejada"))

        if (opcao == 1):
            id_medico = int(input("Digite o id do médico"))
            dt_inicial = input("Digite a data inicial da pesquisa")
            dt_final = input("Digite a data final da pesquisa")

            print(Relatorios.ganhosMedico(dt_inicial, dt_final, id_medico))
        elif (opcao == 2):
            dt_inicial = input("Digite a data inicial da pesquisa")
            dt_final = input("Digite a data final da pesquisa")

            print(Relatorios.ganhosDoPeriodo(dt_inicial, dt_final))
        elif (opcao == 3):
            dt_inicial = input("Digite a data inicial da pesquisa")
            dt_final = input("Digite a data final da pesquisa")

            print(Relatorios.folhaPagamento(dt_inicial, dt_final))
    elif opcao == 8:
        id_medico = int(input("Digite o id do médico"))
        id_paciente = int(input("Digite o id do paciente"))
        input("Digite a data de registro")
        valor = input("Digite o valor")

        Inserir.inserirConsulta(Usuario.usuarioLogado.getId(), id_medico, id_paciente, "", datetime.datetime.now(), "", 0, valor)
        print("Consulta inserida com sucesso")









