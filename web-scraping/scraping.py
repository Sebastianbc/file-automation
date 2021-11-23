# install requests library and import it
import requests
# instal beautifulsoup4 and lxml libraries and use it
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

print(soup)