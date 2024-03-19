"""
18)Escreva um programa para calcular a soma dos elementos em índices pares de uma lista.

"""

def soma_indices_pares(lista):
    soma = 0 
    for i in range(0, len(lista), 2):
        soma += lista[i]
    return soma 

lista = [10, 5, 7, 25, 13, 30, 45]

soma = soma_indices_pares(lista)

print("A soma dos elementos em indices pares da lista é:", soma)