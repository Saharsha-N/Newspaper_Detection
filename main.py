import sklearn
import requests
from bs4 import BeautifulSoup
import modules
import nltk

nltk.download('punkt')


# TODO Finish HTML Parser and provide input command
new_article = modules.Analysis('https://en.wikipedia.org/wiki/World_War_I')
print(f"Article Summary: {new_article.article_summary()}\n \nArticle Text: {new_article.article_text(500)}")