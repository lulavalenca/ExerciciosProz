# Recebe a altura como entrada do usuário (em metros)
altura = float(input("Digite a altura (em metros): "))

# Recebe o sexo como entrada do usuário (M para masculino, F para feminino)
sexo = input("Digite o sexo (M para masculino, F para feminino): ")

# Verifica o sexo e calcula o peso ideal
if sexo == 'M' or sexo == 'm':
    peso_ideal = (72.7 * altura) - 58
    print(f"O peso ideal para um homem com {altura} metros de altura é {peso_ideal:.2f} kg.")
elif sexo == 'F' or sexo == 'f':
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma mulher com {altura} metros de altura é {peso_ideal:.2f} kg.")
else:
    print("Sexo não reconhecido. Use M para masculino e F para feminino.")
