# Recebe a primeira nota como entrada do usuário
nota1 = float(input("Digite a primeira nota: "))

# Verifica se a primeira nota é válida
if nota1 < 0.0 or nota1 > 10.0:
    print("Nota inválida. As notas devem estar no intervalo de 0.0 a 10.0.")
else:
    # Recebe a segunda nota como entrada do usuário
    nota2 = float(input("Digite a segunda nota: "))

    # Verifica se a segunda nota é válida
    if nota2 < 0.0 or nota2 > 10.0:
        print("Nota inválida. As notas devem estar no intervalo de 0.0 a 10.0.")
    else:
        # Calcula a média e exibe o resultado
        media = (nota1 + nota2) / 2
        print(f"A média das notas é {media:.2f}")
