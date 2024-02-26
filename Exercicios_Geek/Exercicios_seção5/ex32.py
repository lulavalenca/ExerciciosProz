"""
32) Escrever um programa que leia o código do produto escolhido do cardápio
de uma lanchonete e a quantidade. O programa deve calcular o valor a ser pago
por aquele lanche. Considere que a cada execução somente será calculado um
pedido. O cardápio da lanchonete segue o padrão abaixo:

    | Especificação    | Código | Preço |
    | Cachorro Quente  |  100   | 1.20  |
    | Bauru Simples    |  101   | 1.30  |
    | Bauru com Ovo    |  102   | 1.50  |
    | Hamburguer       |  103   | 1.20  |
    | Cheeseburguer    |  104   | 1.70  |
    | Suco             |  105   | 2.20  |
    | Refrigerante     |  106   | 1.00  |

# Define o cardápio da lanchonete
cardapio = {
    100: ("Cachorro Quente", 1.20),
    101: ("Bauru Simples", 1.30),
    102: ("Bauru com Ovo", 1.50),
    103: ("Hamburguer", 1.20),
    104: ("Cheeseburguer", 1.70),
    105: ("Suco", 2.20),
    106: ("Refrigerante", 1.00)
}

# Recebe o código do produto e a quantidade como entrada do usuário
codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade: "))

# Verifica se o código do produto está no cardápio
if codigo in cardapio:
    # Calcula o valor total do pedido
    produto, preco_unitario = cardapio[codigo]
    valor_total = preco_unitario * quantidade
    print(f"Produto: {produto}\nPreço unitário: R$ {preco_unitario:.2f}\nQuantidade: {quantidade}\nValor total: R$ {valor_total:.2f}")
else:
    print("Código de produto inválido.")
    


"""

codigo = int(input("Digite o codigo do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

if codigo == 100:
    preco = 1.20
    print(f"{quantidade} cachorro(s) quente = {preco * quantidade}")

elif codigo == 101:
    preco = 1.30
    print(f"{quantidade} bauru(s) simples = {preco * quantidade}")

elif codigo == 102:
    preco = 1.50
    print(f"{quantidade} bauru(s) com ovo = {preco * quantidade}")

elif codigo == 103:
    preco = 1.20
    print(f"{quantidade} hamburguer(s) = {preco * quantidade}")

elif codigo == 104:
    preco = 1.70
    print(f"{quantidade} cheeseburguer(s) = {preco * quantidade}")

elif codigo == 105:
    preco = 2.20
    print(f"{quantidade} sucos(s) = {preco * quantidade}") 

elif codigo == 106:
    preco = 1.00
    print(f"{quantidade} refrigerante(s) = {preco * quantidade}")

else:
    print("Código inválido!")