
# Projet_02_OCR

Utilisez les bases de Python pour l'analyse de marché

# Web Scraping Books from "books.toscrape.com"

## Description

This project consists of two Python scripts for web scraping book information from the website "books.toscrape.com." 
The main script, `main.py`, scrapes book details and stores them in a CSV file. 
The second script, `recover_urls.py`, is used to generate a list of book URLs for scraping.

## Requirements
You need to have python 3.9 installed on your computer : [https://www.python.org/downloads/](https://www.python.org/downloads/release/python-3918/)

Then clone the repository 
```
git clone https://github.com/Razvan-drb/Projet_02_OCR.git
```

Run 
```
python3 -m venv .venv
```
to install the virtual environment
and then
```
source .venv/bin/activate
```


Before running the scripts, make sure you have the necessary Python packages installed. 
You can install them using the following command:

```
pip install -r requirements.txt
```

## Usage

1. Clone or download the project repository to your local machine.

2. Install the required Python packages as mentioned in the "Requirements" section.

3. Execute the `recover_urls.py` script to generate a list of book URLs. This will create a file named `urls.txt` 
4. in the "data" directory.

```
python recover_urls.py
```

4. After generating the list of URLs, you can run the `main.py` script to scrape book data. 
5. It will use the URLs from `data/urls.txt` and store the scraped data in `data/books.csv`.

```
python3 main.py
```

5. The scraped data will be saved in a file named `books.csv` in the "data" directory.

## Structure

The project structure is as follows:

- `main.py`: The main Python script for scraping book data.
- `recover_urls.py`: A Python script for generating book URLs to scrape.
- `requirements.txt`: A list of required Python packages and their versions.
- `README.md`: This file providing project information.
- `data/urls.txt`: A file containing the URLs of books to scrape.
- `data/books.csv`: The output file where the scraped data is stored.


## Author

[Razvan DARABAN]

## Acknowledgments


Feel free to modify and expand this `README.md` to include any additional information, acknowledgments, or 
specific usage instructions relevant to your project.
