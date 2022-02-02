import requests
from bs4 import BeautifulSoup
import lxml
import re
from time import sleep
from random import uniform
import mysql.connector

a = 1

while a <= 5:
    url = 'https://www.stoloto.ru/6x36/archive/' + str(a)
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/"
                  "apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                  "96.0.4664.110 YaBrowser/22.1.0.2517 Yowser/2.5 Safari/537.36"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    data = soup.find("div", id="content")
    number_edition = data.find('h1').text.split('№')[1][1:].rsplit(',')[0]
    date = data.find('h1').text.split('от')[1][1:].rsplit(' в')[0]
    time = data.find('h1').text.split('в ')[1]
    number_1 = data.find(class_="girl1").text.strip()
    number_2 = data.find(class_="girl2").text.strip()
    number_3 = data.find(class_="girl3").text.strip()
    number_4 = data.find(class_="girl4").text.strip()
    number_5 = data.find(class_="girl5").text.strip()
    number_6 = data.find(class_="girl6").text.strip()
    number_of_tickets = data.find(class_="numeric").text
    number_of_tickets = re.sub(r"\s+", "", number_of_tickets, flags=re.UNICODE)
    super_prize = data.find_all(class_="numeric")[2].text
    super_prize = re.sub(r"\s+", "", super_prize, flags=re.UNICODE)

    dbconfig = {'host': '45.81.225.246',
                'user': 'cuxhausen',
                'password': '04101957Pa!?',
                'database': '6_36db',}
    conn = mysql.connector.connect(**dbconfig)
    cur = conn.cursor()
    _SQL = """insert into data
            (number_edition, date, time, number_1,
            number_2, number_3, number_4, number_5, number_6,
            number_of_tickets, super_prize) values
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    cur.execute(_SQL, (number_edition, date, time, number_1, number_2, number_3, number_4, number_5, number_6,
                number_of_tickets, super_prize))
    conn.commit()
    cur.close()
    conn.close()
    a = a + 1
    v = uniform(2, 3)
    sleep(v)
