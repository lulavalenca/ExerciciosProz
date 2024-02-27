def mes_correspondente(numero):
    if numero == 1:
        return "Janeiro"
    elif numero == 2:
        return "Fevereiro"
    elif numero == 3:
        return "Março"
    elif numero == 4:
        return "Abril"
    elif numero == 5:
        return "Maio"
    elif numero == 6:
        return "Junho"
    elif numero == 7:
        return "Julho"
    elif numero == 8:
        return "Agosto"
    elif numero == 9:
        return "Setembro"
    elif numero == 10:
        return "Outubro"
    elif numero == 11:
        return "Novembro"
    elif numero == 12:
        return "Dezembro"
    else:
        return "Numero invalido"
    
numero = int(input("Digite entre 1 a 12 os meses do ano: "))

print(mes_correspondente(numero))