"""
22) Escreva um programa para criar uma lista de todos os números primos até um determinado número.

"""

def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos_ate(maximo):
    primos = []
    for numero in range(2, maximo + 1):
        if eh_primo(numero):
            primos.append(numero)
    return primos

maximo = 50

primos = numeros_primos_ate(maximo)

print("Numeros primos até", maximo, "são", primos)