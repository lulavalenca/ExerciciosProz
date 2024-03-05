"""
46. Faça um programa que gera um número aleatório de 1 a 1000. 
O usuário deve tentar acertar qual o número foi gerado, a cada tentativa o programa deverá informar se o chute é menor ou maior que o número gerado. 
O programa acaba quando o usuário acerta o número gerado. O programa deve informar em quantas tentativas o número foi descoberto.

1 Exemplo

import random

numero_gerado = random.randint(1, 1000)
tentativas = 0

while True:
    tentativas += 1
    chute = int(input("Tente adivinhar o número gerado (entre 1 e 1000): "))
    if chute < numero_gerado:
        print("Maior! Tente novamente.")
    elif chute > numero_gerado:
        print("Menor! Tente novamente.")
    else:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break


        
2 Exemplo 

import random

# Gera uma lista de números de 1 a 1000
numeros = list(range(1, 1001))

# Seleciona aleatoriamente um número da lista
numero_gerado = random.choice(numeros)

tentativas = 0

while True:
    tentativas += 1
    chute = int(input("Tente adivinhar o número gerado (entre 1 e 1000): "))
    if chute < numero_gerado:
        print("Maior! Tente novamente.")
    elif chute > numero_gerado:
        print("Menor! Tente novamente.")
    else:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break


"""



import random

numero_gerado = random.randint(1, 1000)
tentativas = 0

while True:
    tentativas += 1
    chute = int(input("Tente adivinhar o número gerado (entre 1 e 1000): "))
    if chute < numero_gerado:
        print("Maior! Tente novamente.")
    elif chute > numero_gerado:
        print("Menor! Tente novamente.")
    else:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break
