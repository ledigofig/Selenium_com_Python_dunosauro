'''
Faça um programa para a leitura de duas notas parciais de alunos. O aluno deve
calcular a média alcançada por aluno e apresentar:
* A menssagem "Aprovado" se a média alcançada for maior igual a sete;
* A menssagem "Reprovado" se a media for menor do que sete;
* A menssagem "Aprovado com Distinção" se a media for igual a dez.
'''
nome = input("Informe o seu nome ? ")
nota1 = float(input("informe a sua primeira nota :\n"))
nota2 = float(input("informe a sua segunda nota :\n"))

#fazendo media
media = (nota1+nota2)/2

menssagem = f'Ola caro {nome} suas notas foram {nota1},{nota2} com essas notas você obteve a nota media {media} sendo assim você foi'

if media == 10.0:
    print(menssagem,'"Aprovado com Distinção"')
elif media >= 7.0:
    print(menssagem,'"Aprovado"')
else:
    print(menssagem,'"Reprovado"')
