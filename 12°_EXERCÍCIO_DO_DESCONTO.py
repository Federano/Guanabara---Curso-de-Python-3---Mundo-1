# DESAFIO 12
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# preco = preço original
# novo_preco = preço com desconto aplicado

preco = float(input("Por favor, digite o valor do produto selecionado: ").replace(",", "."))

# Cálculo: Preço - 5%
novo_preco = preco - (preco * 5 / 100)

# Ajuste gramatical: "ficar" -> "ficará"
print(f"O valor do produto com o desconto ficará R$ {novo_preco:.2f}")