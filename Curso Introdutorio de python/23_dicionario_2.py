'''Dicionarios
x['Maria']
acessa pelo atributo

x.keys()
pega todas as chaves

x.values()
pega todos os valores

x['Maria'] == 10

x.popitem()
tira um item qualquer do Dicionario sem saber qual é

x.setdefault('Carlos')
defini um valor padrão
'''
def imprime_relatorio (nome, cpf,telefone):
    return f'''
    relátorio parcial

    {pessoa['nome']}, portador do cpf {pessoa['cpf']}, o qual tem o numero de
    contato {pessoa['telefone']} encontra-se de feria no presente
    favor encaminhar todas a correspondencias ao setor de


    Assinado a direção

    '''

print(imprime_relatorio(
                        nome ='Leandro Diniz Gomes',
                        cpf= '123.123.123-45',
                        telefone='1234-5678'
                        )
        )
