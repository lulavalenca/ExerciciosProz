"""
12 - Faça um programa que leia um número inteiro positivo N e 
imprima todos os números naturais de 0 até N em ordem decrescente.

"""

N = int(input("Digite um numero inteiro positivo: "))

print("Numeros naturais de", N, "até 0 em ordem decrescente: ")

for i in range(N, -1, -1):
    print(i)