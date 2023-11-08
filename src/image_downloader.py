import os
import requests


def download_image(image_url, category, book_title):
    img_dir = 'img/' + category
    os.makedirs(img_dir, exist_ok=True)
    file_extension = os.path.splitext(image_url)[1]
    img_filename = f'{img_dir}/{book_title}{file_extension}'

    response = requests.get(image_url)
    
    if response.ok:
        try:
            with open(img_filename, 'wb') as img_file:
                img_file.write(response.content)
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}. Skipping file and continuing.")
    else:
        print(f"Failed to download image from {image_url}.")
