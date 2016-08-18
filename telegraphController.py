'''
Controller for the project
This calls the particular service functions
'''

from telegraphCrawler import crawl
from urllib.parse import urljoin
from connection import connect

baseUrl = 'http://www.telegraph.co.uk/travel/destinations/'

destinations = ['India', 'Maldives', 'Seychelles', 'Mauritius', 'Hong Kong', 'Macau',  'Philipines', 'Thailand', 'Indonesia', 'China', 'Vietnam', 'Singapore', 'Laos', 'Malaysia', 'Oman', 'Qatar', 'United Arab Erimates']

def getDestinationLinks(soup):
    a_tags = soup.find_all('a')
    for tag in a_tags:
        tag_text = tag.text
        if tag_text in destinations:
            url = tag.get('href')
            abs_url = urljoin(baseUrl, url)
            links.append(abs_url)


def telegraphController(url):
    mainUrl = getHotelsPageSoup()


# calls crawl function to scrape data for all links
def start():
    soup = connect(baseUrl)
    destination_links = getDestinationLinks(soup)
    for url in destination_links:
        telegraphController(url)

