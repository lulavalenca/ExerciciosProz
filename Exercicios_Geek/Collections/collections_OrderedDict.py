"""
collections.OrderedDict em Python: Uma Visão Geral

O OrderedDict é uma subclasse do tipo dict que mantém a ordem de inserção dos itens. Ao contrário de um dicionário padrão, que não garante a ordem dos elementos, o OrderedDict lembra a ordem em que os elementos foram originalmente inseridos.

Importando OrderedDict:

python
Copy code
from collections import OrderedDict
Criando um OrderedDict:

python
Copy code
ord_dict = OrderedDict()
Adicionando Itens:

python
Copy code
ord_dict['um'] = 1
ord_dict['dois'] = 2
ord_dict['três'] = 3
Ordem de Iteração:

python
Copy code
for chave, valor in ord_dict.items():
    print(chave, valor)
# Saída: um 1
#        dois 2
#        três 3
Métodos Úteis:

move_to_end(key, last=True): Move a chave para o último lugar (ou primeiro se last for False).
popitem(last=True): Remove e retorna um par chave-valor (último por padrão).
reverse(): Inverte a ordem dos itens.
Exemplo Prático: Registro de Ações:

python
Copy code
registro = OrderedDict()

registro['login'] = 'usuário1'
registro['logout'] = 'usuário2'
registro['download'] = 'usuário1'
registro['upload'] = 'usuário3'

for acao, usuario in registro.items():
    print(f'{usuario} realizou a ação: {acao}')
# Saída:
# usuário1 realizou a ação: login
# usuário2 realizou a ação: logout
# usuário1 realizou a ação: download
# usuário3 realizou a ação: upload
Considerações Adicionais:

OrderedDict é útil quando a ordem dos itens é importante.
Pode ser utilizado em situações onde a ordem de inserção precisa ser mantida.
Introduzido no Python 3.1 e disponível no Python 2.7.

"""

