from connection import connect
from repository import saveImages

def getAllBookingImages(url, name, destination):
    soup = connect(url)
    if soup:
        div = soup.find(id = 'photo_wrapper')
        if div:
            img_tags = div.find_all('img')
            img_paths = set()
            for i in img_tags:
                try:
                    link = i.get('src')
                    if not link:
                        link = i.get('data-lazy')
                except:
                    continue

            ctr = 0
            for i in img_paths:
                try:
                    re = getRequest(i)
                except:
                    continue

            filename = name + str(ctr) + '.' + i.split('.')[-1]
            ctr = ctr + 1

            saveImage()



