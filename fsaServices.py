'''
Service layer, has functions to extract particular data
'''

from connection import connect


# get basic info such as title and location of hotel
def getBasicInfo(soup, info):
    print("Getting Basic Info")
    try:
        name_tag = soup.find(id = 'heading_title_hotel')
        info['name'] = name_tag.text
        location_tag = soup.find(id = 'title_location')
        info['location'] = location_tag.text
    except:
        print('Exception in getBasicInfo')

# get rating and description of hotel
def getOverview(soup, info):
    print("Getting Overview")
    try:
        rating_tag = soup.find(class_ = 'score')
        if rating_tag:
            info['rating'] = rating_tag.text
        score_tag = soup.find(class_ = 'value')
        if score_tag:
            info['score'] = score_tag.text
        description_tag = soup.find(class_ = 'hotel_content',
                itemprop = 'description')
        info['description'] = description_tag.text
    except:
        print('Exception in getOverview')

# get absolute location details of hotel
def getLocation(soup, info):
    print("Getting Location")
    try:
        address_tag = soup.find(itemprop = 'address')
        info['address'] = address_tag.text
        location_summary_tag = soup.find(id = 'tab2')
        info['location_summary'] = location_summary_tag.text
    except:
        print('Exception in get location')


# get reviews highlights of hotel
def getReviewsHighlights(soup, info):
    print("Getting Reviews & Highlights")
    try:
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
            getReviews(newSoup, info)

    except:
        print('Exception in getReviewHighlights')


# get reviews for hotel
def getReviews(soup, info):
    print('Getting Reviews')
    try:
        a_tag = soup.find('a')
        if a_tag:
            link = a_tag.get('href')
            print('TempSoup source', link)
            tempSoup = connect(link)
            iframe_tags = tempSoup.find_all('iframe')
            #print(iframe_tags)
            if iframe_tags != None and len(iframe_tags) > 0:
                tag = None
                if len(iframe_tags) == 1:
                    tag = iframe_tags[0]
                else:
                    tag = iframe_tags[1]

                print('iframe source', tag.get('src'))
                newSoup = connect(tag.get('src'))
                getDiscreteReviews(newSoup, info)
    except:
        print('Exception in getReviews')

def getDiscreteReviews(soup, info):
    try:
        print('Getting Discrete Reviews')
        main_description_tag = soup.find(class_ = 'summary')
        main_description = main_description_tag.text
        main_description = processString(main_description)

        main_div = soup.find(class_ = 'gtk')
        ul = main_div.find('ul')
        li = ul.find_all('li')
        trustMap = {}
        overview = {}
        for tag in li:
            heading = tag.find('h2').text
            body = tag.find(class_ = 'snippet').find_all('span')
            body_text = []
            for b in body:
                body_text.append(b.text)
            overview[heading] = body_text

        trustMap['overview'] = overview

        section = soup.find('section', class_ = 'review-highlights')
        divs = section.find_all(class_ = 'category')
        for div in divs:
            key = div.find(class_ = 'category-stats').find('h2').text
            rating = div.find(class_ = 'score').text
            reviews = []
            review_spans = div.find(class_ = 'category-details').find_all('span')
            for span in review_spans:
                reviews.append(span.text)

            values = {'reviews' : reviews, 'rating' : rating}
            trustMap[key] = values

        print("The trustMap reviews are: ", trustMap)

    except:
        print('Not enogh data for trust you reviews')
        info['trustYou_review'] = None
        return

    info['trustYou_review'] = trustMap




# get rating for hotel
def getRatingNumbers(soup, info):
    print("Getting Rating Numbers")
    try:
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

    except:
        print('Exception in getRatingNumbers')

# get info of amenities of hotel
def getAmenitiesInfo(soup, info):
    print("Getting amenities info")
    try:
        hotelAmenities_tag = soup.find(id = 'detail-amenities-list1')
        hotelAmenities = hotelAmenities_tag.text
        info['hotel_amenities'] = hotelAmenities
        available_activities_tag = soup.find(id = 'detail-amenities-list2')
        if available_activities_tag:
            available_activities = available_activities_tag.text
            info['available_activities'] = available_activities
    except:
        print('Exception in getAmenitiesInfo')

# get Awards info for hotel
def getAwardsInfo(soup, info):
    print("Getting Awards info")
    try:
        award_tag = soup.find(id = 'tab5')
        if award_tag == None:
            return
        else:
            list = []
            a_tags = award_tag.find_all('a')
            for i in range(1, len(a_tags)):
                list.append(a_tags[i].text)

            info['awards'] = list
    except:
        print('Exception in getAwardsInfo')

def processString(string):
    string = string[ : 0]
    string = string[1 : ]

    return string
