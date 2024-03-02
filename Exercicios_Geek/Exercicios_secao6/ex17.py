"""
17 - Faça um programa que leia um número inteiro positivo n e calcule a soma dos primeiros números naturais.

"""

n = int(input("Digite um numero inteiro positivo: "))

soma = 0
for i in range(1, n + 1):
    soma += i

print("A soma dos primeiros", n, "numeros naturais é:", soma)    