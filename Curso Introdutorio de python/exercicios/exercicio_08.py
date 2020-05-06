#"""faça um programa que receba uma data de nascimento (18/08/87) e imprima

##voce nasceu em <dia> de <mês> de <ano>
#"""


resposta = input('Qual sua data de nascimento? ')

dia, mes, ano = resposta.split('/')

print(f'você nascei em {dia} de {mes} de {ano}')
