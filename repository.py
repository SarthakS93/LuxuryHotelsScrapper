import csv

tempPath = 'temp.csv'
filePath = 'fsa.csv'


header = ['name', 'location', 'address', 'location summary', 'desctiption',
         'highlights', 'travellers type', 'available activities', 'hotel amenities', 'awards',
         'score', 'rating', 'trust you review', 'tripadvisor review', 'review numbers']

def saveData(dataList):
    file = open(filePath, 'w', newLine = '')
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
    file = open(filePath, 'w', newline = '')
    out = csv.writer(file)
    list = getInfoAsList(info)
    if list:
        out.writerow(header)
        out.writerow(list)
    file.close()


def getInfoAsList(info):
    try:
        name = info['name']
        location = info['location']
        address = ''
        if info['address']:
            address = info['address']

        location_summary = ''
        if info['location_summary']:
            location_summary = info['location_summary']

        description = info['description']

        highlights = ''
        if info['highlights']:
            highlights = info['highlights']

        travellers = ''
        if info['traveller_type']:
            travellers = info['traveller_type']

        trustMapReview = ''
        if info['trustYou_review']:
            trustMapReview = info['trustYou_review']

        numberReviews = ''
        if info['number_reviews']:
            numberReviews = info['number_reviews']

        hotelAmenities = ''
        if info['hotel_amenities']:
            hotelAmenities = info['hotel_amenities']

        availableActivities = ''
        if info['available_activities']:
            availableActivities = info['available_activities']

        awards = ''
        if info['awards']:
            awards = info['awards']

        rating = ''
        if info['rating']:
            rating = info['rating']

        score = ''
        if info['score']:
            score = info['score']


        tripAdvisor = []
        if info['tripadvisor']:
            tripAdvisor = info['tripadvisor']


        list = [name, location, address, location_summary, description, highlights,
                travellers, availableActivities, hotelAmenities, awards,
                score, rating, trustMapReview, tripAdvisor, numberReviews]

        return list

    except:
        print('Exception while parsing map into list')
        return None


