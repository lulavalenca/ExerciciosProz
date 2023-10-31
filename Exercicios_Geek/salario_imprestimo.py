# Recebe o salário do trabalhador como entrada do usuário
salario = float(input("Digite o salário do trabalhador: "))

# Recebe o valor da prestação do empréstimo como entrada do usuário
prestacao_emprestimo = float(input("Digite o valor da prestação do empréstimo: "))

# Calcula 20% do salário
limite_prestacao = salario * 0.2

# Verifica se a prestação é maior que 20% do salário
if prestacao_emprestimo > limite_prestacao:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")
