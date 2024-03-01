"""
8. Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

# Inicialize as variáveis para armazenar o menor e o maior valor
menor = float('inf')  # Inicialize como infinito para garantir que qualquer número seja menor
maior = float('-inf') # Inicialize como menos infinito para garantir que qualquer número seja maior

# Loop para ler os 10 números
for _ in range(10):
    numero = float(input("Digite um número: "))
    
    # Atualize o menor e o maior valor, se necessário
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero

# Imprima o menor e o maior valor lido
print("O menor valor digitado foi:", menor)
print("O maior valor digitado foi:", maior)


"""

menor = float('inf')
maior = float('inf')

for _ in range(10):
    numero = float(input("Digite um numero: "))

    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero

print("O menor valor digitado foi:", menor)
print("O maior valor digitado foi:", maior)            