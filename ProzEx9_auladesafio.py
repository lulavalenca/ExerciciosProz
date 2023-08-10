def adicionar_produto(lista, produto):
    lista.append(produto)
    print(f"Produto '{produto}' adicionado à lista.")

def remover_produto(lista, produto):
    if produto in lista:
        lista.remove(produto)
        print(f"Produto '{produto}' removido da lista.")
    else:
        print(f"Produto '{produto}' não encontrado na lista.")

def mostrar_produtos(lista):
    print("Lista de produtos:")
    for produto in lista:
        print(produto)

# Inicialização da lista de produtos
lista_de_produtos = []

# Menu para interação com o usuário
while True:
    print("\nMenu:")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Mostrar produtos")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        produto = input("Digite o nome do produto a ser adicionado: ")
        adicionar_produto(lista_de_produtos, produto)
    elif opcao == '2':
        produto = input("Digite o nome do produto a ser removido: ")
        remover_produto(lista_de_produtos, produto)
    elif opcao == '3':
        mostrar_produtos(lista_de_produtos)
    elif opcao == '4':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Escolha novamente.")
