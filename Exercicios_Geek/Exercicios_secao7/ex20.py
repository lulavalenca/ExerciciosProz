"""
20) Escreva um programa para encontrar o elemento mais frequente em uma lista.

"""

# Função para encontrar o elemento mais frequente em uma lista
def elemento_mais_frequente(lista):
    contagem = {}
    for elemento in lista:
        if elemento in contagem:
            contagem[elemento] += 1
        else:
            contagem[elemento] = 1
    
    elemento_mais_frequente = None
    max_contagem = 0
    for elemento, freq in contagem.items():
        if freq > max_contagem:
            elemento_mais_frequente = elemento
            max_contagem = freq
    
    return elemento_mais_frequente

# Lista de números
lista = [10, 5, 7, 25, 13, 30, 45, 10, 7, 25, 10, 10]

# Encontra o elemento mais frequente na lista
elemento = elemento_mais_frequente(lista)

# Imprime o elemento mais frequente
print("O elemento mais frequente na lista é:", elemento)
