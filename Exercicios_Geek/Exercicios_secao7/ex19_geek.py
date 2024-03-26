"""
19) Faça um vetor de tamanho 50 preenchido com o seguinte valor:
(i + 5 * i) % (i + 1), sendo i a posição do elemento no vetor.
Em seguida imprima o vetor na tela.

"""
# 1 Exemplo de codigo

# Tamanho do vetor
tamanho = 50

# Criando o vetor com os valores específicos
vetor = [(i + 5 * i) % (i + 1) for i in range(tamanho)]

# Imprimindo o vetor na tela
print("Vetor preenchido:")
print(vetor)


# 2 Exemplo de codigo

vetor = [(i + 5 * i) % (i + 1) for i in range(50)]
print(vetor)

# 3 Exemplo de codigo

# Declaração do vetor
vetor = []

# Preenchimento do vetor
for i in range(50):
    valor = (i + 5 * i) % (i + 1)
    vetor.append(valor)

# Exibição do vetor
print("Vetor:", vetor)
