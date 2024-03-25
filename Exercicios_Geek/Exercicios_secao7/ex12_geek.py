"""
12) Fazer um programa para ler 5 valores e, 
em seguida, mostrar todos os valores lidos juntamente com o maior, 
o menor e a média dos valores.

1 Exemplo de codigo
maior_numero = 0
menor_numero = 0
media = 0 

for i in range(5):
    numero = float(input("Digite um numero: "))
    if maior_numero is 0 or numero > maior_numero:
        maior_numero = numero
    if menor_numero is 0 or menor_numero < menor_numero:
        menor_numero = numero
    media += numero

print("Maior numero:", maior_numero)
print("Menor numero:", menor_numero)
print("Media:", media / 5)

"""

maior_numero = 0
menor_numero = 0
media = 0 

for i in range(5):
    numero = float(input("Digite um numero: "))
    if maior_numero is 0 or numero > maior_numero:
        maior_numero = numero
    if menor_numero is 0 or menor_numero < menor_numero:
        menor_numero = numero
    media += numero

print("Maior numero:", maior_numero)
print("Menor numero:", menor_numero)
print("Media:", media / 5)

# codigo 2 

# Função para ler os valores e calcular o maior, o menor e a média
def calcular_estatisticas(valores):
    maior = max(valores)
    menor = min(valores)
    media = sum(valores) / len(valores)
    return maior, menor, media

# Função para formatar a exibição das estatísticas
def exibir_estatisticas(valores, maior, menor, media):
    print("Valores lidos:", valores)
    print("Maior valor:", maior)
    print("Menor valor:", menor)
    print("Média dos valores:", media)

# Lê os valores do usuário
valores = []
for i in range(5):
    valor = float(input("Digite o {}º valor: ".format(i + 1)))
    valores.append(valor)

# Calcula as estatísticas
maior, menor, media = calcular_estatisticas(valores)

# Exibe as estatísticas
exibir_estatisticas(valores, maior, menor, media)
