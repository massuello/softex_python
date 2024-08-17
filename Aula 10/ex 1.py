a = int(input("Insira o primeiro valor: "))

b = int(input("Insira o segundo valor: "))
while b == a:
    b = int(input("Valor já inserido, insira novamente o segundo valor: "))

c = int(input("Insira o terceiro valor: "))
while c == a or c == b:
    c = int(input("Valor já inserido, insira novamente o terceiro valor: "))

d = int(input("Insira o quarto valor: "))
while d == a or d == b or d == c:
    d = int(input("Valor já inserido, insira novamente o quarto valor: "))

resultado_soma = c + d
print(f"Resultado da soma é: {resultado_soma}")




