from bs4 import BeautifulSoup
import requests
import sys

city=sys.args[1]
url = 'https://postmates.com/los-angeles'
webpage = requests.get(url)
html = BeautifulSoup(webpage.text, 'html.parser')

soup=html.find_all("div",class_="css-pca8m e12wrbia0")
soup
result=set()
j=0
for i in soup:
  print(i.find("a")["href"])
  url = 'https://postmates.com/'+str(i.find("a")["href"])
  print(url)
  webpage = requests.get(url)
  html = BeautifulSoup(webpage.text, 'html.parser')
  soup=html.find_all('h3',class_="product-name css-1yjxguc e1tw3vxs4")
  if len(soup)>0:
    j+=1
  for i in soup:
      result.add(i.text)
  if j>9:
    break
print(result)

