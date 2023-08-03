def soma (a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:    
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida."
    
def mostrar_opçoes():
    print("Operaçôes disponiveis:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

def calculadora_infinita():
    while True:
        mostrar_opçoes()
        opcao = input("Digite o numero para a operação correspondente: ")

        if opcao == "0":
            print("Saindo da calculadora.")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("Essa opção não existe.")
            continue

        try:
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
        except ValueError:
            print("Valor inválido. Insira apenas números.")
            continue

        if opcao == "1":
            resultado = soma(num1, num2)
        elif opcao == "2":
            resultado = subtracao(num1, num2)
        elif opcao == "3":
            resultado = multiplicacao(num1, num2)
        else:
            resultado = divisao(num1, num2)

        print(f"Resultado: {resultado}") 

calculadora_infinita()                       

