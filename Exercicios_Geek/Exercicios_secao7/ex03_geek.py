"""
3) Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado
das componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm
10 elementos cada. Imprimir todos os conjuntos.3) Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado
das componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm
10 elementos cada. Imprimir todos os conjuntos.

"""
def calcular_quadrado(vetor):
    quadrados = []
    for numero in vetor:
        quadrado = numero ** 2
        quadrados.append(quadrado)
    return quadrados    

def ler_conjunto(tamanho):
    conjunto = []
    for i in range(tamanho):
        numero = float(input(f"Digite o {i+1}º numero real: "))
        conjunto.append(numero)
    return conjunto    

print("Digite os numeros do primeiro conjunto:")
conjunto1 = ler_conjunto(10)

quadrados_conjunto1 = calcular_quadrado(conjunto1)

print("\nDigite os numeros do segundo conjunto:")
conjunto2 = ler_conjunto(10)

quadrados_conjunto2 = calcular_quadrado(conjunto2)

print("\nPrimeiro conjunto e seus quadrados:")
for i in range(10):
    print(f"Numero: {conjunto1[i]} - Quadrado: {quadrados_conjunto1[i]}")

    print("\nSegundo conjunto e seus quadrados:")
for i in range(10):
    print(f"Número: {conjunto2[i]} - Quadrado: {quadrados_conjunto2[i]}")
