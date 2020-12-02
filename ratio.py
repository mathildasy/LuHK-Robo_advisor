import numpy as np
import pandas as pd
#import yfinance as yf

#yf.pdr_override()                   
#pd.options.display.float_format = '{:.4%}'.format

# Date range
#start = '2016-01-01'
#end = '2019-12-30'

# Tickers of assets
#assets = ['JCI', 'TGT', 'CMCSA', 'CPB', 'MO', 'NBL', 'APA', 'MMC', 'JPM',
#         'ZION', 'PSA', 'AGN', 'BAX', 'BMY', 'LUV', 'PCAR', 'TXT', 'DHR',
#          'DE', 'MSFT', 'HPQ', 'SEE', 'VZ', 'CNP', 'NI']
#assets.sort()

# Downloading data
#data = yf.download(assets, start = start, end = end)
#data = data.loc[:,('Adj Close', slice(None))]
#data.columns = assets

# Calculating returns

R = pd.read_csv('return/1mreturn.csv')

#print(Y.head())

# 读取Rf
rf = pd.read_excel('hkrf.xlsx')['1m']

#print(rf.head())

premium = R.sub(rf, axis = 0).dropna()

print(premium)

#import riskfolio.Portfolio as pf


#port = pf.Portfolio(returns=Y)
