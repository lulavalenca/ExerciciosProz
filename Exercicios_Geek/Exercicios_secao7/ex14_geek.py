"""
14) Faça um programa que leia um vetor de 10 posiçoes e verifique se existem valores iguais
e os escreva na tela.

"""

vetor = []
valores_iguais = []

for i in range(10):
    numero = float(input("Digite um numero: "))
    vetor.append(numero)

for i in range(len(vetor)):
    for j in range(i + 1, len(vetor)):
        if vetor[i] == vetor[j] and vetor[i] not in valores_iguais:
            valores_iguais.append(vetor[i])

if valores_iguais:
    print("Valores iguais:", valores_iguais)
else:
    print("Não existem valores iguais no vetor. ")                    