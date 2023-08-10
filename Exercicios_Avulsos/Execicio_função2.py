def encontrar_maior_valor(lista):
    if not lista:
        raise ValueError("A lista esta vazia.")
    
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero

    return maior

# Exemplo de Uso:
numeros = [23, 45, 12, 67, 90, 32]
maior_valor = encontrar_maior_valor(numeros)
print(f"O maior valor da lista é: {maior_valor}")        