import numpy as np
# a = np.array([[1,2,3],[3,4,5],[4,5,6]])
# print (a[...,1])   # 第2列元素
# print (a[1,...])   # 第2行元素
# print(a[1])

# 数组 = np.arange(10).reshape(2,5)
# 索引 = np.array([[0,1],[1,1]])
# print(数组)
# print(索引)
# print("*"*30)
# print(数组[索引])
# a=np.random.randint(1,100,(2,3))
# c=a.flatten()
# b=c.argsort()
# # 数组 = np.arange(32).reshape((8,4))
# # print(数组)
# # 读取 = 数组[[1,5,7,2],[0,3,1,2]]     # 取第1行第0列，第5行第3列，第7行第1列，第2行第2列
# # print(读取)
# a=np.linspace(0,10,10)
# print(a)
# np.random.rand()
a = np.array([[1,3,6],[9,3,2],[1,4,3]])
print(f'数组:\n{a}')
print('-'*30)
print(a>3)
print('-'*30)
print(np.where(a>3,520,1314))