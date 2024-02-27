import math

# Coeficientes da equação
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Verifica se a é diferente de zero
if a == 0:
    print("Não é uma equação de segundo grau.")
else:
    # Calcula o discriminante
    delta = b**2 - 4*a*c

    # Verifica o valor do discriminante
    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        raiz_unica = -b / (2*a)
        print(f"Raiz única: {raiz_unica}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Duas raízes reais: {raiz1} e {raiz2}")
