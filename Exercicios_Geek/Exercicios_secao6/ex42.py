"""
42. Faça um programa que leia um conjunto não determinado de valores, 
um de cada vez, e escreva para cada um dos valores lidos, o quadrado, 
o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.



"""

import math

while True:
    valor = float(input("Digite um valor (0 ou negativo para sair): "))
    if valor <= 0:
        break
    quadrado = valor ** 2
    cubo = valor ** 3
    raiz_quadrada = math.sqrt(valor)
    print(f"Para o valor {valor}, o quadrado é {quadrado}, o cubo é {cubo} e a raiz quadrada é {raiz_quadrada} ")