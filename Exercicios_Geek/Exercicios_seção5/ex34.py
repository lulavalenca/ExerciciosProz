"""
 Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo
com a tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma reduçãoo
de conceito.

    |    NOTA       |  CONCEITO (ATÉ 20 FALTAS) | CONCEITO (MAIS DE 20 FALTAS) |
    | 9.0 até 10.0  |             A             |              B               |
    | 7.5 até 8.9   |             B             |              C               |
    | 5.0 até 7.4   |             C             |              D               |
    | 4.0 até 4.9   |             D             |              E               |
    | 0.0 até 3.9   |             E             |              E               |


   # Lê a nota e o número de faltas do aluno
nota = float(input("Digite a nota do aluno: "))
faltas = int(input("Digite o número de faltas do aluno: "))

# Define o conceito padrão
conceito = ""

# Verifica o conceito com base na nota e no número de faltas
if faltas <= 20:
    if nota >= 9.0:
        conceito = "A"
    elif 7.5 <= nota < 9.0:
        conceito = "B"
    elif 5.0 <= nota < 7.5:
        conceito = "C"
    elif 4.0 <= nota < 5.0:
        conceito = "D"
    else:
        conceito = "E"
else:
    if nota >= 9.0:
        conceito = "B"
    elif 7.5 <= nota < 9.0:
        conceito = "C"
    elif 5.0 <= nota < 7.5:
        conceito = "D"
    elif 4.0 <= nota < 5.0:
        conceito = "E"
    else:
        conceito = "E"

# Exibe o conceito do aluno
print("Conceito do aluno:", conceito)
 


"""

nota = float(input("Digite a nota do aluno: "))
faltas = int(input("Digite o numero de faltas do aluno: "))

conceito = ""

if faltas <= 20:
    if nota >= 9.0:
        conceito = "A"
    elif 7.5 <= nota < 9.0:
        conceito = "B"
    elif 5.0 <= nota < 7.5:
        conceito = "C"
    elif 4.0 <= nota < 5.0:
        conceito = "D"
    else:
        conceito = "E"
else:
    if nota >= 9.0:
        conceito = "B" 
    elif 7.5 <= nota < 9.0:
        conceito = "C"
    elif 5.0 <= nota < 7.5:
        conceito = "D"
    elif 4.0 <= nota < 5.0:
        conceito = "E"
    else:
        conceito = "E"       

print("Conceito do aluno:", conceito)                                  