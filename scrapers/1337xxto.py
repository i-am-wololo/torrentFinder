import requests
from bs4 import BeautifulSoup


url = "https://www.1337xx.to/category-search/{query}/{type}/{page}/"



def search(query, type):
    #type should either be Movies or TV
    page = 1
    results = []
    query = query.replace(' ', "%20") # Make query Url friendly
