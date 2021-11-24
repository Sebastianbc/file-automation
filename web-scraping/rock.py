# This program will write in a file the 66 best hard rock songs of the 21st century from a loudwire's blog

import requests
from bs4 import BeautifulSoup

# The hard rock list is below a Twitch streamer interview with Mike Shinoda
url = 'https://www.loudersound.com/features/the-100-greatest-rock-songs-of-the-century-so-far'

# get the HTML content from url
response = requests.get(url)

# Get the HTML response formatted
soup = BeautifulSoup(response.text, 'lxml')

# There is one major HTML element (div) which holds the hard rock songs list
rock_songs = soup.find_all('h2')

# iterate through the h2 tags list and get the text
for song in rock_songs:
    print(song.text)

# Get the pagination
pagination = soup.find('div', class_='box article pagination internal current-prev-next navigation-sequential')
anchor_list = pagination.find_all('a', class_='pagination-numerical-list-item-link')

# Once the pagination is done, just request the url for every href value and search for the h2 elements as done firstly
for i in anchor_list:
    url = i.get('href')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    rock_songs = soup.find_all('h2')
    for song in rock_songs:
        print(song.text)
