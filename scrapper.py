from bs4 import BeautifulSoup
import requests
import lxml
from numpy import savetxt
import csv
import codecs


URL = 'https://www.webstore.com/product-sitemap.xml'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'lxml')
addresses = soup.find_all('loc')

urls = []

for address in addresses:
    urls.append(address.get_text())

prices = []

for i in range(len(urls)):
    try:
        current_url = urls[i]
        print(current_url)
        scrapper_page = requests.get(current_url)

        scrapper = BeautifulSoup(scrapper_page.content, 'html.parser')
        
        title = scrapper.find('h1', class_='product_title').text
        print(title)
        try:
            price = scrapper.find('ins').find('span', class_='woocommerce-Price-amount').text
        except:
            print('Price not found - 1')
            try:
                price = scrapper.find('p').find('span', class_='woocommerce-Price-amount').text
            except:
                print('Price not found. - 2')
        prices.append([title, price])
    except:
        print('elo')
with codecs.open('data.csv', "w", encoding='utf-16') as file:
    writer = csv.writer(file)
    writer.writerow(['Nazwa', 'Cena'])
    for line in prices:
        writer.writerow(line)







