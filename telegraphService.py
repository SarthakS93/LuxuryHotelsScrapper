from connection import connect, getNewSoup


def getReviews(soup, info):
    newMarkup_tag = soup.find_all(class_ = 'js-tabs')
    newMarkup = newMarkup_tag[1].contents
    newMarkup_string = newMarkup[0] + str(newMarkup[1]) + newMarkup[2]
    miniSoup = getNewSoup(newMarkup_string)
    container = miniSoup.find_all(class_ = 'review-rating__container')
    for tag in container:
        miniMap = {}
        property_heading_tag = tag.find(class_ = 'review-rating__heading')
        property_heading = property_heading_tag.text
        property_body_tag = tag.find(class_ = 'review-rating__description')
        property_body = processString(property_body_tag.text)
        miniMap['property'] = property_body
        property_rating_tag = tag.find(class_ = 'review-rating__rate')
        if property_rating_tag:
            property_rating = property_rating_tag.text
            miniMap['rating'] = property_rating
        else:
            miniMap['rating'] = None

        info[property_heading] = miniMap



def getBasicInfo(soup, info):
    name_tag = soup.find(class_ = 'product-card__name')
    name = name_tag.text[1 : ]
    info['name'] = name
    address_tag = soup.find(class_ = 'product-card__address')
    address = address_tag.get('content')
    info['address'] = address
    rating_tag = soup.find(class_ = 'product-card__rating__rate')
    rating = rating_tag.text
    info['rating'] = rating
    description_tag = soup.find(class_ = 'product-card__overview')
    description = processString(description_tag.text)
    info['description'] = description


def processString(string):
    string = string[ : -1]
    string = string[1 : ]
    return string
