def sao_anagramas(palavra1, palavra2):
    if len(palavra1) != len(palavra2):
        return False
    
    contador = [0] * 26  # Lista para contar as ocorrências de cada letra
    ord_a = ord('a')  # Valor ASCII da letra 'a'

    for letra in palavra1:
        contador[ord(letra) - ord_a] += 1

    for letra in palavra2:
        contador[ord(letra) - ord_a] -= 1
        if contador[ord(letra) - ord_a] < 0:
            return False
    
    return True

# Exemplos de palavras
palavra1 = "listen"
palavra2 = "silent"
palavra3 = "hello"
palavra4 = "world"

# Chamando a função e exibindo os resultados
print(f"{palavra1} e {palavra2} são anagramas:", sao_anagramas(palavra1, palavra2))
print(f"{palavra1} e {palavra3} são anagramas:", sao_anagramas(palavra1, palavra3))
print(f"{palavra1} e {palavra4} são anagramas:", sao_anagramas(palavra1, palavra4))

"""
Neste exemplo, a função sao_anagramas utiliza um contador para contar as ocorrências de cada letra nas palavras. 
Ela percorre ambas as palavras, incrementando o contador para cada letra na primeira palavra e decrementando para cada letra na segunda palavra. 
Se as palavras forem anagramas, os contadores para todas as letras devem ser iguais no final.
Teste a função com diferentes pares de palavras para verificar se ela está identificando corretamente os anagramas.


"""