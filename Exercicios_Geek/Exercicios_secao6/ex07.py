"""
07 - Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.



"""

soma = 0
contador = 0

for _ in range(10):
    numero = int(input("Digite um numero inteiro positivo: "))
    if numero > 0:
        soma += numero
        contador += 1

if contador > 0:
    media = soma / contador
    print("A media dos numeros positivos é:", media)
else:
    print("Nenhum numero positivo foi inserido.")    