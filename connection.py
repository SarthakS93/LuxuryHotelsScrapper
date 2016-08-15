import requests
from bs4 import BeautifulSoup

def connect(url):
    print("Connecting to", url)
    r = requests.get(url)
    if r.status_code != 200:
        print("Exception")
        return None
    else:
        soup = BeautifulSoup(r.text)
        return soup