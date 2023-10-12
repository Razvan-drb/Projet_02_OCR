import requests
from bs4 import BeautifulSoup
import time

'''
links = []

for i in range(1, 3):
    url = 'http://books.toscrape.com/catalogue/page-' + str(i) + '.html'
    res = requests.get(url)
    if res.ok:

        soup = BeautifulSoup(res.text, 'lxml')
        h3s = soup.findAll('h3')
        for h3 in h3s:
            a = h3.find('a')
            link = a['href']
            links.append('http://books.toscrape.com/' + link)
        time.sleep(1)
print(links)

with open('urls.txt', 'w') as books:
    for link in links:
        books.write(link + '\n')
'''

with open('urls.txt', 'r') as books:
    with open('books.csv', 'w') as output:
        output.write('books, prices\n')
        for row in books:
            url = row.strip()
            response = requests.get(url)
            if response.ok:
                soup = BeautifulSoup(response.text, 'lxml')
                title = soup.find('div', {'class': 'product_main'}).h1
                price = soup.find('p', {'class': 'price_color'})
                print('Book title: ' + title.text.strip())
                print('Book price: ' + price.text.strip())
                output.write(title.text.strip() + ' , ' + price.text.strip() + '\n')
            time.sleep(2)



'''
with open('urls.txt', 'r') as books:
    for row in books:
        url = row.strip()
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'lxml')
            title = soup.find('div', {'class': 'product_main'}).h1
            price = soup.find('p', {'class': 'price_color'})
            print('Book title:', title.text.strip().encode('utf-8').decode('ascii', 'ignore'))
            print('Book price:', price.text.strip().encode('utf-8').decode('ascii', 'ignore'))
'''

