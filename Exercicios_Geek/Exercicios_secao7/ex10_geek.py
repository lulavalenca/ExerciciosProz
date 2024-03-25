"""
10) Faça um programa para ler a nota da prova de 15 alunos.txt e armazene num vetor,
calcule e imprima a média geral.

"""

def ler_notas():
    notas = []
    for i in range(15):
        nota = float(input(f"Digite a nota do aluno {i+1}: "))
        notas.append(nota)
    return notas

def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

notas_alunos = ler_notas()

media_geral = calcular_media(notas_alunos)

print(f"A média geral das notas é: {media_geral:.2f}")
