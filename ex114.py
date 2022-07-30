import urllib
import urllib.request

try:
    site = input('Url do site: ')
    site = urllib.request.urlopen(site)
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read())