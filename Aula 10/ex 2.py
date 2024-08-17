a = int(input("Insira o primeiro valor: "))

b = int(input("Insira o segundo valor: "))
while b == 0:
    b = int(input("Valor deve ser diferente de 0, insira novamente o segundo valor: "))

resultado_divisao = a / b
print(f"O resutaldo da divisão é {resultado_divisao}")