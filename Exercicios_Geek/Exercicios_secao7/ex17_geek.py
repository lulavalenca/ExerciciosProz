"""
17) Leia um vetor de 10 posições e atribua valor 0
para todos os elemntos que possírem valores negativos

# 1 Excemplo de codigo

vetor = []

for i in range(10):
    numero = float(input("Digite um numero: "))
    vetor.append(numero)

for i in range(len(vetor)):
    if vetor[i] < 0:
        vetor[i] = 0

print("vetor com elementos negativos substituidos por 0:", vetor)


# 2 Exemplo de codigo

# Função para atribuir valor 0 a elementos negativos do vetor
def substituir_negativos_por_zero(vetor):
    for i in range(len(vetor)):
        if vetor[i] < 0:
            vetor[i] = 0

# Lê os valores do vetor
vetor = []
for i in range(10):
    valor = float(input("Digite o valor da posição {}: ".format(i + 1)))
    vetor.append(valor)

# Substitui os valores negativos por zero
substituir_negativos_por_zero(vetor)

# Exibe o vetor após a substituição
print("Vetor após substituir os valores negativos por zero:", vetor)



"""
# 1 Excemplo de codigo

vetor = []

for i in range(10):
    numero = float(input("Digite um numero: "))
    vetor.append(numero)

for i in range(len(vetor)):
    if vetor[i] < 0:
        vetor[i] = 0

print("vetor com elementos negativos substituidos por 0:", vetor)


# 2 Exemplo de codigo

# Função para atribuir valor 0 a elementos negativos do vetor
def substituir_negativos_por_zero(vetor):
    for i in range(len(vetor)):
        if vetor[i] < 0:
            vetor[i] = 0

# Lê os valores do vetor
vetor = []
for i in range(10):
    valor = float(input("Digite o valor da posição {}: ".format(i + 1)))
    vetor.append(valor)

# Substitui os valores negativos por zero
substituir_negativos_por_zero(vetor)

# Exibe o vetor após a substituição
print("Vetor após substituir os valores negativos por zero:", vetor)
