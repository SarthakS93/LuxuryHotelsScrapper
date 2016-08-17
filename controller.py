'''
Controller for the project
This calls the particular service functions
'''

from crawler import crawl
from urllib.parse import urljoin

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
def start(soup, url):
    list = getAllLinks(soup, url)
    for i in list:
        crawl(i)

