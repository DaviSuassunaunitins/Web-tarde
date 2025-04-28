import os
alunos = []
def alterar():
    while True:
        os.system("cls")
        print("-----------------------------------------------------------------------------------\n")
        print("Alterar aluno\n")
        print("1 - Adicionar aluno")
        print("2 - Excluir aluno")
        print("3 - Voltar\n")
        print("-----------------------------------------------------------------------------------\n")
        optionAlterar = int(input("Digite sua escolha: "))
        if optionAlterar == 1:
            adicionar()
        elif optionAlterar == 2:
            excluir()
        elif optionAlterar == 3:
            print("Voltando...")
            break
        else:
            print("Digite um número válido")
def adicionar():
    while True:
        os.system("cls")
        print("-----------------------------------------------------------------------------------\n")
        print("Adicionar aluno\n")
        print("1 - Adicionar aluno")
        print("2 - Voltar\n")
        print("-----------------------------------------------------------------------------------\n")
        optionAdicionar = int(input("Digite sua escolha: "))
        if optionAdicionar == 1: 
            aluno = input("Digite o nome do(a) aluno(a): ")
            alunos.append(aluno)
        elif optionAdicionar == 2:
            print("Voltando...")
            break
        else:
            print("Digite um número válido")
def excluir():
    while True:
        os.system("cls")
        print("-----------------------------------------------------------------------------------\n")
        print("Excluir aluno\n")
        print("1 - Excluir aluno")
        print("2 - Voltar\n")
        print("-----------------------------------------------------------------------------------\n")
        optionExcluir = int(input("Digite sua escolha: "))
        if optionExcluir == 1:
            print("-----------------------------------------------------------------------------------\n")
            for nome in alunos:
                print(nome)
            print("\n")
            print("-----------------------------------------------------------------------------------\n")
            nome = input("Digite o nome do aluno: ")
            if nome in alunos:
                alunos.remove(nome)
                print(f"({nome} foi excluido)")
            else:
                print("Aluno não encontrado")
        elif optionExcluir == 2:
            print("Voltando...")
            break
        else:
            print("Digite um número válido")
def listaAluno():
    while True:
        os.system("cls")
        print("-----------------------------------------------------------------------------------\n")
        if alunos:
            print("Lista de aluno\n")
            for nome in alunos:
                print(nome)
            print("\n")
            print("-----------------------------------------------------------------------------------\n")
            optionLista = int(input("Digite 0 para voltar: "))
            if optionLista == 0:
                print("Voltando...")
                break
            else:
                print("Digite um número válido")
while True:
    os.system("cls")
    print("-----------------------------------------------------------------------------------\n")
    print("""
        ░█▀▀█ █▀▀█ █▀▀█ █▀▀▀ █▀▀█ █▀▀█ █▀▄▀█ █▀▀█ 　 █▀▀ █▀▀ █▀▀ █▀▀█ █── █▀▀█ █▀▀█ 
        ░█▄▄█ █▄▄▀ █──█ █─▀█ █▄▄▀ █▄▄█ █─▀─█ █▄▄█ 　 █▀▀ ▀▀█ █── █──█ █── █▄▄█ █▄▄▀ 
        ░█─── ▀─▀▀ ▀▀▀▀ ▀▀▀▀ ▀─▀▀ ▀──▀ ▀───▀ ▀──▀ 　 ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀ ▀──▀ ▀─▀▀\n""")
    print("1 - Alterar aluno")
    print("2 - Lista de alunos")
    print("3 - Sair")
    print("-----------------------------------------------------------------------------------\n")
    option = int(input("Digite sua escolha: "))
    if option == 1:
        alterar()
    elif option == 2:
        listaAluno()
    elif option == 3:
        print("Saindo...")
        break
    else:
        print("Digite um número válido")