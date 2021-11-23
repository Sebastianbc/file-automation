# install requests library and import it
import requests
# instal beautifulsoup4 and lxml libraries and use it
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

# Get just the text quote, with its author and its corresponding tags, then print them.
# Getting all span text classes with their html tags
quotes = soup.find_all('span', class_='text')
# Get the quote's author
authors = soup.find_all('small', class_='author')
# Get the tags related the quotes
tags = soup.find_all('div', class_='tags')
print(tags)
# Get just the span tag text
for i in range(0, len(quotes)):
    print(quotes[i].text, 'by', authors[i].text, tags[i].text)
    
#print(quotes)