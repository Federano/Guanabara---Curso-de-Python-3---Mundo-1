# DESAFIO 11°
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de $2m^2$.

# altura:  a
# largura: l
# parede:  p = a*l
# tinta:   t = p / 2

a = float(input("Digite a altura da parede: ").replace(",", "."))
l = float(input("Digite a largura da parede:").replace(",", "."))
p = a * l
t = p/2

print(f"A parede tem {p:.2f} de metros")
print(f"Por tanto, será gasto {t:.2f} de tinta.")





  
