import numpy as np
import pandas as pd

R = dict()
SharpeRatio = dict()
PERIOD = {1:'on', 7:'1w', 14:'2w', 30:'1m', 61:'2m', 91:'3m', 182:'6m', 365:'12m'}
periodList = [1,7,14,30, 61, 91, 182, 365] 

# 计算夏普比率
def get_Sharpe(R, rf):
    nrow = R.shape[0]
    premium = R.sub(rf[:nrow-1], axis = 0)
    #print('Return Premium:')
    #print(premium.head())

    return_mean = premium.mean(0)
    #print('Expected return:')
    #print(return_mean.head())

    risk_std = premium.std()
    #print('Standardized Risk:')
    #print(risk_std.head())
    sharpe_ratio = return_mean / risk_std

    print('----Sharpe Ratio----')
    print(sharpe_ratio)
    return sharpe_ratio

# 读取Rf
rf = pd.read_excel('hkrf.xlsx')

# 读取23只基金的收益率
for period in periodList:
    R[period] = pd.read_csv('return/'+PERIOD[period]+'return.csv').dropna()
    rf_p = rf[PERIOD[period]]
    print('----'+PERIOD[period]+'----')
    #print('Risk-free Ratio:')
    #print(rf_p)
    SharpeRatio[period] = get_Sharpe(R[period], rf_p)

print('---Final Sharpe Ratio---')
print(pd.DataFrame(SharpeRatio))

# 考虑到交易成本，实际夏普比率会低于预估值