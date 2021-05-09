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

# =============================================================================
# Banking = driver.find_element_by_name('type')
# Banking.send_keys('金融保險')
# StartDate = '2020-12-31'
# YearButton = driver.find_element_by_name('yy')
# YearButton.send_keys(webdriver.common.keys.Keys.DOWN)
# YearButton.send_keys(webdriver.common.keys.Keys.DOWN)
# MonthButton = driver.find_element_by_name('mm')
# DayButton = driver.find_element_by_name('dd')
# Search = driver.find_element_by_css_selector('.search.button')
# MonthButton.send_keys(StartDate.split("-")[1])
# while 1:
#     DayButton.send_keys(StartDate.split("-")[2])
#     Search.click()
#     sleep(3)
#     Result = driver.find_element_by_id('result-message')
#     Result_contents = Result.get_attribute('innerHTML')
#     if Result_contents == ('很抱歉，沒有符合條件的資料!'):
#         pass
#     else:
#         CSVButton = driver.find_element_by_class_name('csv')
#         CSVButton.click()
#         sleep(3)
#     StartDate = str(to_datetime(StartDate)-timedelta(1))
#     print(StartDate)
#     if StartDate.split(" ")[0].split("-")[2]=="01":
#         MonthButton.send_keys(webdriver.common.keys.Keys.UP)
#     if StartDate.split(" ")[0]=="2019-01-01":
#         YearButton.send_keys(webdriver.common.keys.Keys.DOWN)
#         MonthButton.send_keys(12)
#     if StartDate.split(" ")[0]=="2018-01-01":
#         YearButton.send_keys(webdriver.common.keys.Keys.DOWN)
#         MonthButton.send_keys(12)
#     if StartDate.split(" ")[0].split("-")[0]=="2017":
#         break
# =============================================================================

#%%

from pandas import read_csv

path = "C:/Users/C.F_Lin/Downloads/金融股107-109股價/MI_INDEX_17_"
StartDate = "20151231"
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
    if StartDate == "20210507":
        break

#%%

df.to_csv("C:/Users/C.F_Lin/Downloads/StockPrice_金融股.csv",encoding='utf-8')


#%%

Banking = driver.find_element_by_name('type')
Banking.send_keys('收盤指數資訊')
StartDate = '2016-04-20'
YearButton = driver.find_element_by_name('yy')
YearButton.send_keys(webdriver.common.keys.Keys.DOWN*5)
MonthButton = driver.find_element_by_name('mm')
DayButton = driver.find_element_by_name('dd')
MonthButton.send_keys(webdriver.common.keys.Keys.DOWN*3)
DayButton.send_keys(webdriver.common.keys.Keys.DOWN*19)
Search = driver.find_element_by_css_selector('.search.button')
while 1:
    #DayButton.send_keys(StartDate.split("-")[2])
    Search.click()
    sleep(3)
    Result = driver.find_element_by_id('result-message')
    Result_contents = Result.get_attribute('innerHTML')
    if Result_contents == ('很抱歉，沒有符合條件的資料!'):
        pass
    else:
        try:
            CSVButton = driver.find_element_by_class_name('csv')
            CSVButton.click()
            sleep(1)
        except:
            pass
    DayButton.send_keys(webdriver.common.keys.Keys.UP)    
    print(StartDate)
    if StartDate.split(" ")[0].split("-")[2]=="01":
        if StartDate.split(" ")[0].split("-")[1]=="01":
            YearButton.send_keys(webdriver.common.keys.Keys.DOWN)
            MonthButton.send_keys(webdriver.common.keys.Keys.END)
            DayButton.send_keys(webdriver.common.keys.Keys.END) 
        else:
            MonthButton.send_keys(webdriver.common.keys.Keys.UP)
            DayButton.send_keys(webdriver.common.keys.Keys.END)
       
    StartDate = str(to_datetime(StartDate)-timedelta(1))
    
    #if StartDate.split(" ")[0]=="2019-12-31":
    #    YearButton.send_keys(webdriver.common.keys.Keys.DOWN)
    #    MonthButton.send_keys(12)
    #if StartDate.split(" ")[0]=="2018-12-31":
    #    YearButton.send_keys(webdriver.common.keys.Keys.DOWN)
    #    MonthButton.send_keys(12)
    #if StartDate.split(" ")[0]=="2018-01-01":
    #    YearButton.send_keys(webdriver.common.keys.Keys.DOWN)
    #    MonthButton.send_keys(12)
    if StartDate.split(" ")[0].split("-")[0]=="2015":
        break

#%%

