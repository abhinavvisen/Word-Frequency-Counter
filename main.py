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
            
            
 def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = '!@#$%^&*()_+'

        for i in range(0,len(symbols)):
            word = word.replace(symbols[i],"")
        if len(word)>0:
            clean_word_list[word]

           

start('give the url here')
