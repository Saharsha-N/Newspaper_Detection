import sklearn
import requests
from bs4 import BeautifulSoup
import modules

# TODO Finish HTML Parser and provide input command
new_article = modules.Analysis('https://en.wikipedia.org/wiki/World_War_I')
print(new_article.article_text)