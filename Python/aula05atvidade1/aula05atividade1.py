import os
lista = []
def alterar():
    os.system("cls")
    while True:
        print("-----------------------------------------------------------------------------------\n")
        print("Alterar aluno\n")
        print("1 - Adicionar aluno")
        print("2 - Excluir aluno")
        print("3 - Voltar\n")
        print("-----------------------------------------------------------------------------------\n")
        optionAlterar = int(input("Digite sua escolha: "))
        if optionAlterar == 1:
            adcionar()
        elif optionAlterar == 2:
            excluir()
        elif optionAlterar == 3:
            print("Voltando...")
            break
        else:
            print("Digite um número válido")
def adcionar():
    os.system("cls")
    while True:
        print("-----------------------------------------------------------------------------------\n")
        print("Adcionar aluno\n")
        print("1 - Adicionar aluno")
        print("2 - Voltar\n")
        print("-----------------------------------------------------------------------------------\n")
        optionAdicionar = int(input("Digite sua escolha: "))
        if optionAdicionar == 1: 
            aluno = input("Digite o nome do(a) aluno(a)")
            lista.append(aluno)
        elif optionAdicionar == 2:
            print("Voltando...")
            break
        else:
            print("Digite um número válido")
def excluir():
    os.system("cls")
    while True:
        print("-----------------------------------------------------------------------------------\n")
        print("Excluir aluno\n")
        print("1 - Excluir aluno")
        print("2 - Voltar\n")
        print("-----------------------------------------------------------------------------------\n")
        optionExcluir = int(input("Digite sua escolha: "))
        if optionExcluir == 1:




            nome = input("Digite o nome do aluno:")
            lista.remove(nome)
            print(f"({nome} foi excluido)")
        elif optionExcluir == 2:
            print("Voltando...")
            break
        else:
            print("Digite um número válido")
def listaAluno():
    os.system("cls")
    while True:
        print("-----------------------------------------------------------------------------------\n")
        if lista:
            for nome in lista():
                print(nome)
            print("-----------------------------------------------------------------------------------\n")
            optionLista = int(input("Digite 0 para sair: "))
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