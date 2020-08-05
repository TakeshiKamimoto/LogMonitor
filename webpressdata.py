#coding: utf-8

import re
import requests
from bs4 import BeautifulSoup

def readData():

    URL2 = 'http://web.sugiyama-u.ac.jp/~yamane/honkoma/Vantage_Pro_Plus.htm'
    r = requests.get(URL2)
    html = r.text.encode(r.encoding)
    s = BeautifulSoup(html, 'lxml')
    weathernow = s.find_all('tr')
    pres_m = re.sub('hPa','',weathernow[5].select('small')[2].text)

    return pres_m
    
if __name__ == '__main__':
    print(readData())