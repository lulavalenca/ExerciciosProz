"""
2 - exercicio


"""

numero = float(input("Digite um numero: "))

if numero >= 0:
    raiz_quadrada = numero ** 2 
    print(f"A raiz quadrada do numero {numero} é {raiz_quadrada:.2f}")
else:
    print("O numero é invalido porque é negativo.")    