"""
29. Escreva um programa para calcular o valor da série, para 5 termos.
S
0+1/2+2/4!+3/6!+.... 

1 Exemplo
s = 0
for i in range(1, 6):
    s += i / (2 * i)
print(s)    



"""

# Função para calcular o valor de E conforme a fórmula fornecida
def calcular_e(n):
    s = 0
    for i in range(1, n + 1):
        s += 1 / (i * 2)
    return s

# Solicitar ao usuário que insira o valor de N
n = int(input("Digite o valor de N: "))

# Calcular o valor de E
resultado = calcular_e(n)

# Exibir o resultado
print("O valor de E é:", resultado)
