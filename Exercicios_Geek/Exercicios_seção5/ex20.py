
A = float(input("Digite o valo do lado A: "))
B = float(input("Digite o valor do lado B: "))
C = float(input("Digite o valor do lado C: "))

if A < B + C and B < A + C and C < A + B:
    if A == B == C:
        print("É um triangulo equilatero.")
    elif A == B or A == C or B == C:
        print("É um triangulo isosceles.")
    else:
        print("É um triangulo escaleno.")
else:
    print("Os valores fornecidos não forman um triangulo.")          
    