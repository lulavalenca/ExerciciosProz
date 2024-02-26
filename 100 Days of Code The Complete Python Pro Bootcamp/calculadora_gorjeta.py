'''
input("Bem vindo a calculadora de gorjeta")
contaPagar = float(input("A conta para pagar ficou em R$ ")
porcentagem_Gorjeta = int(input("Qual o valor da sua gorjeta? 10, 12 or 15? ")) 
pessoas = int(input("Quantas pessoas irão pagar e dividir a conta"))           

gorjeta_porcentagem = porcentagem_Gorjeta / 100
total_porcentagem = contaPagar * gorjeta_porcentagem
total_conta = contaPagar * total_porcentagem
'''

# Se a conta foi de $150.00, dividida entre 5 pessoas, com uma gorjeta de 12%.
# Cada pessoa deve pagar (150.00 / 5) * 1.12 = 33.6
# Arredonde o resultado para 2 casas decimais.
print("Bem-vindo à calculadora de gorjetas!")
conta = float(input("Qual foi o total da conta? R$"))
gorjeta = int(input("Quanto de gorjeta você gostaria de dar? 10, 12 ou 15? "))
pessoas = int(input("Quantas pessoas vão dividir a conta?"))

gorjeta_como_percentual = gorjeta / 100
valor_total_gorjeta = conta * gorjeta_como_percentual
valor_total_conta = conta + valor_total_gorjeta
conta_por_pessoa = valor_total_conta / pessoas
valor_final = round(conta_por_pessoa, 2)

# FAQ: Como arredondar para 2 casas decimais?
# Encontre a resposta na seção de Perguntas e Respostas aqui: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048

print(f"Cada pessoa deve pagar: R${valor_final}")