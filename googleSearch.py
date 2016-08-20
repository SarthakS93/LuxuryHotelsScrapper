from connection import googleSearchConnect

def search(query):
    soup = googleSearchConnect(query['search'])
    a_tags = soup.find_all('a')
    for tag in a_tags:
        tag_text = tag.text
        tag_text = tag_text.lower()
        href_text = tag.get('href')
        if 'tripadvisor.in' in href_text:
            if query['name'].lower in tag_text and
                query['location'].lower in tag.text:
                    return tag.get('href')

