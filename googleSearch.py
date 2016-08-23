from connection import googleSearchConnect

def tripAdvisorSearch(query):
    print('Inside tripadvisor search')
    try:
        soup = googleSearchConnect(query['search'])
        if soup:
            a_tags = soup.find_all('a')
            for tag in a_tags:
                tag_text = tag.text
                tag_text = tag_text.lower()
                href_text = tag.get('href')
                name = query['name'].lower()
                if 'tripadvisor.in' in href_text:
                    #if name in tag_text:
                    if '/url?q=' in href_text:
                        return href_text[7 : ]
                    else:
                        return href_text

        return None

    except:
        print('Exception in tripadvisor search')


def agodaSearch(query):
    print('Inside agoda search')
    try:
        soup = googleSearchConnect(query['search'])
        if soup:
            a_tags = soup.find_all('a')
            for tag in a_tags:
                tag_text = tag.text
                href_text = tag.get('href')
                if 'agoda.com' in href_text and '/hotel/' in href_text:
                    link = ''

                    if '&' in href_text:
                        link = href_text.split('&')[0]

                    if '/url?q=' in link:
                        return link[7 : ]
                    else:
                        return link


