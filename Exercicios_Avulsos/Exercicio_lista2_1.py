def encontrar_maior_menor_par_impar(lista):
    if not lista:
        return None, None, None, None  # Retorna None se a lista estiver vazia

    maior = menor = lista[0]  # Inicializa 'maior' e 'menor' com o primeiro elemento da lista
    par = impar = 0  # Inicializa contadores para números pares e ímpares

    for numero in lista:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
        
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1

    return maior, menor, par, impar

# Exemplo de lista de números
numeros = [15, 8, 30, 42, 5, 20]

# Chamando a função para encontrar o maior, o menor valor, números pares e ímpares
maior_valor, menor_valor, total_pares, total_impares = encontrar_maior_menor_par_impar(numeros)

# Exibindo os resultados
print("Maior valor:", maior_valor)
print("Menor valor:", menor_valor)
print("Total de números pares:", total_pares)
print("Total de números ímpares:", total_impares)
