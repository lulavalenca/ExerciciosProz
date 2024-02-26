nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Verifica se as notas são válidas
if 0.0 <= nota1 <= 10.0 and 0.0 <= nota2 <= 10.0:
    # Calcula a média das notas
    media = (nota1 + nota2) / 2
    print(f"A média das notas é {media:.2f}")
else:
    print("Notas inválidas. As notas devem estar entre 0.0 e 10.0.")
