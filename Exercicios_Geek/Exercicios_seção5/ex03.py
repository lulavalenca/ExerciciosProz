"""
Exemplo-1

numero = float(input("Digite um numero para tirar a raiz quadrada ou o numero ao quadrado: "))

if numero >= 0:
    raiz_quadrada = numero ** 0.5
    print(f"A raiz quadrada de {numero} ")

else:
    numero_quadrado = numero ** 2
    print(f"O numero elevado ao quadrado é numero {numero_quadrada}")


Exemplo-2    

# Lê um número real do usuário
numero = float(input("Digite um número real: "))

# Verifica se o número é positivo ou não
if numero >= 0:
    # Calcula e imprime a raiz quadrada se o número for positivo
    print(f"A raiz quadrada de {numero} é {numero**0.5:.2f}")
else:
    # Imprime o número ao quadrado se for negativo
    print(f"O quadrado de {numero} é {numero**2:.2f}")


"""

# Lê um número real do usuário
numero = float(input("Digite um número real: "))

# Calcula a raiz quadrada do número se for positivo ou imprime o quadrado se for negativo
if numero >= 0:
    resultado = numero ** 0.5
    print(f"A raiz quadrada de {numero} é {resultado:.2f}")
else:
    resultado = numero ** 2
    print(f"O quadrado de {numero} é {resultado:.2f}")


