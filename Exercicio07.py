# QUESTÃO 07 - Inicialize uma lista de 20 números inteiros. Armazene os números pares em uma lista PAR e os 
# números ímpares em uma lista IMPAR. Imprima as listas PAR e IMPAR.

par =  []
impar = []

for i in range(20):

    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        par.append(numero)
    
    else:
        impar.append(numero)

print(f"Pares: {par}")
print(f"Ímpares: {impar}")