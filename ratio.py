import numpy as np
import pandas as pd

R = dict()
SharpeRatio = dict()
PERIOD = {1:'on', 7:'1w', 14:'2w', 30:'1m', 61:'2m', 91:'3m', 182:'6m', 365:'12m'}

# 计算夏普比率
def get_Sharpe(R, rf):
    premium = R.sub(rf, axis = 0)
    #print(premium.head())
    return_mean = premium.mean(0)
    #print(return_mean.head())
    risk_std = premium.std()
    #print(risk_std.head())
    sharpe_ratio = return_mean / risk_std

    return sharpe_ratio

# 读取Rf
rf = pd.read_excel('hkrf.xlsx')

# 读取23只基金的收益率
periodList = [1,7,14,30, 61, 91, 182, 365] 
for period in periodList:
    R[period] = pd.read_csv('return/'+PERIOD[period]+'return.csv')
    SharpeRatio[period] = get_Sharpe(R[period], rf[PERIOD[period]])




