"""
16) Escreva um programa para encontrar o produto de todos os elementos em uma lista.

"""

def produto_lista(lista):
    produto = 1
    for elemento in lista:
        produto *= elemento
    return produto

lista = [1, 2, 3, 4, 5]

resultado = produto_lista(lista)

print("O produto de todos os elementos na lista é:", resultado)