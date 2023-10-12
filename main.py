import requests
from bs4 import BeautifulSoup
import time


def clean_text(text):
    return text.strip().encode('utf-8').decode('ascii', 'ignore')


with open('data/urls.txt', 'r') as books:
    with open('data/books.csv', 'w') as output:
        output.write('Book Title,Price (excl. tax),Price (incl. tax),Tax,Availability,Currency\n')
        for url in books:
            url = url.strip()
            response = requests.get(url)
            if response.ok:
                soup = BeautifulSoup(response.text, 'lxml')
                title = clean_text(soup.find('div', {'class': 'product_main'}).h1.text)
                price = clean_text(soup.find('p', {'class': 'price_color'}).text)
                tax_info = soup.find_all('tr')

                for row in tax_info:
                    th = row.find('th')
                    td = row.find('td')
                    if th and td:
                        if 'Price (excl. tax)' in th.text:
                            price_excl_tax = clean_text(td.text)
                        elif 'Price (incl. tax)' in th.text:
                            price_incl_tax = clean_text(td.text)
                        elif 'Tax' in th.text:
                            tax = clean_text(td.text)
                        elif 'Availability' in th.text:
                            availability = clean_text(td.text)

                print('Book title: ' + title)
                print('Price (excl. tax): ' + price_excl_tax)
                print('Price (incl. tax): ' + price_incl_tax)
                print('Tax: ' + tax)
                print('Availability: ' + availability)

                output.write(f'"{title}",{price_excl_tax},{price_incl_tax},{tax},{availability},Pounds: £\n')
            time.sleep(1)
