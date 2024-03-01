"""
9. Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais impares.

N = int(input("Digite um número inteiro positivo: "))

# Inicialize o contador e o número atual
contador = 0
numero = 1

# Loop para imprimir os N primeiros números naturais ímpares
while contador < N:
    if numero % 2 != 0:
        print(numero, end=" ")
        contador += 1
    numero += 1


"""

N = int(input("Digite um numero inteiro positivo: "))

contador = 0
numero = 1

while contador < N:
    if numero % 2 != 0:
        print(numero, end=" ")
        contador += 1
    numero += 1    