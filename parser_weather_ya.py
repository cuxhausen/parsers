import requests
import urllib.request
from bs4 import BeautifulSoup
import lxml
import re
from time import sleep
from random import uniform
import mysql.connector
#"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/"
                #"apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#a = 3399

#while a <= 3499:
    #v = uniform(5, 7)
    #sleep(v)
#city = input("Введи название города: ")
#url = f'https://yandex.ru/pogoda/{city}'
url = 'https://yandex.ru/pogoda/artyn'
headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                  "96.0.4664.110 YaBrowser/22.1.0.2517 Yowser/2.5 Safari/537.36"
            }

r = urllib.request.urlopen(url)
soup = BeautifulSoup(r, "lxml")
#"html.parser"
#print(soup)
#r = requests.get(url, headers=headers)

#with open("index.html", "w", encoding="utf-8") as file:
    #file.write(r.text)

#print(r.text)
#soup = BeautifulSoup(r.text, 'lxml')
data = soup.find("div", class_="b-page__container").text
time = soup.find("time", class_="time fact__time").text
temp = soup.find("span", class_="temp__value temp__value_with-unit").text
cond = soup.find("div", class_="link__condition day-anchor i-bem").text
cond_temp = soup.find_all(class_="temp__value temp__value_with-unit")[2].text

wind = soup.find("span", class_="wind-speed").text
wind_direc = soup.find(class_="icon-abbr").text
#print(wind, wind_direc, type(wind, wind_direc))

hum = soup.find("div", class_="term term_orient_v fact__humidity").text
#print(hum, type(hum))

press = soup.find("div", class_="term term_orient_v fact__pressure").text.split()[0]
#print(press)

sunrise = soup.find("div", class_="sun-card__sunrise-sunset-info sun-card__sunrise-sunset-info_value_rise-time").text.\
    split('д')[1]
#print(sunrise, type(sunrise))

sunset = soup.find("div", class_="sun-card__sunrise-sunset-info sun-card__sunrise-sunset-info_value_set-time").text.\
    split('т')[1]
#print(sunset, type(sunset))

long_day = soup.find("div", class_="sun-card__day-duration-value").text
#print(long_day, type(long_day))

any_info = soup.find("div", class_="sun-card__text-info").text
print(any_info, type(any_info))
