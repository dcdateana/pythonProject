import pandas as pd

# path = '新建空白文件.xlsx'
# datas = pd.read_excel(path,header=0,index_col='id')  # 写入的datas
# datas.columns = ['姓名','年']
# # datas.set_index('id', inplace=True)
# print(datas)
# print('*'*30)
# print(datas.columns)
# print('*'*30)
# print(datas.head())
# print('*'*30)
# print(datas.index)
# datas=pd.Series({'姓名':'孙兴华','性别':'男','年龄':'20','地址':'花果山水帘洞'})
# print(datas)
# print('*'*30)
# print(datas.index)
# print('*'*30)
# print(datas.values)
# print('*'*30)
# print(datas[['姓名','性别']])
# 字典 = {
#         '姓名':['孙兴华','李小龙','叶问'],
#         '年龄':[20,80,127],
#         '功夫':['撸铁','截拳道','咏春']
#         }
# datas = pd.DataFrame(字典)
# print(datas)
# print(datas.dtypes)    # 返回每一列的类型
# print('*'*30)
# print(datas.columns) # 返回列索引，以列表形式返回：[列名1，列名2，…]
# print('*'*30)
# print(datas.index)
# print(datas['姓名'])
# print(datas.loc[1])
b=pd.read_excel('新建空白文件.xlsx')
print(type(b))
