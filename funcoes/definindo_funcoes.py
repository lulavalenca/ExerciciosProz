"""
#Definindo Funções 

- funções sao pequenos trechos de codigos que realizam tarefas especificas:
- pode ou não receber entradas de dados e retornar uma saida de dados:
- Muito uteis para executar procedimentos similares por repetidas vezes:

OBS: se voce escrever uma função que realiza varias tarefas dentro dela:
é bom fazer uma verificação para que a função seja simplificada.


já utilizamos varias funções desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras:
"""

# Exemplo de utilização de funções

#cores = ['verde', 'Vermelho', 'Azul', 'Branco', 'Amarelo']

# Utilizando a função integrada (built-in) do Python print()

#print(cores)

#curso = 'Programação em Python: Essencial'

#print(curso)

#cores.append('Roxo')
#print(cores)

#curso.append('Mais dados...') # AtributeError
#print(curso)

#cores.clear()
#print(cores)

#print(help(print(curso)))

# DRY - Don't Repeat yourself - Não repita você mesmo / não repita seu código.

# Mas então, como definir funções?

"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:

nome_da_funcao -> Sempre, com letras minusculas, e se for nome composto, separado por underline (Snake Case);
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por virgula, podendo ser opcionais ou não;
bloco_função -> também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste blovo, pode ter ou não retorno da função.

OBS: veja que para definir uma função, utilizamos uma palavra reservada 'def' informando ao Python que estamos definindo uma função.
Também abrirmos o bloco de codigo com o já conhecido dois pontos : que é ultilizado para definir blocos.

"""

# Definindo a primeira função

# Definição
def diz_oi():
    print('oi')

"""
OBS: 

1 - Veja que, dentro das nossas funções podemo utilizar outras funções:
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que eka faz é dizer oi:
3 - veja que essa função não recebe nenhum parâmetro de entrada;
4 - veja que essa função não retorna nada;
"""        

# Utilizando função

# Chamada de execução
#diz_oi()

"""
ATENÇÃO:

Nunca esqueça de utilizar os parênteses ao executar uma função

Exemplo:

#Errado
diz_oi

# Certo
diz_oi()

# Errado
diz_oi ()

"""

# Exemplo 2 

def cantar_parabens():
    print('Parabens pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante')

#cantar_parabens()


#for n in range(5):
#    cantar_parabens()

# Em Python, Podemos inclusive criar variáveis do tipo de uma função e executar esta função atraves da variável 

canta = cantar_parabens

canta()







