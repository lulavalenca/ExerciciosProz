"""
﻿30. Faça programas para calcular as seguintes sequências:
1+2+3+4+5+...+n.
1-2-3-4+5+...+(2n-1) 1+3+5+7++ (2n-1) faça esse codigo em python 




"""

def soma_ate_n(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma

n = int(input("Digite o valor de n: "))
resultado = soma_ate_n(n)
print("A soma dos numeros de 1 a", n, "é:", resultado)    

# exemplo2 de codigo

def alternancia_ate_2n_menos_1(n):
    soma = 0
    sinal = 1
    for i in range(1, 2 * n):
        soma += sinal * i
        sinal *= -1
    return soma

n = int(input("Digite o valor de n: "))
resultado = alternancia_ate_2n_menos_1(n)
print("A sequência alternada de 1 a", 2 * n - 1, "é:", resultado)


# Exemplo3 de codigo 

def soma_impares_ate_2n_menos_1(n):
    soma = 0
    for i in range(1, 2 * n, 2):
        soma += i
    return soma

n = int(input("Digite o valor de n: "))
resultado = soma_impares_ate_2n_menos_1(n)
print("A soma dos números ímpares de 1 a", 2 * n - 1, "é:", resultado)
