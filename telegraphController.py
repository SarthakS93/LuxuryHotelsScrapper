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
    print("Getting all the destination links from the page: ", soup.title)
    a_tags = soup.find_all('a')
    links = []
    for tag in a_tags:
        tag_text = tag.text
        for name in destinations:
            if name in tag_text:
                url = tag.get('href')
                abs_url = urljoin(baseUrl, url)
                links.append(abs_url)

    print('The length of the destination links is: ', len(links))
    return links

def findHotelLinks(soup, hotel_links):
    print('Finding hotel links')
    container_tags = soup.find_all(class_ = 'product-article-listing__headline')
    for tag in container_tags:
        link_tag = tag.find('a')
        if link_tag:
            link = link_tag.get('href')
            hotel_links.append(link)

    print('Length of hotel links now is: ', len(hotel_links))



def telegraphController(url):
    print('Inside controller')
    try:
        link = getHotelsPageLink(url)
        if link:
            soup = connect(link)
            if soup:
                hotel_links = []
                findHotelLinks(soup, hotel_links)
                pagination_tags = soup.find_all(class_ = 'product-pagination__items')
                if pagination_tags:
                    for i in range(1, len(pagination_tags)):
                        abs_url = urljoin(baseUrl, i.get('href'))
                        newSoup = connect(abs_url)
                        findHotelLinks(newSoup, hotel_links)

                for i in hotel_links:
                    crawl(i)

    except:
        print('Exception in telegraphController')


# calls crawl function to scrape data for all links
def start():
    print("Starting to crawl Telegraph.co.uk")
    try:
        soup = connect(baseUrl)
        if soup:
            destination_links = getDestinationLinks(soup)
            for url in destination_links:
                print('Destination link is: ', url)
                try:
                    telegraphController(url)
                except:
                    print('Exception in start Telegraph loop')
        else:
            print('Nothing found in start Telegraph')
    except:
        print('Exception in start Telegraph')

def getHotelsPageLink(url):
    soup = connect(url)
    tag = soup.find(class_ = 'product-listing__more')
    if tag:
        link_tag = tag.find('a')
        link = link_tag.get('href')
        abs_url = urljoin(url, link)
        print('Hotel listing page link is: ', abs_url)
        return abs_url
    else:
        return None



if __name__ == '__main__':
    print('Running Script')
    start()
