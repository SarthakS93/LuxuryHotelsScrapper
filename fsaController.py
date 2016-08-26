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


#urls = [asiaURL, middleEastURL, africaURL]
urls = [asiaURL]

africaDestinations = ['Cairo', 'Hurghada', 'Mauritius', 'Seychelles']
#africaDestinations = ['Maasai Mara']

middleEastDestinations = ['Dubai', 'Abu Dhabi', 'Muscat']

asiaDestinations = ['Jaipur', 'Udaipur', 'Jodhpur', 'Bali', 'Hong Kong', 'Mataram', 'Macau',
        'Male',  'Singapore', 'Colombo', 'Bangkok', 'Chiang Mai', 'Chiang Rai', 'Koh Samui', 'Hua Hin',
        'Krabi', 'Pattaya', 'Phangan', 'Phuket', 'Galle', 'Tangelle',]

thailand = ['Bangkok', 'Chiang Rai', 'Chiang Mai', 'Koh Samui', 'Hua Hin', 'Phuket', 'Phangan', 'Pattaya', 'Krabi']

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
                    for dest in africaDestinations:
                        if dest in a_text:
                            abs_url = urljoin(baseUrl, url)
                            list.append((abs_url, dest))

    elif 'middle-east' in baseUrl:
        for i in a_tags:
            if i.has_attr('href'):
                url = i.get('href')
                if '/luxury-hotels/' in url:
                    a_text = i.text
                    for dest in middleEastDestinations:
                        if dest in a_text:
                            abs_url = urljoin(baseUrl, url)
                            list.append((abs_url, dest))

    elif 'asia' in baseUrl:
        for i in a_tags:
            if i.has_attr('href'):
                url = i.get('href')
                if '/luxury-hotels/' in url:
                    a_text = i.text
                    for dest in thailand:
                        if dest in a_text:
                            abs_url = urljoin(baseUrl, url)
                            list.append((abs_url, dest))

    return list


# calls crawl function to scrape data for all links
def start(soup, url):
    list = getAllLinks(soup, url)
    print('Start fsaController with links: ', len(list))
    dataList = []
    for i in list:
        try:
            info = crawl(i[0])
            if info:
                info['destination'] = i[1]
                dataList.append(info)
        except:
            print('Exception in start')

    return dataList

# controller method
def controller():
    for url in urls:
        soup = connect(url)
        if soup:
            dataList = start(soup, url)

            print('******Crawling complete******')
            saveData(dataList)
