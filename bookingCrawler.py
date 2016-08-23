from googleSearch import bookingSearch
from connection import connect
from urllib.parse import urljoin
import csv

def booking(url, info):
    print('Inside booking.com', url)
    try:
        soup = connect(url)
        if soup:
    except:
        print('Exception in tripAdvisor')

def startAgoda(info):
    try:
        queryDictionary = {'name' : info['name'], 'location' : info['location']}
        searchString = 'booking.com' + ' ' + info['name'] + ' ' + info['location']
        queryDictionary['search'] = searchString
        url = None
        i = 0
        while(i < 10):
            if url == None:
                url = booking(queryDictionary)
                i = i + 1
            else:
                break


        if url:
            agoda(url, info)
        else:
            print('Agoda.com could not be found for: ', info['search'])
    except:
        print('Exception in startAgoda')

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
