"""
22 - 22. Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequência arbitrária de notas (válidas no intervalo de 10 a 20) e que mostre na tela, como resultado, a correspondente média aritmética. O número de notas com que o aluno pretenda efetuar o cálculo não será fornecido ao programa, o qual terminará quando for introduzido um valor que não seja válido como nota de aprovação

"""

soma = 0
contagem = 0

print("Digite as notas (entre 10 e 20). Para encerrar, digite um nota inválida.")

while True:
    nota = float(input("Digite a nota: "))

    if 10 <= nota <= 20:
        soma += nota
        contagem += 1
    else:
        break

if contagem > 0:
    media = soma / contagem
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")            