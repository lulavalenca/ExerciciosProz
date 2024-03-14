"""
01) - Escreva um programa para encontrar o maior número em uma lista.

1 Exemplo do codigo

lista = [10, 5, 7, 25, 13, 30]

maior_numero = None

for numero in lista:
    if maior_numero is None or numero > maior_numero:
        maior_numero = numero

tamanho_lista = len(lista)

print("O maior numero na lista é:", maior_numero)
print("O tamanho da lista é:", tamanho_lista)     


2 Exemplo do codigo

lista = [10, 5, 7, 25, 13, 30, 45 , 46]

maior_numero = None

for numero in lista:
    if maior_numero is None or numero > maior_numero:
        maior_numero = numero

tamanho_lista = len(lista)

print("O maior numero na lista é:", maior_numero)
print("O tamanho da lista é:", tamanho_lista)

3 - Exemplo codigo 

lista = [10, 5, 7, 25, 13, 30, 45]

maior_numero = None
for numero in lista:
    if maior_numero is None or numero > maior_numero:
        maior_numero = numero

menor_numero = None
for numero in lista:
    if menor_numero is None or numero < menor_numero:
        menor_numero = numero      

lista_ordenada = sorted(lista)

soma_elementos = sum(lista)

media_elementos = soma_elementos / len(lista)

numero_procurado = 7 
esta_na_lista = numero_procurado in lista

ocorrencias_de_7 = lista.count(7)

elemento_removido = lista.pop(2)

outra_lista = [1, 2, 3]
lista_concatenada = lista + outra_lista

lista.reverse()

indice_de_25 = lista.index(25)

print("O maior número na lista é:", maior_numero)
print("O menor número na lista é:", menor_numero)
print("A lista ordenada é:", lista_ordenada)
print("A soma dos elementos é:", soma_elementos)
print("A média dos elementos é:", media_elementos)
print("O número 7 está na lista?", esta_na_lista)
print("O número 7 aparece", ocorrencias_de_7, "vezes na lista")
print("O elemento removido foi:", elemento_removido)
print("A lista concatenada é:", lista_concatenada)
print("A lista com ordem invertida é:", lista)
print("O índice do número 25 na lista é:", indice_de_25)


"""

lista = [10, 5, 7, 25, 13, 30, 45]

maior_numero = None
for numero in lista:
    if maior_numero is None or numero > maior_numero:
        maior_numero = numero

menor_numero = None
for numero in lista:
    if menor_numero is None or numero < menor_numero:
        menor_numero = numero      

lista_ordenada = sorted(lista)

soma_elementos = sum(lista)

media_elementos = soma_elementos / len(lista)

numero_procurado = 7 
esta_na_lista = numero_procurado in lista

ocorrencias_de_7 = lista.count(7)

elemento_removido = lista.pop(2)

outra_lista = [1, 2, 3]
lista_concatenada = lista + outra_lista

lista.reverse()

indice_de_25 = lista.index(25)

print("O maior número na lista é:", maior_numero)
print("O menor número na lista é:", menor_numero)
print("A lista ordenada é:", lista_ordenada)
print("A soma dos elementos é:", soma_elementos)
print("A média dos elementos é:", media_elementos)
print("O número 7 está na lista?", esta_na_lista)
print("O número 7 aparece", ocorrencias_de_7, "vezes na lista")
print("O elemento removido foi:", elemento_removido)
print("A lista concatenada é:", lista_concatenada)
print("A lista com ordem invertida é:", lista)
print("O índice do número 25 na lista é:", indice_de_25)
