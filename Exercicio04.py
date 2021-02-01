# QUESTÃO 04 - Faça um programa que manipula uma lista que contém modelos de carro e seu consumo (km/l), 
# da seguinte forma: [[‘Vectra’, 9], [‘Gol’, 10], [‘Corsa’, 11], [‘Fit’,12.5]]. O programa deve mostrar na tela
# o nome do modelo mais econômico. Além disso, deve mostrar na tela quanto cada um desses modelos gastaria para
# percorrer 1000 Km, assumindo que o valor do litro da gasolina é R$ 4,69.

def criarCarro(quantidadeCarros):
    return [[""]*3 for i in range(quantidadeCarros)]

quantidadeCarros = int(input("Quantos carros deseja adicionar? "))
listaCarros = criarCarro(quantidadeCarros)
menorConsumo = 9999999.9
modelo = ""
quantidadeCombustivel = 0.0
quantidadeGasta = 0.0
precoGasolina = 4.69

for i in range(quantidadeCarros):
    for j in range(1):
        listaCarros[i][j] = input("Digite o nome do carro: ")
        listaCarros[i][j + 1] = float(input("Digite o valor do consumo: "))

print("\n\t\t\tTABELA DE CONSUMO POR MODELO:\n")
for i in listaCarros:

    quantidadeCombustivel = 1000 / i[1]
    i[2] = quantidadeCombustivel * precoGasolina
    print("-----------------------------------------------------------------------------------------------")
    print(f"|Modelo: {i[0]}\t|\tConsumo Médio: {i[1]}\t|\tGasto para percorrer 1000Km: R$ {round(i[2], 2)}|")
    print("-----------------------------------------------------------------------------------------------")
    
for i in listaCarros:
    if i[2] < menorConsumo:
        menorConsumo = i[2]
        modelo = i[0]
print(f"\nO modelo mais econômico é: {modelo}")