Banking = driver.find_element_by_name('type')
Banking.send_keys('金融保險')
StartDate = '2021-05-09'
YearButton = driver.find_element_by_name('yy')
#YearButton.send_keys(webdriver.common.keys.Keys.DOWN*4)
MonthButton = driver.find_element_by_name('mm')
DayButton = driver.find_element_by_name('dd')
#MonthButton.send_keys(webdriver.common.keys.Keys.END)
#DayButton.send_keys(webdriver.common.keys.Keys.DOWN*8)
Search = driver.find_element_by_css_selector('.search.button')
while 1:
    #DayButton.send_keys(StartDate.split("-")[2])
    Search.click()
    sleep(3)
    Result = driver.find_element_by_id('result-message')
    Result_contents = Result.get_attribute('innerHTML')
    if Result_contents == ('很抱歉，沒有符合條件的資料!'):
        pass
    else:
        CSVButton = driver.find_element_by_class_name('csv')
        CSVButton.click()
        sleep(1)
    DayButton.send_keys(webdriver.common.keys.Keys.UP)    
    print(StartDate)
    if StartDate.split(" ")[0].split("-")[2]=="01":
        if StartDate.split(" ")[0].split("-")[1]=="01":
            YearButton.send_keys(webdriver.common.keys.Keys.DOWN)
            MonthButton.send_keys(webdriver.common.keys.Keys.END)
            DayButton.send_keys(webdriver.common.keys.Keys.END) 
        else:
            MonthButton.send_keys(webdriver.common.keys.Keys.UP)
            DayButton.send_keys(webdriver.common.keys.Keys.END)
       
    StartDate = str(to_datetime(StartDate)-timedelta(1))
    
    #if StartDate.split(" ")[0]=="2019-12-31":
    #    YearButton.send_keys(webdriver.common.keys.Keys.DOWN)
    #    MonthButton.send_keys(12)
    #if StartDate.split(" ")[0]=="2018-12-31":
    #    YearButton.send_keys(webdriver.common.keys.Keys.DOWN)
    #    MonthButton.send_keys(12)
    #if StartDate.split(" ")[0]=="2018-01-01":
    #    YearButton.send_keys(webdriver.common.keys.Keys.DOWN)
    #    MonthButton.send_keys(12)
    if StartDate.split(" ")[0]=="2021-01-15":
        break

#%%

from pandas import read_csv

path = "C:/Users/C.F_Lin/Downloads/大盤107-109股價/MI_INDEX_IND_"
StartDate = "20151231"
df = read_csv(path+StartDate+".csv",skiprows=1,encoding='big5')
df['日期'] = StartDate
df = df.iloc[0:-5]
while 1:
    StartDate = (to_datetime(StartDate)+timedelta(1)).strftime("%Y%m%d")
    try:
        df2 = read_csv(path+StartDate+".csv",skiprows=1,encoding='big5')
        df2 = df2.iloc[0:-5]
        df2['日期'] = StartDate
        df = df.append(df2,ignore_index=True)   
    except:
        pass
    print(StartDate)
    if StartDate == "20210507":
        break

#%%
for i in ["指數","報酬指數(跨市場)","報酬指數(臺灣指數公司)","報酬指數(臺灣證券交易所)","報酬指數"]:
    df = df[df["指數"]!=i]

df.to_csv("C:/Users/C.F_Lin/Downloads/StockPrice_大盤.csv",encoding='utf-8')

#%%

from datetime import timedelta
from selenium import webdriver
from time import sleep
#import requests
from pandas import to_datetime
import os

quote_page = "https://rate.bot.com.tw/twd/csv/"
os.chdir('C:/Users/C.F_Lin/Downloads')

location = "C:/Users/C.F_Lin/AppData/Local/Programs/Opera/75.0.3969.243/Opera.exe"#69.0.3686.95#65.0.3467.78
options = webdriver.ChromeOptions()
options.binary_location = location
driver = webdriver.Opera(options=options,executable_path="C:/Users/C.F_Lin/Desktop/operadriver.exe")
#driver.get("https://rate.bot.com.tw/twd?Lang=zh-TW")
StartDate = "2021-05-08"
while 1:
    driver.get(quote_page+StartDate)    
    driver.implicitly_wait(300)
    sleep(1)
    print(StartDate)
    StartDate = (to_datetime(StartDate)-timedelta(1)).strftime("%Y-%m-%d")
    if StartDate == "2016-12-31":
        break
#%%
from pandas import read_csv

path = "C:/Users/C.F_Lin/Downloads/臺銀106-109利率/InterestRate@"
StartDate = "2017-01-01"
df = read_csv(path+StartDate+".csv",skiprows=1)
df['日期'] = StartDate
#df = df.iloc[0:-5]
while 1:
    StartDate = (to_datetime(StartDate)+timedelta(1)).strftime("%Y-%m-%d")
    try:
        df2 = read_csv(path+StartDate+".csv",skiprows=1)
        df2['日期'] = StartDate
        df = df.append(df2,ignore_index=True)   
    except:
        pass
    print(StartDate)
    if StartDate == "2021-05-08":
        break
    
#%%

df.to_csv("C:/Users/C.F_Lin/Downloads/InterestRate.csv",encoding='utf-8')
   


