# QUESTÃO 02 - Escreva um programa que leia inteiros do usuário até que seja inserida uma linha em branco. 
# Uma vez que todos os inteiros tenham sido lidos seu programa deve exibir todos os números negativos, seguidos 
# de todos os zeros, seguidos de todos os números positivos. Os elementos de cada um destes três grupos
# devem ser impressos na mesma ordem em que foram inseridos na lista. Por exemplo, se o usuário inseriu os 
# valores 3, -4, 1, 0, -1, 0, -2, então o programa deve imprimir -4, -1, -2, 0 , 0 , 3 , 1.

listaNegativos = []
listaPositivos = []
listaZeros = []
listaFinal = []
numero = "1"

while numero != "":

    numero = input("Digite um valor inteiro positivo ou negativo: ")

    if numero != "" and int(numero) < 0:
        listaNegativos.append(int(numero))
    
    elif numero != "" and int(numero) == 0:
        listaZeros.append(int(numero))

    elif numero != "" and int(numero) > 0:
        listaPositivos.append(int(numero))

listaFinal = listaNegativos + listaZeros + listaPositivos    
print(listaFinal)