import csv

tempPath = 'temp.csv'
filePath = 'fsa.csv'


header = ['name', 'location', 'address', 'location summary', 'desctiption', 'highlights', 'rooms',
        'travellers type', 'available activities', 'hotel amenities', 'awards', 'score', 'rating',
        'attractions', 'eateries', 'trust you review', 'tripadvisor review', 'agoda.com review',
        'booking.com data', 'review numbers']

def saveData(dataList):
    file = open(filePath, 'w', newline = '')
    out = csv.writer(file)
    out.writerow(header)
    try:
        for i in dataList:
            try:
                list = getInfoAsList(i)
                if list:
                    out.writerow(list)
            except:
                print('Exception while saving for: ', i)
    except:
        print('Exception while saving')
    print('Data written to: ', filePath)
    file.close()


def save(info):
    file = open(tempPath, 'w', newline = '')
    out = csv.writer(file)
    list = getInfoAsList(info)
    if list:
        out.writerow(header)
        out.writerow(list)
    file.close()


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
        if 'tripadvisor' in info and info['tripadvisor']:
            tripAdvisor = info['tripadvisor']

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


        list = [name, location, address, location_summary, description, highlights,
                rooms, travellers, availableActivities, hotelAmenities, awards,
                score, rating, attractions, eateries, trustMapReview, tripAdvisor,
                agoda, booking_data, numberReviews]

        return list

    except:
        print('Exception while parsing map into list')
        return None


