import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup

user_agent = {'User-agent': 'Mozilla/5.0'}
url = 'https://www.alka.co.rs/monitori-najbolja-cena-led-tft-lcd.html'

def get_page_contents(url):
    page = requests.get(url, headers = user_agent)
    return BeautifulSoup(page.text, 'html.parser')

soup = get_page_contents(url)

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
