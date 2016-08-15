import os
import sys
from urllib.parse import urljoin
from services import getBasicInfo, getOverview, getLocation, getReviews, getAmenitiesInfo, getAwardsInfo
from connection import connect

url = 'http://www.fivestaralliance.com/luxury-hotels/bangkok/banyan-tree-bangkok'

info = {}

def scrape(soup):
    getBasicInfo(soup, info)
    getOverview(soup, info)
    getLocation(soup, info)
    getReviews(soup, info)
    getAmenitiesInfo(soup, info)
    getAwardsInfo(soup, info)
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
