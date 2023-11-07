import re
import requests
from bs4 import BeautifulSoup
import time
from src.csv_manager import create_category_csv, book_data_exists_in_csv, append_book_data_to_csv
from src.image_downloader import download_image
import os


def clean_text(text):
    return text.strip().encode('utf-8').decode('ascii', 'ignore')


def extract_star_rating(star_rating_element):
    star_rating_class = star_rating_element['class'][1]
    rating = star_rating_class.lower()

    if rating == 'one':
        return 1
    elif rating == 'two':
        return 2
    elif rating == 'three':
        return 3
    elif rating == 'four':
        return 4
    elif rating == 'five':
        return 5
    else:
        return None


def extract_category(soup):
    category_tags = soup.select('ul.breadcrumb li')
    if len(category_tags) > 2:
        return clean_text(category_tags[2].a.text)
    return None


def get_book_data(soup):
    title = clean_text(soup.find('div', {'class': 'product_main'}).h1.text)
    tax_info = soup.find_all('tr')
    star_rating_element = soup.find('p', {'class': 'star-rating'})
    star_rating = extract_star_rating(star_rating_element)
    category = extract_category(soup)

    price_excl_tax, price_incl_tax, tax, availability_number = None, None, None, None

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
                availability_text = td.text
                availability_number = int(re.search(r'\d+', availability_text).group())

    return category, title, price_excl_tax, price_incl_tax, tax, availability_number, star_rating


def process_book_url(url):
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        category, title, price_excl_tax, price_incl_tax, tax, availability_number, star_rating = get_book_data(soup)
        book_title = clean_text(title)
        photo_url = 'http://books.toscrape.com/' + soup.find('div', {'class': 'thumbnail'}).img['src']

        filename = f'data/{category}.csv'

        if not os.path.exists(filename):
            create_category_csv(category)

        if not book_data_exists_in_csv(filename, category, book_title):
            append_book_data_to_csv(filename, category, book_title, price_excl_tax, price_incl_tax, tax,
                                    availability_number, star_rating, photo_url)

        download_image(photo_url, category, book_title)

        print_book_data(category, book_title, price_excl_tax, price_incl_tax, tax, availability_number, star_rating,
                        photo_url)

    time.sleep(0.3)


def print_book_data(category, title, price_excl_tax, price_incl_tax, tax, availability_number, star_rating, photo_url):
    print('Category: ' + category)
    print('Book title: ' + title)
    print('Price (excl. tax): ' + price_excl_tax)
    print('Price (incl. tax): ' + price_incl_tax)
    print('Tax: ' + tax)
    print('Availability: ' + str(availability_number))
    print('Star Rating: ' + str(star_rating))
    print('Photo URL: ' + photo_url)
