import requests
from bs4 import BeautifulSoup

#
url = "https://rarbgaccessed.org/torrents.php?search={query}&page={page}"





def search(query):
    page = 1
    results = []

    r = requests.get(url.format(query=query, page=page))
    soup = BeautifulSoup(r.text, 'html.parser')
    torrents = soup.find_all('tbody')[0].find_all('tr')
    torrents.pop(0)

    for tr in torrents:
        entry = {}

        entry["title"]




# if title has xxx, pass
