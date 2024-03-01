
altura = float(input("Digite a sua altura: "))
sexo = input("Digite o seu sexo (M para masculino, F para feminino): ")

if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo.upper() == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Sexo inválido. Use M para masculino, F para feminino.") 
    exit() 
print(f"O peso ideal para uma pessoa de {altura:.2f} metros de altura é {peso_ideal:.2f} Kg.")          
