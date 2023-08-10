def gerar_fibonacci(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        proximo_numero = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo_numero)
    return fibonacci

# Quantidade de números da sequência de Fibonacci a gerar
n = 10

# Chamando a função para gerar a lista de Fibonacci
sequencia_fibonacci = gerar_fibonacci(n)

# Exibindo o resultado
print("Primeiros", n, "números da sequência de Fibonacci:")
print(sequencia_fibonacci)

"""
Neste exemplo, a função gerar_fibonacci começa com uma lista contendo os dois primeiros números da sequência (0 e 1). 
Em seguida, ela utiliza um loop while para adicionar os próximos números na sequência, somando os dois últimos números já presentes na lista.
A variável n determina quantos números da sequência de Fibonacci você deseja gerar. 
A lista resultante é exibida no console.
Teste o código com diferentes valores de n para gerar diferentes quantidades de números da sequência de Fibonacci.


"""