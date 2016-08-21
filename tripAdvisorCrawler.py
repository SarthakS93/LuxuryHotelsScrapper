from googleSearch import search
from connection import connect
from urllib.parse import urljoin

def tripAdvisor(url, info):
    print('Inside TripAdvisor', url)
    soup = connect(url)
    tag = soup.find(class_ = 'reviewSelector')
    div_tag = tag.find(class_ = 'quote isNew')
    link_tag = div_tag.find('a')
    print(link_tag)
    if link_tag:
        link = link_tag.get('href')
        abs_url = urljoin(url, link)
        print('Getting reviews: ', abs_url)
        list = getReviews(abs_url)
        print(list)
        info['tripadvisor'] = list



def scrape(div):
    review = {}
    overview_tag = div.find(class_ = 'quote')
    overview = overview_tag.text[1 : -1]
    review['overview'] = overview
    rating = div.find('img', class_ = 'rating_s_fill').get('alt')
    review['rating'] = rating
    review_body_tag = div.find('p')
    review_body = review_body_tag.text[1 : -1]
    review['body'] = review_body
    review_points_tag = div.find_all(class_ = 'recommend-answer')
    review_points = {}
    if review_points_tag != None and len(review_points_tag) > 0:
        for point in review_points_tag:
            key = point.find(class_ = 'recommend-description').text
            value = point.find('img').get('alt')
            review_points[key] = value
            review['points'] = review_points
    else:
        review['points'] = None

    return review


def getReviews(url):
    soup = connect(url)
    divs = soup.find_all(class_ = 'innerBubble')
    list = []
    for div in divs:
        review = scrape(div)
        list.append(review)

    return list


def start(info):
    queryDictionary = {'name' : info['name'], 'location' : info['location']}
    searchString = 'tripadvisor' + ' ' + info['name'] + ' ' + info['location']
    queryDictionary['search'] = searchString
    url = None
    while(url == None):
        url = search(queryDictionary)
    if url:
        tripAdvisor(url, info)

if __name__ == '__main__':
    name = input('Enter name: ')
    loc = input('Enter loc: ')
    q = {}
    q['name'] = name
    q['location'] = loc
    q['search'] = 'tripadvisor' + ' ' + name + ' ' + loc
    url = None
    while(url == None):
        url = search(q)
    if url:
        tripAdvisor(url)
