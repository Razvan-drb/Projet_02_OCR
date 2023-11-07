import os
import csv


def create_category_csv(category):
    filename = f'data/{category}.csv'
    with open(filename, 'w') as output:
        output.write('Category,Book Title,Price (excl. tax),Price (incl. tax),Tax,Availability,'
                     'Star Rating,Currency,Photo URL\n')
    return filename


def book_data_exists_in_csv(filename, category, title):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader, [])  # Skip the header
        for row in reader:
            if row[:2] == [category, title]:
                return True
    return False


def append_book_data_to_csv(filename, category, title, price_excl_tax, price_incl_tax, tax, availability_number,
                            star_rating, photo_url):
    with open(filename, 'a', newline='') as output:
        writer = csv.writer(output)
        if os.stat(filename).st_size == 0:
            writer.writerow(['Category', 'Book Title', 'Price (excl. tax)', 'Price (incl. tax)', 'Tax', 'Availability',
                             'Star Rating', 'Currency', 'Photo URL'])
        writer.writerow([category, title, price_excl_tax, price_incl_tax, tax, availability_number, star_rating,
                         'Pounds: £', photo_url])
