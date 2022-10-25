from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=Teste'

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
print(soup)