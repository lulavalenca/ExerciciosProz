
numero = int(input("digite um numero para saber se ele e divisivel por 3 ou por 5: "))

if numero % 3 == 0 and numero % 5 == 0:
    print(f"O número é divisível por 3 e por 5 simultaneamente.")
elif numero % 3 == 0:
    print("O número é divisível por 3, mas não por 5.")
elif numero % 5 == 0:
    print("O número é divisível por 5, mas não por 3.")
else:
     print("O número não é divisível por 3 nem por 5.")