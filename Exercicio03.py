# QUESTÃO 03 - Para ganhar a Mega Sena, é necessário que o apostador acerte todos os 6 números sorteados, que 
# estão em um intervalo que vai de 1 a 60. Escreva um programa que gere os 6 números sorteados e os armazene 
# em uma lista. Garanta que não haja valores duplicados. Exiba os números em ordem crescente.

from random import *

numeros = []
while len(numeros) < 6:
    numero = randint(1, 60)
    
    if numero in numeros:
        continue
    else:
        numeros.append(numero)

numeros.sort()
print(numeros)