

import yfinance as yf
import pandas as pd 
from pandas_datareader import data as pdr 
import datetime as dt 
import numpy as np 
import matplotlib.pyplot as plt  


f = open('title.txt', 'r')


file_contents = f.read()

print(file_contents)

f.close()



ticker = input("type ticker here: ")

stocks = [ticker]

sd_date_entry = input('Enter a start date in YYYY-MM-DD format: ')
sd_year, sd_month, sd_day = map(int, sd_date_entry.split('-'))
sd_date1 = dt.date(sd_year, sd_month, sd_day)

ed_date_entry = input('Enter a end date in YYYY-MM-DD format: ')
ed_year, ed_month, ed_day = map(int, ed_date_entry.split('-'))
ed_date1 = dt.date(ed_year, ed_month, ed_day)



stocktick = yf.Ticker(ticker)
companyname = stocktick.info['longName']

print(companyname + " data loading...")



df = yf.download(stocks, start = sd_date1, end = ed_date1)


close_price = df['Close']

close_price.plot(title = companyname + " Price", figsize = (10,6))

plt.show()

