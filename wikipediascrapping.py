#import all modules
from bs4 import BeautifulSoup
import requests
import pyttsx3
#Get the url which I want scrap
url = requests.get('https://en.wikipedia.org/wiki/Artificial_intelligence').text


#Convert the url to xml
soup = BeautifulSoup(url, 'lxml')


#Settings of speech
text_speech = pyttsx3.init()
text_speech.setProperty('rate', 140)
voices = text_speech.getProperty('voices')
text_speech.setProperty('voice', voices[1].id)

#find <span> which is classed mw-page-title-main from HTML of website
title = soup.find('span', class_='mw-page-title-main').text
#find <div> which is classed noprint from HTML of website
source = soup.find('div', class_='noprint').text
#Find all <p> tags of the website
information = soup.find_all('p')


theme  = f"Now we are going to talk about {title}!"
#Say theme variable
text_speech.say(theme)
#wait till the speech ends
text_speech.runAndWait()
sources = f"The information given {source}"
#Say theme variable
text_speech.say(sources)
#wait till the speech ends
text_speech.runAndWait()



for info in information:
    info = info.text
    print(info)
    text_speech.say(info)
    text_speech.runAndWait()