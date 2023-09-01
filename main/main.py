import sklearn
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/World_War_I"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = ''
for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
    data += tag.get_text()

print(data)