"""
11) Escreva um programa para mesclar duas listas em uma única lista ordenada.

"""

def mesclar_e_ordenar(lista1, lista2):
    
    lista_mesclada = lista1.copy()
    lista_mesclada.extend(lista2)
    
    lista_mesclada_ordenada = sorted(lista_mesclada)
    return lista_mesclada_ordenada

lista1 = [10, 5, 7, 25]
lista2 = [13, 30, 45]

lista_mesclada_ordenada = mesclar_e_ordenar(lista1, lista2)

print("Lista mesclada e ordenada:", lista_mesclada_ordenada)