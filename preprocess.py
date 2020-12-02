import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import xlrd
from datetime import datetime, timedelta

g_label_added = False
fund_return = {}
WEEKENDS = [6,0]
PERIOD = {1:'on', 7:'1w', 14:'2w', 30:'1m', 61:'2m', 91:'3m', 182:'6m', 365:'12m'}

# 我们得到每只基金数据第一行对应的星期？，便于计算有效回报
week = {'CUAM China-Hong Kong Strategy A' : 5,\
'E Fund (HK) China Equity Div' : 1,\
'Allianz Global Artfcl Intlgc AT' : 5,\
'Franklin Technology A Acc HKD' : 2,\
'Da Cheng Overseas China Concept' : 1,\
'Harvest China Equity A HKD Acc' : 3,\
'Franklin Biotechnology Discv A' : 2,\
'Da Cheng China Balanced A (HKD)' : 1,\
'Janus Henderson Balanced A2 HKD' : 3,\
'Bosera Orient Sun Rise Grt CNH' : 4,\
'ChinaAMC Select Fixed Inc Allc' : 5,\
'Allianz Income and Growth AM HK' : 5,\
'Franklin US Government A(acc)HK' : 5,\
'E Fund (HK) HKD Mny Mkt B HKD A' : 3,\
'AB SICAV I Low Volatility Eq A' : 3,\
'Templeton Em Mkts Dyn Inc A MDi' : 5,\
'CSOP Select US Dollar Bd A HKD' : 2,\
'E Fund (HK) Select Asia HY Bd A' : 3,\
'Allianz US Short Dur Hi Inc Bd' : 2,\
'AB Global High Yield AA HKD Inc' : 2,\
'Harvest China Income A HKD Inc' : 2,\
'Harvest China A Research Select' : 5,\
'E Fund (HK) Grtr Chn Leaders A' : 2
    }

# 画图函数
def plot(nav, pct_change, name):
    global g_label_added
    #plt.plot(nav, color='red', label='NAV',linestyle=':')
    plt.plot(pct_change, color='#F08080', label='Monthly Return',linestyle='-')
    plt.xlabel('Time')
    plt.ylabel('Monthly Return / NAV')
    plt.title(name)
    if not g_label_added:
        plt.legend(loc = 0, ncol = 2)
        g_label_added = True
    plt.savefig('pic/'+name+'.png')
    #plt.show()

# 得到Excel Sheet名称
def get_names(excelName):
    b=xlrd.open_workbook(excelName)
    fund_names = []
    for sheet in b.sheets():
        fund_names.append(sheet.name.strip())
    return fund_names


def get_return(excelName,period = 30):
    fund_return = dict()
    fund_names = get_names(excelName)

    # 对每个基金sheet获取信息
    for i in range(1,len(fund_names)):
        name = fund_names[i]
        fund = pd.read_excel(excelName, sheet_name = i)
        print('----No.'+str(i)+' Fund----')
        print()
        print(fund.head()) #查看前五个

        # 做些微调
        pct_change = [np.nan]
        nav = [np.nan]
        for i in range(1,period):
            pct_change.append(np.nan)
            nav.append(np.nan)

        # 从数据初始值加上期限的那天，开始计算收益
        date = week[name]+period
        date %= 7 # 保存星期几
        for i in range(0,fund.shape[0]-period): # 考虑change of price的初始天
            change = fund.iloc[i + period,1] - fund.iloc[i,1] 
            if date in WEEKENDS:
                date += 1
                date %= 7
                continue
            pct_change.append(100.0 * change / fund.iloc[i,1]) #记录基金收益率的时序
            nav.append(fund.iloc[i + period,1])
            date += 1
            date %= 7

        # 存储每个基金的收益率
        fund_return[name] = pd.Series(pct_change[::-1])

        # 画montly图
        if period == 30:
            plot(nav, pct_change, name)
        
    #return pd.DataFrame(fund_return)


if __name__ == "__main__":
    periodList = [1,7,14,30, 61, 91, 182, 365] # monthly
    #for period in periodList:
    #    fund_return = get_return('fund_data.xlsx', period)
    #    fund_return.to_csv('return/'+PERIOD[period]+'return.csv',index=False)
    get_return('fund_data.xlsx')





