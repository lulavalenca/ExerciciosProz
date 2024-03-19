"""
12) Escreva um programa para criar uma lista de listas (matriz) a partir de duas listas


"""

def criar_matriz(lista1, lista2):
    matriz = [lista1, lista2]
    return matriz

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

matriz = criar_matriz(lista1, lista2)

print("Matriz crizada:")
for linha in matriz:
    print(linha)