"""
Exemplo 1

def eh_bissexto(ano):
    return ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)

def data_valida(dia, mes, ano):
    if mes < 1 or mes > 12:
        return False
    
    if mes == 2:
        if eh_bissexto(ano):
            return 1 <= dia <= 29
        else:
            return 1 <= dia <= 28
    elif mes in [4, 6, 9, 11]:
        return 1 <= dia <= 30
    else:
        return 1 <= dia <= 31

# Lê a data fornecida pelo usuário
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

# Verifica se a data é válida
if data_valida(dia, mes, ano):
    print("A data é válida.")
else:
    print("A data é inválida.")

/---------------------------------------------------------------------/    

Exemplo 2 

def eh_bissexto(ano):
    return ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)

# Lê a data fornecida pelo usuário
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

# Verifica se o mês está entre 1 e 12
if mes < 1 or mes > 12:
    print("A data é inválida.")
else:
    # Verifica se o dia está dentro do intervalo correto para o mês
    if mes == 2:
        if eh_bissexto(ano):
            if not (1 <= dia <= 29):
                print("A data é inválida.")
            else:
                print("A data é válida.")
        else:
            if not (1 <= dia <= 28):
                print("A data é inválida.")
            else:
                print("A data é válida.")
    elif mes in [4, 6, 9, 11]:
        if not (1 <= dia <= 30):
            print("A data é inválida.")
        else:
            print("A data é válida.")
    else:
        if not (1 <= dia <= 31):
            print("A data é inválida.")
        else:
            print("A data é válida.")



"""

def eh_bissexto(ano):
    return ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)

# Lê a data fornecida pelo usuário
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

# Verifica se o mês está entre 1 e 12
if mes < 1 or mes > 12:
    print("A data é inválida.")
else:
    # Verifica se o dia está dentro do intervalo correto para o mês
    if mes == 2:
        if eh_bissexto(ano):
            if not (1 <= dia <= 29):
                print("A data é inválida.")
            else:
                print("A data é válida.")
        else:
            if not (1 <= dia <= 28):
                print("A data é inválida.")
            else:
                print("A data é válida.")
    elif mes in [4, 6, 9, 11]:
        if not (1 <= dia <= 30):
            print("A data é inválida.")
        else:
            print("A data é válida.")
    else:
        if not (1 <= dia <= 31):
            print("A data é inválida.")
        else:
            print("A data é válida.")
