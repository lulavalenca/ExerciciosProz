"""
21) Escreva um programa para encontrar o elemento menos frequente em uma lista.

"""

# Função para encontrar o elemento menos frequente em uma lista
def elemento_menos_frequente(lista):
    contagem = {}
    for elemento in lista:
        if elemento in contagem:
            contagem[elemento] += 1
        else:
            contagem[elemento] = 1
    
    elemento_menos_frequente = None
    min_contagem = float('inf')
    for elemento, freq in contagem.items():
        if freq < min_contagem:
            elemento_menos_frequente = elemento
            min_contagem = freq
    
    return elemento_menos_frequente

# Lista de números
lista = [10, 5, 7, 25, 13, 30, 45, 10, 7, 25, 10, 10]

# Encontra o elemento menos frequente na lista
elemento = elemento_menos_frequente(lista)

# Imprime o elemento menos frequente
print("O elemento menos frequente na lista é:", elemento)
