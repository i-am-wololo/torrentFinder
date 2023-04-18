import importlib
import tomli
# remove rarbg and torrent9 because not done yet

providers = ['nyaa', 'yts', '1337x']

'''
you usually dont need to make the search query url safe
Providers must be an array, even if it only has 1 element
'''


def search(query, quality=None, providers=providers):
    results = []
    for i in providers:
        print("executing:", i)
        provider = importlib.import_module('scrapers.'+i)
        results += provider.search(query, quality)
    
    return results




if __name__=="__main__":
    cli()
