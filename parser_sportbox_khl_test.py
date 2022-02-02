import requests
from bs4 import BeautifulSoup
import lxml
import re
from datetime import date

# url = f'https://news.sportbox.ru/stats/{date.today()}'
url = 'https://news.sportbox.ru/stats/2022-01-22'


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 YaBrowser/22.1.0.2517 Yowser/2.5 Safari/537.36"
}


req = requests.get(url, headers=headers)

soup = BeautifulSoup(req.text, 'lxml')
if soup.find('div', id='sport_2').find('div', class_='b-online__tour-title')\
    .find('a', href=re.compile('/Vidy_sporta/Hokkej/KHL/stats')) is not None:
    data = soup.find('div', id='sport_2').find('div', class_='b-onlines-box')\
        .find_all('a', class_='b-onlines-box__item')
    for i in data:
        print(i.find('div', class_='b-onlines-box__side_left').text.strip())
        print(i.find('div', class_='b-onlines-box__side_left').find('i', class_='b-onlines-box__side_flag').text)
        print(i.find('div', class_='count').text.strip())
        print(i.find('div', class_='b-onlines-box__side_right').text.strip())
        print(i.find('div', class_='b-onlines-box__side_right').find('i', class_='b-onlines-box__side_flag').text)
        if i.find('div', class_='b-onlines-box__comment') is not None:
            print(i.find('div', class_='b-onlines-box__comment').text.strip())
        else:
            continue
        print('#####################################################################')
else:
    print('В этот день нет матчей КХЛ')

