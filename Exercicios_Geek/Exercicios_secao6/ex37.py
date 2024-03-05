"""
37. Escreve um programa que verifique quais números
entre 1000 e 9999 (inclusive) pos- suem a propriedade seguinte: a soma dos dois 
digitos de mais baixa ordem com os dois digitos de mais alta ordem elevada ao quadrado é igual ao próprio numero. 
Por exemplo, para o inteiro 3025, temos que:
30+25=55
5523025

for numero in range(1000, 10000):
    alta_ordem = numero // 100
    baixa_ordem = numero % 100

soma = alta_ordem + baixa_ordem

if soma ** 2 == numero:
    print(numero)

    
Exemplo 2
    
inicio = 0
fim = 0
quadrado = 0
lista = []
for i in range(1000, 10001):
    inicio = i // 100
    fim = i % 100
    if (inicio + fim) ** 2 == i:
        lista.append(i)
print(f'Os números verificados foram: {lista}')    


Exemplo 3 

for numero in range(1000, 10000):
    # Extrair os dois dígitos de mais alta ordem e de mais baixa ordem
    alta_ordem = numero // 100
    baixa_ordem = numero % 100
    
    # Calcular a soma dos dois dígitos de mais baixa ordem com os dois dígitos de mais alta ordem elevados ao quadrado
    soma = (alta_ordem // 10) + (alta_ordem % 10) + (baixa_ordem // 10) + (baixa_ordem % 10)
    
    # Verificar se a soma ao quadrado é igual ao número original
    if soma ** 2 == numero:
        print(numero)


"""








def verificar_numero(numero):
  """
  Função para verificar se um número possui a propriedade especificada.

  Argumentos:
    numero: O número a ser verificado.

  Retorna:
    True se o número possui a propriedade, False caso contrário.
  """
  # Extrai os dígitos de baixa e alta ordem
  digitos_baixos = numero % 100
  digitos_altos = numero // 100

  # Soma os dígitos
  soma_digitos = digitos_baixos + digitos_altos

  # Calcula o quadrado da soma dos dígitos
  quadrado_soma = soma_digitos ** 2

  # Retorna True se o quadrado da soma for igual ao número
  return quadrado_soma == numero

# Percorre os números entre 1000 e 9999
for numero in range(1000, 10000):
  # Verifica se o número possui a propriedade
  if verificar_numero(numero):
    # Imprime o número
    print(numero)

# Exemplo de uso da função verificar_numero
numero = 4005
if verificar_numero(numero):
  print(f"O número {numero} possui a propriedade.")
else:
  print(f"O número {numero} não possui a propriedade.")
