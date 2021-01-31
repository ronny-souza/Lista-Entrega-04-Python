# QUESTÃO 01 - Escreva um programa que leia inteiros do usuário e os armazene em uma lista. Use o valor zero 
# para parar a solicitação e armazenagem de valores. Após todos os valores terem sido preenchidos, seu programa
# deve exibi-los em ordem inversa, com cada valor aparecendo em uma linha.

listaNumeros = []
numero = 1

while numero != 0:

    numero = int(input("Digite um número inteiro: "))
    if numero != 0:
        listaNumeros.append(numero)

listaNumeros.reverse()

for i in range(len(listaNumeros)):
    print(f"{listaNumeros[i]}")