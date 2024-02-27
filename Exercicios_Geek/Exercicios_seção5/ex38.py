"""
Leia uma data de nascimento de uma pessoa fornecida através de três números
inteiros: Dia, Mês e Ano. Teste a validade desta data para saber se esta é uma
data válida. Teste se o dia fornecido é um dia válido: dia > 0, dia <= 28 para o mês
(29 se o ano for bissexto), dia <= 30 em abril, junho, setembro e novembro,
dia <= 31 nos outros meses. Teste a validade do mês: mês > 0 e mês <13. Teste a
validade do ano: ano <= ano atual (use uma constante definida com o valor igual a 2008).
Imprimir: "data válida" ou "data inválida" no final da execução.


Exemplo 1: 

def validar_data(dia, mes, ano):
    bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    max_dia = {
        1: 31, 2: 29 if bissexto else 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }.get(mes, -1)

    if max_dia == -1 or not (1 <= dia <= max_dia) or not (1 <= mes <= 12) or ano > 2008:
        return "data inválida"
    return "data válida"

# Leitura da data de nascimento
dia, mes, ano = map(int, input("Digite a data de nascimento (dia mês ano): ").split())

# Verificação da validade da data
resultado = validar_data(dia, mes, ano)

# Exibição do resultado
print(resultado)



"""

from datetime import date

def validar_data(dia, mes, ano):
    # Verifica se o ano é bissexto
    bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    
    # Verifica se o dia fornecido é válido
    if mes in [4, 6, 9, 11]:
        max_dia = 30
    elif mes == 2:
        max_dia = 29 if bissexto else 28
    else:
        max_dia = 31
    
    # Verifica a validade do dia, mês e ano
    if (dia > 0 and dia <= max_dia) and (mes > 0 and mes < 13) and (ano <= date.today().year):
        return "data válida"
    else:
        return "data inválida"

# Leitura da data de nascimento
dia, mes, ano = map(int, input("Digite a data de nascimento (dia mês ano): ").split())

# Verificação da validade da data
resultado = validar_data(dia, mes, ano)

# Exibição do resultado
print(resultado)
