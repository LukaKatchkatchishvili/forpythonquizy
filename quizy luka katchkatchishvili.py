import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint
file=open('movies.csv','w',newline='\n')
file_obj=csv.writer(file)
file_obj.writerow(['title','seasons'])
h={'Accept-Language':'en-US'}
index=1
while index<=6:
    url='https://www1.movieorca.com/tv-show?page='+str(index)
    r=requests.get(url,headers=h)
    content=r.text
    soup=BeautifulSoup(content,'html.parser')
    yvelafilm=soup.find('div',class_="film_list-wrap")
    movies=yvelafilm.find_all('div',class_="flw-item")
    for each in movies:
        title=each.find('div',class_="film-detail film-detail-fix").h2.a.text
        seasons=each.find('div',class_="film-detail film-detail-fix").find('div',class_="fd-infor").find('span',class_="fdi-item").text
        print(title,seasons)
        file_obj.writerow([title,seasons])
    index+=1
    sleep(randint(15,20))