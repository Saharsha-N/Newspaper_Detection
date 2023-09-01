import sklearn
import requests
from bs4 import BeautifulSoup
import numpy as np
from newspaper import Article


# TODO Finish HTML Parser and provide input command
# Idea: parse metadata from articles for citation purposes

class Analysis(Article, requests):
    def __init__(self, url) -> str:
        self.url = url
        article = Article(url)
    
    def extract_text(url):
        """Extracts text from the URL"""
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        data = ''
        for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            data += tag.get_text()
        return data

    def article_text(article) -> str:
        article.parse()
        article_data = article.text
        return article_data[:216]

    def article_summary(article) -> str:
        article.nlp()
        return article.summary()

    def get_metadata(article_data) -> str:
        print()