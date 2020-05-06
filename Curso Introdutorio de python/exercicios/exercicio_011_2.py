"""Exercicio 11
Faça um programa que itera em uma string e toda vez que uma vogal aparece
na sua string o seu nome entre as letras
string = bananas
b
Leandro
n
Leandro
n
Leandro
"""
palavra = 'abracadabra'
vogais = 'aeiou'
for letra in palavra:
    if letra in vogais:
        print('Ola mundo')
    else:
        print(letra)
