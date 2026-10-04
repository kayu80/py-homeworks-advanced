import re

import requests
import bs4

KEYWORDS = ['дизайн', 'фото', 'web', 'python']


pattern = re.compile('|'.join(map(re.escape, KEYWORDS)), re.IGNORECASE)

url = 'https://habr.com/ru/articles/'
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, 'lxml')

for article in soup.find_all('article'):

    text = article.get_text(' ')

    if pattern.search(text):
        title_tag = article.find('a', class_='tm-title__link')
        title = title_tag.get_text(' ', strip=True)
        href = 'https://habr.com' + title_tag['href']
        date = article.find('time')['datetime'][:10]

        print(f'{date} – {title} – {href}')



