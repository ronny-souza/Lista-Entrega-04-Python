# QUESTÃO 06 - O Zodíaco Chinês é composto por animais com ciclo de 12 anos. Uma maneira simplificada de 
# identificá-lo é verificando-se apenas o ano de seu nascimento do seguinte modo:
#
# > AQUI VEM UMA TABELA <

# Crie um programa que tenha uma tupla preenchida com os signos e seus respectivos valores exibidos na tabela.
# Com a tupla criada, o usuário poderá entrar com seu ano de nascimento, e o programa deve exibir qual é o 
# signo correspondente.

valoresSignos = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
signos = ("Macaco", "Galo", "Cão", "Porco", "Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Carneiro")
signosComValores = (valoresSignos, signos)

def identificaSigno(valor):
    
    if valor == signosComValores[0][0]:
        print(signosComValores[1][0])

    elif valor == signosComValores[0][1]:
        print(signosComValores[1][1])
    
    elif valor == signosComValores[0][2]:
        print(signosComValores[1][2])

    elif valor == signosComValores[0][3]:
        print(signosComValores[1][3])

    elif valor == signosComValores[0][4]:
        print(signosComValores[1][4])

    elif valor == signosComValores[0][5]:
        print(signosComValores[1][5])

    elif valor == signosComValores[0][6]:
        print(signosComValores[1][6])

    elif valor == signosComValores[0][7]:
        print(signosComValores[1][7])

    elif valor == signosComValores[0][8]:
        print(signosComValores[1][8])

    elif valor == signosComValores[0][9]:
        print(signosComValores[1][9])

    elif valor == signosComValores[0][10]:
        print(signosComValores[1][10])

    elif valor == signosComValores[0][11]:
        print(signosComValores[1][11])

    else:
        print("Não foi possível definir seu signo correspondente!")

def calculaAno(anoNascimento):
    valorCorrespondente = anoNascimento % 12
    return valorCorrespondente


anoNascimento = int(input("Digite seu ano de nascimento: "))
valorCorrespondenteSigno = calculaAno(anoNascimento)
identificaSigno(valorCorrespondenteSigno)

