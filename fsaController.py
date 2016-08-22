'''
Controller for the project
This calls the particular service functions
'''

from fsaCrawler import crawl
from urllib.parse import urljoin
from connection import connect
from repository import save, saveData

middleEastURL = 'http://www.fivestaralliance.com/luxury-hotels-worldwide/destination/7/middle-east'

asiaURL = 'http://www.fivestaralliance.com/luxury-hotels-worldwide/destination/5/asia'

africaURL = 'http://www.fivestaralliance.com/luxury-hotels-worldwide/destination/6/africa'


urls = [asiaURL, middleEastURL, africaURL]

# gets all the links of luxury hotels on a particular page
def getAllLinks(soup, baseUrl):
    a_tags = soup.find_all('a')
    list = []

    if 'africa' in baseUrl:
        for i in a_tags:
            if i.has_attr('href'):
                url = i.get('href')
                if '/luxury-hotels/' in url:
                    a_text = i.text
                    if 'Mauritius' in a_text or 'Seychelles' in a_text:
                        abs_url = urljoin(baseUrl, url)
                        list.append(abs_url)

    else:
        for i in a_tags:
            if i.has_attr('href'):
                url = i.get('href')
                if '/luxury-hotels/' in url:
                    abs_url = urljoin(baseUrl, url)
                    list.append(abs_url)

    return list


# calls crawl function to scrape data for all links
def start(soup, url, dataList):
    list = getAllLinks(soup, url)
    for i in list:
        info = crawl(i)
        dataList.append(info)

# controller method
def controller():
    dataList = []
    for url in urls:
        soup = connect(url)
        start(soup, url, dataList)

    print('******Crawling complete******')
    saveData(dataList)
