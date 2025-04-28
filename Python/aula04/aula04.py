produtos = {}
while True:
    print("""
    ╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
    ┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭╮╭╮┃╱╱╱╱╱╱╱╱╱╭╯╰╮
    ┃╰━━┳━━┫╰━┳━━┳━╮╰╯┃┃┣┻━┳━━┳━━┳━╋╮╭╋┳━╮╭━━┳━╮╭━━┳━━╮
    ╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯╱╱┃┃┃╭╮┃╭━┫╭╮┃╭╮┫┃┣┫╭╮┫┃━┫╭╮┫━━┫┃━┫
    ┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱╱╱┃┃┃╰╯┃╰━┫╭╮┃┃┃┃╰┫┃┃┃┃┃━┫┃┃┣━━┃┃━┫
    ╰━━━┻╯╰┻━━┻━━┻╯╱╱╱╰╯╰━━┻━━┻╯╰┻╯╰┻━┻┻╯╰┻━━┻╯╰┻━━┻━━╯\n""")
    print("1 - Cadastrar produtos")
    print("2 - Listar produtos")
    print("3 - Excluir produtos")
    print("4 - Sair")
    option = int(input("Digite sua opção: "))
    print("Opção digitada - ", option)
    if option == 1:
        while True:
            print("Cadastrar produto")
            print("1 - Cadastrar produto")
            print("2 - Voltar")
            option1 = input("Digite sua opção: ")
            print("Opção digitada - ", option1)
            if option1 == "1":
                nome = input("Digite o nome do produto: ")
                valor = float(input("Digite o preço do produto: "))
                produtos[nome] = valor
            elif option1 == "2":
                break
            else:
                print("Digite um número válido")
    elif option == 2:
        print("------------------------------------------------------------------------\n")
        print("Listar produtos\n")
        if produtos:
            for nome, valor in produtos.items():
                print(f"{nome}: R$ {valor:.2f}")
        else:
            print("Nenhum produto cadastrado")
        print("------------------------------------------------------------------------\n")
    elif option == 3:
        print("------------------------------------------------------------------------\n")
        print("Excluir produto\n")
        if produtos:
            nomeExcluir = input("Digite o nome do produto que você quer excluir: ")
            if nomeExcluir in produtos:
                del produtos[nomeExcluir]
                print(f"{nomeExcluir} foi excluido")
            else:
                print("Item não encontrado")
        else:
            print("Nenhum item cadastrado")
        print("------------------------------------------------------------------------\n")
    elif option == 4:
        print("Sair")
        break
    else:
        print("Digite um número válido")