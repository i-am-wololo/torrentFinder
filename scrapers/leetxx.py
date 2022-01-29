import requests
from bs4 import BeautifulSoup


# shenanigans to import file from parent folder
import sys
sys.path.append('../')
import utils

url = "https://www.1337xx.to/category-search/{query}/{type}/{page}/"



def search(query, type):
    #type should either be Movies or TV
    page = 1
    results = []
    query = query.replace(' ', "%20") # Make query Url friendly

    r = requests.get(url.format(query=query, type=type, page=page))
    soup = BeautifulSoup(r.text, "html.parser")
    torrents_table = soup.find_all('table')[0].tbody
    
    print(utils.qualities)
    for tr in torrents_table.find_all('tr'):
    #for this website i have to get the torrent link on each torrent page individually


        #weird shenanigans to get the link
        link =  "https://www.1337xx.to/"+tr.find_all('td')[0].find_all('a')[1]['href']
        page = requests.get(link)
        parsed_page = BeautifulSoup(page.text, 'html.parser')
        magnet = parsed_page.find_all('a', "l3426749b3b895e9356348e295596e5f2634c98d8 la1038a02a9e0ee51f6e4be8730ec3edea40279a2 l0d669aa8b23687a65b2981747a14a1be1174ba2c")[0]['href']


        entry = {}
        
        entry["magnet"] = {}
        entry['magnet']['link'] = magnet
        entry['title'] = tr.find_all('td')[0].find_all('a')[1].string
        entry['magnet']['seeds'] = tr.find_all('td')[1].string
        entry['magnet']['quality'] = utils.guess_quality(entry['title'])
        entry['source'] = "1337xx"
        results.append(entry) 
       
        

    return results
        # entry['title']
