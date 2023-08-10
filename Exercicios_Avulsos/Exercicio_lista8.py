def sao_anagramas(palavra1, palavra2):
    return sorted(palavra1) == sorted(palavra2)

# Exemplos de palavras
palavra1 = "pular"
palavra2 = "plural"
palavra3 = "ola"
palavra4 = "mundo"

# Chamando a função e exibindo os resultados
print(f"{palavra1} e {palavra2} são anagramas:", sao_anagramas(palavra1, palavra2))
print(f"{palavra1} e {palavra3} são anagramas:", sao_anagramas(palavra1, palavra3))
print(f"{palavra1} e {palavra4} são anagramas:", sao_anagramas(palavra1, palavra4))

"""
Neste exemplo, a função sao_anagramas recebe duas palavras como argumentos e verifica se as palavras são anagramas, ou seja, 
se as letras de uma podem ser reorganizadas para formar a outra. 
Para fazer essa verificação, a função converte as palavras em listas de caracteres usando a função sorted() e, 
em seguida, compara se as listas são idênticas.

"""