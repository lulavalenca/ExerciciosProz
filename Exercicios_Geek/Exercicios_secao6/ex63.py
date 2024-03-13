"""
62) Se os números de 1 a 5 são escritos em palavras: um, dois, três, quatro,
cinco, então há 2 + 4 + 4 + 6 + 5 = 21 letras usadas no total. Faça um programa
que conte quantas letras seriam utilizadas se todos os números de 1 a 1000 (mil)
fossem escritos em palavras.
OBS: Não conte espaços ou hífens faça esse programa em python


1 - EXEMPLO DE CODIGO

# Função para contar o número de letras em um número por extenso
def contar_letras(numero):
    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
                "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

    # Números especiais
    if numero == 1000:
        return len("mil")
    if numero < 20:
        return len(unidades[numero])
    if numero < 100:
        return len(dezenas[numero // 10]) + len(unidades[numero % 10])
    if numero % 100 == 0:
        return len(centenas[numero // 100])
    if numero > 100:
        return len(centenas[numero // 100]) + len("e") + contar_letras(numero % 100)
    return 0

# Contagem total de letras
total_letras = 0
for i in range(1, 1001):
    total_letras += contar_letras(i)

print("O total de letras usadas se todos os números de 1 a 1000 fossem escritos por extenso é:", total_letras)


1 exemplo de codigo 

unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
especiais = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

def escrever_numero(num):
    if num == 1000:
        return "mil"
    elif num == 100:
        return "cem"
    elif num < 10:
        return unidades[num]
    elif num < 20:
        return especiais[num-10]
    elif num < 100:
        if num % 10 == 0:
            return dezenas[num//10]
        else:
            return dezenas[num//10] + "e" + unidades[num%10]
    else:
        if num % 100 < 10:
            return centenas[num//100] + "e" + unidades[num%100]
        elif num % 100 < 20:
            return centenas[num//100] + "e" + especiais[num%100-10]
        else:
            return centenas[num//100] + "e" + dezenas[(num%100)//10] + "e" + unidades[num%10]

total_letras = 0
for i in range(1, 1001):
    total_letras += len(escrever_numero(i).replace(" ", ""))

print(f"O total de letras usadas para escrever todos os números de 1 a 1000 é {total_letras}.")


2 EXEMPLO 



"""

unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
especiais = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

def escrever_numero(num):
    if num == 1000:
        return "mil"
    elif num == 100:
        return "cem"
    elif num < 20:
        return unidades[num] if num < 10 else especiais[num-10]
    elif num < 100:
        return dezenas[num//10] if num % 10 == 0 else dezenas[num//10] + " e " + unidades[num%10]
    else:
        centena = centenas[num//100]
        dezena_unidade = num % 100
        if dezena_unidade < 20:
            return centena + " e " + (unidades[dezena_unidade] if dezena_unidade < 10 else especiais[dezena_unidade-10])
        else:
            return centena + " e " + (dezenas[dezena_unidade//10] if dezena_unidade % 10 == 0 else dezenas[dezena_unidade//10] + " e " + unidades[dezena_unidade%10])

num_usuario = int(input("Digite um número entre 1 e 1000: "))
print(f"O número {num_usuario} por extenso é: {escrever_numero(num_usuario)}")
