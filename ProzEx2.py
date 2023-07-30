def categoria_habilitacao(rodas, peso, pessoas):
    if rodas == 2 or rodas == 3:
        return "A"
    elif rodas == 4 and peso <= 3500 and pessoas <= 8:
        return "B"
    elif rodas >= 4 and 3500 < peso <= 6000:
        return "C"
    elif rodas >= 4 and pessoas > 8:
        return "D"
    elif rodas >= 4 and peso > 6000:
        return "E"
    else:
        return "Categoria de habilitação não encontrada para essas informações."

# Solicita ao usuário as informações do veículo
rodas = int(input("Digite a quantidade de rodas do veículo: "))
peso = float(input("Digite o peso bruto em quilogramas do veículo: "))
pessoas = int(input("Digite a quantidade de pessoas no veículo: "))

# Determina a categoria de habilitação e exibe o resultado
categoria = categoria_habilitacao(rodas, peso, pessoas)
print(f"A categoria de habilitação para o veículo informado é: {categoria}")
