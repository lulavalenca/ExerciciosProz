"""
9) Crie um programa que lê 6 valores inteiros pares e,
em seguida, mostre na tela os valores lidos na ordem inversa


"""

def ler_valor_par():
    while True:
        valor = int(input("Digite um valor inteiro par: "))
        if valor % 2 == 0:
            return valor
        else:
            print("O valor digitado não é par. Por favor, digite um valor inteiro par.")

valores = []

for i in range(6):
    valor = ler_valor_par()
    valores.append(valor)

print("Valores lidos na ordem inversa:")
for valor in reversed(valores):
    print(valor)    