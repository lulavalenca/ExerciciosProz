def numero_para_mes(numero):
    meses = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return meses[numero - 1]

def main():
    # Lê o número do mês
    numero = int(input())

    # Converte o número do mês para o nome por extenso
    nome_mes = numero_para_mes(numero)

    # Imprime o nome do mês por extenso
    print(nome_mes)

if __name__ == "__main__":
    main()