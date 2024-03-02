"""
16 - Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os
números impares de 1 até N em ordem decrescente.

"""


N = int(input("Digite um numero inteiro positivo impar: "))

print("Numeros impares de", N, "até 1 e, ordem decrescente:")

for i in range(N, 0, -2):
    print(i)


    