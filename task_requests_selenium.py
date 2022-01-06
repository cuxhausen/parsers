import requests
import hashlib
from random import choice, randrange
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
}

#def get_page(url):
#    s = requests.Session()
#    response = s.get(url=url, headers=headers)

#    with open("index.html", "w") as file:
 #       file.write(response.text)


#def get_json(url):
#    s = requests.Session()
#    response = s.get(url=url, headers=headers)

#    with open("result.json", "w") as file:
#       json.dump(response.json(), file, indent=4, ensure_ascii=True)



def collect_data():
    s = requests.Session()
    response = s.get(url = "https://line14.bkfon-resources.com/live/currentLine/ru", headers=headers)

    id_footbal = 0
    pairs_players = []
    data = response.json()
    for i in data['sports']:
        if i['name'] == 'Футбол' and i['kind'] == 'sport':
            id_footbal = i['id']
            break

    if id_footbal != 0:
        ligaID_footbal = []
        for i in data['sports']:
            if 'parentId' in i:
                if i['parentId'] == id_footbal:
                    ligaID_footbal.append(i['id'])

    if len(ligaID_footbal) > 0:
        for i in data['events']:
            if i['sportId'] in ligaID_footbal and i['level'] == 1:
                pairs_players.append(i['team1'] + ' - ' + i['team2'])
                #print(i['team1'] + ' - ' + i['team2'])
    #print(pairs_players)


    pairs_dict = {}
    for i in data['events']:
        for p in pairs_players:
            #print(p)
            p1 = (p.split('- '))[0].strip ()
            p2 = (p.split('- '))[1].strip ()
            #print(p1)
            #print(p2)
            if i.get('team1') != p1 and i.get('team2') != p2:
                continue
            else:
                #print(i.get('id'), type(i.get('id')))
                #pairs_dict[i.get('id')] = p
                pairs_dict[hashlib.md5(str(i.get('id')).encode()).hexdigest()] = p
                #print(pairs_dict)

    
    dt = list(pairs_dict.keys())
    key = dt[randrange(len(dt))]

    #print(pairs_dict)
    #print(pairs_dict[key])
    return pairs_dict[key]


def browser():
    options = webdriver.FirefoxOptions()

    options.set_preference(
        "general.useragent.override", 
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
    )

    driver = webdriver.Firefox(
        service=Service(r"D:\programming\python\programs\parsers\geckodriver.exe"),
            options=options,
    )


    try:
        driver.get("https://fonbet.ru/")
        time.sleep(60)

        search_input = driver.find_element_by_class_name("search__link").click()
        time.sleep(5)

        search_input = driver.find_element_by_class_name("search__input--DF661")
        time.sleep(5)

        search_input.send_keys(collect_data())
        time.sleep(20)

        search_input = driver.find_element_by_class_name("search-result__event-name--3Qfnn").click()
        time.sleep(20)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    #get_page(url = "https://line14.bkfon-resources.com/live/currentLine/ru")
    #get_json(url = "https://line14.bkfon-resources.com/live/currentLine/ru")
    #collect_data()
    browser()
    print(collect_data())


if __name__ == '__main__':
    main()
