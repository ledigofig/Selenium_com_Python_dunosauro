lista_de_compras = []
resposta = ''

while resposta != 'Acabou':
    resposta = input('O que temos que comprar? ')
    lista_de_compras.append(resposta)

print(lista_de_compras)

'''
[leandro]@[Curso Introdutorio de python]python -i
Python 3.8.2 (default, Apr 30 2020, 14:54:47)
[GCC 9.2.1 20191008] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> l.append(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'l' is not defined
>>> l = []
>>> l.append(0)
>>> l

[0]
>>> l.append(12)
>>> l
[0, 12]
>>> l.append(100)
>>> l.append(5)
>>> l
[0, 12, 100, 5]
>>> l.pop()
5
>>> l.pop(12)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop index out of range
>>> l.reverse()
>>> l
[100, 12, 0]
>>> l.insert(1.2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: insert expected 2 arguments, got 1
>>> l.insert(1,2)
>>> l
[100, 2, 12, 0]
>>> x.count()
Traceback (most recent call last)
>> l.count(2)
1
>
'''
