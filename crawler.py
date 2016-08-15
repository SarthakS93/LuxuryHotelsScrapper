import requests
from bs4 import BeautifulSoup
import os
import sys
from urllib.parse import urljoin

url = 'http://www.fivestaralliance.com/luxury-hotels/bangkok/banyan-tree-bangkok'

info = {}

def getBasicInfo(soup):
    print("Getting Basic Info")
    name_tag = soup.find(id = 'heading_title_hotel')
    info['name'] = name_tag.text
    location_tag = soup.find(id = 'title_location')
    info['location'] = location_tag.text

def connect(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        soup = BeautifulSoup(r.text)
        return soup


def scrape(soup):
    getBasicInfo(soup)
    #getOverView(soup)
    #getLocation(soup)
    #getReviews(soup)
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
