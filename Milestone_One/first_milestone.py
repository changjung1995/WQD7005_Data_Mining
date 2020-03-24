# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 21:59:40 2020
WQD 7005 - Data Mining: Milestone One
@author: Tan Chang Jung & Tan Sia Hong
"""

#%%
import requests 
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import time
#%%
# select the top 20 from the ranking of cryptocurrencies
cryptocurrency = ['bitcoin','ethereum','xrp','bitcoin-cash','tether',
                  'bitcoin-sv','litecoin','eos','binance-coin','neo',
                  'chainlink','cardano','stellar','tron','unus-sed-leo',
                  'monero','huobi-token','ethereum-classic','crypto-com-coin',
                  'dash']

#%%
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X '
               '10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/72.0.3626.109 Safari/537.36'}

# capture today date
today = date.today().strftime("%Y%m%d")

# format the base url link
base_url = 'https://coinmarketcap.com/currencies/{}/historical-data/?start=20100101&end=' + today

# create loop to crawl the price data
for cc in cryptocurrency:
    url = base_url.format(cc)
    response = requests.get(url, headers = headers)
    time.sleep(5)
    html = BeautifulSoup(response.text, 'html.parser')
    table = html.find('div', class_='cmc-tab-historical-data ctxmt9-0 ASvFA')
    
    heading = []
    for th in table.find_all('th'):
        heading.append(th.text.replace('\n', '').strip())
        
    

    data = []
    for tr in table.find_all('tr'):
        row = {}
        for td, th in zip(tr.find_all('td'), heading):
            row[th] = td.text.replace('\n','').strip()
        data.append(row)
    
    data = data[3:]
    
    # get the title from html content
    title = table.h2.text
    df = pd.DataFrame(data)
    df["Date"] = pd.to_datetime(df["Date"]).dt.strftime('%Y-%m-%d')
    df['Open*'] = df['Open*'].str.replace(',','')
    df['Open*'] = df['Open*'].astype('float64').round(2)
    df['High'] = df['High'].str.replace(',','')
    df['High'] = df['High'].astype('float64').round(2)
    df['Low'] = df['Low'].str.replace(',','')
    df['Low'] = df['Low'].astype('float64').round(2)
    df['Close**'] = df['Close**'].str.replace(',','')
    df['Close**'] = df['Close**'].astype('float64').round(2)
    df['Volume'] = df['Volume'].str.replace(',','')
    df['Volume'] = df['Volume'].astype('float64').round(2)
    df['Market Cap'] = df['Market Cap'].str.replace(',','')
    df['Market Cap'] = df['Market Cap'].astype('float64').round(2)
    
    # save to csv
    df.to_csv(title + '.csv', index = False)
    
    