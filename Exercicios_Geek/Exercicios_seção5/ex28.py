"""
Faça um programa que leia três números inteiros positivos e efetue
o cálculo de uma das seguintes médias de acordo com um valor numérico
digitado pelo usuário:
    (a) Geométrica: ³√x * y * z
    (b) Ponderada: (x + 2 * y + 3 * z) / 6
    (c) Harmônica: 1 / ((1 / x) + (1 / y) + (1 / z))
    (d) Aritmética: (x + y + z) / 3


"""
# Função para calcular a média geométrica
def media_geometrica(x, y, z):
    return (x * y * z) ** (1 / 3)

#Função para calcular a média ponderada
def media_ponderada(x, y, z):
    return (x + 2 * y + 3 * z) / 6

# Função para calcular a média harmônica
def media_harmonica(x, y, z):
    return 1 / ((1 / x) + (1 / y) + (1 / z))

# Função para calcular a média aritmética
def media_aritmetica(x, y, z):
    return (x + y + z) / 3

x = int(input("Digite o primeiro numero inteiro positivo: "))
y = int(input("Digite o segungo numero inteiro positivo: "))
z = int(input("Digite o terceiro numero inteiro positivo:"))

# Escolha do tipo de média
opcao = input("Escolha o tipo de média (a - Geométrica, b - Ponderada, c - Harmônica, d - Aritmética): ")

# Calcula a média de acordo com a opção escolhida
if opcao == 'a':
    resultado = media_geometrica(x, y, z)
elif opcao == 'b':
    resultado = media_ponderada(x, y, z)
elif opcao == 'c':
    resultado = media_harmonica(x, y, z)
elif opcao == 'd':
    resultado = media_aritmetica(x, y, z)
else:
    print("Opção inválida!")
    resultado = None

# Exibe o resultado se não for nulo
if resultado is not None:
    print(f"O resultado da média é: {resultado:.2f}")