# Leitura dos valores investidos por cada apostador
investimento1 = float(input("Valor investido pelo primeiro apostador: "))
investimento2 = float(input("Valor investido pelo segundo apostador: "))
investimento3 = float(input("Valor investido pelo terceiro apostador: "))

# Leitura do valor total do prêmio
valor_premio = float(input("Valor total do prêmio: "))

# Calculando a proporção de cada apostador com base no valor total investido
total_investido = investimento1 + investimento2 + investimento3
proporcao1 = investimento1 / total_investido
proporcao2 = investimento2 / total_investido
proporcao3 = investimento3 / total_investido

# Calculando quanto cada apostador ganharia do prêmio
premio1 = proporcao1 * valor_premio
premio2 = proporcao2 * valor_premio
premio3 = proporcao3 * valor_premio

# Imprimindo os resultados
print(f"O primeiro apostador ganharia: R$ {premio1:.2f}")
print(f"O segundo apostador ganharia: R$ {premio2:.2f}")
print(f"O terceiro apostador ganharia: R$ {premio3:.2f}")
