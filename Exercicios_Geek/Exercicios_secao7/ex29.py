"""
29) Escreva um programa para encontrar o maior elemento na diagonal principal de uma matriz.

"""
def maior_diagonal_principal(matriz):
    if len(matriz) != len(matriz[0]):
        return "A matriz não é quadrada."
    
    maior_elemento = matriz[0][0]

    for i in range(len(matriz)):
        if matriz[i][i] > maior_elemento:
            maior_elemento = matriz[i][i]

    return maior_elemento        

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

maior = maior_diagonal_principal(matriz)

print("O maior elemento na diagonal principal da matriz é:", maior)