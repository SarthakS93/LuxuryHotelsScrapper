import os, csv

def check(filename):
    print('Inside check')

    folders_list = os.listdir('pics/')

    file = open(filename, 'r')
    reader = csv.reader(file)

    data_list = list(reader)
    ctr = 1
    for i in data_list:
        name = i[0]
        location = i[1]

        temp = 0

        for j in folders_list:
            if name in j and location in j:
                temp = 1
                break

        if temp == 0:
            print('$$$$', ctr, name, location)

        ctr += 1


if __name__ == '__main__':
    print('Starting')
    check('thailand.csv')
    print('End')


