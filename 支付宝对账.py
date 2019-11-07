import pandas as pd
data = pd.read_excel(r'd:\支付宝账单.xlsx', sheet_name=None)
n = list(data)
dfs = []
for i in n[1:]:
    df = pd.read_excel(r"d:\支付宝账单.xlsx", sheet_name=i)
    dfs.append(df)
Others = pd.concat(dfs)
First = pd.read_excel(r'd:\支付宝账单.xlsx',skiprows=2)
Others.columns = First.columns.values
All = pd.concat([First,Others])
print(All.head())