def remover_duplicatas(lista):
    lista_sem_duplicatas = []
    for elemento in lista:
        if elemento not in lista_sem_duplicatas:
            lista_sem_duplicatas.append(elemento)
    return lista_sem_duplicatas

# Exemplo de lista com elementos duplicados
numeros = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]

# Chamando a função para remover duplicatas 
lista_sem_duplicatas = remover_duplicatas(numeros)

#Exibindo o resultado
print("Lista original:", numeros)
print("Lista sem duplicatas:", lista_sem_duplicatas)