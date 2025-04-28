import os
produtos = {}
def cadastrar():
    while True:
        os.system("cls")
        print("------------------------------------------------------------------------\n")
        print("Cadastrar produto\n")
        print("1 - Cadastrar produto")
        print("2 - Voltar\n")
        print("------------------------------------------------------------------------\n")
        option1 = input("Digite sua opção: ")
        print("Opção digitada - ", option1)
        print("\n")
        if option1 == "1":
            os.system("cls")
            print("------------------------------------------------------------------------\n")
            nome = input("Digite o nome do produto: ")
            valor = float(input("Digite o preço do produto: "))
            produtos[nome] = valor
            print(f"Produto {nome}: R$ {valor:.2f}\n")
            print("Foi cadastrado com sucesso!")
            print("------------------------------------------------------------------------\n")
        elif option1 == "2":
            break
        else:
            print("Digite um número válido")
def listaDeProdutos():
        os.system("cls")
        while True:
            os.system("cls")
            print("------------------------------------------------------------------------\n")
            print("Lista de produtos\n")
            if produtos:
                for nome, valor in produtos.items():
                    print(f"{nome}: R$ {valor:.2f}")
                print("------------------------------------------------------------------------\n")
                option2 = int(input("Digite 0 para sair: "))
                if option2 == 0:
                    break
                else:
                    print("Digite um número válido")
            else:
                print("Nenhum produto cadastrado")
def excluirProduto():
        os.system("cls")
        while True:
            print("------------------------------------------------------------------------\n")
            print("Excluir produto\n")
            if produtos:
                print("------------------------------------------------------------------------\n")
                print("Lista de produtos\n")
                for nome, valor in produtos.items():
                    print(f"{nome}: R$ {valor:.2f}")
                print("------------------------------------------------------------------------\n")
                nomeExcluir = input("Digite o nome do produto que você quer excluir: ")
                if nomeExcluir in produtos:
                    del produtos[nomeExcluir]
                    print(f"{nomeExcluir} foi excluido")
                    print("------------------------------------------------------------------------\n")
                else:
                    print("Item não encontrado")
                    print("------------------------------------------------------------------------\n")
                option3 = int(input("Digite 0 para voltar: "))
                if option3 == 0:
                    break
                else:
                    print("Digite um número válido")
            else:
                print("Nenhum item cadastrado")
                break
while True:
    print("\n\n")
    print("""
    ╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
    ┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭╮╭╮┃╱╱╱╱╱╱╱╱╱╭╯╰╮
    ┃╰━━┳━━┫╰━┳━━┳━╮╰╯┃┃┣┻━┳━━┳━━┳━╋╮╭╋┳━╮╭━━┳━╮╭━━┳━━╮
    ╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯╱╱┃┃┃╭╮┃╭━┫╭╮┃╭╮┫┃┣┫╭╮┫┃━┫╭╮┫━━┫┃━┫
    ┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱╱╱┃┃┃╰╯┃╰━┫╭╮┃┃┃┃╰┫┃┃┃┃┃━┫┃┃┣━━┃┃━┫
    ╰━━━┻╯╰┻━━┻━━┻╯╱╱╱╰╯╰━━┻━━┻╯╰┻╯╰┻━┻┻╯╰┻━━┻╯╰┻━━┻━━╯\n\n""")
    print("1 - Cadastrar produtos")
    print("2 - Lista de produtos")
    print("3 - Excluir produtos")
    print("4 - Sair\n")
    option = int(input("Digite sua opção: "))
    print("Opção digitada - ", option)
    if option == 1:
        cadastrar()
    elif option == 2:
        listaDeProdutos()
    elif option == 3:
        excluirProduto()
    elif option == 4:
        print("Sair")
        break
    else:
        print("Digite um número válido")