"""
21. Faça um programa que receba do usuário dois vetores, A e B, 
com 10 números inteiros cada. Crie um novo vetor denominado C calculando C = AB. 
Mostre na tela os dados do vetor C. faça esse codigo em python

"""

A = [int(input(f"Digite o numero {i+1} para o vetor A:")) for i in range(10)]
B = [int(input(f"Digite o numero {i+1} para o vetor B:")) for i in range(10)]

C = [a * b for a, b in zip(A, B)]

print("Vetor C:", C)