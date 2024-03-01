"""

# Obtenha o número de dias trabalhados pelo encanador
dias_trabalhados = int(input("Digite o número de dias trabalhados pelo encanador: "))

# Dados fornecidos
salario_diario = 30.0  # salário diário em R$
taxa_imposto_renda = 8.0  # taxa de imposto de renda em porcentagem

# Calcule o rendimento bruto e líquido
rendimento_bruto = dias_trabalhados * salario_diario
imposto_renda = (taxa_imposto_renda / 100) * rendimento_bruto
rendimento_liquido = rendimento_bruto - imposto_renda

# Exiba o rendimento líquido
print(f"A quantia líquida que deverá ser paga é R${rendimento_liquido:.2f}")


"""

dias_trabalhados = int(input("Digite o numero de dias trabalhado pelo encanador: "))

salario_por_dia = 30.00

salario_bruto = dias_trabalhados * salario_por_dia

imposto_de_renda = salario_bruto * 0.08

salario_liquido = salario_bruto - imposto_de_renda

print("O salario liquido a ser pago é: R$", salario_liquido)