'''
Service layer, has functions to extract particular data
'''

from connection import connect


# get basic info such as title and location of hotel
def getBasicInfo(soup, info):
    print("Getting Basic Info")
    name_tag = soup.find(id = 'heading_title_hotel')
    info['name'] = name_tag.text
    location_tag = soup.find(id = 'title_location')
    info['location'] = location_tag.text


# get rating and description of hotel
def getOverview(soup, info):
    print("Getting Overview")
    rating_tag = soup.find(class_ = 'score')
    if rating_tag:
        info['rating'] = rating_tag.text
    score_tag = soup.find(class_ = 'value')
    if score_tag:
        info['score'] = score_tag.text
    description_tag = soup.find(class_ = 'hotel_content',
            itemprop = 'description')
    info['description'] = description_tag.text


# get absolute location details of hotel
def getLocation(soup, info):
    print("Getting Location")
    address_tag = soup.find(itemprop = 'address')
    info['address'] = address_tag.text
    location_summary_tag = soup.find(id = 'tab2')
    info['location_summary'] = location_summary_tag.text


# get reviews highlights of hotel
def getReviews(soup, info):
    print("Getting Reviews")
    highlights_tag = soup.find_all(id = 'detail-highlight')
    highlightsList = []
    for i in highlights_tag:
        highlightsList.append(i.text)
    info['highlights'] = highlightsList
    traveller_type_tag = soup.find_all(class_ = 'traveler-type')
    traveller_type_list = []
    for i in traveller_type_tag:
        traveller_type_list.append(i.text)
    info['traveller_type'] = traveller_type_list
    ext_tag = soup.find(id = 'trustyou_main_div')
    if ext_tag:
        newUrl = ext_tag.contents[0].get('src')
        newSoup = connect(newUrl)
        getRatingNumbers(newSoup, info)


# get rating for hotel
def getRatingNumbers(soup, info):
    print("Getting Rating Numbers")
    ratingValue_tags = soup.find_all(class_ = 'rating-value')
    ratingCount_tags = soup.find_all(class_ = 'rating-count')
    ratings = {}
    ratingValue_list = []
    ratingCount_list = []

    for i in range(len(ratingValue_tags)):
        ratingValue_list.append(ratingValue_tags[i].text[1 : ])
        ratingCount_list.append(ratingCount_tags[i].text)

    for i in range(len(ratingValue_list)):
        ratings[ratingValue_list[i]] = ratingCount_list[i]

    info['number_reviews'] = ratings


# get info of amenities of hotel
def getAmenitiesInfo(soup, info):
    print("Getting amenities info")
    hotelAmenities_tag = soup.find(id = 'detail-amenities-list1')
    hotelAmenities = hotelAmenities_tag.text
    info['hotel_amenities'] = hotelAmenities
    available_activities_tag = soup.find(id = 'detail-amenities-list2')
    if available_activities_tag:
        available_activities = available_activities_tag.text
        info['available_activities'] = available_activities


# get Awards info for hotel
def getAwardsInfo(soup, info):
    print("Getting Awards info")
    award_tag = soup.find(id = 'tab5')
    if award_tag == None:
        return
    else:
        list = []
        a_tags = award_tag.find_all('a')
        for i in range(1, len(a_tags)):
            list.append(a_tags[i].text)

        info['awards'] = list



