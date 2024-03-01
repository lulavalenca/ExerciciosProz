# Errado
nota = 0
for nota in range(10):
    numero = int(input("Digite as notas:"))
    nota += numero
    media = nota / 10
print("A media das notas foi de:", media)    

# Certo

soma_notas = 0
for _ in range(10):
    nota = int(input("digite a nota: "))
    soma_notas += nota

media = soma_notas / 10
print("A média das notas é:", media)
