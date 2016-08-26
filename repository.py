import csv

tempPath = 'temp.csv'
filePath = 'fsa.csv'
africaPath = 'africa.csv'
thailandPath = 'thailand.csv'
middleEastPath = 'middleEast.csv'
southAsiaPath = 'southAsia.csv'
indiaPath = 'india.csv'

header = ['name', 'location', 'address', 'location summary', 'destination', 'desctiption', 'highlights',
        'rooms', 'travellers type', 'available activities', 'hotel amenities', 'awards', 'score', 'rating',
        'additional info', 'attractions', 'eateries', 'trust you review', 'agoda.com review', 'booking.com data',
        'misc', 'review numbers', 'reviews1', 'reviews2', 'reviews3', 'reviews4', 'reviews6', 'reviews7', 'reviews8']

def saveData(dataList):
    print('Inside saveData')
    filePath = southAsiaPath
    print('FilePath', filePath)

    file = open(filePath, 'w', newline = '')
    out = csv.writer(file)
    out.writerow(header)
    try:
        for i in dataList:
            try:
                list = getInfoAsList(i)
                if list:
                    print('Writing: ', list[0])
                    out.writerow(list)
            except:
                print('Exception while saving for: ', i)
    except:
        print('Exception while saving')
    print('Data written to: ', filePath)
    file.close()


def saveTelegraphDataList(dataList):
    print('Inside saveTelegraphDataList')
    filePath = 'telegraph.csv'
    try:
        file = open(filePath, 'w', newline = '')
        out = csv.writer(file)
        telegraphHeaders = ['name', 'address', 'rating', 'description', 'facilities', 'reviews']
        out.writerow(telegraphHeaders)
        for i in dataList:
            try:
                list = getTelegraphInfoAsList(i)
                if list:
                    print('Writing: ', list[0])
                    out.writerow(list)
            except:
                print('Exception while saving for: ', i)
    except:
        print('Exception while saving')

    print('Data written to: ', filePath)
    file.close()


def getTelegraphInfoAsList(info):
    print('Inside getTelegraphInfoAsList')
    try:

        name = ''
        if 'name' in info and info['name']:
            name = info['name']

        address = ''
        if 'address' in info and info['address']:
            address = info['address']

        rating = ''
        if 'rating' in info and info['rating']:
            rating = info['rating']

        description = ''
        if 'description' in info and info['description']:
            description = info['description']

        facilities = []
        if 'facilities' in info and info['facilities']:
            facilities = info['facilities']

        reviews = []
        if 'reviews' in info and info['reviews']:
            reviews = info['reviews']

        list = [name, address, rating, description, facilities, reviews]

        return list

    except:
        print('Exception in getTelegraphInfoAsList')
        return None


def save(info):
    file = open(tempPath, 'w', newline = '')
    out = csv.writer(file)
    list = getInfoAsList(info)
    if list:
        out.writerow(header)
        out.writerow(list)
    file.close()


def helper(big, small, n, ctr):
    print('Inside helper')
    try:
        for i in range(n):
            print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&0    ', ctr)
            small.append(big[ctr])
            ctr = ctr + 1

        return ctr
    except:
        print('Exception in helper')

def getInfoAsList(info):
    try:
        name = ''
        if 'name' in info and info['name']:
            name = info['name']

        location = ''
        if 'location' in info and info['location']:
            location = info['location']

        address = ''
        if 'address' in info and info['address']:
            address = info['address']

        location_summary = ''
        if 'location_summary' in info and info['location_summary']:
            location_summary = info['location_summary']

        description = ''
        if 'description' in info and info['description']:
            description = info['description']

        highlights = ''
        if 'highlights' in info and info['highlights']:
            highlights = info['highlights']

        travellers = ''
        if 'traveller_type' in info and info['traveller_type']:
            travellers = info['traveller_type']

        trustMapReview = ''
        if 'trustYou_review' in info and info['trustYou_review']:
            trustMapReview = info['trustYou_review']

        numberReviews = ''
        if 'number_reviews' in info and info['number_reviews']:
            numberReviews = info['number_reviews']

        hotelAmenities = ''
        if 'hotel_amenities' in info and info['hotel_amenities']:
            hotelAmenities = info['hotel_amenities']

        availableActivities = ''
        if 'available_activities' in info and info['available_activities']:
            availableActivities = info['available_activities']

        awards = ''
        if 'awards' in info and info['awards']:
            awards = info['awards']

        rating = ''
        if 'rating' in info and info['rating']:
            rating = info['rating']

        score = ''
        if 'score' in info and info['score']:
            score = info['score']


        tripAdvisor = []
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        list8 = []
        if 'tripadvisor' in info and info['tripadvisor']:
            tripAdvisor = info['tripadvisor']
            length = len(tripAdvisor)
            n = int(length/8)
            ctr = 0
            l = [list1, list2, list3, list4, list5, list6, list7]
            for i in l:
                ctr = helper(tripAdvisor, i, n, ctr)

            for i in range(ctr, length):
                print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', i)
                list8.append(tripAdvisor[i])


        agoda = None
        if 'agoda' in info and info['agoda']:
            agoda = info['agoda']

        rooms = []
        if 'rooms' in info and info['rooms']:
            rooms = info['rooms']

        booking_data = ''
        if 'booking_data' in info and info['booking_data']:
            booking_data = info['booking_data']

        eateries = []
        if 'eateries' in info and info['eateries']:
            eateries = info['eateries']

        attractions = []
        if 'attractions' in info and info['attractions']:
            attractions = info['attractions']

        destination = ''
        if 'destination' in info and info['description']:
            destination = info['destination']

        additionalInfo = ''
        if 'additionalInfo' in info and info['additionalInfo']:
            additionalInfo = info['additionalInfo']

        misc = None
        if 'misc' in info and info['misc']:
            misc = info['misc']

        list = [name, location, address, location_summary, destination, description, highlights, rooms,
                travellers, availableActivities, hotelAmenities, awards, score, rating, additionalInfo,
                attractions, eateries, trustMapReview, agoda, booking_data, misc, numberReviews,
                list1, list2, list3, list4, list5, list6, list7, list8]

        return list

    except:
        print('Exception while parsing map into list')
        return None


