import os
import requests
from bs4 import BeautifulSoup
import time


def retrieve_and_save_urls():
    links = []

    if not os.path.exists("data"):
        os.mkdir("data")

    for i in range(1, 50):
        url = 'http://books.toscrape.com/catalogue/page-' + str(i) + '.html'
        res = requests.get(url)
        if res.ok:
            soup = BeautifulSoup(res.text, 'lxml')
            h3s = soup.findAll('h3')
            for h3 in h3s:
                a = h3.find('a')
                link = a['href']
                links.append('http://books.toscrape.com/catalogue/' + link)
            time.sleep(0.1)

    with open('data/urls.txt', 'w') as books:
        for link in links:
            books.write(link + '\n')
