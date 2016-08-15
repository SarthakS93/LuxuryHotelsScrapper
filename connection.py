import requests
from bs4 import BeautifulSoup

def connect(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    return soup
