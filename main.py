import importlib


providers = ['leetxx', 'nyaa', 'rarbg', 'torrent9', 'yts']


def search(query, providers=None):
    providers= [ ]
    for i in providers:
        providers.append(__import__('scrapers.'+i))
    print providers

