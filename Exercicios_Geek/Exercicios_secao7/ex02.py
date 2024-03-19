"""
2) Escreva um programa para encontrar o menor número em uma lista.

# Lista de números
lista = [10, 5, 7, 25, 13, 30, 45]

# Inicializa uma variável para armazenar o menor número
menor_numero = None

# Itera sobre cada número na lista
for numero in lista:
    # Se o menor_numero ainda não estiver definido ou o número atual for menor do que o menor_numero
    if menor_numero is None or numero < menor_numero:
        # Atualiza o menor_numero
        menor_numero = numero

# Imprime o menor número encontrado na lista
print("O menor número na lista é:", menor_numero)


1 EXEMPLO DE CODIGO 

lista = [10, 5, 7, 25, 13, 30, 45]

menor_numero = None 

for numero in lista:
    if menor_numero is None or numero < menor_numero:
        menor_numero = numero

print("O menor numero na lista é:", menor_numero)      


2 EXEMPLO DE CODIGO 

lista = [10, 4, 5, 25, 13, 30, 45, 67]

menor_numero = None
indices_do_menor_numero = []

for i, numero in enumerate(lista):
    if menor_numero is None or numero < menor_numero:
        menor_numero = numero
        indices_do_menor_numero = [i]
    elif numero == menor_numero:
        indices_do_menor_numero.append(i)

print("O menor numero na lista é:", menor_numero)
print("Os indices onde o menor numero ocorre na lista são:", indices_do_menor_numero)            



"""

lista = [10, 4, 5, 25, 13, 30, 45, 67]

menor_numero = None
indices_do_menor_numero = []

for i, numero in enumerate(lista):
    if menor_numero is None or numero < menor_numero:
        menor_numero = numero
        indices_do_menor_numero = [i]
    elif numero == menor_numero:
        indices_do_menor_numero.append(i)

print("O menor numero na lista é:", menor_numero)
print("Os indices onde o menor numero ocorre na lista são:", indices_do_menor_numero)            


