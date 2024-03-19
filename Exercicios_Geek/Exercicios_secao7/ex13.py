"""
13) Escreva um programa para encontrar o segundo maior número em uma lista

"""

def segundo_maior(lista):
    lista_ordenada = sorted(lista, reverse=True)

    return lista_ordenada[1]

lista = [10, 5, 7, 25, 13, 30, 45]

segundo_maior_numero = segundo_maior(lista)

print("O segundo maior numero na lista é:", segundo_maior_numero)