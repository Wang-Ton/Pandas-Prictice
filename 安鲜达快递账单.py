# %%
import pandas as pd
bcf = pd.read_excel(r'G:\工作备份\招联文件\安鲜达对账\三方-百富勤食品专营店_201909_对账单-20191018120856.xlsx',
                    sheet_name='包材辅料费',index_col='订单流水号', usecols=['订单流水号', '包材辅料总费用'])
psf = pd.read_excel(r'G:\工作备份\招联文件\安鲜达对账\三方-百富勤食品专营店_201909_对账单-20191018120856.xlsx',
                    sheet_name='配送费', index_col='订单流水号', usecols=['订单流水号', "配送费用",'客户订单号'])
ddf = pd.read_excel(r'G:\工作备份\招联文件\安鲜达对账\三方-百富勤食品专营店_201909_对账单-20191018120856.xlsx',
                    sheet_name='订单操作费', index_col='订单流水号', usecols=['订单流水号', '订单操作费'])
Table = bcf.join(ddf, how='left').join(psf)
Column_sum = Table.sum(axis=1)
Table.insert(4,'合计',Column_sum)
#order = ['客户订单号', '包材辅料总费用', '订单操作费', '配送费用', '合计']
Table = Table[['客户订单号', '包材辅料总费用', '订单操作费', '配送费用', '合计']]
col=list(Table)
print(col)
#print(Table.head())
Table.to_excel(r'g:\sum.xlsx')


# %%
