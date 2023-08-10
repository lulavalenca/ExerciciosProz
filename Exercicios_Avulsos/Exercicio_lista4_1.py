def inverter_lista(lista):
    lista_invertida = []
    for elemento in reversed(lista):
        lista_invertida.append(elemento)
    return lista_invertida

# Exemplo de lista de números
numeros = [1, 2, 3, 4, 5]

# Chamando a função para inverter a lista
lista_invertida = inverter_lista(numeros)

# Exibindo o resultado
print("Lista original:", numeros)
print("Lista invertida:", lista_invertida)

"""
Neste exemplo, a função inverter_lista cria uma nova lista chamada lista_invertida. 
Ela percorre a lista original usando um loop for, utilizando a função reversed() para percorrer os elementos em ordem inversa. 
Em seguida, a função append() é usada para adicionar cada elemento à nova lista.
Dessa forma, estamos criando uma nova lista com a ordem dos elementos invertida, sem modificar a lista original.
Teste o código com diferentes listas para verificar se ele está invertendo corretamente a ordem dos elementos.



"""