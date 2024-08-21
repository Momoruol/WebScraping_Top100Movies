import requests as r
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = r.get(URL)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(name='h3', class_='title')

movie_titles = [filme.getText() for filme in title]
movies_correct_order = movie_titles[::-1]


with open('movies.txt', mode='w', encoding='utf-8')as file:
    for movie in movies_correct_order:
        file.write(f'{movie}\n')