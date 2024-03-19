"""
05) Escreva um programa para encontrar todos os números pares em uma lista. 
   
"""

def encontrar_numeros_pares(lista):
    numeros_pares = []
    for numero in lista:
        if numero % 2 == 0:
            numeros_pares.append(numero)
    return numeros_pares

lista = [10, 5, 7, 25, 13, 30, 45, 42, 8]

pares = encontrar_numeros_pares(lista)

print("Os numeros pares na lista são:", pares)