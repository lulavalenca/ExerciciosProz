"""
5. Faça um programa que peça ao usuário para digitar 10 valores e some-os.

"""

#Exemplo 1

soma = 0
for i in range(10):
    valor = float(input("Digite um valor: "))
    soma += valor

print("A soma dos valores digitados é: ", soma)