import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# 创建特征值列表
column = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniform of Cell Shape',
          'Marginal Adhesion'
    , 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses', 'Class']

# 使用pandas.read_csv函数从互联网读取指定数据


# print(column)


# t1 = pd.Series([1,2,3,4])
# print(t1)
# std_x = StandardScaler()
# t1 = std_x.fit_transform(t1)
# print(t1)
#
# t2 = pd.Series([1,2,3,4])
# t2 = std_x.fit_transform(t2)
# print(t2)

# print(type(t))
# print("===================")

data = pd.read_csv("F:\\信息化\\大数据中心\\模型组\\需求\\漫游结算预测\\研发设计\\数据处理\\test\\test.txt", header=None);
data.columns = ['a', 'b', 'c', 'd', 'e', 'f']
print(data)
# std_x = StandardScaler()
# print(std_x.fit_transform([1,2,3,4]))

# print("=================")
# # print(data.dropna())
# # data[data < 3] =100
# #
# # data['ex']=data['a']+data['c']
# # print(data)
data1 = pd.read_csv("F:\\信息化\\大数据中心\\模型组\\需求\\漫游结算预测\\研发设计\\数据处理\\test\\test.txt", header=None);
data1['a'] = data['b']
print(data1)
# print(data)
meg = pd.merge(data, data1, on=["a"], how='left')
# print("=============合并表1=======================")
# print(data1)
# print(meg)
# meg = pd.merge(meg,data1,on=['a'])
# meg = pd.merge(meg,data1,on=['a'],how='outer')
print("=============合并表2=======================")
print(meg)
# 填充指定值，没成功，不好用，还是均值好用
# im = SimpleImputer(strategy='constant', fill_value=0)
# im.fit(meg)
meg.fillna(0)
print("===========")
print(meg)
#
#
#
# print("=============交叉表=======================")
# cros = pd.crosstab(data['a'],data['b'])
# print(cros)
# # 进行主成分分析
# pca = PCA(n_components=0.9)
# data2 = pca.fit_transform(cros)
# print(data2.shape)
# #
# print("==============")
# print(cros)
# cros['e'] = data['a']
# print("=============")
# print(cros)
# print("=============")
# print(cros['e'].iloc[1])
# print(len(cros))
# print("\n")


# print("====================")
# # 删除a列
# data = data.drop(['a'], axis=1)
# # 取出某几列
# print(data[['b','c']])
#
# print("====================")
#
# a = data
# a['t']=3
# print(data['b'].iloc[0])
#
# print("==============")
# str = "3e324[]"
# print(str.replace("[","").replace("]",""))

# data['ss']=data['col1'].map(lambda x: x**2)

result = 9.229381 * 10 ** 6
gprs = 1.487139 * 10 ** 4
total = result * gprs / 10 ** 6
print(result)
print(gprs)
print(total)

print("=========================")
liul = 160920338586499328 / 10 ** 12
print(liul)
money = 13805067553.36 / 100 / 10 ** 4
print(money)

df1 = pd.DataFrame([{'col1': 'a', 'col2': 1}, {'col1': 'b', 'col2': 2}])
df2 = pd.DataFrame([{'col1': 'a', 'col3': 11}, {'col1': 'c', 'col3': 33}])

data = pd.merge(left=df1, right=df2, how='left', left_on='col1', right_on='col1')
print(data)
# 将NaN替换为0
print(data.fillna(0))

# dropna操作
# df.dropna(axis=0, how='any', inplace=True)
# axis：0-行操作（默认），1-列操作
# how：any-只要有空值就删除（默认），all-全部为空值才删除
# inplace：False-返回新的数据集（默认），True-在愿数据集上操作


