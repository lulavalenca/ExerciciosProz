"""
30) Faça um programa que leia dois vetores de 10 elementos. 
Crie um vetor que seja a intersecção entre os 2 vetores anteriores, 
ou seja, que contém apenas os números que estão em ambos os vetores. 
Não deve conter números repetidos.

# 1 Exemplo de codigo
# Lendo 10 números inteiros para cada vetor
vetor1 = [int(input(f"Digite o número {i+1} para o vetor 1: ")) for i in range(10)]
vetor2 = [int(input(f"Digite o número {i+1} para o vetor 2: ")) for i in range(10)]

# Calculando a intersecção dos vetores
intersecao = list(set(vetor1) & set(vetor2))

# Imprimindo a intersecção
print("Intersecção:", intersecao)


# 2 Exemplo de codigo

def encontrar_intersecao(vetor1, vetor2):
    intersecao = []
    for elemento in vetor1:
        if elemento in vetor2 and elemento not in intersecao:
            intersecao.append(elemento)
    return intersecao 

vetor1 = [int(input("Digite o {}º elemento do primeiro vetor: ".format(i+1))) for i in range(10)]
vetor2 = [int(input("Digite o {}º elemento do segundo vetor: ".format(i+1))) for i in range(10)]

intersecao = encontrar_intersecao(vetor1, vetor2)

print("Intersecao entre os dois vetores:")
print(intersecao)

"""

# 2 Exemplo de codigo

def encontrar_intersecao(vetor1, vetor2):
    intersecao = []
    for elemento in vetor1:
        if elemento in vetor2 and elemento not in intersecao:
            intersecao.append(elemento)
    return intersecao 

vetor1 = [int(input("Digite o {}º elemento do primeiro vetor: ".format(i+1))) for i in range(10)]
vetor2 = [int(input("Digite o {}º elemento do segundo vetor: ".format(i+1))) for i in range(10)]

intersecao = encontrar_intersecao(vetor1, vetor2)

print("Intersecao entre os dois vetores:")
print(intersecao)