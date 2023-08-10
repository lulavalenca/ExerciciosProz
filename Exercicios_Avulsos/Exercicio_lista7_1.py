def gerar_fibonacci(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

# Quantidade de números da sequência de Fibonacci a gerar
n = 12

# Chamando a função e exibindo o resultado
print("Primeiro", n, "números de sequência de Fibonacci:", gerar_fibonacci(n))