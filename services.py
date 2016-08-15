
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
    list = []
    for i in highlights_tag:
        list.append(i.text)
    info['highlights'] = list

