homem_mais_velho = 0
mulher_mais_velha = 0
a = int(input("Insira a idade do primeiro homem: "))

b = int(input("Insira a idade do segundo homem: "))
while b == a:
    b = int(input("Valor já inserido, insira novamente o segundo valor: "))

c = int(input("Insira a idade da primeira mulher "))

d = int(input("Insira a idade da segunda mulher "))
while d == c:
    d = int(input("Valor já inserido, insira novamente a idade da segunda mulher "))

if a > b:
    homem_mais_velho = a
else:
    homem_mais_velho = b

if c > d:
    mulher_mais_velha = c
else:
    mulher_mais_velha = d

print(f"O homem mais velho tem: {homem_mais_velho}")
print(f"A mulher mais velha tem: {mulher_mais_velha}")