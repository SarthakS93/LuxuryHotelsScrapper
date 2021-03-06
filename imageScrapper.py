import csv
from getImages import getAllBookingImages
from googleSearch import bookingSearch


filename = 'temp.csv'

def readFile():
    print('Inside readFile')
    try:
        file = open(filename, 'r')
        reader = csv.reader(file)
        data = list(reader)

        newList = []
        for i in data:
            tuple = (i[0], i[1])
            newList.append(tuple)

        newList = newList[1 : ]
        return newList
    except:
        print('Exception in readFile')
        return None


def start():
    print('Inside start')
    try:
        data = readFile()

        for i in data:
            info = {'name' : i[0], 'location' : i[1]}
            searchString = 'booking.com' + ' ' + info['name'] + ' ' + info['location']
            print('searching: %%% ', searchString)
            queryDictionary = {'search' : searchString}

            url = None
            url = bookingSearch(queryDictionary)

            if url:
                getAllBookingImages(url, i[0], i[1])
            else:
                print('Booking.com could not be found for: ', i[0] + ', ' + i[1])
    except:
        print('Exception in start')


if __name__ == '__main__':
    print('Starting the srcipt')
    start()
    print('Finished')
