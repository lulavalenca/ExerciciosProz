"""
25) Escreva um programa para criar uma lista de todos os divisores de um número

"""

def encontrar_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

numero = 42

divisores = encontrar_divisores(numero)

print(f"Os divisores de {numero} são:", divisores)
