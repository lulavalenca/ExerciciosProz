numero = float(input("Digite um numero: "))

if numero >= 0:
    
    raiz_quadrada = numero ** 0.5
    print(f"A rais quadrada de {numero} é {raiz_quadrada:.2f}")
else:
    print("Numero inválido. Por favor, insira um número positivo.")   