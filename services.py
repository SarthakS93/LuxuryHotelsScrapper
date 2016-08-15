from connection import connect


def getBasicInfo(soup, info):
    print("Getting Basic Info")
    name_tag = soup.find(id = 'heading_title_hotel')
    info['name'] = name_tag.text
    location_tag = soup.find(id = 'title_location')
    info['location'] = location_tag.text

def getOverview(soup, info):
    print("Getting Overview")
    rating_tag = soup.find(class_ = 'score')
    info['rating'] = rating_tag.text
    score_tag = soup.find(class_ = 'value')
    info['score'] = score_tag.text
    description_tag = soup.find(class_ = 'hotel_content',
            itemprop = 'description')
    info['description'] = description_tag.text

def getLocation(soup, info):
    print("Getting Location")
    address_tag = soup.find(itemprop = 'address')
    info['address'] = address_tag.text
    location_summary_tag = soup.find(id = 'tab2')
    info['location_summary'] = location_summary_tag.text


def getReviews(soup, info):
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
    newUrl = ext_tag.contents[0].get('src')
    newSoup = connect(newUrl)
    getRatingNumbers(newSoup, info)


def getRatingNumbers(soup, info):
    ratingValue_tags = soup.find_all(class_ = 'rating-value')
    ratingCount_tags = soup.find_all(class_ = 'rating-count')
    ratings = {}
    ratingValue_list = []
    ratingCount_list = []

    for i in range(len(ratingValue_tags)):
        ratingValue_list.append(ratingValue_tags[i].text)
        ratingCount_list.append(ratingCount_tags[i].text)

    for i in range(len(ratingValue_list)):
        ratings[ratingValue_list[i]] = ratingCount_list[i]

    info['number_reviews'] = ratings


def getAmenitiesInfo(soup, info):
    hotelAmenities_tag = soup.find(id = 'detail-amenities-list1')
    hotelAmenities = hotelAmenities_tag.text
    info['hotel_amenities'] = hotelAmenities
    available_activities_tag = soup.find(id = 'detail-amenities-list2')
    available_activities = available_activities_tag.text
    info['available_activities'] = available_activities





