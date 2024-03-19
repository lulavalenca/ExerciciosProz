"""
10) Escreva um programa para contar quantas vezes um determinado elemento aparece em uma lista.

"""

def contar_ocorrencias(elemento, lista):
    return lista.count(elemento)

lista = [10, 5, 7, 25, 13, 30, 45, 10, 7, 25]

elemento_procurado = 25

ocorrencias = contar_ocorrencias(elemento_procurado, lista)

print(f"O elemento {elemento_procurado} aparece {ocorrencias} vezes na lista.")