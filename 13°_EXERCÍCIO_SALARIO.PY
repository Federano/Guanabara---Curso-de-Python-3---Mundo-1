# DESAFIO 13°
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# Salario = s
# Aumento = a

s = float(input("Digite o seu salario atual:").replace(",", "."))
a = s + (s * 15) / 100

print(f"Seu novo salario é de {a:.2f}")