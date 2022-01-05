import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://www.fpx.de/fp/Disney/Scripts/SleepingBeauty/sb.html'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
ch = soup.find_all('dt')
sp = soup.find_all('dd')

sp1 = []
sp2 = []

for a in ch:
    b = (str(a.text)[:-2]).replace(' ', '')
    sp1.append(b)

for a in sp:
    b = (str(a.text)).replace('\n', ' ').replace('\t', '')
    reP = '(\[[^\]]*\]|\([^\)]*\))'
    reS = '\s+'
    r = re.sub(reS, ' ', re.sub(reP, ' ', b.replace('\xa0',' '))).strip()
    sp2.append(r)

pd.options.display.max_rows = 444
df = pd.DataFrame(list(zip(sp1, sp2)), columns = ['Character', 'Speech'])
blankIndex=[''] * len(df)
df.index=blankIndex
print(df)
