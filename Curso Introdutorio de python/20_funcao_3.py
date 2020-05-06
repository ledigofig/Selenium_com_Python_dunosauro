
def nome(argumento_posicional, *pacote_de_argumentos):
    print(argumento_posicional, pacote_de_argumentos)

def nome2(argumento_nomeado = 'Não tem nada',
            **pacote_nomeado):
    print(argumento_nomeado, pacote_nomeado)

'''
eandro]@[01;34mCurso Introdutorio de python $python -i 20_funcao_3.py
>>> nome('Python', 1, 2, 3, 4, 5, 6)
Python (1, 2, 3, 4, 5, 6)
>>>
eandro]@[01;34mCurso Introdutorio de python $python -i 20_funcao_3.py
>>> nome2()
Não tem nada {}
>>> nome2('a')
a {}
>>> nome2(letra='a')
Não tem nada {'letra': 'a'}
'''
