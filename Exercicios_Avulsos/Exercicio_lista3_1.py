def contar_elemento(lista, elemento):
    return lista.count(elemento)

#Exemplo de lista de números
numeros = [1, 2, 3, 2, 4, 2, 5, 2]
# Elemento específico que queremos contar

elemento_procurado = 2

# Chamando a função para contar a ocorrência do elemento 
ocorrencias = contar_elemento(numeros, elemento_procurado)


# Exibindo o resultado
print(f"O elemento {elemento_procurado} aparece {ocorrencias} vezes na lista.")