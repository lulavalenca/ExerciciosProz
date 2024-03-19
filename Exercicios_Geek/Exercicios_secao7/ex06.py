"""
06) Escreva um programa para encontrar todos os números ímpares em uma lista.

"""

def encontrar_numeros_impares(lista):
    numeros_impares = []
    for numero in lista:
        if numero % 2 != 0:
            numeros_impares.append(numero)
    return numeros_impares 

lista = [10, 5, 7, 25, 13, 30, 45, 42, 8]

impares = encontrar_numeros_impares(lista)

print("Os numeros impares na lista são: ", impares)