from bs4 import BeautifulSoup
import requests

url = requests.get('https://www.wepro.uz/courses/').text

soup = BeautifulSoup(url, 'lxml')
course_cards = soup.find_all('ul')

for course in course_cards:
    coursen = course.text
    print(coursen)