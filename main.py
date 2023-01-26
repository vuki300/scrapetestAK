import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup

user_agent = {'User-agent': 'Mozilla/5.0'}
url = 'https://www.alka.co.rs/jbl.html'

def get_page_contents(url):
    page = requests.get(url, headers = user_agent)
    return BeautifulSoup(page.text, 'html.parser')

soup = get_page_contents(url)

#SCRAPE

products = []
for links in soup.find_all('h1', class_='naziv_proizvoda'):
     product = links.get_text().strip()
     products.append(product)
print(products)

pricesM = []
for links in soup.find_all('span', class_='cifra malaCena'):
    priceM = links.get_text().strip()
    pricesM.append(priceM)
print(pricesM)

pricesK = []
for links in soup.find_all('span', class_='cifra velikaCena'):
    priceK = links.get_text().strip()
    pricesK.append(priceK)
print(pricesK)

descs = []
for links in soup.find_all('span', class_='naslov'):
    desc = links.get_text().strip()
    descs.append(desc)
print(descs)


#Dict CSV?

list_dict = {'Product': products, 'PriceMP': pricesM, 'PriceVP': pricesK, 'Descrpiton': descs}
print(len(products), len(pricesM), len(pricesK), len(descs))

game = pd.DataFrame.from_dict(list_dict, orient='index')
games = game.transpose()
games.head(4)

games.to_csv('list.csv', index=False, header=True)
descs = pd.read_csv('list.csv', lineterminator='\n')
