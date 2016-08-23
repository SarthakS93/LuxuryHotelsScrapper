from connection import googleSearchConnect

def tripAdvisorSearch(query):
    print('Inside tripadvisor search')
    try:
        soup = googleSearchConnect(query['search'])
        if soup:
            print('asd')
            a_tags = soup.find_all('a')
            for tag in a_tags:
                href_text = tag.get('href')
                if 'tripadvisor.in' in href_text:
                    link = getLinkFromText(href_text)
                    return link

        print('Nothing found in tripadvisor')
        return None

    except:
        print('Exception in tripadvisor search')
        return None


def agodaSearch(query):
    print('Inside agoda search')
    try:
        soup = googleSearchConnect(query['search'])
        if soup:
            print('asd')
            a_tags = soup.find_all('a')
            for tag in a_tags:
                href_text = tag.get('href')
                if 'agoda.com' in href_text and '/hotel/' in href_text:
                    link = getLinkFromText(href_text)
                    return link

        print('Nothing found in agoda search')
        return None

    except:
        print('Exception in agoda search')
        return None


def getLinkFromText(href_text):
    link = ''
    print(href_text)
    if '&' in href_text:
        link = href_text.split('&')[0]
    else:
        link = href_text

    if '/url?q=' in link:
        return link[7 : ]
    else:
        return link
