from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen('https://www.nytimes.com/')
bs = BeautifulSoup(html.read(), 'html.parser')
#print(bs.prettify())
lista_noticias = []
#print(bs.find_all('h2'))
#lista_noticias.extend(bs.find_all('h3'))

for x in bs.find_all('h3'):
    #print(type(x.string))
    if x.string != None and len(x.string.split(" ")) > 1 and not(x['class'][0].startswith('svelte')):
        #print(x['class'])
        #a = text.split(' ')[-1]
        lista_noticias.append(x.string)
#print("Another Christmas of Distress in America’s I.C.U.s" in lista_noticias)
print('toda as noticias do The NY Times:')
print('\n'.join(lista_noticias))
'''
    .prettify() organiza para uma melhor visualização a sintaxe do html
'''
