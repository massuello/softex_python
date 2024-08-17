# entrada = int(input("Digite o número: "))
# match entrada:
#     case 1:
#         print("Segunda")
#     case 2:
#         print("Terça")
#     case 3:
#         print("Quarta")
#     case 4:
#         print("Quinta")
#     case 5:
#         print("Sexta")
#     case 6:
#         print("Sábado")
#     case 7:
#         print("Domingo")
#     case _:
#         print("Inválido")

# entrada = int(input("Digite o número: "))
# match entrada:
#     case 1:
#         print("Janeiro")
#     case 2:
#         print("Fevereiro")
#     case 3:
#         print("Março")
#     case 4:
#         print("Abril")
#     case 5:
#         print("Maio")
#     case 6:
#         print("Junho")
#     case 7:
#         print("Julho")
#     case 8:
#         print("Agosto")
#     case 9:
#         print("Setembro")
#     case 10:
#         print("Outubro")
#     case 11:
#         print("Novembro")
#     case 12:
#         print("Dezembro")
#     case _:
#         print("Inválido")

# estado_civil = input("Digite o estado civil(casado, solteiro, divorciado, outro): ")
#
# match estado_civil:
#     case "solteiro":
#         print("Você é solteiro")
#     case "casado":
#         print("Você é casado")
#     case "divorciado":
#         print("Você é casado")
#     case "outro":
#         print("Outro")
#     case _:
#         print("Inválido")


def calculadora():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    op = input("Digite o operador: multiplicador, soma, subtração, divisão: ")

    match op:
        case "multiplicador":
            print(num1 * num2)
        case "soma":
            print(num1 + num2)
        case "subtração":
            print(num1 - num2)
        case "divisão":
            print(num1 - num2)


calculadora()
