import requests
from bs4 import BeautifulSoup
import time

parser = 'lxml'

def connect(url):
    print("Connecting to", url)
    r = requests.get(url, timeout = (10, 20))
    if r.status_code != 200:
        print("Exception")
        return None
    else:
        time.sleep(2)
        soup = BeautifulSoup(r.text, parser)
        return soup

def getNewSoup(markup):
    soup = BeautifulSoup(markup, parser)
    return soup

def googleSearchConnect(query):
    print('Inside Google Search Connect')
    data = {'q' : query}
    url = 'http://www.google.com/search'
    r = requests.get(url, params = data, timeout = (10, 20))
    if r.status_code != 200:
        print("Exception")
        return None
    else:
        time.sleep(2)
        soup = BeautifulSoup(r.text, parser)
        return soup


