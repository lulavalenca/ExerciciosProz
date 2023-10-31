# Recebe o ano como entrada do usuário
ano = int(input("Digite um ano: "))

# Verifica se o ano é bissexto com base nas condições
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
