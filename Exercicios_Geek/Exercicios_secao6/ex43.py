"""
43. Faça um programa que leia um número indeterminado de idades de indivíduos (pare
quando for informada a idade 0), e calcule a idade média desse grupo.

1 - Exemplo de Codigo

idades = []
while True:
    idade = int(input("Digite a idade (0 para sair): "))
    if idade == 0:
        break
    idades.append(idade)

if idades:
    media = sum(idades) / len(idades)
    print(f"A idade média do grupo é {media}")
else:
    print("Nenhuma idade foi inserida.")    


2 Exemplo de Codigo

# Inicializar variáveis
soma_idades = 0
quantidade_individuos = 0

# Loop para ler as idades e calcular a soma
while True:
    idade = int(input("Digite a idade (digite 0 para encerrar): "))
    if idade == 0:
        break
    soma_idades += idade
    quantidade_individuos += 1

# Verificar se foram fornecidas idades
if quantidade_individuos == 0:
    print("Nenhuma idade foi fornecida.")
else:
    # Calcular a média das idades
    media_idades = soma_idades / quantidade_individuos
    print("A média das idades é:", media_idades)



"""

# Inicializar variáveis
soma_idades = 0
quantidade_individuos = 0

# Loop para ler as idades e calcular a soma
while True:
    idade = int(input("Digite a idade (digite 0 para encerrar): "))
    if idade == 0:
        break
    soma_idades += idade
    quantidade_individuos += 1

# Verificar se foram fornecidas idades
if quantidade_individuos == 0:
    print("Nenhuma idade foi fornecida.")
else:
    # Calcular a média das idades
    media_idades = soma_idades / quantidade_individuos
    print("A média das idades é:", media_idades)
