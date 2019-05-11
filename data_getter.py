#!/usr/bin/env python3

import os
import pandas
import time
import datetime as dt

alpha_vantage_key = os.environ('av_key')
today = dt.datetime.now().date()

from alpha_vantage.timeseries import TimeSeries
cwd = os.getcwd()
tickers = ['RR.L', '^FTSE', '^FTMC', 'BA.L', 'GE', 'UTX', 'TSLA', 'FB']
ts = TimeSeries(key=alpha_vantage_key, output_format='pandas')

daily = True
intraday = True
for t in tickers:
    if intraday:
        print(f'Getting {t} intraday data...')
        df, md = ts.get_intraday(symbol=t,interval='1min', outputsize='full')
        fname = f'{t}_stock_data_intraday_{today}.csv'
        time.sleep(20)
        df.to_csv(fname)
    if daily:  
        print(f'Getting {t} daily data...')
        df, md = ts.get_daily_adjusted(symbol=t, outputsize='full')
        fname = f'{t}_stock_data_daily_{today}.csv'
        time.sleep(20)
        df.to_csv(fname)
