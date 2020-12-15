#!/usr/bin/python3
from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
import time
import pytz
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")    
mydb = myclient["my_database"]
mycol = mydb["air_polution"]
time_th = pytz.timezone('Asia/Bangkok')

def requests():
    url = 'https://aqicn.org/city/thailand/bangkok/national-housing-authority-huaykwang/'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    value = html_soup.find_all('td', {'id':'cur_pm25'})                                 # Data of pm2.5 at bu
    dt = str(datetime.now(time_th))                                                 # Last update 
    address = html_soup.find('div', {'class':'aqiwgt-table-title'}).find('a').text      # Address
    polution_status = html_soup.find('div',{'id':'aqiwgtinfo'}).text
    pm1_0 = html_soup.find('td', {'id':'cur_pm10'}).text
    pm2_5 = value[0].text
    mydict = {'datetime':str(dt),'address':str(address),'pm25':int(pm2_5),'pm10':int(pm1_0),'polution_lv':str(polution_status)}
    mycol.insert_one(mydict)
    print(mydict)

while True:
    requests()
    time.sleep(10)