numero = int(input("Digite um numero com três algarismo ou mais: "))

if numero <= 0:
    print("Número invalido.")
else:
    soma = 0 

    while numero > 0:
        digito = numero % 10
        soma += digito

        numero //=10
    print("A soma dos algarismos é: ", soma)    