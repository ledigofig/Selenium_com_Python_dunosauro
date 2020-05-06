#lista é definida poor []

minha_lista_compras = ['sabão', 'sabonete', 'arroz', 'moster',10,[1,2,3] ]

#minha_lista_compras

for item in minha_lista_compras:
    print(item)
'''
[leandro]@[Curso Introdutorio de python]python -i 16_listas.py
>>> minha_lista_compras[0]
'sabão'
>>> minha_lista_compras[1]
'sabonete'
>>> minha_lista_compras[2]
'arroz'
>>> minha_lista_compras[3]
'moster'
>>>
-------------------------------
#pegando por posição

[leandro]@[Curso Introdutorio de python]python -i 16_listas.py
sabão
sabonete
arroz
moster
10
[1, 2, 3]
>>> minha_lista_compras[-1]
[1, 2, 3]
>>> minha_lista_compras[-1][-1]
3
>>> minha_lista_compras[-1][0]
1
----------------------------------------
slice - listas
[leandro]@[Curso Introdutorio de python]python -i 16_listas.py
sabão
sabonete
arroz
moster
10
[1, 2, 3]
>>> minha_lista_compras[-1]
[1, 2, 3]
>>> minha_lista_compras[-1][-1]
3
>>> minha_lista_compras[-1][0]
1

>>> nomes = ['Eduardo','leandro','Rosangela','Theo','Mariaclara']
>>> nomes[-1]
'Mariaclara'
>>> nomes[0:-1]
['Eduardo', 'leandro', 'Rosangela', 'Theo']
>>> nomes[0:-2]
['Eduardo', 'leandro', 'Rosangela']
>>> nomes[0:2]
['Eduardo', 'leandro']
>>> nomes::2]
  File "<stdin>", line 1
    nomes::2]
          ^
SyntaxError: invalid syntax
>>> nomes[::2]
['Eduardo', 'Rosangela', 'Mariaclara']
>>> 'Leandro' [::-1]
'ordnaeL'
----------------
Comandos
x.append()
inseri na ultima posição
x.remove()
remove
x.insert()
inseri na posição desejada
x.pop()
*tira um valor
x.count()
counta um valor
x.reverse()
mostra a lista de traz para frente
'''
