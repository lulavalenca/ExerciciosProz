# Recebe os valores dos lados do triângulo como entrada do usuário
A = float(input("Digite o valor do lado A: "))
B = float(input("Digite o valor do lado B: "))
C = float(input("Digite o valor do lado C: "))

# Verifica se os lados podem formar um triângulo
if A + B > C and A + C > B and B + C > A:
    if A == B and B == C:
        print("É um triângulo equilátero.")
    elif A == B or B == C or A == C:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Não é possível formar um triângulo com os valores fornecidos.")
