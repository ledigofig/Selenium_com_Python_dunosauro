'''Exercicio 13
Faça um programa que: dada uma lista [1,2,3,4,5,6,7,8,9,10] e um numero inteiro
,imprima a tabuada desse numero.
'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_inteiro = int(input('Informe um numero inteiro por favor?'))

for numero in lista:
    #print(numero_inteiro,' x ',numero, ' = ',(numero_inteiro * numero))
    print(f'{numero_inteiro} x {numero} = {numero_inteiro * numero}')
