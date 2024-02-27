"""
salario_base = float(input("Digite o salario base do trabalhador: "))

gratificacao = salario_base * 0.05

imposto = salario_base * 0.07

salario_receber = salario_base + gratificacao - imposto

print("O salario a receber é: R$", salario_receber)


"""


# Recebe o salário base do funcionário
salario_base = float(input("Informe o salário base: "))

# Calcula a gratificação (5% do salário base)
gratificacao = salario_base * 0.05

# Calcula o imposto (7% do salário base)
imposto = salario_base * 0.07

# Calcula o salário a receber (salário base + gratificação - imposto)
salario_receber = salario_base + gratificacao - imposto

# Exibe o resultado para o usuário
print(f"O salário a receber é: R${salario_receber:.2f}")
