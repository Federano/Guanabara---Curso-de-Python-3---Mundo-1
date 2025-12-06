# DESAFIO 08
# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTÍMETROS E MILÍMETROS

# Metros = m
# Centímetros = c
# Milímetros = mi

m = float(input("Digite a quantidade de metros que você deseja converter: "))

c = m * 100
mi = m * 1000

print(f"O valor de {m} metros convertido em centímetros fica {c} e em milímetros fica {mi}.")