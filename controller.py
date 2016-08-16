from crawler import crawl

visited = {}


def getAllLinks(soup, baseUrl):
    a_tags = soup.find_all('a')
    list = []
    for i in a_tags:
        if i.has_attr('href'):
            url = i.get('href')
            if '/luxury-hotels/' in url:
                abs_url = urljoin(baseUrl, url)
                list.append(abs_url)

    return list



def start(soup, url):
    list = getAllLinks(soup, url)
    visited[url] = True
    for i in list:
        crawl(i)

