def verificar_numero(numero):
    if not isinstance(numero, int):
        return False, "Precisa digitar um numero inteiro."
    
    if numero <= 0:
        return False, "O numero deve ser positivo."
    
    if numero % 2 != 0:
        return False, "O numero deve ser par."
    
    if numero > 100:
        return False, "O numero deve ser menor ou igual a 100."
    
    if numero % 2 != 0 and numero % 3 != 0:
        return False, "O numero deve ser divisivel por 2 ou 3."
    
    return True, "Numero valido."

def mostrar_numero():
    numero_valido = False

    while not numero_valido:
        try:
            numero = int(input("Escreva um numero inteiro positivo, par, menor ou igual a 100 e divisivel por 2 ou 3: "))

            valido, mensagem = verificar_numero(numero)
            if valido:
                numero_valido = True
                print(f"O numero que voce escolheu foi : {numero}")
            else:
                print(mensagem)
        except ValueError:
            print("Precisa digitar um numero inteiro.")

mostrar_numero()                        
