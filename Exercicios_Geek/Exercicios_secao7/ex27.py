"""
27) Escreva um programa para criar uma lista de números no intervalo entre dois números dados.

"""

def lista_numeros_intervalo(inicio, fim):
    return list(range(inicio, fim + 1))

inicio = 10
fim = 20.

numeros_intervalo = lista_numeros_intervalo(inicio, fim)

print("Lista de numeros no intervalo [", inicio, ",", fim, "]:", numeros_intervalo)