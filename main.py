'''
Author: SarthakS93

This is the main python script, which will be run to get the data of Luxury Hotels.
Run this script from terminal by the following command:
    python3 main.py

The dependencies to run this project are:
    1. python3
    2. BeautifulSoup4
    3. Requests module

For any queries, mail to sarthaks93@gmail.com
'''

from connection import connect
from fsaController import start


middleEastURL = 'http://www.fivestaralliance.com/luxury-hotels-worldwide/destination/7/middle-east'

asiaURL = 'http://www.fivestaralliance.com/luxury-hotels-worldwide/destination/5/asia'

africaURL = 'http://www.fivestaralliance.com/luxury-hotels-worldwide/destination/6/africa'


urls = [asiaURL, middleEastURL, africaURL]


def main():
    for url in urls:
        soup = connect(url)
        start(soup, url)


if __name__ == '__main__':
    print('Starting to Crawl')
    main()
