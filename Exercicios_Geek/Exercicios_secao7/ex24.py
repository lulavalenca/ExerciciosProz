"""
24) Escreva um programa para verificar se todos os elementos em uma lista são iguais.

"""

def elementos_iguais(lista):
    primeiro_elemento = lista[0]
    for elemento in lista[1:]:
        if elemento != primeiro_elemento:
            return False
    return True

lista1 = [1, 1, 1, 1, 1, 1, 1]
lista2 = [1, 2, 3, 4, 5] 

if elementos_iguais(lista1):
    print("todos os elementos em lista1 são iguais.")
else:
    print("Lista1 contém elementos diferentes.") 

if elementos_iguais(lista2):
    print("todos os elementos em lista2 são iguais.")
else:
    print("Lista2 contém elementos diferentes.")        
