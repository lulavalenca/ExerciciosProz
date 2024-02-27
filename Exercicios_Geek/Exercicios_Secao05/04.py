numero = int(input("Digite um numero: "))

if numero >= 0:
    quadrado = numero ** 2
    print(f"O numero digitado ao quadrado: {quadrado}")

    raiz_quadrada = numero ** 0.05
    print(f"A raiz quadrada do numero digitado é : {raiz_quadrada:.2f}")
else:
    print("Por favor, digite um número positivo.")
