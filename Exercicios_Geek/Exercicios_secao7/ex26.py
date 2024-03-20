"""
26) Escreva um programa para criar uma lista de números aleatórios.

"""

import random

def lista_numeros_aleatorios(tamanho, minimo, maximo):
    return [random.randint(minimo, maximo) for _ in range(tamanho)]

tamanho =  10
minimo = 1
maximo = 100

numeros_aleatorios = lista_numeros_aleatorios(tamanho, minimo, maximo)

print("Lista de numeros aleatorios:", numeros_aleatorios)