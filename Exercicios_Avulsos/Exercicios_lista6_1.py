def multiplicar_matrizes(matriz1, matriz2):
    linhas_matriz1 = len(matriz1)
    colunas_matriz1 = len(matriz1[0])
    linhas_matriz2 = len(matriz2)
    colunas_matriz2 = len(matriz2[0])

    # Verifica se as matrizes podem ser multiplicadas
    if colunas_matriz1 != linhas_matriz2:
        return None  # Retona None se a multiplicação não é possivel
    
    matriz_resultante = [
        [
            sum(matriz1[i][k] * matriz2[k][j] for k in range(colunas_matriz1))
            for j in range(colunas_matriz2)
        ]
        for i in range(linhas_matriz1)
    ]

    return matriz_resultante

# Exemplo de duas matrizes
matriz1 = [[1, 2, 3], [4, 5, 6]]
matriz2 = [[7, 8], [9, 10], [11, 12]]

#Chamando a função para multiplicar as matrizes
matriz_resultante = multiplicar_matrizes(matriz1, matriz2)

#Exibindo o resultado
if matriz_resultante is None:
    print("As matrizes não podem ser multiplicadas.")
else:
    print("Matriz resultante:")
    for linha in matriz_resultante:
        print(linha)    