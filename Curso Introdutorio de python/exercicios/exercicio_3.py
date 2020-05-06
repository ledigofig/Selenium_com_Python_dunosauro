#Exercicio 3
'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. informe ao usuario a quantidades de latas de tinta
serem comprada e preço total.
'''
print('_________________________________________________________________________')
print('Bem vindo usuario, então quer dizer que precisa pintar um determinado espaço\n\n')
nome = input('Informe seu nome para o cadastro\n')
entrada_metros_quadrados = input('Informe o tamanho da area em metros quadrados que deseja pintar\n')
litros_metros = (int(entrada_metros_quadrados)/3)
balde_de_tinta = 18
total = (litros_metros/balde_de_tinta)

print(f'Ola{nome} vocẽ deseja pintar {entrada_metros_quadrados} para essa metragem ')
print(f'serão utilizados {litros_metros} litros de tinta')
print(f'Total de balde de tinta é {total} com valor de R${(float(total)*80)}')
