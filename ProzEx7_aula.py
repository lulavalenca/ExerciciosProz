def mostrar_numero():
    numero_valido = False

    while not numero_valido:
        try:
            numero = int(input("Escreva um número inteiro positivo, par, menor ou igual a 100 e divisível por 2 ou 3: "))

            if numero > 0 and numero % 2 == 0 and numero <= 100 and (numero % 2 == 0 or numero % 3 == 0):
                numero_valido = True
                print(f"O número que você escolheu foi: {numero}")
            else:
                print("Número inválido. Verifique as regras.")
        except ValueError:
            print("Precisa digitar um número inteiro.")

# Chamando a função para solicitar e verificar o número
mostrar_numero()