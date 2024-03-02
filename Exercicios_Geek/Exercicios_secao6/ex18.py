"""
18. Escreva um algoritmo que leia certa quantidade de números e 
imprima o maior deles e quantas vezes o maior número foi lido. 
A quantidade de números a serem lidos deve ser fornecida pelo usuário.

"""

quantidade = int(input("quantos numeros voce deseja digitar? "))

maior_numero = None
quantidade_maior = 0

for i in range(quantidade):
    numero = float(input(f"Digite o {i + 1}º numero: "))
    if i == 0 or numero > maior_numero:
        maior_numero = numero
        quantidade_maior = 1
    elif numero == maior_numero:
        quantidade_maior += 1

print("O maior numero digitado é:", maior_numero)
print("Ele foi digitado", quantidade_maior, "vezes.")            