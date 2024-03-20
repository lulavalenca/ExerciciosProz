"""
5) Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.

# Função para ler um vetor de tamanho especificado
def ler_vetor(tamanho):
    vetor = []
    for i in range(tamanho):
        valor = int(input(f"Digite o valor para a posição {i + 1}: "))
        vetor.append(valor)
    return vetor

# Função para contar quantos valores pares o vetor possui
def contar_pares(vetor):
    contador = 0
    for valor in vetor:
        if valor % 2 == 0:
            contador += 1
    return contador

# Lendo o vetor de 10 posições
vetor = ler_vetor(10)

# Contando quantos valores pares o vetor possui
quantidade_pares = contar_pares(vetor)

# Escrevendo o resultado na tela
print(f"O vetor possui {quantidade_pares} valores pares.")


"""

def ler_vetor(tamanho):
    vetor = []
    for i in range(tamanho):
        valor = int(input(f"Digite o valor para a posição {i + 1}:"))
        vetor.append(valor)
    return vetor 

def contar_pares(vetor):
    contador = 0
    for valor in vetor:
        if valor % 2 == 0:
            contador += 1
    return contador

vetor = ler_vetor(10)

quantidade_pares = contar_pares(vetor)

print(f"O vetor possui {quantidade_pares} valores pares.")
