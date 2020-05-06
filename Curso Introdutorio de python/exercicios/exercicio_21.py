
def quadrado (entrada):
    lista_resposta = []
    for numero in entrada:
        lista_resposta.append(numero ** 2)

    return lista_resposta

def cubo (entrada):
    lista_resposta = []
    for numero in entrada:
        lista_resposta.append(numero ** 3)
        
    return lista_resposta


entrada = []

for valor in range(10):
    entrada.append(
        int(input('Favor informar um numero '))
    )

dicionario = {
    'lista padrao': entrada,
    'Lista quadrada': quadrado(entrada),
    'lista cubica': cubo(entrada)
}

print(dicionario)
