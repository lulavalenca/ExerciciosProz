"""
salario = float(input("Digite o valor do salario atual: "))
prestacao_emprestimo = float(input("O valor da prestação atual: "))

if (salario / prestacao_emprestimo) < 0.20:
    print("Emprestimo concedido!!!!.")
else:
    print("Emprestimo Recusado")  
"""

salario = float(input("Digite o valor do salario atual: "))
prestacao_emprestimo = float(input("Digite o valor da prestação do emprestimo: "))

limite_porcentagem = 0.20
limite_prestacao = salario * limite_porcentagem

if prestacao_emprestimo <= limite_prestacao:
    print("Emprestimo Concedido")
else:
    print("Emprestimo Recusado. A prestação excede 20% do salário. ")    