"""/7
7) Escreva um programa que leia 10 números inteiros e os armazene em um vetor.
Imprima o vetor, o maior elemento e a posição que ele se encontra.



"""

def ler_vetor(tamanho):
    vetor = []
    for i in range(tamanho):
        valor = int(input(f"Digite o {i + 1}º numero inteiro: "))
        vetor.append(valor)
    return vetor

def encontrar_maior_e_posicao(vetor):
    maior = vetor[0]
    posicao = 0
    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
            posicao = i
    return maior, posicao

vetor = ler_vetor(10)

print("Vetor:", vetor)

maior_elemento, posicao = encontrar_maior_e_posicao(vetor)

print("O maior elemento é:", maior_elemento)
print("Ele está ma posição:", posicao)