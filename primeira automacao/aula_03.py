#immportação da url
from selenium.webdriver import Firefox
from time import sleep

#url para pesquisa
url = 'https://curso-python-selenium.netlify.app/aula_03.html'

#abrindo o navegador
navegador = Firefox()

#pesquisando na rede mundial de computadores
navegador.get(url)
sleep(6)




#pegando elemento
a = navegador.find_element_by_tag_name('a')
p = navegador.find_element_by_tag_name('p')


#Clicando 3 vezes
n = 1
for click in range(10):
    ps = navegador.find_elements_by_tag_name('p')
    a.click()
    print(f'Valor de {ps[-1].text}')
    print(f'Os valores são iguais {ps[-1].text == str(click)}')


#printando texro de a e de p
#print(f'texto de a: {a.text}')
#print(f'texto de p: {p.text}')

#Fechando o navegador
navegador.quit()
#parie em 55 minutos
