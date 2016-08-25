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
            if link_tag:
                link = link_tag.get('href')
                abs_url = urljoin(url, link)
                print('Getting reviews: ', abs_url)
                list = getReviews(abs_url)
                info['tripadvisor'] = list

            attractions = getAttractions(soup, info)
            info['attractions'] = attractions

            eateries = getEateryInfo(soup, url)
            info['eateries'] = eateries

            #print(info)
        else:
            print('Nothing found in tripAdvisor')

    except:
        print('Exception in tripAdvisor')


def getAttractions(soup, info):
    print('Inside getAttractions')
    try:
        attractions = soup.find(class_ = 'attractions')
        list = []
        if attractions:
            divs = attractions.find_all(class_ = 'attraction')
            if divs:
                for div in divs:
                    tag = div.find(class_ = 'nameWrapper')
                    text = tag.text[1 : -1]
                    list.append(text)

                return list

        print('Nothing found in getAttractions')
        return None


    except:
        print('Exception in getAttractions')
        return None


def getEateryInfo(soup, url):
    print('Inside getEateryInfo')
    try:
        eateries = soup.find(class_ = 'eateries')
        if eateries:
            divs = eateries.find_all(class_ = 'eatery')
            if divs:
                list = []
                for div in divs:
                    tag = div.find(class_ = 'nameWrapper')
                    link_tag = div.find('a')
                    link = link_tag.get('href')
                    abs_url = urljoin(url, link)
                    data = getCuisine(abs_url)
                    name = tag.text[1 : -1]
                    newMap = {}
                    newMap[name] = data
                    list.append(newMap)

            return list

        print('Nothing found in getEateryInfo')
        return None

    except:
        print('Exception in getEateryInfo')
        return None


def getCuisine(url):
    print('Inside getCuisine')
    try:
        soup = connect(url)
        container = soup.find(class_ = 'details_tab')
        divs = container.find_all(class_ = 'row')
        keys = {'Cuisine': 1, 'Meals': 1, 'Good for': 1, 'Restaurant features': 1}
        data = {}
        for div in divs:
            title_tag = div.find(class_ = 'title')
            if title_tag:
                title = title_tag.text[1 : -1]
                if title in keys:
                    content_tag = div.find(class_ = 'content')
                    content = content_tag.text[1 : -1]
                    content = content.replace('\xa0', '')
                    data[title] = content

        return data
    except:
        print('Exception in getCuisine')
        return None

def scrape(div):
    print('Inside tripadvisor scrape')
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
        while(i < 3):
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
