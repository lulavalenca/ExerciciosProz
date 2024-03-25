"""
30) Escreva um programa para verificar se uma lista é sublista de outra lista.

"""

def eh_sublista(lista, sublista):
    if len(sublista) == 0:
        return True
    try:
        indice = lista.index((sublista[0]))
        return lista[indice:indice + len(sublista)] == sublista
    except ValueError:
        return False

lista_principal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sublista1 = [1, 2, 3, 4]
sublista2 = [8, 9, 10]                         

print("A lista sublista1 é sublista principal:", eh_sublista(lista_principal, sublista1))
print("A lista sublista2 é sublista principal:", eh_sublista(lista_principal, sublista2))