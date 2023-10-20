import re
import requests
from bs4 import BeautifulSoup
import time


def clean_text(text):
    """
    Clean and format text by stripping, encoding to utf-8, and decoding to ascii.
    """
    return text.strip().encode('utf-8').decode('ascii', 'ignore')


def extract_star_rating(star_rating_element):
    """
    Extract and return the star rating from the star rating element.
    """
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
    """
    Extract and return the category of the book from the provided soup object.
    """
    category_tags = soup.select('ul.breadcrumb li')
    if len(category_tags) > 2:
        return clean_text(category_tags[2].a.text)
    return None


def get_book_data(soup):
    """
    Extract book data from the BeautifulSoup object.
    """
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


def print_book_data(category, title, price_excl_tax, price_incl_tax, tax, availability_number, star_rating):
    """
    Print book data to the console.
    """
    print('Category: ' + category)
    print('Book title: ' + title)
    print('Price (excl. tax): ' + price_excl_tax)
    print('Price (incl. tax): ' + price_incl_tax)
    print('Tax: ' + tax)
    print('Availability: ' + str(availability_number))
    print('Star Rating: ' + str(star_rating))


def process_book_url(url, output):
    """
    Process a book URL, extract data, and write it to the output CSV file.
    """
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        category, title, price_excl_tax, price_incl_tax, tax, availability_number, star_rating = get_book_data(soup)

        print_book_data(category, title, price_excl_tax, price_incl_tax, tax, availability_number, star_rating)

        output.write(f'"{category}","{title}",{price_excl_tax},{price_incl_tax},{tax},{availability_number},'
                     f'{star_rating},Pounds: £\n')
    time.sleep(1)


if __name__ == '__main__':
    with open('data/urls.txt', 'r') as books:
        with open('data/books.csv', 'w') as output:
            output.write('Category,Book Title,Price (excl. tax),Price (incl. tax),Tax,Availability,Star '
                         'Rating,Currency\n')
            for url in books:
                url = url.strip()
                process_book_url(url, output)
