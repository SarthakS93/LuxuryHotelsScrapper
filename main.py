from urllib.parse import urljoin
from connection import connect
from controller import start


middleEastURL = 'http://www.fivestaralliance.com/luxury-hotels-worldwide/destination/7/middle-east'

asiaURL = 'http://www.fivestaralliance.com/luxury-hotels-worldwide/destination/5/asia'

urls = [asiaUrl, middleEastURL]


def main():
    for url in urls:
        soup = connect(url)
        start(soup, url)


if __name__ == '__main__':
    print('Starting to Crawl')
    main()
