"""
15 - Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os
números impares de 1 até N em ordem crescente.

"""

N = int(input("Digite um numero inteiro positivo impar: "))

print("Numeros impares de 1 até", N, "em ordem crescente:")

for i in range(1, N+1, 2):
    print(i)