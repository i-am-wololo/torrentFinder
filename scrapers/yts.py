import requests
import json


# shenanigans to import file from parent folder
import sys
sys.path.append('../')
import utils

# luckily this one has a rest api
# it will be easier to scrape of this website
# yts can only be used for movies though

# torrent string  magnet:?xt=urn:btih:TORRENT_HASH&dn=Url+Encoded+Movie+Name&tr=http://track.one:1234/announce&tr=udp://track.two:80

torrent_string_template =  "magnet:?xt=urn:btih:{hash}&dn={movieurl}&tr=udp://open.demonii.com:1337/announce&tr=udp://tracker.openbittorrent.com:80&tr=udp://glotorrents.pw:6969/announce&tr=udp://tracker.coppersurfer.tk:6969"

url =  "https://yts.torrentbay.to/api/v2/list_movies.json?query_term={query}&sort=seeds" 



# if no quality format is told, its going to get all of them
def search(query, quality=None):
    request = requests.get(url.format(query=query))
    requestsDict = json.loads(request.text)
    if requestsDict['data']['movie_count'] == 0:
        return []
    movies = requestsDict['data']['movies']
    results = []

    for movie in movies:
        entry_template= {}

        entry_template['title'] = movie['title']
        entry_template['magnet'] = {}
        entry_template['source']  = 'yts'
        for torrents in movie['torrents']:
            if quality is not None and quality != torrents['quality']:
                continue
            entry = entry_template.copy()
            entry['title'] += ' [' + str(torrents['quality']) + ']'
            magnet = {}
            magnet['link'] = torrent_string_template.format(hash=torrents['hash'], movieurl=entry['title'].replace(" ", "+").replace(':', '+').replace('-', "+"))
            magnet['seed'] = torrents['seeds']
            magnet['quality'] = torrents['quality']
            entry["magnet"] = magnet
            results.append(entry) 
        

    return results
    
