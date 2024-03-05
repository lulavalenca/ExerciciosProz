"""
35. Faça um programa que some os números impares contidos em um intervalo definido pelo usuário. 
O usuário define o valor inicial do intervalo e o valor final deste intervalo 
e o programa deve somar todos os números ímpares contidos neste intervalo. 
Caso o usuário digite um intervalo inválido (começando por um valor maior que o valor final) 
deve ser escrito uma mensagem de erro na tela, "Intervalo de valores inválido" e o programa termina. 
Exemplo de tela de saída: Digite o valor inicial e valor final:
10
Soma dos impares neste intervalo: 21
5

"""



# Solicitar ao usuário que insira o valor inicial e final do intervalo
valor_inicial = int(input("Digite o valor inicial do intervalo: "))
valor_final = int(input("Digite o valor final do intervalo: "))

# Verificar se o intervalo é válido
if valor_inicial > valor_final:
    print("Intervalo de valores inválido")
else:
    # Inicializar a variável de soma de números ímpares
    soma_impares = 0

    # Iterar sobre o intervalo e somar os números ímpares
    for num in range(valor_inicial, valor_final + 1):
        if num % 2 != 0:  # Verificar se o número é ímpar
            soma_impares += num

    # Exibir a soma dos números ímpares no intervalo
    print("Soma dos ímpares neste intervalo:", soma_impares)
