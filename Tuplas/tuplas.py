"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças basicas:

1 - As tuplas são representadas por parênteses () 

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda 
operação em uma tupla para uma nova tupla.

# Cuidado 1: As tuplas são representadas por () parênteses, mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type((tupla1)))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type((tupla2)))

# Cuidado 2: Tuplas com 1 elemento

tupla3 = (4) # Isso não é uma tupla
print(tupla3)

print(type(tupla3))

tupla4 = (4,) # Isso é uma tupla
print(tupla4)

print(type(tupla4))

tupla5 = 4,
print(tupla5)

print(type(tupla5))

# CONCLUSÃO: podemos concluir que tuplas são definidas pela virgula e não pelo uso do parênteses 

(4) -> não é tupla
(4,) -> é tupla
4, -> é tupla

# Podemos gerar uma tupla dinamicamente com range(inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla 

tupla = ('Luiz Gonzaga', 'Programação em pythone')

escola, curso = tupla
print(escola)
print(curso)

# Obs: Gera erro (ValueError) se colocarmos um numero diferente de elementos para desenpacotar.

# Métodos para adição e remoção de elmentos nas tuplas são existem, dado o fato das tuplas serem imutáveis.

# Soma*, valor Maximo*, valor Minimo* e Tamanho

# Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6, 7, 8)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas 

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) # Tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)

tupla4 = tupla3 + tupla1 + tupla2
print(tupla4)
print(sum(tupla4))
print(len(tupla4))

# verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)

print(3 in tupla)

# Iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)    

    
    
# Contando elemento dentro de uma tupla

tupla = ('a', 'b', 'c', 'a', 'b', 'c')

print(tupla.count('c'))

# O acesso a elementos de uma tupla também é semelhante a de uma lista 

print(meses[5])

# Iterar com while 
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual indice um elemento está na tupla 

print(meses.index('Junho')) 

# OBS: Caso o elemento não exista. será gerado erro.
    
# Dicas na utilização de tuplas 

# Devemos utilizar tuplas Sempre que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1 

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho ', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# Slicing

# tupla[inicio:fim:passo]

print(meses[5:9])

# Por quê utilizar tuplas?

# - Tuplas são mais rapidas do que listas.
# - Tuplas deixam seu codigo mais seguro.

# - Porque trabalhar com elementos imutáveis traz segurança para o Código.


       
"""

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)

