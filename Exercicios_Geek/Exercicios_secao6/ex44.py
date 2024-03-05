"""
44. Leia um número positivo do usuário, então, calcule e imprima a sequência Fibonacci até
o primeiro número superior ao número lido. Exemplo: se o usuário informou o número 30, 
a sequência a ser impressa será 0 11235 8 13 21 34.

1 Exemplo de codigo

# Função para calcular a sequência Fibonacci até o primeiro número superior ao número dado
def fibonacci_ate_n(numero):
    fibonacci = [0, 1]  # Inicializa a lista com os dois primeiros números da sequência
    while True:
        # Calcula o próximo número da sequência e adiciona à lista
        proximo = fibonacci[-1] + fibonacci[-2]
        if proximo > numero:
            break
        fibonacci.append(proximo)
    return fibonacci

# Função para imprimir a sequência Fibonacci formatada
def imprimir_sequencia_fibonacci(lista):
    print("Sequência Fibonacci até o primeiro número superior ao número dado:")
    for num in lista:
        print(num, end=" ")

# Solicita ao usuário um número positivo
numero = int(input("Digite um número positivo: "))

# Verifica se o número é positivo
if numero <= 0:
    print("Por favor, digite um número positivo.")
else:
    # Calcula e imprime a sequência Fibonacci até o primeiro número superior ao número dado
    sequencia = fibonacci_ate_n(numero)
    imprimir_sequencia_fibonacci(sequencia)




"""

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b
    print()

num = int(input("Digite um número positivo: "))
if num > 0:
    print("A sequência Fibonacci até o primeiro número superior a", num, "é:")
    fibonacci(num)
else:
    print("Por favor, insira um número positivo.")

