"""
22. Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo, 
nas posições pares os valores do primeiro e nas posições impares os valores do segundo.

"""

# 1 Exemplo de codigo

A = [int(input(f"Digite o numero {i+1} para o vetor A: ")) for i in range(10)]
B = [int(input(f"Digite o numero {i+1} para o vetor B: ")) for i in range(10)]

C = [A[i] if i % 2 == 0 else B[i] for i in range(10)]

print("Vetor C:", C)