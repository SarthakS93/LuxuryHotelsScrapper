
def getBasicInfo(soup, info):
    print("Getting Basic Info")
    name_tag = soup.find(id = 'heading_title_hotel')
    info['name'] = name_tag.text
    location_tag = soup.find(id = 'title_location')
    info['location'] = location_tag.text
