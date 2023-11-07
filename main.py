from src.recover_urls import retrieve_and_save_urls
from src.book_scraper import process_book_url

if __name__ == '__main__':
    # Retrieve and save book URLs to 'data/urls.txt'
    retrieve_and_save_urls()

    with open('data/urls.txt', 'r') as books:
        for url in books:
            url = url.strip()
            process_book_url(url)
