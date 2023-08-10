def contar_elemento(lista, elemento):
    contador = 0
    for item in lista:
        if item == elemento:
            contador += 1
    return contador        

# Exemplos de lista de numeros
numeros = [1, 2, 3, 4, 2, 5, 2]

# Elemento especifico que queremos contar
elemento_procurado = 2

# Chamando a função para contar a ocorrência do elemento
ocorrencias = contar_elemento(numeros, elemento_procurado)

# Exibindo o resultado
print(f"O elemento {elemento_procurado} aparece {ocorrencias} vezes na lista")