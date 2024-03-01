"""
# Lê os valores dos catetos a e b
a = float(input("Digite o valor do cateto a: "))
b = float(input("Digite o valor do cateto b: "))

# Calcula a hipotenusa diretamente usando a fórmula
hipotenusa = (a ** 2 + b ** 2) ** 0.5

# Imprime o resultado
print("O valor da hipotenusa é:", hipotenusa)


"""

import math

a = float(input("Digite o valor do cateto a: "))
b = float(input("Digite o valor do cateto b: "))

hipotenusa = math.sqrt(a ** 2 + b ** 2)

print("O valor da hipotenusa é:",hipotenusa)