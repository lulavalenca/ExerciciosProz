"""
31. Faça um programa que calcule e escreva o valor de S
S
1
3 5 7 99
+ +-+
1 2 3 4 50


"""

def calcular_S(n):
    S = 0
    sinal = 1
    for i in range(1, n+1):
        termo = sinal * (2*i - 1) / i
        S += termo
        sinal *= -1  # Alternar o sinal a cada termo
    return S

# Solicitar ao usuário o valor de n
n = int(input("Digite o valor de n: "))

# Calcular o valor de S
resultado_S = calcular_S(n)

# Exibir o resultado
print("O valor de S é:", resultado_S)
