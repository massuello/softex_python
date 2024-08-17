cliente = ["Massuello"]
opcao = ""


def show_menu():
    print("Output:")
    print("========Menu========")
    print("1 - Listar Clientes")
    print("2 - Cadastrar Cliente")
    print("3 - Editar Cliente")
    print("4 - Remover Cliente")
    print("0 - Sair do Sistema")
    print("====================")
    opcao = int(input("Opção:"))
    print("====================")
    return opcao


while True:
    opcao = show_menu()
    if opcao == 1:
        print(cliente)
    elif opcao == 2:
        novo_cliente = input("Cadastre o novo cliente: ")
        cliente += [novo_cliente]
    elif opcao == 3:
        print(cliente)
        remover_cliente = input("Qual cliente você quer editar?")
        cliente.remove(remover_cliente)
        novo_nome = input("Qual o novo nome?")
        cliente.append(novo_nome)
    elif opcao == 0:
        break
