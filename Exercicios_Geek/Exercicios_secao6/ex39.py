"""
39) Faça um programa que calcule a área de um triângulo, cuja base e altura
são fornecida pelo usuário. Esse programa não pode permitir a entrada de dados inválidos,
ou seja, medidas menores ou iguais a 0.

def calcular_area_triangulo(base, altura):
    
    if base > 0 and altura > 0:

        area = (base * altura) / 2
        return area
    else:
        return None
    
base = float(input("Digite a medida da base do triângulo: "))
altura = float(input(("Digite a medida da altura do triângulo: "))) 

area = calcular_area_triangulo(base, altura)

if area is not None:
    print("A area do triangulo é:", area)
else:
    print("A medidas fornecidas são invalidas. Certifique-se de que a base e a altura sejam valores positivos.")


"""

     

def calcular_area_triangulo(base, altura):
    
    if base > 0 and altura > 0:

        area = (base * altura) / 2
        return area
    else:
        return None
    
base = float(input("Digite a medida da base do triângulo: "))
altura = float(input(("Digite a medida da altura do triângulo: "))) 

area = calcular_area_triangulo(base, altura)

if area is not None:
    print("A area do triangulo é:", area)
else:
    print("A medidas fornecidas são invalidas. Certifique-se de que a base e a altura sejam valores positivos.")     

