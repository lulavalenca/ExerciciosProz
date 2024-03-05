"""
40) Elabore um programa que faça leitura de vários números inteiros, até que se
digite um número negativo. O programa tem que retornar o maior e o menor
número lido.

# Inicializar as variáveis para armazenar o maior e o menor números
maior_numero = float('-inf')  # Inicializando com o menor valor possível
menor_numero = float('inf')   # Inicializando com o maior valor possível

# Loop para ler os números até que seja digitado um número negativo
while True:
    numero = int(input("Digite um número inteiro (ou um número negativo para encerrar): "))
    
    # Verificar se o número digitado é negativo (condição de saída do loop)
    if numero < 0:
        break
    
    # Atualizar o maior número, se necessário
    if numero > maior_numero:
        maior_numero = numero
    
    # Atualizar o menor número, se necessário
    if numero < menor_numero:
        menor_numero = numero

# Verificar se foram digitados números positivos antes de exibir os resultados
if maior_numero == float('-inf') or menor_numero == float('inf'):
    print("Nenhum número válido foi digitado.")
else:
    # Exibir o maior e o menor número digitado
    print("O maior número digitado foi:", maior_numero)
    print("O menor número digitado foi:", menor_numero)



"""

# Inicializar as variáveis para armazenar o maior e o menor números
maior_numero = float('-inf')  # Inicializando com o menor valor possível
menor_numero = float('inf')   # Inicializando com o maior valor possível

# Loop para ler os números até que seja digitado um número negativo
while True:
    numero = int(input("Digite um número inteiro (ou um número negativo para encerrar): "))
    
    # Verificar se o número digitado é negativo (condição de saída do loop)
    if numero < 0:
        break
    
    # Atualizar o maior número, se necessário
    if numero > maior_numero:
        maior_numero = numero
    
    # Atualizar o menor número, se necessário
    if numero < menor_numero:
        menor_numero = numero

# Verificar se foram digitados números positivos antes de exibir os resultados
if maior_numero == float('-inf') or menor_numero == float('inf'):
    print("Nenhum número válido foi digitado.")
else:
    # Exibir o maior e o menor número digitado
    print("O maior número digitado foi:", maior_numero)
    print("O menor número digitado foi:", menor_numero)


