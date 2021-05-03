# -*- coding: utf-8 -*-
"""
Created on Sat May  1 22:32:12 2021

@author: C.F_Lin
"""

#from bs4 import BeautifulSoup
#from urllib.request import urlopen
#import csv
from datetime import timedelta
from selenium import webdriver
from time import sleep
#import requests
from pandas import to_datetime
import os

quote_page = "https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html"
os.chdir('C:/Users/C.F_Lin/Downloads')

location = "C:/Users/C.F_Lin/AppData/Local/Programs/Opera/75.0.3969.243/Opera.exe"#69.0.3686.95#65.0.3467.78
options = webdriver.ChromeOptions()
options.binary_location = location
driver = webdriver.Opera(options=options,executable_path="C:/Users/C.F_Lin/Desktop/operadriver.exe")
driver.get(quote_page)
driver.implicitly_wait(300)
sleep(1)

#%%

Banking = driver.find_element_by_name('type')
Banking.send_keys('金融保險')
StartDate = '2020-12-31'
YearButton = driver.find_element_by_name('yy')
YearButton.send_keys(webdriver.common.keys.Keys.DOWN)
YearButton.send_keys(webdriver.common.keys.Keys.DOWN)
MonthButton = driver.find_element_by_name('mm')
DayButton = driver.find_element_by_name('dd')
Search = driver.find_element_by_css_selector('.search.button')
MonthButton.send_keys(StartDate.split("-")[1])
while 1:
    DayButton.send_keys(StartDate.split("-")[2])
    Search.click()
    sleep(3)
    Result = driver.find_element_by_id('result-message')
    Result_contents = Result.get_attribute('innerHTML')
    if Result_contents == ('很抱歉，沒有符合條件的資料!'):
        pass
    else:
        CSVButton = driver.find_element_by_class_name('csv')
        CSVButton.click()
        sleep(3)
    StartDate = str(to_datetime(StartDate)-timedelta(1))
    print(StartDate)
    if StartDate.split(" ")[0].split("-")[2]=="01":
        MonthButton.send_keys(webdriver.common.keys.Keys.UP)
    if StartDate.split(" ")[0]=="2019-01-01":
        YearButton.send_keys(webdriver.common.keys.Keys.DOWN)
        MonthButton.send_keys(12)
    if StartDate.split(" ")[0]=="2018-01-01":
        YearButton.send_keys(webdriver.common.keys.Keys.DOWN)
        MonthButton.send_keys(12)
    if StartDate.split("-")[0]=="2017":
        break

#%%

from pandas import read_csv

path = "C:/Users/C.F_Lin/Downloads/金融股107-109股價/MI_INDEX_17_"
StartDate = "20180102"
df = read_csv(path+StartDate+".csv",skiprows=2,encoding='big5')
df['日期'] = StartDate
df = df.iloc[0:-5]
while 1:
    StartDate = (to_datetime(StartDate)+timedelta(1)).strftime("%Y%m%d")
    try:
        df2 = read_csv(path+StartDate+".csv",skiprows=2,encoding='big5')
        df2 = df2.iloc[0:-5]
        df2['日期'] = StartDate
        df = df.append(df2,ignore_index=True)   
    except:
        pass
    print(StartDate)

#%%

df.to_csv("C:/Users/C.F_Lin/Downloads/StockPrice.csv",encoding='utf-8')


#%%

Banking = driver.find_element_by_name('type')
Banking.send_keys('收盤指數資訊')
StartDate = '2020-04-01'
YearButton = driver.find_element_by_name('yy')
YearButton.send_keys(webdriver.common.keys.Keys.DOWN)
MonthButton = driver.find_element_by_name('mm')
DayButton = driver.find_element_by_name('dd')
Search = driver.find_element_by_css_selector('.search.button')
MonthButton.send_keys(StartDate.split("-")[1])
while 1:
    DayButton.send_keys(StartDate.split("-")[2])
    Search.click()
    sleep(3)
    Result = driver.find_element_by_id('result-message')
    Result_contents = Result.get_attribute('innerHTML')
    if Result_contents == ('很抱歉，沒有符合條件的資料!'):
        pass
    else:
        CSVButton = driver.find_element_by_class_name('csv')
        CSVButton.click()
        sleep(3)
    StartDate = str(to_datetime(StartDate)-timedelta(1))
    print(StartDate)
    #if StartDate.split(" ")[0].split("-")[2]=="01":
    #    MonthButton.send_keys(webdriver.common.keys.Keys.UP)
    if StartDate.split(" ")[0]=="2019-01-01":
        YearButton.send_keys(webdriver.common.keys.Keys.DOWN)
        MonthButton.send_keys(12)
    if StartDate.split(" ")[0]=="2018-01-01":
        YearButton.send_keys(webdriver.common.keys.Keys.DOWN)
        MonthButton.send_keys(12)
    if StartDate.split("-")[0]=="2017":
        break






