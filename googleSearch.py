from connection import googleSearchConnect

def search(query):
    print('Inside search')
    print('data input to search is: ', query)
    soup = googleSearchConnect(query['search'])
    a_tags = soup.find_all('a')
    print('Number of links found: ', len(a_tags))
    for tag in a_tags:
        tag_text = tag.text
        tag_text = tag_text.lower()
        href_text = tag.get('href')
        name = query['name'].lower()
        if 'tripadvisor.in' in href_text:
            #if name in tag_text:
            print('Found link: ', tag.get('href'))
            if '/url?q=' in href_text:
                return href_text[7 : ]
            else:
                return href_text

