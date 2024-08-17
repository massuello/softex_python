# 4: Ler o salário fixo e o valor total das vendas efetuadas pelo vendedor de uma empresa.
# Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00
# mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.

# salario = float(input("Digite o salário: "))
venda = float(input("Digite o valor de vendas: "))
comissao1 = 0
comissao2 = 0
comissao_total = 0

if venda <= 1500:
    comissao1 = venda * 0.03

if venda > 1500:
    comissao1 = 1500 * 0.03
    comissao2 = (venda - 1500) * 0.05

comissao_total = comissao1 + comissao2

print(f"A comissão é de {comissao_total}")

