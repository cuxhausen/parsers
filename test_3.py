from time import sleep
import requests
from bs4 import BeautifulSoup
from random import uniform
import mysql.connector
import re

#a = 3920

#while a <= 3999:
url = 'https://www.stoloto.ru/6x45/archive/6368'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/"
                "apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                "96.0.4664.110 YaBrowser/22.1.0.2517 Yowser/2.5 Safari/537.36"
        }

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
data = soup.find("div", id="content")

#number_of_tickets = data.find(class_="numeric").text
#number_of_tickets = re.sub(r"\s+", "", number_of_tickets, flags=re.UNICODE)

#number_of_combinations = data.find_all(class_="numeric")[1].text
#number_of_combinations = re.sub(r"\s+", "", number_of_combinations, flags=re.UNICODE)

super_prize = data.find_all(class_="numeric")[3].text.strip()
super_prize = re.sub(r"\s+", "", super_prize, flags=re.UNICODE)

print(super_prize, type(super_prize))