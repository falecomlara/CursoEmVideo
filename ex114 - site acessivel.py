# Crie um site para verificar se o site está possível.


import urllib.request
import urllib

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu erro no endereço do site')
else:
    print('Consegui acessar o site')
    print(site.read())
finally:
    print(f'Código {urllib.request.urlopen("http://www.pudim.com.br").getcode()}')


# Fonte: https://docs.python.org/pt-br/3/library/urllib.request.html#module-urllib.request

