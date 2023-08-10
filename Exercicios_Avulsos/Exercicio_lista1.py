def calcular_soma(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

# Chamando a função para calcular a soma
numeros = [10, 20, 30, 40, 50]

# Chamando a função para calcular a soma
soma_total = calcular_soma(numeros)

# Exibindo o resultado
print("A soma dos elementos é:", soma_total)