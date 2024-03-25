"""
13. Fazer um programa para ler 5 valores e, 
em seguida, mostrar a posição onde se encontram o maior e o menor valor.

"""

def encontrar_posicoes_maior_menor(valores):
    maior_valor = max(valores)
    menor_valor = min(valores)
    posicao_maior = valores.index(maior_valor)
    posicao_menor = valores.index(menor_valor)
    return posicao_maior, posicao_menor

valores = []
for i in range(5):
    valor = float(input("Digite o {}º valor: ".format(i + 1)))
    valores.append(valor)

posicao_maior, posicao_menor = encontrar_posicoes_maior_menor(valores)

print("Posicao do maior valor: ", posicao_maior + 1)
print("Posicao do menor valor: ", posicao_menor + 1)


# 2 Exemplo de codigo

valores = [float(input(f"Digite o valor {i + 1}: ") for i in range(5))]

posicao_maior = valores.index(max(valores))
posicao_menor = valores.index(min(valores))

print(f"A posição do maior valor é: {posicao_maior + 1}")
print(f"A posição do menor valor é: {posicao_menor + 1}")