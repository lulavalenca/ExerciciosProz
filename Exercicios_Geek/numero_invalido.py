# Recebe um número inteiro como entrada do usuário
numero = input("Digite um número inteiro maior do que zero: ")

# Verifica se a entrada é um número inteiro e maior do que zero
if numero.isdigit() and int(numero) > 0:
    numero = int(numero)
    soma = 0

    # Calcula a soma dos algarismos do número
    while numero > 0:
        digito = numero % 10
        soma += digito
        numero //= 10

    print(f"A soma dos algarismos é {soma}")
else:
    print("Número inválido.")
