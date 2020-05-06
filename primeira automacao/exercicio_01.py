'''
Crie um programa com selenium que

* Gere um dicionario, onde a chave é a tag h1
    * O valor deve ser um novo dicionario.
    * cada chave  do valor deve ser o valor do 'atributo'.
    * Cada valor deve ser o texto contido no elemento


'''
from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'


navegador = Firefox()

navegador.get(url)
sleep(6)


pega_h1 = navegador.find_element_by_tag_name('h1')
print(pega_h1.text)
