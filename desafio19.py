from bs4 import BeautifulSoup
from urllib.request import urlopen
texto_html = urlopen('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')
bs = BeautifulSoup(texto_html.read(), 'html.parser')
print(bs.find_all(class_ = 'paywall'))
