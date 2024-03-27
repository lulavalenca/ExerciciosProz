"""
23. Ler dois conjuntos de números reais, 
armazenando-os em vetores e calcular o produto escalar entre eles. 
Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, 
sendo que o produto escalar é dado por: x1 y1+X2 Y2+...+ In * Yn. 
faça esse programa em python



"""

# 1 Exemplo de codigo

A = [float(input(f"Digite o numero {i+1} para o vetor A: ")) for i in range(5)]
B = [float(input(f"Digite o numero {i+1} para o vetor B: ")) for i in range(5)]


produto_escalar = sum(a * b for a, b in zip(A, B))

print("vetor A:", A)
print("vetor B:", B)
print("Produto escalar:", produto_escalar)


# 2 Exemplo de codigo

