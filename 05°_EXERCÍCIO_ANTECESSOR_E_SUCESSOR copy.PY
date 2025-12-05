# DESAFIO 05°
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E O SEU ANTECESSOR.

import time

print("O objetivo é criar um programa que leia um número e mostre o seu sucessor e antecessor.")
time.sleep(1)
print("Vamos ver se o codigo esta dando certo?")

"""
Primeiro, preciso colocar o comando INT e depois o INPUT. Isso é necessário porque preciso informar ao Python que se trata de um número inteiro, e não o contrário, como eu costumava fazer.
"""
numero_que_vou_analisar = int(input("Por favor, digite o número de sua preferência: "))

numero_antecessor = (numero_que_vou_analisar - 1)
numero_sucessor = (numero_que_vou_analisar + 1)

print(f"Analisei o seu número: {numero_que_vou_analisar} \nO antecessor dele é: {numero_antecessor} \nO sucessor é: {numero_sucessor}")