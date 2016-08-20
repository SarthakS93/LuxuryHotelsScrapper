from googleSearch import search
from connection import connect
from urllib.parse import urljoin

def tripAdvisor(url):
    soup = connect(url)
    tag = soup.find(class_ = 'reviewSelector')
    div_tag = tag.find(class_ = 'quote isNew')
    link_tag = div_tag.find('a')
    if link_tag:
        link = link_tag.get('href')
        abs_url = urljoin(url, link)
        getReviews(abs_url)


def getReviews(url):
    soup = connect(url)
    divs = soup.find_all(class_ = 'innerBubble')
    list = []
    for div in divs:
        review = {}
        overview = div.find(property = 'name').text[1 : -1]
        review['overview'] = overview
        rating = div.find('img', class_ = 's50').get('alt')
        review_body = div.find('p', property = 'reviewBody').text[1 : -1]
        review['body'] = review_body
        review_points_tag = div.find_all(class_ = 'recommend_answer')
        review_points = {}
        if review_points_tag != None and len(review_points) > 0:
            for point in review_points_tag:
                key = point.find(class_ = 'recommend-description').text
                value = point.find('img').get('alt')
                review_points[key] = value
                review['points'] = review_points
        else:
            review['points'] = None

        list.append(review)







