"""
48. Faça um programa que some os termos de valor par da sequência de Fibonacci, cujos
valores não ultrapassem quatro milhões.



"""

def soma_fibonacci_par(limite):
    a, b = 0, 1
    soma = 0
    while a <= limite:
        if a % 2 == 0:
            soma += a
        a, b = b, a + b
    return soma

limite = 4000000
soma = soma_fibonacci_par(limite)
print(f"A soma dos termos de valor par da sequência de Fibonacci que não ultrapassam {limite} é {soma}")
