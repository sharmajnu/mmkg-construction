import os
from typing import List
import requests
from bs4 import BeautifulSoup
from typings import Article, Image

import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    try:
        # Make a request to the article URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract article text content
        text_content = ""
        article_text_elements = soup.find_all('p')  # Adjust this based on HTML structure
        for element in article_text_elements:
            text_content += element.get_text() + "\n"

        # Extract images
        images = []
        image_elements = soup.find_all('img')  # Adjust this based on HTML structure
        for img in image_elements:
            image_src = img.get('src')
            images.append({'src': image_src})

        return {'textContent': text_content, 'images': images}

    except requests.exceptions.RequestException as e:
        print(f"Error fetching article from {url}: {e}")
        return None
    except Exception as e:
        print(f"Error parsing article content: {e}")
        return None


def save_images_on_local_folder(images: List[Image]):
    for image in images:
        response = requests.get(image.imageUrl)
        response.raise_for_status() # Raise an error for bad response
        
        image_name = os.path.basename(image.imageUrl)

        with open('article/images/' + image_name, 'wb') as f:
            f.write(response.content)
