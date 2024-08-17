def soma():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    resultado_soma = x + y
    print("O resultado da sua soma é: ", resultado_soma)
    return resultado_soma


def subtracao():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    resultado_subtracao = x - y
    print("O resultado da sua soma é: ", resultado_subtracao)
    return resultado_subtracao


def multiplicacao():
    resultado_multiplicacao = x * y
    return resultado_multiplicacao


def divisao():
    resultado_divisao = x / y
    return resultado_divisao


while True:
    print("#####################")
    print("#####################")
    print("Calculadora em python")
    print("#####################")
    print("                     ")
    print("Menu:                ")
    print("1. Soma              ")
    print("2. Subtração         ")
    print("3. Multiplicação     ")
    print("4. Divisão           ")
    print("#################")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
       soma()
    elif escolha == "2":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print(f"Resultado: {subtrair(a, b)}")
    elif escolha == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

print("Programa encerrado.")