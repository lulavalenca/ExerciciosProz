"""
28. Faça um programa que leia um valor N inteiro e positivo, calcule o mostre o valor E, conforme a fórmula a seguir
E=1+1/1!+1/2+1/3+...+1/N!




"""

def calcular_fatorial(numero):
    fatoria = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial    

def calcular_e(n):
    e = 1
    for i in range(1, n + 1):
        e += 1 / calcular_fatorial(i)
    return e    