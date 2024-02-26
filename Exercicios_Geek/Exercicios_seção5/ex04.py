numero = float(input("Digite um numero: "))

if numero >= 0:
    quadrado = numero ** 2
    print(f"O numero digitado ao quadrado é {quadrado:.2f}")

    raiz_quadrada = numero ** 0.5
    print(f"A raiz quadrada do número digitado é {raiz_quadrada:.2f}")
else:
    print(f"O numero digitado não é positivo.")    