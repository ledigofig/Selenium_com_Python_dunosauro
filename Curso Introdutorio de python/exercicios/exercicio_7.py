"""
Faça um programa que receba uma string e responda se ela tem alguma vogal,
se sim quais são as vogais
E tambem diga se ela é uma frase ou não.
"""
frase = input('Diga-nos o que deseja ')
#frase =frase.split('')
vogais  = ('a', 'e', 'i', 'o', 'u')
conjunto_vogais_frase = ''
for palavra in frase:
    for vogal in vogais :
        if vogal == palavra :
             conjunto_vogais_frase= conjunto_vogais_frase + palavra
else:
    print() 


print(f'O usuario informou a seguinte {frase} e nessa string informada a os seguintes caracteres do tipo vogal {conjunto_vogais_frase}')
