"""
25 - Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.

soma = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        soma += 1

print("A soma dos numeros naturais abaixo de 1000 que são multiplos de 3 ou 5 é:", soma)        

Exemplo 2


limite = int(input("Digite o numero limite: "))

soma = 0

for i in range(1, limite):
    if i % 3 == 0 or i % 5 == 0:
        soma += i

print(f"A soma dos numeros naturais abaixo de {limite} que são multiplos de 3 ou 5 é:", soma)      



"""

limite = int(input("Digite o numero limite: "))

soma = 0

for i in range(1, limite):
    if i % 3 == 0 or i % 5 == 0:
        soma += i

print(f"A soma dos numeros naturais abaixo de {limite} que são multiplos de 3 ou 5 é:", soma)      