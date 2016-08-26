from connection import connect, getNewSoup


def getReviews(soup, info):
    print('Inside getReviews')
    try:
        newMarkup_tag = soup.find_all(class_ = 'js-tabs')
        if newMarkup_tag:
            newMarkup = newMarkup_tag[1].contents
            if newMarkup:
                newMarkup_string = newMarkup[0] + str(newMarkup[1]) + newMarkup[2]
                miniSoup = getNewSoup(newMarkup_string)
                if miniSoup:
                    container = miniSoup.find_all(class_ = 'review-rating__container')
                    data = []
                    for tag in container:
                        miniMap = {}

                        property_heading_tag = tag.find(class_ = 'review-rating__heading')
                        property_heading = ''
                        if property_heading_tag:
                            property_heading = property_heading_tag.text

                        property_body_tag = tag.find(class_ = 'review-rating__description')
                        if property_body_tag:
                            property_body = processString(property_body_tag.text)
                            miniMap['description'] = property_body

                        property_rating_tag = tag.find(class_ = 'review-rating__rate')
                        if property_rating_tag:
                            property_rating = property_rating_tag.text
                            miniMap['rating'] = property_rating
                        else:
                            miniMap['rating'] = None

                        if property_heading != '':
                            miniMap['property'] = property_heading
                            data.append(miniMap)

                    return data

        print('Nothing found in getReviews')
        return None

    except:
        print('Exception in getReviews')


def getFacilities(soup):
    print('Inside getFacilities')
    try:
        items = soup.find_all(class_ = 'review-rating__facility')
        if items:
            list = []
            for i in items:
                list.append(i.text)

            return list

        print('Nothing found in getFacilities')
        return None
    except:
        print('Exception in getFacilities')
        return None



def getBasicInfo(soup, info):
    print('Inside getBasicInfo')
    try:
        name_tag = soup.find(class_ = 'product-card__name')
        if name_tag:
            name = name_tag.text[1 : ]
            info['name'] = name

        address_tag = soup.find(class_ = 'product-card__address')
        if address_tag:
            address = address_tag.get('content')
            info['address'] = address

        rating_tag = soup.find(class_ = 'product-card__rating__rate')
        if rating_tag:
            rating = rating_tag.text
            info['rating'] = rating

        description_tag = soup.find(class_ = 'product-card__overview')
        if description_tag:
            description = processString(description_tag.text)
            info['description'] = description

    except:
        print('Exception in getBasicInfo')

def processString(string):
    string = string[1 : -1]
    string = string.replace('\xa0', '')
    string = string.replace('\n', '')
    return string
