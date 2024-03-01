"""
11. Faça um programa que leia um número inteiro positivo N e 
imprima todos os números naturais de 0 até N em ordem crescente.

"""

N = int(input("Digite um numero inteiro positivo: "))

print("Numeros naturais de 0 até", N, "em ordem crescente: ")

for i in range(N + 1):
    print(i)