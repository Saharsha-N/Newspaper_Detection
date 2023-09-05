import sklearn
import requests
from bs4 import BeautifulSoup
import numpy as np
from newspaper import Article
import nltk

# TODO Finish HTML Parser and provide input command
# Idea: parse metadata from articles for citation purposes

class Analysis(Article):
    def __init__(self, url) -> str:
        self.url = url
    
    def extract_text(self):
        """Extracts text from the URL"""
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, 'html.parser')

        data = ''
        for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            data += tag.get_text()
        return data

    def article_text(self, summ_length) -> str:
        article = Article(self.url)
        article.download()
        article.parse()
        article_data = article.text
        return article_data[:summ_length]

    def article_summary(self) -> str:
        article = Article(self.url)
        article.download()
        article.parse()
        article.nlp()
        return article.summary

    def get_metadata(self) -> str:
        print(f"")