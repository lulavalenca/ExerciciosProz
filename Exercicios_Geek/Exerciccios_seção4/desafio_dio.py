def verificar_nivel_energia(nivel):
    if nivel > 8000:
        return "Mais de 8000!"
    else:
        return "Inseto!"

def main():
    # Lê o número de casos
    num_casos = int(input())

    # Loop sobre cada caso
    for _ in range(num_casos):
        # Lê o valor do nível de energia
        nivel_energia = int(input())

        # Verifica e imprime o resultado
        resultado = verificar_nivel_energia(nivel_energia)
        print(resultado)

if __name__ == "__main__":
    main()