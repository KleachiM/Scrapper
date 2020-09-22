import re
import requests
from bs4 import BeautifulSoup

KEYWORDS = ['Google', 'фото', 'web', 'python', 'Agile']
keywords = set(KEYWORDS)

response = requests.get('https://habr.com/ru/all/')
bs = BeautifulSoup(response.text, 'html.parser')

articles = bs.find_all('article', class_='post')
for article in articles:
    res = article.find('div', class_='post__text_v1')
    if res:
        hub_words = set(re.findall(r'\w+', res.text))
        if keywords.intersection(hub_words):
            title = article.find('a', class_='post__title_link').text
            link = article.find('a', class_='post__title_link').attrs.get('href')
            date = article.find('span', class_='post__time').text
            print(f'Дата: {date}. Заголовок: {title}. Ссылка: {link}')

