"""
01 importing request modiual to get
            a request from the HTTP
02 importing a BeautifulSoup form bs4
            modiual for scraping
03 importing a pandas moduiual 
            for saving in cvs formats
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
# 01 connecting the request
page = requests.get('https://www.9anime.to/home')
soup = BeautifulSoup(page.content, 'html.parser')
# testing the connexction
# print(page)

# 02 getting information
GettingAnimeList = soup.find(class_='body tab-content')
animeName = GettingAnimeList.find(class_='anime-list')
for anime in animeName:
    gettingAnimeNames = animeName.findAll(class_='name')
    gettingAnimeEq = animeName.findAll(class_='tag ep')
    anime = animeName.findAll('a')


animeNameList = [textAnime.get_text() for textAnime in gettingAnimeNames]
animeEpList = [textAnime.get_text() for textAnime in gettingAnimeEq]

# 03 saving in cvs format

animeList = pd.DataFrame({
    'Name': animeNameList,
    'Episodes': animeEpList,
})
print(animeList)
save =  str(input("If you want to save press y: "))
if save == 'y' and 'Y':
    animeList.to_csv('animelist.csv')
else:
    pass
