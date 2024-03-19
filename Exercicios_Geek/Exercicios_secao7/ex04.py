def calcular_media(lista):
    if not lista:
        return 0
    
    soma = sum(lista)

    media = soma / len(lista)
    return media

lista = [10, 5, 7, 25, 13, 30, 45]

media = calcular_media(lista)

print("A media dos numeros na lista é:", media)