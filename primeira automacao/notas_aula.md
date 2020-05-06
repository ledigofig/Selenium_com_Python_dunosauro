Visão da arquitetura pelo selenium

  codigo
  from selenium.webdriver import firefox
  browser = firefox()

Parentese chama\executa
no caso acima o browser é chamado.


Instalando ambiente virtual e selenium

Instalando ambiente vitual
    (base) leandro@leandro-Inspiron-7460:~/Documentos/python/Selenium com Python/primeira automacao$ python -m venv venv

    Ativando ambiente virtual
    (base) leandro@leandro-Inspiron-7460:~/Documentos/python/Selenium com Python/primeira automacao$ source venv/bin/activate

    Instalando Selenium
    (venv) (base) leandro@leandro-Inspiron-7460:~/Documentos/python/Selenium com Python/primeira automacao$ pip install selenium
    Collecting selenium
      Downloading https://files.pythonhosted.org/packages/80/d6/4294f0b4bce4de0abf13e17190289f9d0613b0a44e5dd6a7f5ca98459853/selenium-3.141.0-py2.py3-none-any.whl (904kB)
         |████████████████████████████████| 911kB 210kB/s
    Collecting urllib3 (from selenium)
      Downloading https://files.pythonhosted.org/packages/e1/e5/df302e8017440f111c11cc41a6b432838672f5a70aa29227bf58149dc72f/urllib3-1.25.9-py2.py3-none-any.whl (126kB)
         |████████████████████████████████| 133kB 222kB/s
    Installing collected packages: urllib3, selenium
    Successfully installed selenium-3.141.0 urllib3-1.25.9
    WARNING: You are using pip version 19.2.3, however version 20.1 is available.
    (venv) (base) leandro@leandro-Inspiron-7460:~/Documentos/python/Selenium com Python/primeira automacao$


Verificando se ambiente virtual foi instalado
  * primeiro tem que estar no ambiente virtual
    source venv/bin/activate

  * Execulta o comando abaixo 
        rimeira automacao$ python -m
      selenium
      /home/leandro/Documentos/python/Selenium com Python/primeira automacao/venv/bin/python:
      No module named selenium.__main__; 'selenium' is a package and cannot be directly executed
      Observação
