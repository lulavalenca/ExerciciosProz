"""
3) - Escreva um programa para calcular a soma de todos os elementos em uma lista.

lista = [10, 5, 7, 25, 33, 35, 40, 45]

soma = 0

for numero in lista:
    soma += numero

print("A soma de todos os elementos da lista é:", soma)

2 - EXEMPLO DE CODIGO
lista = [10, 5, 7, 25, 33, 35, 40, 45]

soma = 0

for numero in lista:
    soma += numero

media = soma / len(lista)    

print("A soma de todos os elementos da lista é:", soma)
print("A média de todos os elementos da lista é:", media)

"""

def calcular_media(lista):
    if not lista:
        return 0 
    return sum(lista) / len(lista)

def encontrar_maiores_que_media(lista):
    media = calcular_media(lista)
    return [numero for numero in lista if numero > media]

def obter_lista_do_usuario():
    entrada = input("Digite os numeros da lista separados por virgula: ")
    numeros_texto = entrada.split(',')
    lista = [ ]
    for texto_numero in numeros_texto:
        try:
            numero = int(texto_numero)
            lista.append(numero)
        except ValueError:
            print("Erro: O valor", texto_numero, "não é um numero inteiro válido.")
        return lista

def verificar_lista_vazia(lista):
    if not lista:
        print("A lista está vazia.")
        return True
    return False 

def calcular_soma(lista):
    return sum(lista)


def verificar_tipo_de_dados(lista):
    for elemento in lista:
        if not isinstance(elemento, (int, float)):
            print("Erro: A lista contém elementos que não são numeros.")
            return False
        return True
    
lista = obter_lista_do_usuario()

if verificar_lista_vazia(lista):
    exit()

if not verificar_tipo_de_dados(lista):
    exit()

soma = calcular_soma(lista)

media = calcular_media(lista)

maiores_que_media = encontrar_maiores_que_media(lista)

print("A lista é:", lista)
print("A soma de todos os elementos da lista é:", soma)
print("A média de todos os elementos da lista é:", media)
print("Os elementos maiores do que a média são:", maiores_que_media)