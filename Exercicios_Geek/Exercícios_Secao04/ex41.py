"""
1 - Exemplo 

valor_hora = float(input("Digite o  valor da hora trabalhada: "))
horas_trabalhadas = int(input("Informe o numero de horas trabalhadas no mês: "))

salario_base = valor_hora * horas_trabalhadas
bonus = salario_base * 0.10
salario_total = salario_base + bonus

print(f"O valor a ser pago ao funcionário é: R${salario_total:.2f} ")

"""

valor_hora = float(input("Digite o valor da hora de trabalho (em Reais): "))
horas_trabalhadas = float(input("Digite o numero de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas
acrescimo = salario_bruto * 0.10
salario_liquido = salario_bruto + acrescimo 

print("O valor a ser pago ao funcionário é: R$", salario_liquido)