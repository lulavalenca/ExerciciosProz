"""
6) Faça um programa que receba do usuáro um vetor com 10 posições.
Em sequida deverá ser impresso o maior e o menor elemento do vetor.

"""

def ler_vetor(tamanho):
    vetor = []
    for i in range(tamanho):
        valor = int(input(f"Digite o valor para a posição {i + 1}: "))
        vetor.append(valor)
    return vetor

def encontrar_maior(vetor):
    maior = vetor[0]
    for valor in vetor:
        if valor > maior:
            maior = valor
    return maior

def encontrar_menor(vetor):
    menor = vetor[0]
    for valor in vetor:
        if valor < menor:
            menor = valor
    return menor

vetor = ler_vetor(10)

maior = encontrar_maior(vetor)
menor = encontrar_menor(vetor)

print("O maior elemento do vetor é:", maior)
print("O menor elemento do vetor é:", menor)
