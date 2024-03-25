"""
8) Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre
na tela os valores lidos na ordem inversa


"""

def ler_valores_pares():
    valores_pares = []
    for i in range(6):
        valor = int(input(f"Digite p {i+1}º valor inteiro par: "))
        while valor % 2 != 0:
            print("O valor digitado não é par. Por favor digite um valor inteiro par.")
            valor = int(input(f"Digite o {i+1}º valor inteiro par: "))
        valores_pares.append(valor)
    return valores_pares

def mostrar_ordem_inversa(valores):
    print("Valores lidos na ordem inversa:")
    for valor in reversed(valores):
        print(valor)

valores_pares = ler_valores_pares()

mostrar_ordem_inversa(valores_pares)