"""
61) Faça um programa que calcule o maior número palíndromo feito
a partir do produto de dois números de 3 dígitos. Ex: O maior palíndromo feito
a partir do produto de dois números de dois dígitos é 9009 = 91*99

1 Exemplo de codigo
maior_palindromo = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        produto = i * j

        produto_str = str(produto)
        if produto_str == produto_str[::-1] and produto > maior_palindromo:
            maior_palindromo = produto

print("O maior palindromo feito a partir do produto de dois numeros de três digitos é:", maior_palindromo)      


2 Exemplo de codigo

for i in range(999, 100, -1):

    polindromo = ''

    for j in range(i, 100, -1):
        polindromo = str(i * j)

        if polindromo[::1] == polindromo[::-1]:
            break

    if polindromo[::1] == polindromo[::-1]:
        print(f'{polindromo} = {i} * {j}')
        break


3 Exemplo         

def eh_palindromo(num):
    return str(num) == str(num)[::-1]

num_digitos = int(input("Digite o numero de digitos: "))
menor = 10 ** (num_digitos - 1)
maior = 10 ** num_digitos


maior_palindromo = 0
for i in range(menor, maior):
    for j in range(i, maior):
        produto = i * j 
        if eh_palindromo(produto) and produto > maior_palindromo:
            maior_palindromo = produto

print(f"O maior palindromo feito a partir do produto de dois numeros de {num_digitos} digitos é {maior_palindromo}.")

"""

def eh_palindromo(num):
    return str(num) == str(num)[::-1]

maior_palindromo = 0
for i in range(100, 1000):
    for j in range(i, 1000):  # Começa de i para evitar duplicatas
        produto = i * j
        if eh_palindromo(produto) and produto > maior_palindromo:
            maior_palindromo = produto

print(f"O maior palíndromo feito a partir do produto de dois números de 3 dígitos é {maior_palindromo}.")
