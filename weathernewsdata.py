#coding: utf-8

import re
import requests
from bs4 import BeautifulSoup

def readData():
    URL = 'https://weathernews.jp/onebox/tenki/tokyo/13108/'

    r = requests.get(URL)
    html = r.text.encode(r.encoding)
    s = BeautifulSoup(html, 'lxml')
    weathernow = s.find('ul', class_='weather-now__ul')
    measdata = weathernow.find_all('li')
    t = re.sub("℃",'',measdata[1].contents[1])
    h = re.sub('%','',measdata[2].contents[1])
    p = re.sub('hPa','',measdata[3].contents[1])
    
    #print(t + ', ' + h + ', ' + p)

    return (t, h, p)
    
if __name__ == '__main__':
    readData()