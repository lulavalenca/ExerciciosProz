def remover_duplicatas(lista):
    return list(set(lista))

# Exemplo de lista com elementos duplicados
numeros = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]

# Chamando a função para remover duplicatas
lista_sem_duplicatas = remover_duplicatas(numeros)

# Exibindo o resultado
print("Lista original:", numeros)
print("Lista sem duplicatas", lista_sem_duplicatas)

"""
Nesta versão, a função remover_duplicatas utiliza um conjunto (set) para armazenar os elementos únicos da lista. 
Um conjunto não permite elementos duplicados, o que simplifica a remoção de duplicatas. 
Em seguida, a função converte o conjunto de volta para uma lista utilizando a função list().
Isso resulta em um código mais conciso e eficiente para a remoção de duplicatas.

Teste o código com diferentes listas para verificar se ele está removendo corretamente as duplicatas.


"""