
def imprimir_dia_semana(numero):
    if numero == 1:
        return "Domingo"
    elif numero == 2:
        return "Segunda-feira"
    elif numero == 3:
        return "Terça-feira"
    elif numero == 4:
        return "Quarta-feira"
    elif numero == 5:
        return "Quinta-feira"
    elif numero == 6:
        return "Sexta-feira"
    elif numero == 7:
        return "Sabado"
    else:
        return "Número inválido"
    
numero = int(input("Digite um numero entre 1 e 7: "))

print(imprimir_dia_semana(numero))