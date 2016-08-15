import requests
from bs4 import BeautifulSoup
import os
import sys
from urllib.parse import urljoin
from services import getBasicInfo, getOverview, getLocation, getReviews

url = 'http://www.fivestaralliance.com/luxury-hotels/bangkok/banyan-tree-bangkok'

info = {}

def connect(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        soup = BeautifulSoup(r.text)
        return soup


def scrape(soup):
    getBasicInfo(soup, info)
    getOverview(soup, info)
    getLocation(soup, info)
    getReviews(soup, info)
    #getAmenities(soup)
    #getAwards(soup)
    showOutput()


def showOutput():
    print("**Output is as follows**")
    print(info)

def crawl(url):
    print("Crawling this page: ", url)
    soup = connect(url)
    if soup == None:
        print("Exception")
        return
    else:
        scrape(soup)


if __name__ == '__main__':
    #print(url)
    crawl(url)
