from googleSearch import agodaSearch
from connection import connect
from urllib.parse import urljoin
import csv

def agoda(url, info):
    print('Inside Agoda.com', url)
    try:
        soup = connect(url)
        if soup:
            panel = soup.find(id = 'abouthotel-panel')
            if panel:
                script_tag = panel.find('script')
                if script_tag:
                    doc_script = script_tag.text
                    snippets = doc_script.split('"')
                    if snippets and len(snippets) >= 2:
                        link = snippets[1]
                        abs_url = urljoin(url, link)
                        newSoup = connect(abs_url)
                        if newSoup:
                            facilities = getFacilities(newSoup)
                            extraInfo = getUsefulInfo(newSoup)

                            agoda = {'facilities' : facilities, 'useful info' : extraInfo}

                            info['agoda'] = agoda
                            #showOutput(info)

    except:
        print('Exception in tripAdvisor')

def getFacilities(soup):
    print('Getting Facilities')
    try:
        div = soup.find(id = 'abouthotel-features')
        if div:
            small_div = div.find(class_ = 'col-xs-9')
            container = small_div.find_all(class_ = 'sub-section')
            if container and len(container) > 0:
                facilities = []
                for item in container:
                    heading_tag = item.find('h3')
                    heading = heading_tag.text
                    list_items = item.find_all('li')
                    features_list = []
                    for i in list_items:
                        text_tag = i.find('span')
                        text = text_tag.text
                        features_list.append(text)


                    feature = {heading : features_list}
                    facilities.append(feature)

                return facilities

        return None

    except:
        print('Exception in getFacilities')
        return None

def getUsefulInfo(soup):
    print('Getting Useful info')
    try:
        div = soup.find(id = 'abouthotel-usefulinfo')
        if div:
            smaller_div = div.find(class_ = 'col-xs-9')
            if smaller_div:
                container = smaller_div.find('div')
                items = container.find_all('div')
                useFullInfoList = []
                for item in items:
                    text = item.text
                    text = processString(text)
                    useFullInfoList.append(text)

                return useFullInfoList

        return None

    except:
        print('Exception in getUsefulInfo')
        return None

def processString(text):
    print('Inside processString')
    try:
        text = text[ : -1]
        for i in range(len(text)):
            if text[i] >= 'A' and text[i] <= 'Z':
                string = text[i : ]
                break
        return string
    except:
        print('Exception in processString')
        return text


def showOutput(info):
    print('*********output************')
    print(info)

def startAgoda(info):
    queryDictionary = {'name' : info['name'], 'location' : info['location']}
    searchString = 'agoda.com' + ' ' + info['name'] + ' ' + info['location']
    queryDictionary['search'] = searchString
    url = None
    i = 0
    while(i < 10):
        if url == None:
            url = agodaSearch(queryDictionary)
            i = i + 1
        else:
            break


    if url:
        agoda(url, info)
    else:
        print('Agoda.com could not be found for: ', info['search'])

if __name__ == '__main__':
    name = input('Enter name: ')
    loc = input('Enter loc: ')
    q = {}
    q['name'] = name
    q['location'] = loc
    q['search'] = 'agoda.com' + ' ' + name + ' ' + loc
    url = None
    while(url == None):
        url = agodaSearch(q)
    if url:
        info = {}
        agoda(url, info)
