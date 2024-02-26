"""
9) Leia o salário de um trabalhador e o valor da prestação
de um empréstimo. Se a prestação for maior que 20% do salário imprima:
'Empréstimo não concedido', caso contrário imprima: 'Empréstimo concedido'
"""

salario = float(input("Digite o seu salario: "))
prestacao = float(input("Digite o valor da prestação: "))

if prestacao > salario * 0.2:
    print ("Emprestimo não concedido ")
else:
    print("Emprestimo concedido!! ")    