"""
53) Escreva um programa que leia um número inteiro positivo n e em
seguida imprima n linhas do chamado Triangulo de Floyd. Para n = 6, temos:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 10 21

"""


"""
1 Exemplo 

def triangulo_floyd(n):
    numero = 1
    linha = 1
    while linha <= n:
        coluna = 1
        while coluna <= linha:
            print(numero, end=" ")
            numero += 1
            coluna += 1
        print()
        linha += 1

n = int(input("Digite um número inteiro positivo: "))
triangulo_floyd(n)



"""

def triangulo_floyd(n):
    numero = 1
    for i in range(1, n+1):
        for j in range(i):
            print(numero, end=" ")
            numero += 1
        print()

n = int(input("Digite um número inteiro positivo: "))
triangulo_floyd(n)
