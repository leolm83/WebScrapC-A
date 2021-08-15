import requests
from bs4 import BeautifulSoup
endereco="https://www.cea.com.br/pantufa-infantil-ursinho-antiderrapante-bege-9976001-bege/p"
html = requests.get(endereco).content
soup = BeautifulSoup(html, 'html.parser')
classe="vtex-product-specifications-1-x-specificationValue vtex-product-specifications-1-x-specificationValue--first vtex-product-specifications-1-x-specificationValue--last"
cor=soup.find("span",class_=classe).string
print(cor)
