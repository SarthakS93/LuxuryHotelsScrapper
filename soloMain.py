'''
This script is re
'''
from connection import connect
from tripAdvisorCrawler import startTripAdvisorSolo
from agodaCrawler import startAgodaSolo
from bookingCrawler import startBookingSolo
from repository import save

url = 'http://www.fivestaralliance.com/luxury-hotels/bangkok/banyan-tree-bangkok'


# call service functions to get particular data
def scrape(info, input_data):
    print('Inside scrape')
    try:
        print('asd')
        startTripAdvisorSolo(info, input_data)
        print('123')
        startAgodaSolo(info, input_data)
        print('123')
        startBookingSolo(info, input_data)
        info['location'] = input_data['location']
        save(info)
        # remove call to showOutput when in production
        #showOutput()
    except:
        print('Exception in scrape')

# show output, optional debugging function
def showOutput():
    print("**Output is as follows**")
    print(info)

# start to crawl a page
def crawl(name, location):
    print('Inside crawl')
    try:
        input_data = {'name': name, 'location': location}
        info = {}
        scrape(info, input_data)
    except:
        print('Exception in crawl')

# code to enable script to run independently
if __name__ == '__main__':
    #print(url)
    name = input('Enter name: ')
    location = input('Enter location: ')

    crawl(name, location)
