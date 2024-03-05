"""
45. Faça um algoritmo que converta uma velocidade expressa em km/h para m/s e vice versa. 
Você deve criar um menu com as duas opções de conversão e com uma opção para finalizar o programa. 
O usuário poderá fazer quantas conversões desejar, 
sendo que o programa só será finalizado quando a opção de finalizar for escolhida.

1 exemplo de codigo

# Função para converter velocidade de km/h para m/s
def kmh_para_ms(velocidade):
    return velocidade / 3.6

# Função para converter velocidade de m/s para km/h
def ms_para_kmh(velocidade):
    return velocidade * 3.6

# Função principal do programa
def main():
    while True:
        print("\nMENU:")
        print("1. Converter de km/h para m/s")
        print("2. Converter de m/s para km/h")
        print("3. Finalizar o programa")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            velocidade_kmh = float(input("Digite a velocidade em km/h: "))
            velocidade_ms = kmh_para_ms(velocidade_kmh)
            print(f"A velocidade em m/s é: {velocidade_ms:.2f}")
        elif opcao == '2':
            velocidade_ms = float(input("Digite a velocidade em m/s: "))
            velocidade_kmh = ms_para_kmh(velocidade_ms)
            print(f"A velocidade em km/h é: {velocidade_kmh:.2f}")
        elif opcao == '3':
            print("Programa finalizado.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Chamada da função principal
main()




"""
def menu():
    print("1. Converter de km/h para m/s")
    print("2. Converter de m/s para km/h")
    print("3. Sair do programa")

def converter_kmh_ms():
    kmh = float(input("Digite a velocidade em km/h: "))
    ms = kmh / 3.6
    print(f"A velocidade é {ms} m/s")

def converter_ms_kmh():
    ms = float(input("Digite a velocidade em m/s: "))
    kmh = ms * 3.6
    print(f"A velocidade é {kmh} km/h")

while True:
    menu()
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        converter_kmh_ms()
    elif opcao == 2:
        converter_ms_kmh()
    elif opcao == 3:
        print("Finalizando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
