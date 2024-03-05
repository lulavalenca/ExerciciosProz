"""
36. Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 números naturais e o quadrado da soma. Ex: A soma dos quadrados dos dez pri- meiros números naturais é,
12+22+...+102 = 385
O quadrado da soma dos dez primeiros números naturais é,
(1+2+...+10)2
552=3025
A diferença entre a soma dos quadrados dos dez primeiros números naturais e o quadrado da soma é 3025-385 = 2640.


1 Exemplo 

# Função para calcular a soma dos quadrados dos primeiros n números naturais
def soma_quadrados(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i ** 2
    return soma

# Função para calcular o quadrado da soma dos primeiros n números naturais
def quadrado_soma(n):
    soma = sum(range(1, n + 1))
    return soma ** 2

# Definir o número de termos
n = 100

# Calcular a diferença
diferenca = quadrado_soma(n) - soma_quadrados(n)

# Exibir o resultado
print("A diferença entre a soma dos quadrados e o quadrado da soma dos primeiros", n, "números naturais é:", diferenca)


2 Exemplo 





"""

soma_quadrados = 0
soma_numeros = 0

for i in range(1, 101):
    soma_quadrados += i ** 2

for i in range(1, 101):
    soma_numeros += i

quadrado_soma = soma_numeros ** 2 

diferenca = quadrado_soma - soma_quadrados

print()
print("A diferença entre a soma dos quadrados e o quadrado da soma dos primeiros 100 números naturais é:", diferenca)