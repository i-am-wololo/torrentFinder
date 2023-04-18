#!/usr/bin/python
import importlib
import tomli
import sys
# remove rarbg and torrent9 because not done yet

providers = ['nyaa', 'yts']

'''
you usually dont need to make the search query url safe
Providers must be an array, even if it only has 1 element
'''


def tui():
    if len(sys.argv) > 1:
        results = search(sys.argv[1])
 

def search(query, quality=None, providers=providers):
    results = []
    for i in providers:
        print("executing:", i)
        provider = importlib.import_module('scrapers.'+i)
        results += provider.search(query, quality)
    
    return results


def parse_results(results: list):
    pass

if __name__=="__main__":
    tui()
