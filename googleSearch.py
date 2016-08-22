from connection import googleSearchConnect

def search(query):
    print('Inside search')
    soup = googleSearchConnect(query['search'])
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

