"""
15) Leia um vetor com 20 números inteiros. Escreva os elementos do vetor
eliminando elementos repetidos.

# 1) Exemplo da implementação do codigo

def eliminar_repitidos(vetor):
    return list(set(vetor))

vetor = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10, 11, 12, 12, 13, 14]
print(eliminar_repitidos(vetor))

# 2 Exemplo de implementação do codigo  

vetor = []
numeros_lidos = set()

for i in range(20):
    numero = int(input("Digite um numero: "))
    if numero not in numeros_lidos:
        numeros_lidos.add(numero)
        vetor.append(numero)

for numero in vetor:
    print(numero)        




"""
 
vetor = []
numeros_lidos = set()

for i in range(20):
    numero = int(input("Digite um numero: "))
    if numero not in numeros_lidos:
        numeros_lidos.add(numero)
        vetor.append(numero)

for numero in vetor:
    print(numero)        


