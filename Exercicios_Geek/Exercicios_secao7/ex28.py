"""
28) Escreva um programa para criar uma lista de strings a partir de uma string, 
onde cada elemento da lista é uma letra da string original.

"""

def lista_de_letras(string):
    return [letra for letra in string]

string_original = "Luiz Gonzaga"

lista_letras = lista_de_letras(string_original)

print("Lista de letras: ", lista_letras)