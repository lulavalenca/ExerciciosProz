"""
09) Escreva um programa para remover os elementos duplicados de uma lista.

"""

def remover_duplicatas(lista):
    return list(set(lista))

lista = [10, 5, 7, 25, 13, 30, 45, 10, 7, 25]

lista_sem_duplicatas = remover_duplicatas(lista)

print("Lista original:", lista)
print("lista sem elementos duplicados:", lista_sem_duplicatas)