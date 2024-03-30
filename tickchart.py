
import yfinance as yf
import pandas as pd 
from pandas_datareader import data as pdr 
import datetime as dt 
import numpy as np 
import matplotlib.pyplot as plt  


#displays the title of the program
f = open('title.txt', 'r')
file_contents = f.read()
print(file_contents)
f.close()


input_string = input('Enter tickers sperated by a space: \n')
tickers = input_string.split()

#'''

#user input for date range
sd_date_entry = input('Enter a start date in YYYY-MM-DD format: ')
sd_year, sd_month, sd_day = map(int, sd_date_entry.split('-'))
sd_date1 = dt.date(sd_year, sd_month, sd_day)

ed_date_entry = input('Enter a end date in YYYY-MM-DD format: ')
ed_year, ed_month, ed_day = map(int, ed_date_entry.split('-'))
ed_date1 = dt.date(ed_year, ed_month, ed_day)

'''

#temporary date range for quicker testing
sd_date1 = dt.date(2020, 1, 1)
ed_date1 = dt.date(2023, 12, 31)

'''

df = pd.DataFrame()
for ticker in tickers:
    data = yf.download(ticker, start=sd_date1, end=ed_date1)
    df[ticker] = data['Adj Close']

returns = df.apply(lambda x: (x / x.iloc[0] - 1) * 100)

returns.plot(figsize=(10, 6))
plt.title(input_string + ' Prices')

plt.legend()
plt.ylabel('Cumulative Return %')
plt.xlabel('Time')
plt.grid(lw=0.2)
plt.show()

