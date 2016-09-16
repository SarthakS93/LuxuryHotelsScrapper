from connection import connect
import csv
from googleSearch import weatherSearch
from repository import saveWeatherData

destination_list = ['Dubai', 'Abu Dhabi', 'Muscat', 'Jaipur', 'Udaipur', 'Jodhpur',
        'Bali', 'Macau', 'Seychelles', 'Mauritius', 'Cairo', 'Hurghada', 'Male',
        'Singapore', 'Colombo', 'Galle', 'Tangelle', 'Bangkok', 'Koh Samui', 'Hua Hin',
        'Hong Kong', 'Chiang Mai', 'Chiang Rai', 'Pattaya', 'Phuket', 'Krabi', 'Phangan',
        'Hue', 'Phan Thiet', 'Mumbai', 'Nha Trang', 'Ho Chi Minh City']

#destination_list = ['Dubai', 'Abu Dhabi', 'Bangkok', 'Koh Samui']

def template1(url):
    print('Inside template1')
    try:
        soup = connect(url)
        if soup:
            body = soup.find(id = 'NEXUS')
            container = body.find(class_ = 'articleBody')

            str = container.text
            str = str.replace('\n', '')
            str = str.replace('\xa0', '')

            map = {}
            weather = getWeather(soup)
            map['weather'] = weather
            map['description'] = str
            print(map)
            print('$$$$$$$$$')

            return map

        print('Nothing found in template1')
        return None

    except:
        print('Exception in template1')
        return None


def template2(url):
    print('Inside template2')
    try:
        soup = connect(url)
        if soup:
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

        print('Nothing found in template2')
        return None
    except:
        print('Exception in template2')
        return None


def getWeather(soup):
    print('Inside getWeather')
    try:
        container = soup.find(id = 'weatherHistory')
        if container:
            divs = soup.find_all(class_ = 'historyRow')
            weather = {}
            if divs:
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

        print('Nothing inside getWeather')
        return None

    except:
        print('Exception in getWeather')
        return None

def crawl(destination):
    print('Inside Crawl')
    try:
        query = 'tripadvisor best time to visit ' + destination
        queryDictionary = {'search' : query}
        urls = weatherSearch(queryDictionary)
        data = {}

        template1Data = None
        template2Data = None

        if urls[0] != '':
            template1Data = template1(urls[0])
        if urls[1] != '':
            template2Data = template2(urls[1])

        print(destination)

        map = getInfoAsMap(template1Data, template2Data, destination)

        return map
    except:
        print('Exception in crawl')
        return None


def start():
    print('Inside start')
    try:
        dataList = []
        for i in destination_list:
            try:
                data = crawl(i)
                if data:
                    dataList.append(data)
            except:
                print('Exception')

        saveWeatherData(dataList)

    except:
        print('Exception in start')



def getInfoAsMap(template1Data, template2Data, destination):
    print('Inside getInfoAsMap')
    try:

        weatherFacts = None
        description = ''
        reviews = []

        if template1Data:
            if 'weather' in template1Data and template1Data['weather']:
                weatherFacts = template1Data['weather']

            if 'description' in template1Data and template1Data['description']:
                description = template1Data['description']

        if template2Data:
            reviews = template2Data

        data = {'facts' : weatherFacts, 'description' : description, 'reviews' : reviews,
                'destination' : destination}

        return data

    except:
        print('Exception in getInfoAsMap')
        return None


if __name__ == '__main__':
    #destination = input('Enter destination: ')
    print('Starting')
    url  = 'http://www.tripadvisor.com/Travel-g293738-s208/Seychelles:Weather.And.When.To.Go.html'
    #func(url)
    #start(destination)
    start()
