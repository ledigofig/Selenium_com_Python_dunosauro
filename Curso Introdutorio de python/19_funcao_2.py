'''
def = define
definir nome(paramentro1, parametro2):
    return
'''
def soma(n1,n2):
    return n1+n2

def media(lista_de_numero):
    return sum(lista_de_numero)/len(lista_de_numero)

def imprime_relatorio (nome, cpf,telefone):
    return f'''
    relátorio parcial

    {nome}, portador do cpf {cpf}, o qual tem o numero de
    contato {telefone} encontra-se de feria no presente
    favor encaminhar todas a correspondencias ao setor de


    Assinado a direção

    '''

print(imprime_relatorio(
                        nome ='Leandro Diniz Gomes',
                        cpf= '123.123.123-45',
                        telefone='1234-5678'
                        )
        )
