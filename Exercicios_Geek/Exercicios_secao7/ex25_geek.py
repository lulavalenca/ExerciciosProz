"""
25. Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais
 que não são múltiplos de 7 ou que terminam com 7.

"""

vetor = []
i = 0

while len(vetor) < 100:
    if i % 7 != 0 and i % 10 != 7:
        vetor.append(i)
    i += 1

print("Vetor: ", vetor)        