"""
17) Escreva um programa para verificar se uma lista é palíndromo.

"""

def eh_palindromo(lista):
    return lista == lista[::-1]

lista = [1, 2, 3, 2, 1]

if eh_palindromo(lista):
    print("A lista é um palindromo.")
else:
    print("A lista não é um palindromo.")