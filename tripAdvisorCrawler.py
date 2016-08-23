from googleSearch import tripAdvisorSearch
from connection import connect
from urllib.parse import urljoin
import csv

def tripAdvisor(url, info):
    print('Inside TripAdvisor', url)
    try:
        soup = connect(url)
        if soup:
            tag = soup.find(class_ = 'reviewSelector')
            div_tag = tag.find(class_ = 'quote')
            if div_tag == None:
                div_tag = tag.find(class_ = 'noQuotes')
            link_tag = div_tag.find('a')
            print(link_tag)
            if link_tag:
                link = link_tag.get('href')
                abs_url = urljoin(url, link)
                print('Getting reviews: ', abs_url)
                list = getReviews(abs_url)
                info['tripadvisor'] = list
                '''
                file = open('temp.csv', 'w', newline = '')
                out = csv.writer(file)
                out.writerow(list)
                file.close()
                '''
    except:
        print('Exception in tripAdvisor')

def scrape(div):
    try:
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
    except:
        print('Exception in scrape')


def getReviews(url):
    try:
        soup = connect(url)
        if soup:
            divs = soup.find_all(class_ = 'innerBubble')
            list = []
            for div in divs:
                review = scrape(div)
                list.append(review)

            return list
    except:
        print('Exception in getReviews')


def startTripAdvisor(info):
    try:
        queryDictionary = {'name' : info['name'], 'location' : info['location']}
        searchString = 'tripadvisor' + ' ' + info['name'] + ' ' + info['location']
        queryDictionary['search'] = searchString
        url = None
        i = 0
        while(i < 10):
            if url == None:
                url = tripAdvisorSearch(queryDictionary)
                i = i + 1
            else:
                break


        if url:
            tripAdvisor(url, info)
        else:
            print('Tripadvisor could not be found for: ', info['search'])
    except:
        print('Exception in startTripAdvisor')

if __name__ == '__main__':
    name = input('Enter name: ')
    loc = input('Enter loc: ')
    q = {}
    q['name'] = name
    q['location'] = loc
    q['search'] = 'tripadvisor' + ' ' + name + ' ' + loc
    url = None
    while(url == None):
        url = tripAdvisorSearch(q)
    if url:
        info = {}
        tripAdvisor(url, info)
