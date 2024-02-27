numero = float(input("Digite um numero: "))

if numero >= 0:
    raiz_quadrada = numero ** 0.5
    print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}")
else:
    quadrado = numero ** 2
    print(f"O quadrado de {numero} é {quadrado:.2f}")    