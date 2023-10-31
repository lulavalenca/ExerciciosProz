"""
# loop For

loop -> estrutura de repetição.
for -> uma dessas estruturas

C ou Java

for(int i = 0; i < 10; i++){
    //execução do loop
}

Python

for item in interavel:
    //execução do loop


Ultilizamos loops para iterar sobre sequencias ouu sobre valores iteraveis 

Exemplos de iteraveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 2, 3, 4, 5]
- Range
    numeros = range(1, 10)    

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

OBS: quando nçao precisamos de um valor, podemos descarta-lo utilizando um underline (_) 

nome = 'Luiz Valença'
lista = [1, 2, 4, 12, 22, 33]
numeros = range(1, 10) # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0    

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')    
"""
nome = 'Luiz Valença'
lista = [1, 2, 4, 12, 22, 33]
numeros = range(1, 10) # temos que transformar em uma lista 
# Exemplo de for
for letra in nome:
    print(letra)

#Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)    

#Exemplo fde for 3 (Iterando sobre um range)
for numero in range(1, 10):
    print(numero)

nome = 'Luiz Valença'
for letra in nome:
    print(letra, end='' )
