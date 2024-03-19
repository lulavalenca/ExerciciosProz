"""
15) Escreva um programa para verificar se uma lista está vazia.

"""


def lista_esta_vazia(lista):
    return len(lista) == 0

lista_vazia = []
lista_nao_vazia = [1, 2, 3]

if lista_esta_vazia(lista_vazia):
    print("A lista está vazia.")
else:
    print("A lista não esta vazia.")
