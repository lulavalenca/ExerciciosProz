"""
28)Leia 10 números inteiros e armazene em um vetor 2. 
Crie dois novos vetores vl e v2. Copie os valores ímpares de v para v1, 
e os valores pares de v para v2. Note que cada um dos vetores vl e v2 têm no máximo 10 elementos, 
mas nem todos os elementos são utilizados. 
No final escreva os elementos UTILIZADOS de vi e v2. faça esse codigo em python

#Exemplo de codigo 1
# Lendo 10 números inteiros e armazenando em um vetor
v = [int(input(f"Digite o número {i+1}: ")) for i in range(10)]

# Criando dois novos vetores v1 e v2
v1 = [num for num in v if num % 2 != 0]  # valores ímpares de v
v2 = [num for num in v if num % 2 == 0]  # valores pares de v

# Imprimindo os elementos utilizados de v1 e v2
print("Elementos ímpares em v1:", v1)
print("Elementos pares em v2:", v2)


# 2 Exemplo de codigo 

# Lê 10 números inteiros e armazena em um vetor
vetor = []
for i in range(10):
    numero = int(input("Digite o {}º número inteiro: ".format(i + 1)))
    vetor.append(numero)

# Cria os vetores v1 e v2
v1 = []
v2 = []

# Copia os valores ímpares para v1 e os valores pares para v2
for num in vetor:
    if num % 2 != 0:
        v1.append(num)
    else:
        v2.append(num)

# Imprime os elementos UTILIZADOS de v1 e v2
print("Elementos ímpares de v1:", v1)
print("Elementos pares de v2:", v2)


"""

# 1 Exemplo de codigo 

v = [int(input(f"Digite o número {i+1}: ")) for i in range(10)]


v1 = [num for num in v if num % 2 != 0]  # valores ímpares de v
v2 = [num for num in v if num % 2 == 0]  # valores pares de v

print("Elementos ímpares em v1:", v1)
print("Elementos pares em v2:", v2)


# 2 Exemplo de codigo 

# Lê 10 números inteiros e armazena em um vetor
vetor = []
for i in range(10):
    numero = int(input("Digite o {}º número inteiro: ".format(i + 1)))
    vetor.append(numero)

# Cria os vetores v1 e v2
v1 = []
v2 = []

# Copia os valores ímpares para v1 e os valores pares para v2
for num in vetor:
    if num % 2 != 0:
        v1.append(num)
    else:
        v2.append(num)

# Imprime os elementos UTILIZADOS de v1 e v2
print("Elementos ímpares de v1:", v1)
print("Elementos pares de v2:", v2)
