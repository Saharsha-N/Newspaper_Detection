import string
import requests
import pandas
from bs4 import BeautifulSoup
from newspaper import Article
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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

    def lemmat(self, summ_length) -> str:
        article = Article(self.url)
        article.download()
        article.parse()
        output = []
        lemm = WordNetLemmatizer()
        # Remove punctuation
        raw_text = article.text[:summ_length].translate(str.maketrans("", "", string.punctuation))
        # Tokenize the words
        tokens = word_tokenize(raw_text)
        for word in tokens:
            output.append((lemm.lemmatize(word, pos='v')))
        return output

    # def get_metadata(self) -> str:
    #     print(f"")

