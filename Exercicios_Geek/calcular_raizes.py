# Recebe os coeficientes a, b e c como entrada do usuário
a = float(input("Digite o coeficiente 'a' (deve ser diferente de zero): "))
b = float(input("Digite o coeficiente 'b': "))
c = float(input("Digite o coeficiente 'c': "))

# Calcula o discriminante Delta
delta = b**2 - 4 * a * c

# Verifica se a é diferente de zero
if a == 0:
    print("Não é uma equação de segundo grau.")
else:
    # Verifica o valor do discriminante Delta
    if delta < 0:
        print("Não existe raiz real.")
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f"Raiz única: x = {raiz}")
    else:
        raiz1 = (-b + delta**0.5) / (2 * a)
        raiz2 = (-b - delta**0.5) / (2 * a)
        print(f"As duas raízes reais são: x1 = {raiz1} e x2 = {raiz2}")
