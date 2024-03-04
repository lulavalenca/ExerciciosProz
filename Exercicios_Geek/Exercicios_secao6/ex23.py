"""
23 - Faca um algoritmo que leia um número positivo e imprima seus divisores.

"""

numero = int(input("Digite um numero popsitivo: "))

if numero <= 0:
    print("O numero não é positivo.")
else:
    print("Divisores de", numero, ":")

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)        