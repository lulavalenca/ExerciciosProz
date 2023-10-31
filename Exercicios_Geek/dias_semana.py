# Cria um dicionário que mapeia números a dias da semana
dias_da_semana = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}

# Recebe um número inteiro entre 1 e 7 como entrada do usuário
numero = int(input("Digite um número entre 1 e 7: "))

# Verifica se o número está no intervalo correto
if 1 <= numero <= 7:
    dia_semana = dias_da_semana[numero]
    print(f"O dia da semana correspondente ao número {numero} é {dia_semana}.")
else:
    print("Número fora do intervalo válido (1 a 7).")
