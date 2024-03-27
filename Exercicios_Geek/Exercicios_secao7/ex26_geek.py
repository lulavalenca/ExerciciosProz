"""
26. Faça um programa que calcule o 
desvio padrão de um vetor contendo 10 números, 
onde mé a media do vetor.

"""

A = [float(input(f"Digite o numero {i+1} para o vetor A: ")) for i in range(10)]
B = [float(input(f"Digite o numero {i+1} para o vetor B: ")) for i in range(10)]

C = [a + b for a, b in zip(A, B)]

print("Vetor C:", C)