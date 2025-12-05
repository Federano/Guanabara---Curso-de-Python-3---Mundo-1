# DESAFIO 06°
# CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E A RAIZ QUADRADA.
 
import time

print("O objetivo é criar um programa que leia um número e mostre o seu dobro, triplo e sua raiz quadrada.")
time.sleep(1)
print("Vamos ver se o código está dando certo?")

# NÚMERO DIGITADO = n
# DOBRO DO NÚMERO = n2
# TRIPLO DO NÚMERO = n3
# RAIZ QUADRADA = q

n = int(input("Por favor, digite o número: "))
n2 = n * 2
n3 = n * 3
q = n ** (1/2)

print(f"O dobro do número é: \n{n2}")
print(f"O triplo do número é: \n{n3}")
print(f"A raiz quadrada do número é: \n{q:.2f}")

 