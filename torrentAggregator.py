#!/usr/bin/python
import importlib
import tomli
import sys
import utils
import subprocess
from simple_term_menu import TerminalMenu
# remove rarbg and torrent9 because not done yet


'''
you usually dont need to make the search query url safe
Providers must be an array, even if it only has 1 element
'''

# Loading config
with open('./config.toml', 'rb') as f:
    config = tomli.load(f)

if config["quality"] not in utils.qualities:
    quality = None
else:
    quality = config["quality"]

providers = config["providers"]


def tui():
    if len(sys.argv) > 1:
        results = search(sys.argv[1])
    else:
        results = search(input('what are you looking for?\n>  '), quality)
    options = ["["+i['source']+"]"+' '+i['title'] for i in results]
    choice = TerminalMenu(options)
    link = results[choice.show()]["magnet"]["link"]
    subprocess.run(config["command"]+"'"+link+"'", shell=True)


def search(query, quality=None, providers=providers):
    results = []
    for i in providers:
        print("executing:", i)
        provider = importlib.import_module('scrapers.'+i)
        results += provider.search(query, quality)
    results = utils.sort_by_seed(results)
    return results


# parsing results for display

if __name__=="__main__":
    tui()
