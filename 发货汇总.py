import pandas as pd
import numpy as np
import re
table = pd.read_csv(r'G:\发货商品汇总.csv', encoding='gbk', dtype=str)
matrix = table.values
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if type(matrix[i][j]) == str:
            matrix[i][j] = matrix[i][j].replace(",", "")

df1 = pd.DataFrame(matrix, columns=table.columns.values)


print(df1.dtypes)
#pt1 = df1.pivot_table(index='品牌', values=['让利后金额'], aggfunc=sum)
# print(pt1)
