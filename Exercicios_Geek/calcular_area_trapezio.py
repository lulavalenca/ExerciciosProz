# Recebe a base maior como entrada do usuário
base_maior = float(input("Digite o valor da base maior do trapézio: "))

# Recebe a base menor como entrada do usuário
base_menor = float(input("Digite o valor da base menor do trapézio: "))

# Recebe a altura como entrada do usuário
altura = float(input("Digite o valor da altura do trapézio: "))

# Verifica se as bases e a altura são maiores que zero
if base_maior > 0 and base_menor > 0 and altura > 0:
    # Calcula a área do trapézio
    area_trapezio = ((base_maior + base_menor) * altura) / 2
    print(f"A área do trapézio é {area_trapezio:.2f}")
else:
    print("As bases e a altura devem ser números maiores que zero.")
