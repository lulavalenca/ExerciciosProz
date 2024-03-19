"""
14) Escreva um programa para encontrar o segundo menor número em uma lista.

"""

def segundo_menor(lista):
    lista_ordenada = sorted(lista)

    return lista_ordenada[1]

lista = [10, 5, 7, 25, 13, 30, 45]

segundo_menor_numero = segundo_menor(lista)

print("O segundo menor numero na lista é:", segundo_menor_numero)