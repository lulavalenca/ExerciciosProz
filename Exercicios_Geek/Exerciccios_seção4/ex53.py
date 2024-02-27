# Leitura das dimensões do terreno e do preço do metro de tela
comprimento = float(input("Digite o comprimento do terreno (em metros): "))
largura = float(input("Digite a largura do terreno (em metros): "))
preco_tela = float(input("Digite o preço do metro de tela (em reais): "))

# Calculando o perímetro do terreno
perimetro = 2 * (comprimento + largura)

# Calculando o custo para cercar o terreno com tela
custo_cercamento = perimetro * preco_tela

# Imprimindo o resultado
print(f"O custo para cercar o terreno com tela é de R$ {custo_cercamento:.2f}")
