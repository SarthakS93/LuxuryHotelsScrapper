
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
