def verificar_tuite(texto):
    if len(texto) <= 140:
        return "TWEET"
    else:
        return "MUTE"

def main():
    # Lê a linha de texto
    texto = input()

    # Chama a função para verificar se é um tuíte e imprime o resultado
    print(verificar_tuite(texto))

if __name__ == "__main__":
    main()
