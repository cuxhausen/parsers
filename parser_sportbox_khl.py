import requests
from bs4 import BeautifulSoup
import lxml
import re
from datetime import date

# url = f'https://news.sportbox.ru/stats/{date.today()}'
url = 'https://news.sportbox.ru/stats/2021-12-10'


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 YaBrowser/22.1.0.2517 Yowser/2.5 Safari/537.36"
}


req = requests.get(url, headers=headers)

soup = BeautifulSoup(req.text, 'lxml')
lst = []
if soup.find('div', id='sport_2').find('div', class_='b-online__tour-title')\
    .find('a', href=re.compile('/Vidy_sporta/Hokkej/KHL/stats')) is not None:
    data = soup.find('div', id='sport_2').find('div', class_='b-onlines-box')\
        .find_all('a', class_='b-onlines-box__item')
    for i in data:
        if i.find('div', class_='b-onlines-box__comment') is not None:
            #print(
            lst.append(
                f"{i.find('div', class_='b-onlines-box__side_left').text.strip()} "
                f"{i.find('div', class_='count').text.strip()}"
                f"({i.find('div', class_='b-onlines-box__comment').text.strip().lstrip('(').rstrip(')')})"
                f" {i.find('div', class_='b-onlines-box__side_right').text.strip()}"
            )
        else:
            #print(
            lst.append(
                f"{i.find('div', class_='b-onlines-box__side_left').text.strip()} "
                f"{i.find('div', class_='count').text.strip()}"
                f" {i.find('div', class_='b-onlines-box__side_right').text.strip()}"
            )
        print("##############################")
else:
    print('В этот день нет матчей КХЛ')

print(lst)

