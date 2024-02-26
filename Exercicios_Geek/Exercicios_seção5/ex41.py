"""

Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua
classificação de acordo com a tabela abaixo:

    |     IMC      | Classificação
    | < 18,5       | Abaixo do Peso
    | 18,6 - 24,9  | Saudável
    | 25,0 - 29,9  | Peso em excesso
    | 30,0 - 34,9  | Obesidade Grau I
    | 35,0 - 39,9  | Obesidade Grau II(severa)
    | >= 40        | Obesidade Grau III(mórbida)


def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do Peso"
    elif 18.5 <= imc <= 24.9:
        return "Saudável"
    elif 25.0 <= imc <= 29.9:
        return "Peso em Excesso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidade Grau I"
    elif 35.0 <= imc <= 39.9:
        return "Obesidade Grau II (severa)"
    else:
        return "Obesidade Grau III (mórbida)"

peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

print(f"O IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")



"""

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do Peso"
    elif 18.5 <= imc <= 24.9:
        return "Saudável"
    elif 25.0 <= imc <= 29.9:
        return "Peso em Excesso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidade Grau I"
    elif 35.0 <= imc <= 39.9:
        return "Obesidade Grau II (severa)"
    else:
        return "Obesidade Grau III (mórbida)"

peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

print(f"O IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
