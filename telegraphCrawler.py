'''
This script is re
'''

from connection import connect
from telegraphService import getBasicInfo, getReviews

#url = 'http://www.telegraph.co.uk/travel/destinations/asia/thailand/natai-beach/hotels/iniala-beach-house-hotel/'

info = {}

list = []

# call service functions to get particular data
def scrape(soup):
    getBasicInfo(soup, info)
    getReviews(soup, info)
    # remove call to showOutput when in production
    showOutput()


# show output, optional debugging function
def showOutput():
    print("**Output is as follows**")
    print(info)
    list.append(info['name'])
    print('***************************************************************************************', len(list), '$$$$$$$$$$$$$$', list[len(list) - 1])

# start to crawl a page
def crawl(url):
    print("Crawling this page: ", url)
    soup = connect(url)
    if soup == None:
        print("Exception")
        return
    else:
        scrape(soup)


# code to enable script to run independently
if __name__ == '__main__':
    #print(url)
    crawl(url)
