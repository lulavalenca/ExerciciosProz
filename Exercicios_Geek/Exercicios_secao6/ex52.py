"""
52) Escreva um programa que receba como entrada o valor do saque
realizado pelo cliente de um banco e retorne quantas notas de cada valor
serão necessárias para atender ao saque com a menor quantidade de notas possível.
Serão utilizadas notas de 100, 50, 20, 10, 5, 2, 1 real.


1 Exemplo de codigo

# Valor do saque
saque = int(input("Digite o valor do saque: "))

# Notas disponíveis
notas = [100, 50, 20, 10, 5, 2, 1]

# Inicializa o índice das notas
i = 0

# Enquanto ainda houver valor a ser sacado
while saque > 0:
    # Se a nota atual pode ser usada
    if saque >= notas[i]:
        # Calcula a quantidade de notas
        qtd_notas = saque // notas[i]
        # Atualiza o valor a ser sacado
        saque -= qtd_notas * notas[i]
        print(f"Notas de R${notas[i]}: {qtd_notas}")
    # Passa para a próxima nota
    i += 1




"""

def calcular_notas(saque):
    notas = [100, 50, 20, 10, 5, 2, 1]
    quantidade_notas = []

    for nota in notas:
        quantidade, saque = divmod(saque, nota)
        quantidade_notas.append(quantidade)

    return quantidade_notas    

saque = int(input("Digite o valor do saque: "))
quantidade_notas = calcular_notas(saque)

print("Quantidade de notas necessarias para o saque:")
print(f"Notas de R$100: {quantidade_notas[0]}")
print(f"Notas de R$50: {quantidade_notas[1]}")
print(f"Notas de R$20: {quantidade_notas[2]}")
print(f"Notas de R$10: {quantidade_notas[3]}")
print(f"Notas de R$5: {quantidade_notas[4]}")
print(f"Notas de R$2: {quantidade_notas[5]}")
print(f"Notas de R$1: {quantidade_notas[6]}")