# Recebe as notas das três provas como entrada do usuário
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

# Calcula a média ponderada
media = (nota1 + nota2 + (nota3 * 2)) / 4

# Verifica se o aluno foi aprovado ou reprovado
if media >= 60:
    print(f"Média: {media:.2f}")
    print("Aluno aprovado!")
else:
    print(f"Média: {media:.2f}")
    print("Aluno reprovado.")
