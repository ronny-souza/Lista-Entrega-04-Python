# QUESTÃO 05 - Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as 
# temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, ...).

temperaturaMeses = [["Janeiro", 0.0], ["Fevereiro", 0.0], ["Março", 0.0], ["Abril", 0.0], ["Maio", 0.0], ["Junho", 0.0], ["Agosto", 0.0], ["Setembro", 0.0], ["Outubro", 0.0], ["Novembro", 0.0], ["Dezembro", 0.0]]
somaTemperaturas = 0.0
maioresTemperaturas = []

for i in range(len(temperaturaMeses)):
    for j in range(1):
        temperatura = float(input(f"Digite a temperatura de {temperaturaMeses[i][j]}: "))
        somaTemperaturas += temperatura
        temperaturaMeses[i][j + 1] = temperatura

mediaTemperaturas = somaTemperaturas / len(temperaturaMeses)
print(f"\nMédia anual de temperatura: {round(mediaTemperaturas, 1)}")
print("\nMESES COM TEMPERATURA MAIOR QUE A MÉDIA ANUAL:\n")
for i in temperaturaMeses:

    if i[1] > mediaTemperaturas:
        print(f"Mês: {i[0]}\t|\tTemperatura: {i[1]}")
