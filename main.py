import importlib


# remove rarbg and torrent9 because not done yet



providers = ['leetxx', 'nyaa', 'yts']

'''
you usually dont need to make the search query url safe
Providers must be an array, even if it only has 1 element
'''
def search(query, providers=providers):
    results = []
    for i in providers:
        provider = importlib.import_module('scrapers.'+i)
        results += provider.search(query)
    
    return results
