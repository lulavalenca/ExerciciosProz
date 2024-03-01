"""
# Lê as três notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média ponderada
media_ponderada = ((nota1 + nota2 + nota3 * 2) / 5) * 10

# Verifica se a média é maior que 60
if media_ponderada >= 60:
    print(f"Aluno aprovado com média {media_ponderada:.2f}.")
else:
    print(f"Aluno reprovado com média {media_ponderada:.2f}.")


"""


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

mediaponderada = ((nota1 + nota2 + nota3 * 2)/ 5) * 10
if mediaponderada >= 60:
    print(f"Aluno aprovado com média {mediaponderada}.") 
else:
    print(f"Aluno reprovado com média {mediaponderada}.")    