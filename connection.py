import requests
from bs4 import BeautifulSoup
import time

parser = 'lxml'

def connect(url):
    print("Connecting to", url)
    try:
        r = requests.get(url, timeout = (10, 20))
        if r.status_code != 200:
            print("Exception")
            return None
        else:
            time.sleep(2)
            soup = BeautifulSoup(r.text, parser)
            return soup
    except:
        print('Exception while connecting')
        return None


def getNewSoup(markup):
    soup = BeautifulSoup(markup, parser)
    return soup

def googleSearchConnect(query):
    print('Inside Google Search Connect')
    data = {'q' : query}
    url = 'http://www.google.com/search'
    try:
        r = requests.get(url, params = data, timeout = (15, 20))
        if r.status_code != 200:
            print("Exception")
            return None
        else:
            time.sleep(1)
            soup = BeautifulSoup(r.text, parser)
            return soup
    except:
        print('Exception while connecting')
        return None

