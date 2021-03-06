'''
This script is re
'''

from fsaServices import getBasicInfo, getOverview, getLocation, getReviewsHighlights, getAmenitiesInfo, getAwardsInfo
from connection import connect
from tripAdvisorCrawler import startTripAdvisor
from agodaCrawler import startAgoda
from bookingCrawler import startBooking
from repository import save

#url = 'http://www.fivestaralliance.com/luxury-hotels/sir-bani-yas-island/anantara-al-yamm-villa-resort'
url='http://www.fivestaralliance.com/4star-hotels/bangalore/vivanta-taj-whitefield-bangalore'

# call service functions to get particular data
def scrape(soup, info):
    try:
        getBasicInfo(soup, info)
        getOverview(soup, info)
        getLocation(soup, info)
        getReviewsHighlights(soup, info)
        getAmenitiesInfo(soup, info)
        getAwardsInfo(soup, info)
        startTripAdvisor(info)
        startAgoda(info)
        startBooking(info)
        save(info)
        # remove call to showOutput when in production
        #showOutput()
    except:
        print('Exception in scrape')

# show output, optional debugging function
def showOutput():
    print("**Output is as follows**")
    print(info)

# start to crawl a page
def crawl(url):
    print("Crawling this page: ", url)
    info = {}
    try:
        soup = connect(url)
        if soup == None:
            print("Exception")
            return None
        else:
            scrape(soup, info)
            return info
    except:
        print('Exception in crawl for url: ', url)
        return None

# code to enable script to run independently
if __name__ == '__main__':
    #print(url)
    crawl(url)
