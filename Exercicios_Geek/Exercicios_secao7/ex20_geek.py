"""
20) Escreva um programa que leia números inteiros no intervalo [0,50] e os armazene em um
vetor com 10 posições. Preencha um segundo vetor apenas com os números ímpares
do primeiro vetor. Imprima os dois vetores, 2 elementos por linha.

"""

def soma_impares(vetor):
    soma = 0
    for numero in vetor:
        if numero % 2 == 1:
            soma += numero
    return soma

vetor = [1, 2, 3, 4, 5]
soma_impares = soma_impares(vetor)
print(f"A soma dos numeros impares do vetor é: {soma_impares}")        

# 1 Exemplo de codigo

entrada = input("Digite 10 numeros inteiros no intervalo [0,50], separados por virgulas: ")
numeros_texto = entrada.split(',')

vetor = []
for texto_numero in numeros_texto:
    try:
        numero = int(texto_numero)
        if 0 <= numero <= 50:
            vetor.append(numero)
        else:
            print("Erro: O numero", numero, "não está no intervalo [0, 50].")
            exit()
    except ValueError:
        print("Erro: o valor", texto_numero, "não é um numero inteiro valido")
        exit()

if len(vetor) != 10:
    print("Erro: Você deve inserir exatamente 10 números.")
    exit()

vetor_impares = [numero for numero in vetor if numero % 2 != 0]

print("Vetor:")
for i in range(0, len(vetor), 2):
    print(vetor[i:i+2])

print("Vetor de numeros impares:")
for i in range(0, len(vetor_impares), 2):
    print(vetor_impares[i:i+2])