'''
This script is re
'''

from fsaServices import getBasicInfo, getOverview, getLocation, getReviewsHighlights, getAmenitiesInfo, getAwardsInfo
from connection import connect
from tripAdvisorCrawler import start
from repository import save

url = 'http://www.fivestaralliance.com/luxury-hotels/bangkok/banyan-tree-bangkok'
#url = 'http://www.fivestaralliance.com/luxury-hotels/mahe-island/banyan-tree-seychelles'

# map to store information
info = {}

# call service functions to get particular data
def scrape(soup):
    getBasicInfo(soup, info)
    getOverview(soup, info)
    getLocation(soup, info)
    getReviewsHighlights(soup, info)
    getAmenitiesInfo(soup, info)
    getAwardsInfo(soup, info)
    start(info)
    #save(info)
    # remove call to showOutput when in production
    showOutput()


# show output, optional debugging function
def showOutput():
    print("**Output is as follows**")
    print(info)

# start to crawl a page
def crawl(url):
    print("Crawling this page: ", url)
    soup = connect(url)
    if soup == None:
        print("Exception")
        return
    else:
        scrape(soup)
        return info


# code to enable script to run independently
if __name__ == '__main__':
    #print(url)
    crawl(url)
