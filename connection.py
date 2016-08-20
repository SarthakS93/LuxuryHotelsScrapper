import requests
from bs4 import BeautifulSoup
import time

def connect(url):
    print("Connecting to", url)
    r = requests.get(url)
    if r.status_code != 200:
        print("Exception")
        return None
    else:
        time.sleep(2)
        soup = BeautifulSoup(r.text)
        return soup

def getNewSoup(markup):
    soup = BeautifulSoup(markup)
    return soup

def googleSearchConnect(query):
    data = {'q' : query}
    url = 'http://www.google.com/search'
    r = requests.get(url, data)
    soup = BeautifulSoup(r.text)
    return soup


