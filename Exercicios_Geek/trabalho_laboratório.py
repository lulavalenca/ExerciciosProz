# Recebe as notas do aluno como entrada do usuário
trabalho_laboratorio = float(input("Nota do Trabalho de Laboratório (0 a 10): "))
avaliacao_semestral = float(input("Nota da Avaliação Semestral (0 a 10): "))
exame_final = float(input("Nota do Exame Final (0 a 10): "))

# Verifica se as notas estão dentro do intervalo correto (0 a 10)
if (0 <= trabalho_laboratorio <= 10) and (0 <= avaliacao_semestral <= 10) and (0 <= exame_final <= 10):
    # Calcula a média ponderada das notas
    media_final = (trabalho_laboratorio * 2 + avaliacao_semestral * 3 + exame_final * 5) / (2 + 3 + 5)

    # Determina a situação do aluno com base na média final
    if 0 <= media_final < 3:
        situacao = "Reprovado"
    elif 3 <= media_final < 5:
        situacao = "Em Recuperação"
    else:
        situacao = "Aprovado"

    # Exibe a média final e a situação do aluno
    print(f"Média Final: {media_final:.2f}")
    print(f"Situação: {situacao}")
else:
    print("Notas fora do intervalo válido (0 a 10).")
