"""
4. Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o de 1000
em 1000, imprimindo seu valor na tela, até que seu valor seja 100000 (cem mil).

"""

# while feito este codigo

numero = 0

while numero <= 100000:
    print(numero)
    numero += 1000

# feito em For

for numero in range(0, 100001, 1000):
    print( )
    print(numero)    