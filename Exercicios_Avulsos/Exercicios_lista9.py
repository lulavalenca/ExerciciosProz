def gerar_subconjuntos(lista):
    n = len(lista)
    subconjuntos = []

    for i in range(1 << n):
        subconjunto = [lista[j] for j in range(n) if (i & (1 << j)) > 0]
        subconjuntos.append(subconjunto)

    return subconjuntos    

#
numeros = [1, 2, 3]

#
subconjuntos = gerar_subconjuntos(numeros)

#
print("Subconjuntos da lista:", subconjuntos)