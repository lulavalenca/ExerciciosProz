# Recebe dois números como entrada do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Compara os números e mostra o maior
if num1 > num2:
    print(f"{num1} é o maior número.")
elif num2 > num1:
    print(f"{num2} é o maior número.")
else:
    print("Os números são iguais.")
