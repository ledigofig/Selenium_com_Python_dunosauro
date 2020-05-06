#pedir o preço de tres produtos e escolher o menor preçoptimize

preço_1 = float(input("Informe o preço do primeiro produto\n"))
preço_2 = float(input("Informe o preço do segundo produto\n"))
preço_3 = float(input("Informe o preço do terceiro produto\n"))

if preço_1 > preço_2 and preço_2 > preço_3:
    print('Compre o terceiro produto')
elif preço_1 > preço_2 and preço_2 < preço_3:
    print('Compre o segundo produto')
else:
    print('Compre o primeiro produto')
