from connection import connect
import csv
from googleSearch import weatherSearch

def func(url):
    soup = connect(url)
    body = soup.find(id = 'NEXUS')
    container = body.find(class_ = 'articleBody')

    str = container.text
    str = str.replace('\n', '')
    str = str.replace('\xa0', '')

    info = {}
    weather = getWeather(soup)
    info['weather'] = weather
    info['description'] = str
    print(info)


def func2(url):
    soup = connect(url)
    container = soup.find(class_ = 'balance')
    divs = container.find_all(class_ = 'post')

    list = []
    for div in divs:
        container = div.find(class_ = 'postBody')
        str = container.text
        str = str.replace('\n', '')
        list.append(str)
    print(list)
    return list

def getWeather(soup):
    container = soup.find(id = 'weatherHistory')
    divs = soup.find_all(class_ = 'historyRow')
    weather = {}
    for i in range(1, len(divs)):
        div = divs[i]
        month = div.find(class_ = 'month').text
        temp_tags = div.find_all(class_ = 'temp')
        high = temp_tags[0].text[1 : -1]
        low = temp_tags[1].text[1 : -1]
        rain = div.find(class_ = 'precip').text[1 : -1]
        map = {}
        map['rain'] = rain
        map['high temp'] = high
        map['low temp'] = low
        weather[month] = map

    return weather


def start(destination):
    query = 'tripadvisor best time to visit ' + destination
    queryDictionary = {'search' : query}
    urls = weatherSearch(queryDictionary)
    if urls[0] != '':
        func(urls[0])
    if urls[1] != '':
        func2(urls[1])

if __name__ == '__main__':
    destination = input('Enter destination: ')
    print('Starting')
    url  = 'http://www.tripadvisor.com/Travel-g293738-s208/Seychelles:Weather.And.When.To.Go.html'
    #func(url)
    start(destination)
