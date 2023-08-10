def encontrar_maior_menor(lista):
    if not lista:
        return None, None #retorna none se a lista estiver vazia
    
    maior = menor = lista[0] # Inicializa 'maior' e 'menor' com o primeiro elemento da lista

    for numero in lista:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

    return maior, menor

# Exemplo de lista de números 
numeros = [15, 8, 30, 43, 6, 20]

# Chamando a função para encontrar o maior e o menor valor
maior_valor, menor_valor = encontrar_maior_menor(numeros)

# Exibindo os resultados
print("Maior valor:", maior_valor)
print("Menor valor:", menor_valor)