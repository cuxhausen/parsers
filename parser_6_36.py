
from time import sleep

import urllib.request

from bs4 import BeautifulSoup

from random import uniform

import mysql.connector

import re

def get_html(url):
    r = urllib.request.urlopen(url)
    return r.read()

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    
    number_edition = soup.find('div', id='content').find('h1').text.strip().split('№')[1][1:].rsplit(',')[:-1]

    date = soup.find('div', id='content').find('h1').text.strip().split('№')[1].split(',')[1][15:-8]

    time = soup.find('div', id='content').find('h1').text.strip()[-5:]
    
    number_1 = soup.find(class_='girl1').find('p').text.strip()

    number_2 = soup.find(class_='girl2').find('p').text.strip()

    number_3 = soup.find(class_='girl3').find('p').text.strip()

    number_4 = soup.find(class_='girl4').find('p').text.strip()

    number_5 = soup.find(class_='girl5').find('p').text.strip()

    number_6 = soup.find(class_='girl6').find('p').text.strip()
    # Получаем нужную строку со страницы
    number_of_tickets = soup.find(class_='col drawing_details').find('tr').text.strip()[46:]
    # Удаляем все пробелы из строки
    number_of_tickets = re.sub(r"\s+", "", number_of_tickets, flags=re.UNICODE)
    # Получаем нужную строку со страницы
    super_prize = soup.find(class_='col drawing_details').find('table').text.strip()[115:]
    # Удаляем все пробелы из строки
    super_prize = re.sub(r"\s+", "", super_prize, flags=re.UNICODE)

    # Ищем нужное
    while super_prize[0] != '.':
        super_prize = super_prize[1:]

    super_prize = super_prize[1:]

    # Ищем нужное (продолжаем)
    st = ''
    while super_prize[0] != 'В':
        st += super_prize[0]
        super_prize = super_prize[1:]

    super_prize = st
    
    return ''.join(number_edition), date, time, number_1, number_2, number_3, number_4, number_5, number_6, number_of_tickets, super_prize

def main():
    try:
        dbconfig = {'host': '127.0.0.1',
                    'user': 'user',
                    'password': '123',
                    'database': '6_36db',}
        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("select max(number_edition) from data")
        a = int(str(list(cursor.fetchone()))[1:-1])
        cursor.close()
        conn.close() 
        while a <= 50000:
            x = str(a + 1)
            url = 'https://www.stoloto.ru/6x36/archive/' + x
            s = uniform(1, 2)
            sleep(s)
            dbconfig = {'host': '127.0.0.1',
                        'user': 'user',
                        'password': '123',
                        'database': '6_36db',}
            conn = mysql.connector.connect(**dbconfig)
            cursor = conn.cursor()
            _SQL = """insert into data
                    (number_edition, date, time, number_1,
                    number_2, number_3, number_4, number_5, number_6,
                    number_of_tickets, super_prize ) values
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(_SQL, get_data(get_html(url)))
            conn.commit()
            cursor.close()
            conn.close()
            a = a + 1
    except AttributeError:
        print ('Готово')
        p = uniform(5, 7)
        sleep(p)
    
if __name__ == '__main__':
    main()
