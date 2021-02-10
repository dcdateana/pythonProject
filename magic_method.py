# class Nstr(str):
#     def __sub__(self, other):
#         nstr=''
#         for a in self:
#             if a in other:
#                 pass
#             else:
#                 nstr+=a
#         return nstr
# a=Nstr('iloveyou')
# b=Nstr('i')
# print(a-b)
import time
# class TimeRecord:
#     def __init__(self):
#         self.start_time=0
#         self.end_time=0
#         print('未开始计时')
#     def start(self):
#         self.start_time=time.localtime()
#         print('开始计时')
#     def end(self):
#         self.end_time=time.localtime()
#         print('结束计时')
#     def get_record(self):
#         return (self.end_time-self.start_time)
#     def __add__(self, other):
#         return ((self.end_time-self.start_time)+(other.end_time-other.start_time))
# t1=TimeRecord()
# t2=TimeRecord()
# t1.start()
# t2.start()
# t1.end()
# t2.end()
# t1.get_record()
# t2.get_record()
# print(t1+t2)

a=time.localtime()
print(a)