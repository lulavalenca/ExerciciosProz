# Cria um dicionário que mapeia números a meses do ano
meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

# Recebe um número inteiro entre 1 e 12 como entrada do usuário
numero = int(input("Digite um número entre 1 e 12: "))

# Verifica se o número está no intervalo correto
if 1 <= numero <= 12:
    mes = meses[numero]
    print(f"O mês correspondente ao número {numero} é {mes}.")
else:
    print("Número fora do intervalo válido (1 a 12).")
