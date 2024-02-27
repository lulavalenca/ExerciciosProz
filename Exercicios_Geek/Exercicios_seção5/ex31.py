"""
Faça um programa que receba a altura e o peso de uma pessoa.
De acordo com a tabela a seguir, verifique e mostre qual a classificação
dessa pessoa.

    |    Altura    |                       Peso                       |
    |              |Até 60 | Entre 60 e 90 (Inclusive) | Acima de 90  |
    |Menor que 1,20|   A   |             D             |      G       |
    |De 1,20 a 1,70|   B   |             E             |      H       |
    |Maior que 1,70|   C   |             F             |      I       |



# Recebe a altura e o peso da pessoa como entrada do usuário
altura = float(input("Digite a altura da pessoa (em metros): "))
peso = float(input("Digite o peso da pessoa (em quilogramas): "))

# Verifica a classificação da pessoa com base na tabela fornecida
classificacao = ""

if altura < 1.20:
    if peso <= 60:
        classificacao = "A"
    elif peso <= 90:
        classificacao = "D"
    else:
        classificacao = "G"
elif altura <= 1.70:
    if peso <= 60:
        classificacao = "B"
    elif peso <= 90:
        classificacao = "E"
    else:
        classificacao = "H"
else:
    if peso <= 60:
        classificacao = "C"
    elif peso <= 90:
        classificacao = "F"
    else:
        classificacao = "I"

# Exibe a classificação da pessoa
print("Classificação da pessoa:", classificacao)



"""

altura = float(input("Digite a altura(em metros): "))
peso = float(input("Digite o peso(kg): "))

if (altura <= 1.20) and (peso <= 60):
    print("Classificação: A")

elif (altura > 1.20) and (altura <= 1.70) and (peso <= 60):
    print("Classificação: B")

elif (altura > 1.70) and (peso <= 60):
    print("Classificação: C")

elif (altura <= 1.20) and (peso > 60) and (peso <= 90):
    print("Classificação: D")

elif (altura > 1.20) and (altura <= 1.70) and (peso > 60) and (peso <= 90):
    print("Classificação: E")

elif (altura > 1.70) and (peso > 60) and (peso <= 90):
    print("Classificação: F")

elif (altura <= 1.20) and (peso > 90):
    print("Classificação: G")

elif (altura > 1.20) and (altura <= 1.70) and (peso > 90):
    print("Classificação: H")

elif (altura > 1.70) and (peso > 90):
    print("Classificação: I")

else:
    print("Erro inesperado!")