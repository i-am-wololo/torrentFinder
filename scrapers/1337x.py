import requests
from bs4 import BeautifulSoup


# shenanigans to import file from parent folder
import sys
sys.path.append('../')
import utils


url = "https://www.1337x.to/category-search/{query}/{type}/{page}/"
url_none = "https://www.1337x.to/search/{query}/{page}/"


def search(query, type=None):
    # type should either be Movies or TV
    page = 1
    results = []
    query = query.replace(' ', "%20")   # Make query Url friendly

    # if type is not mentionned
    if type is None:
        r = requests.get(url_none.format(query=query, page=page))
    else:
        r = requests.get(url.format(query=query, type=type, page=page))


    soup = BeautifulSoup(r.text, "html.parser")
    torrents_table = soup.find_all('table')[0].tbody

    for tr in torrents_table.find_all('tr'):
    # for this website i have to get the torrent link on each torrent page individually


        #weird shenanigans to get the link
        link =  "https://www.1337xxx.to"+tr.find_all('td')[0].find_all('a')[1]['href']
        page = requests.get(link)
        print(link)
        parsed_page = BeautifulSoup(page.text, 'html.parser')
        magnet = parsed_page.find_all('a', string="Magnet Download")[0]['href']


        entry = {}
        
        entry["magnet"] = {}
        entry['magnet']['link'] = magnet
        entry['title'] = tr.find_all('td')[0].find_all('a')[1].string
        entry['magnet']['seeds'] = int(tr.find_all('td')[1].string)
        entry['magnet']['quality'] = utils.guess_quality(entry['title'])
        entry['source'] = "1337xxx"
        results.append(entry) 
    return results
    # entry['title']
