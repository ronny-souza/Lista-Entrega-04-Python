# QUESTÃO 08 - Dada a lista S = [1, 2, [3, 4, [5, 6, [7, 8, [9,[0]]]]]]. Qual o tamanho da lista S?
# Escreva a expressão que troca o 0 da lista por 17 (você pode usar um editor de texto como o Notepad++ ou 
# Sublime para ajudar a verificar os colchetes).

s = [1, 2, [3, 4, [5, 6, [7, 8, [9,[0]]]]]]

# S tem 5 dimensões e abaixo segue o código para trocar o 0 por 17

s[2][2][2][2][1] = [17]
print(s)