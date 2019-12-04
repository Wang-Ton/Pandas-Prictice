import pandas as pd
import re
data = pd.read_excel(r'd:\支付宝账单.xlsx', sheet_name=None)
First = pd.read_excel(r'd:\支付宝账单.xlsx', skiprows=2)
n = list(data)
if len(n) > 1:
    dfs = []
    for i in n[1:]:
        df = pd.read_excel(r"d:\支付宝账单.xlsx", sheet_name=i)
        dfs.append(df)
    Others = pd.concat(dfs)
if Others.empty == False :
    Others.columns = First.columns.values
    All = pd.concat([First, Others], ignore_index=True)
else:
    All=First
#if Others.shape != []:
All['提取订单号'] = None
if isinstance(All.iloc[All.index[-1],[0]].values[0],str) :
    All.drop(All.index[-1], inplace=True)
All.dtypes
for x in All.index:
    if 'HJCOM' in All.at[x, '商户订单号']:
        All.at[x, '提取订单号'] = All.at[x, '商户订单号'][-18:]
    elif 'T200P'in All.at[x, '商户订单号']:
        All.at[x, '提取订单号'] = All.at[x, '商户订单号'][-18:]
    elif bool(re.search(r'\d', All.at[x,'备注']))==True:
        All.at[x, '提取订单号'] = re.findall(r'\d+',All.at[x,'备注'])[0]
All.set_index('序号',inplace = True)
All.to_excel(r'd:\支付宝对账单-提取订单号.xlsx')
print('Done')

# k = All.loc[2, '商户订单号']
# m = All.loc[2, '提取订单号']
# if 'HJCOM' in k:
#         m = k[-18:]
# elif 'T200P' in k:
#         m = k[-18:]
# else:
#         m = re.findall(r'\d+',All.at[x,'备注'])

