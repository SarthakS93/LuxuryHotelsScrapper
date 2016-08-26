'''
This script is re
'''

from connection import connect
from telegraphService import getBasicInfo, getReviews, getFacilities

url = 'http://www.telegraph.co.uk/travel/destinations/asia/thailand/bangkok/hotels/the-siam-hotel/'

# call service functions to get particular data
def scrape(soup, info):
    print('Inside scrape')
    try:
        if soup:
            getBasicInfo(soup, info)
            data = getReviews(soup, info)
            if data:
                info['reviews'] = data
            else:
                info['reviews'] = None

            facilities = getFacilities(soup)
            if facilities:
                info['facilities'] = facilities
            else:
                info['facilities'] = None

        else:
            print('Nothing found in scrape')
    except:
        print('Exception in scrape')


# start to crawl a page
def crawl(url):
    print("Crawling this page: ", url)
    try:
        soup = connect(url)
        if soup:
            info = {}
            scrape(soup, info)
            return info
        else:
            print('Nothing found in crawl')
            return None

    except:
        print('Exception in crawl')


# code to enable script to run independently
if __name__ == '__main__':
    #print(url)
    crawl(url)
