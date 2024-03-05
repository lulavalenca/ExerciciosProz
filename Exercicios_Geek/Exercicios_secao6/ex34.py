"""
34. Faça um programa que calcule o menor número divisível 
por cada um dos números de 1 a 20? Ex: 2520 é o menor número que 
pode ser dividido por cada um dos números de 1 a 10, sem sobrar resto.

1 Exemplo de codigo

# Função para calcular o máximo divisor comum (MDC) de dois números
def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

# Função para calcular o mínimo múltiplo comum (MMC) de dois números
def mmc(a, b):
    return a * b // mdc(a, b)

# Função para calcular o MMC de uma lista de números
def mmc_lista(lista):
    resultado = 1
    for num in lista:
        resultado = mmc(resultado, num)
    return resultado

# Calcula o MMC dos números de 1 a 20
mmc_1_20 = mmc_lista(range(1, 21))

# Exibe o resultado
print("O menor número divisível por todos os números de 1 a 20 é:", mmc_1_20)


2 Exemplo 

# Função para verificar se um número é divisível por todos os números de 1 a 20
def e_divisivel_por_1_a_20(numero):
    for i in range(1, 21):
        if numero % i != 0:
            return False
    return True

# Inicializa um contador
numero = 20

# Encontra o menor número divisível por todos os números de 1 a 20
while True:
    if e_divisivel_por_1_a_20(numero):
        print("O menor número divisível por todos os números de 1 a 20 é:", numero)
        break
    numero += 20  # Incrementa pelo maior número, já que o número precisa ser múltiplo de 20



"""

# Função para calcular o máximo divisor comum (MDC) de dois números
def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

# Função para calcular o mínimo múltiplo comum (MMC) de dois números
def mmc(a, b):
    return a * b // mdc(a, b)

# Função para calcular o MMC de uma lista de números
def mmc_lista(lista):
    resultado = 1
    for num in lista:
        resultado = mmc(resultado, num)
    return resultado

# Calcula o MMC dos números de 1 a 20
mmc_1_20 = mmc_lista(range(1, 21))

# Exibe o resultado
print("O menor número divisível por todos os números de 1 a 20 é:", mmc_1_20)


