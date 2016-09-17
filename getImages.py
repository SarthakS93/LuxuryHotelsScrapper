from connection import connect, getRequest
from repository import saveImages, makeDirectory

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

            if not len(img_paths) > 0:
                return

            dir_name = makeDirectory(name, destination)

            if not dir_name:
                return

            ctr = 0
            for i in img_paths:
                try:
                    re = getRequest(i)

                    filename = name + str(ctr) + '.' + i.split('.')[-1]
                    ctr = ctr + 1

                    saveImage(filename, dir_name, re)
                except:
                    continue


if __name__ == '__main__':
    url = 'http://www.booking.com/hotel/th/banyan-tree-bangkok.en-gb.html'
    name = 'Banyan Tree'
    destination = 'Bangkok, Thailand'


