"""
23) Escreva um programa para verificar se todos os elementos em uma lista são únicos.

"""

def elementos_unicos(lista):
    return len(set(lista)) == len(lista)

lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 4, 5]

if elementos_unicos(lista1):
    print("todos os elementos em lista1 são unicos.")
else:
    print("Lista1 contém elementos duplicados.")

if elementos_unicos(lista2):
    print("todos os elementos em lista2 são unicos.")
else:
    print("Lista2 contém elementos duplicados.")            