"""
3) Faça um algoritmo utilizando o comando while que mostra uma mensagem
regressiva na tela, inciando em 10 e terminando em 0. Mostrar uma mensagem "FIM!"
após a contagem

# usando o While
numero = 10

while numero >= 0:
    print(numero)
    numero -= 1

print()
print("Fim")


"""


# Exemplo 1
contador = 10

while contador >= 0:
    print(contador)
    contador -= 1

print("Fim")    


# Exemplo 2
for contador in range(10, -1, -1):
    print(contador)

print( )
print("Fim!")    
