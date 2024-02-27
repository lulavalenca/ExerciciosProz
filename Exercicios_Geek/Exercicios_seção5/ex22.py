# Lê a idade e o tempo de serviço do trabalhador
idade = int(input("Digite a idade do trabalhador: "))
tempo_servico = int(input("Digite o tempo de serviço do trabalhador: "))

# Verifica se o trabalhador pode se aposentar
if idade >= 64 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
    print("O trabalhador pode se aposentar.")
else:
    print("O trabalhador ainda não pode se aposentar.")
