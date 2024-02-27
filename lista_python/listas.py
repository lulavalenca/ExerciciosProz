"""
Listas 

listas em pyt

type([])

lista = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['L', 'u', 'i','z', ' ', 'G','o','n','z','a','g','a']

lista3 = []

lista4 = list(range(11))

lista5 = list('Luiz Gonzaga')

################################################################
# Podemos remover facilmente o último elemento de uma lista
# OBS: O pop não somente remove o último elemento de uma lista mas também o retorna 
print(lista5)

# Podemos remover um elemneto pelo indice
# OBS: Os elementos á direita deste indice serão deslocados para a esquerda.
lista5.pop(2)
print(lista5)

# Podemos remover um elemento pelo indice
# OBS: Os elementos á direita deste indice serão deslocados para a esquerda.
# OBS: Se não houver elemento no indice informado, teremos o erro IndexError.

lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3,] 
nova = nova * 3
print(nova)

# Podemos facilment converter uma string para uma lista

# Exemplo 1

curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# Obs: Por padrão, o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Podemos facilment converter uma string para uma lista

# Exemplo 1

curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# Obs: Por padrão, o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 453453543]
print(lista6)
print(type(lista6))

# Iterando sobre lista

# Exemplo1.1 - Utilizando for 

soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)    


# Exemplo 1 - Utilizando for

soma = ''
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)    

# Exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print ("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print (produto)        


# Utilizando variaveis em listas
numeros = [1,2,3,4,5,6,7,8]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)
    
# Fazemos acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

print(cores)

# Fazer acesso aos elementos de forma inversa

print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])

cores = ['verdes', 'amarelo', 'azul', 'branco', 'vermelho']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice]) 
    indice = indice + 1 

for indice, cor in enumerate(cores):
    print (indice, cor)

# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(45)
lista.append(45)

print(lista)    

# Outros métodos não tão importantes mas também úteis

# Encontrar o indice de um elemento na lista

numeros = [5, 6, 7, 8, 9, 10, 11, 12, 13]

# Em qual indicie da lista está o valor 6?
print(numeros.index(6))

# Em qual indicie da lista está o valor 12?
print(numeros.index(12))

# print(numeros.index(19)) # Gera ValueError

# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError

# OBS: Retorna o indice do primeiro elemento encontrado
print(numeros.index(7, 1))

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(7, 2)) # buscando a partir do indice 1 
print(numeros.index(8, 2)) # buscando a partir2 do indice
print(numeros.index(9, 2)) # buscando a partir do indice 3
#print(numeros.index(
# OBS: Caso não tenha este elemento na lista, será apresentao erro ValueError 

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6))

#Revisão de slicing

#lista[inicio:fim:passo]
#range[inicio:fim:passo]

#Trabalhando com slice de lista com o parâmetro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:]) # Iniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parâmetro 'fim"

print(lista[:2]) # começa em 0. pega até o indice 2 - 1

print(lista[:4]) # começa em 0. pega até o indice 4 - 1

print(lista[1:3]) # começa em 1. pega até o indice 3 - 1

# Trabalhando com slice de lista com parâmetro 'passo'

print(lista[1::2]) # começa em 1. vai até o final, de 2 em 2

print(lista[::2]) # começa em 0. vai até o final, de 2 em 2

# Invertendo valores em uma lista

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes = ['Geek', 'University']

nomes.reverse()
print(nomes)

# Soma*, Valor Maximo*, Valor Minimo*, Tamanho

# Se os valores forem todos inteiros ou reias.

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) # soma
print(max(lista)) # maximo valor 
print(min(lista)) # minimo valor
print(len(lista)) # tamanho da lista  

# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de lista 

lista = [1, 2, 3,]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# Copienado uma lista para outra (Shallow copy e Deep copy)

# Forma 1 Deep copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao ultilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas
# ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra. Isso em Python
# é chamado de Deep Copy (cópia profunda)

# Forma 2 - Shallow copy

lista = [1, 2, 3]
print(lista)

nova = lista # cópia 

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a copia via atribuição e copiamos os dados da lista para a nova lista, mas
# após realizar modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# isso em Python é chamado de Shallow Copy.

# OBS: Se tivermos um numero diferente de elementos na lista ou variáveis para receber os dados, teremos ValueError

# Podemos remover facilmente o ultimo elemento de uma lista 
# OBS: o pop não somente remove o ultimo elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo indice
# OBS: Os elementos á direita deste incide serão deslocados para a esquerda.
# OBS: Se não houver elemento no indice informado, teremos o erro IndexError.
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos e (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista exemplo repetido
nova = [1,2,3]
print(nova)
nova = nova * 3
print(nova)

# Convertendo uma lista em uma string

lista6 = ['Programação', 'em', 'Python:','Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ''.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista6, coloca cifrão entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)


"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['L', 'u', 'i','z', ' ', 'G','o','n','z','a','g','a']

lista3 = []

lista4 = list(range(11))

lista5 = list('Luiz Gonzaga')

##########################################################################################################

