"""
27 -Em Matemática, o número harmônico designado por H (n) define-se como sendo a soma da série harmónica:
H(n)=1+1/2+1/3+ 1/4 + ... + 1/n
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).

def numero_harmonico(n):
    soma = 0
    for i in range(1, n + 1):
        soma += 1 / i
    return soma

# Solicitar ao usuário que insira o valor de n
n = int(input("Digite um número inteiro e positivo (n): "))

# Calcular e exibir o valor de H(n)
resultado = numero_harmonico(n)
print(f"O valor de H({n}) é:", resultado)


"""

def numero_harmonico(n):
    soma = 0
    for i in range(1, n + 1):
        soma += 1 / i
    return soma

# Solicitar ao usuário que insira o valor de n
n = int(input("Digite um número inteiro e positivo (n): "))

# Calcular e exibir o valor de H(n)
resultado = numero_harmonico(n)
print(f"O valor de H({n}) é:", resultado)


