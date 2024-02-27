"""
# Recebendo o valor em segundos do usuário
segundos = int(input("Digite um valor inteiro em segundos: "))

# Calculando horas, minutos e segundos
horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

# Exibindo o resultado
print(f"{horas} horas, {minutos} minutos e {segundos} segundos.")


"""

segundos = int(input("Digite um valor inteiro em segundos: "))

horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

print(f"{horas} horas, {minutos} minutos e {segundos} segundos: ")


