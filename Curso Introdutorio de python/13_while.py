resposta = input('Vamos sair hoje [s/n]    ')

n=1

while resposta != 's':
    resposta = resposta = input(f'Vamo{"o"*n}s  [s/n]    ')
    n +=  1
    if 'chato' in resposta or 'chata' in resposta or 'para' in resposta:
        print('Entendi, não vou incomodar')
        break
else:
    print('Então vamos, lá pelas 20:00 passo na sua casa')
