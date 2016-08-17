'''
Author: SarthakS93

This is the main python script, which will be run to get the data of Luxury Hotels.
Run this script from terminal by the following command:
    python3 main.py

The dependencies to run this project are:
    1. python3
    2. BeautifulSoup4
    3. Requests module

For any queries, mail to sarthaks93@gmail.com
'''

from fsaController import controller




def main():
    controller()


if __name__ == '__main__':
    print('Starting to Crawl')
    main()
