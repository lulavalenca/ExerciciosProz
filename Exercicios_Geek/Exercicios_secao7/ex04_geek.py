"""
4) Faça um programa que leia um vetor de 8 posições e, em seguida,
leia também dois valores X e Y quaisquer correspondentes a duas posições
no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados
nas respectivas posições X e Y.

"""
# Função para ler um vetor de tamanho especificado
def ler_vetor(tamanho):
    vetor = []
    for i in range(tamanho):
        valor = int(input(f"Digite o valor para a posição {i + 1}: "))
        vetor.append(valor)
    return vetor

# Função para calcular a soma dos valores nas posições X e Y
def calcular_soma(vetor, x, y):
    soma = vetor[x] + vetor[y]
    return soma

# Lendo o vetor de 8 posições
vetor = ler_vetor(8)

# Lendo os valores de X e Y
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

# Verificando se os valores de X e Y estão dentro do intervalo válido
if x >= 0 and x < 8 and y >= 0 and y < 8:
    # Calculando a soma dos valores nas posições X e Y
    resultado = calcular_soma(vetor, x, y)
    print(f"A soma dos valores nas posições {x} e {y} é:", resultado)
else:
    print("As posições X e Y devem estar entre 0 e 7, inclusive.")
