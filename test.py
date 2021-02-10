# import os
# dir_path=input("请输入需要变动的文件夹")
# files=os.lisdir(dir_path)
# i=1
# for a in files:
#     print(i,a)
#     i+=1
# file_chosen=input("请输入序号选择要更改的文件")
# new_name=input("请输入要更改的名字")
# os.rename(dir_path+'/'+files[int(file_chosen)-1],new_name)
# class Animal():
#     a=1
#     def __init__(self,a):
#         self.a=2
#     def open(self):
#         print(self.a)
#
#
# class cat(Animal):
#     def __init__(self):
#         self.__a=1
#         pass
#     def open(self):
#         print('cat')
#     def Animal_open(self):
#         super().open()
# c=cat()
# c.open()
# c.Animal_open()
# class a():
#     name='name'
# a.name='aaaa'
# b=a()
# c=a()
# b.na='asd'
# print(b.na)
# import json
# import learn
# file_t='test.json'
# try:
#     with open(file_t) as fi:
#         text=json.load(fi)
# except:
#     name=input('请输入用户名')
#     print('aaa')
#     with open(file_t,'w') as fil:
#         json.dump(name,fil)
# else:
#     print(text)
# import pymysql
#
# connectors = pymysql.connect(host='localhost',user='root',password='',port=3306,db='new_schema')
# b=connectors.cursor()
# b.execute('select version()')
# outcome=b.fetchone()
# print(outcome)
# import re
#
# a = 'abcFBIabcFBIaFBICIAabc'
#
#
# def 函数名(形参):
#     分段获取 = 形参.group()  # group（）在正则表达式中用于获取分段截获的字符串，获取到FBI
#     return '$' + 分段获取 + '$'
#
#
# r = re.sub(pattern='[a-b]',repl= 函数名, string=a)
# print(r)
# import re
# a = 'liiillliiliiii'
# r = re.findall('li{3}',a)
# # print(r)       # 完整正则匹配
# from openpyxl import Workbook, load_workbook
#
# wb = load_workbook('a.xlsx',data_only=True)
# wb_sheet=wb['Sheet1']
# print(wb_sheet['G1'].value)
# # # grab the active worksheet
# ws = wb.active
#
# # Data can be assigned directly to cells
# ws['A1'] = 42N MFFFFFFFFF V
#
# # Rows can also be appended
# ws.append([1, 2, 3])
#
# # Python types will automatically be converted
# import datetime
# ws['A2'] = datetime.datetime.now()

# Save the file
# wb.save("C:/Users/25944/Desktop/pythonProject/a.xlsx")
# a,b,c=1,2,3
# # a,b,c=c,b,a
# b=3/2
# print(a,b,c,sep='-')
# temp=input("mima\n")
# temp=lis(temp)
# secret=[]
# pre=0
# mid=0
# last=0
# for a in temp:
#     if a.isupper():
#         if mid==0:
#             pre+=1
#         else:
#             last+=1
#     elif mid==0 and pre>=3:
#         mid=1
#         secret.append(a)
#     elif mid>0 and last>=3:
#         secret.append(a)
#         pre=last
#         last=0
#         mid=1
#     else:
#          if len(secret)>0:
#              secret.pop()
#          pre=0
#          mid=0
#          last=0
# if last<3 and len(secret)>0:
#     secret.pop()
# print(secret)
# g=lambda x,y=3 : x*y
# print(g(2))
# a=lis(filter(lambda x:1 if x%3==0 else 0,range(0,100)))
# print(a)
# def rabbit(a,b,month):
#     month-=1
#     if month==1:
#         return a+b
#
#     return  rabbit(a+b,a,month)
# print(rabbit(1,0,month=5))
# def bina(lis,number):
#     if number==1:
#         lis.insert(0, 1)
#         return lis
#     lis.insert(0,number%2)
#     return bina(lis,number//2)
# print(bina([],9))
# a=dict((('a',1),('b',2)))
# print(a)
# a=open('a.txt')
# # b=open('b.txt','w')
# # b.write(a.read())
# a=list(a)
# print(a)
# a.close()
# b.close()
# file=open('a.txt')
# for eachline in file:
#     print(eachline,end='')
import os
# os.chdir('C:')
# print(os.listdir())
# print('='*8)
# a=os.listdir(os.curdir)
# print(a)
# print(os.path.abspath())
# import  pickle
# pickle_file=open('pickle_test.pkl','rb')
# a=pickle.load(pickle_file)
# print('asdsdsf'.startswith('s'))
a=1