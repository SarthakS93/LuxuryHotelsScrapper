from googleSearch import bookingSearch
from connection import connect
from urllib.parse import urljoin
import csv

def booking(url, info):
    print('Inside booking.com', url)
    try:
        soup = connect(url)
        if soup:
            rooms = getRoomTypes(soup)
            points = getPoints(soup)
            score = getBookingScore(soup)
            description = getDescription(soup)

            info['rooms'] = rooms
            bookingMap = {'points' : points, 'score' : score, 'description' : description}

            info['booking_data'] = bookingMap

    except:
        print('Exception in tripAdvisor')


def getDescription(soup):
    print('Inside getDescription')
    try:
        tag = soup.find(id = 'summary')
        if tag:
            text = tag.text
            text = text.replace('\n', '')
            return text

        print('Nothing found in getDescription')
        return ''
    except:
        print('Exception in getDescription')
        return ''


def getBookingScore(soup):
    print('Inside getBookingScore')
    try:
        tag = soup.find(class_ = 'average')
        if tag:
            return tag.text

        print('Nothing found in getBookingScore')
        return None

    except:
        print('Exception in getBookingScore')
        return None

def getRoomTypes(soup):
    print('Inside getRoomTypes')
    try:
        table = soup.find(id = 'rooms_table')
        if table:
            divs = table.find_all(class_ = 'ftd')
            list = []
            if divs:
                for item in divs:
                    text = item.text
                    text = text[1 : -1]
                    list.append(text)

                return list

        print('Nothing found in getRoomTypes')
        return None

    except:
        print('Exception in getRoomTypes')
        return None

def getPoints(soup):
    print('Inside getPoints')
    try:
        container = soup.find(id = 'reviewFloater')
        if container:
            labels = soup.find_all('p', class_ = 'review_score_name')
            ratings = soup.find_all('p', class_ = 'review_score_value')

            tempMap = {}

            for i in range(len(labels)):
                label = labels[i].text
                rating = ratings[i].text
                tempMap[label] = rating

            keys = {'Valiue for money': True, 'Comfort': True, 'Location': True,
                    'Staff': True, 'Facilities': True, 'Cleanliness': True,
                    'Free WiFi': True}

            points = {}
            for k in tempMap:
                if k in keys:
                    points[k] = tempMap[k]

            return points

        print('Nothing found in getPoints')
        return None

    except:
        print('Exception in getPoints')
        return None

def startBooking(info):
    try:
        queryDictionary = {'name' : info['name'], 'location' : info['location']}
        searchString = 'booking.com' + ' ' + info['name'] + ' ' + info['location']
        queryDictionary['search'] = searchString
        url = None
        i = 0
        while(i < 3):
            if url == None:
                url = bookingSearch(queryDictionary)
                i = i + 1
            else:
                break


        if url:
            booking(url, info)
        else:
            print('Booking.com could not be found for: ', info['search'])
    except:
        print('Exception in startBooking')

if __name__ == '__main__':
    name = input('Enter name: ')
    loc = input('Enter loc: ')
    q = {}
    q['name'] = name
    q['location'] = loc
    q['search'] = 'booking.com' + ' ' + name + ' ' + loc
    url = None
    while(url == None):
        url = bookingSearch(q)
    if url:
        info = {}
        booking(url, info)
