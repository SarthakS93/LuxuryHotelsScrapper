from connection import connect, getRequest
from repository import saveImage, makeDirectory

def getAllBookingImages(url, name, destination):
    print('Inside getAllBookingImages')
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

                    img_paths.add(link)
                except:
                    continue

            if len(img_paths) == 0:
                return

            dir_name = makeDirectory(name, destination)
            print('Directory name is: ', dir_name)
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
    url = 'http://www.booking.com/hotel/mv/kanuhura.en-gb.html'
    name = 'Kanuhura'
    destination = 'Neeloafaru Magu, Male, Maldives'
    print('Started getAllBookingImages')
    getAllBookingImages(url, name, destination)
    print('Done')

