
nota_lab = float(input("Digite a nota do trabalho de laboratorio: "))
nota_semestral = float(input("Digite a nota da avaliação semestral: "))
nota_final = float(input("Digite a nota do exame final: "))

media = (nota_lab * 2 + nota_semestral * 3 + nota_final * 5) / 10

if 0 <= media < 3:
    print("Aluno reprovado.")
elif 3 <= media < 5:
    print("Aluno em recuperação.")
else:
    print("Aluno aprovado.")    