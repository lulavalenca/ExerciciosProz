"""
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 > numero2:
    print("O primeiro numero e maior que o segundo numero: ")
elif numero2 > numero1:
    print("O segundo numero e maior que o primeiro numero: ")
else:
    print("Os numeros são iguais:")        
"""


numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 > numero2:
    print(f"O primeiro número ({numero1}) é maior que o segundo número ({numero2}).")
elif numero2 > numero1:
    print(f"O segundo número ({numero2}) é maior que o primeiro número ({numero1}).")
else:
    print("Os números são iguais.")
