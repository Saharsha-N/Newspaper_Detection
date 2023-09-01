import sklearn
import requests
from bs4 import BeautifulSoup
import numpy as np
from bs4 import BeautifulSoup
from newspaper import Article


# TODO Finish HTML Parser and provide input command
# Idea: parse metadata from articles for citation purposes

def extract_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    data = ''
    for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        data += tag.get_text()
    return data

def article_text(url):
    article = Article(url)
    article.parse()
    article_data = article.text
    return article, article_data

def get_metadata(article_data):
    print()

