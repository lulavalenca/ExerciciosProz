"""
07) Escreva um programa para inverter uma lista.

"""

def inverter_lista(lista):
    return lista[::-1]

lista = [10, 5, 7, 25, 13, 30, 45]

lista_invertida =inverter_lista(lista)

print("lista original:", lista)
print("lista invertida:", lista_invertida)