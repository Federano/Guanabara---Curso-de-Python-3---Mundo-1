# DESAFIO 04
# FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE ELE.

print("Olá! O objetivo é criar um programa que me diga o tipo de variável do que eu digitar. Vamos testar?")

# DICA: Evite acentos em nomes de variáveis (use 'variavel' em vez de 'Variável')
variavel = input("Digite algo para que eu diga o tipo de variável que ela é: ")

print("O tipo primitivo desse valor é:", type(variavel))
print("O que você digitou é alfabético?", variavel.isalpha())
print("O que você digitou é um numero?", variavel.isnumeric())
print("O que você digitou é alfanumérico?", variavel.isalnum())
print("O que você digitou está com tudo em maiúsculo?", variavel.isupper())
print("O que você digitou está com tudo em minúsculo?", variavel.islower())
print("O que você digitou é apenas espaço?", variavel.isspace())
print("O que você digitou é um título?", variavel.istitle())
print("O que você digitou é um texto que pode ser impresso na tela?", variavel.isprintable())

