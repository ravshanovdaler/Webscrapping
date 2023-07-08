from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content , 'lxml')
    course_cards = soup.find_all('div', class_='card')
    idfind = soup.find('p', id='hellos')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[2]

        print(idfind.text)
        print(f'{course_name} costs {course_price}')