def mostrarNumero():
  print("Escreva um menor ou igual a 100:")

  numero_valido = True

  while(numero_valido == True):
    try:
      numero = int(input())
      if (numero <= 100):
        print("O numero que voce escolheu foi: " + str(numero))
        numero_valido = False
      else:
        print("Numero não é menor que 100")
    except:
      print("Precisa digitar um número inteiro")