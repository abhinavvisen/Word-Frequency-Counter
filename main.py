import requests
from bs4 import BeautifulSoup

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)

    for post_text in soup.findAll('a',{'class':'index-tiles'})
        content = post_text.string

        words = content.lower.split()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)

start('give the url here')
