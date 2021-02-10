# class Person():
#     name='aaaa'
#     def pr_name(self):
#         print(self.name)
# a=Person()
# Person.name='ccc'
# a.pr_name()
# b=Person()
# b.pr_name()


# class Ball:
#     def __init__(self,name):
#         self.name=name
#     def kick(self):
#         print(self.name)
# b=Ball('b')
# b.kick()
# print(b.name)


# import math
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
# class Line:
#     def __init__(self,point1,point2):
#         self.point1=point1
#         self.point2=point2
#     def getLen(self):
#         len=math.sqrt((self.point1.x-self.point2.x)**2+(self.point1.y-self.point2.y)**2)
#         print(len)
# point1=Point(1,1)
# point2=Point(0,0)
# line=Line(point1,point2)
# line.getLen()

# class A:
#     def __init__(self):
#         print('进入A')
#         print('离开A')
# class B(A):
#     def __init__(self):
#         print('进入B')
#         A.__init__(self)
#         print('离开B')
# class C(A):
#     def __init__(self):
#         print('进入C')
#         A.__init__(self)
#         print('离开C')
# class D(B,C):
#     def __init__(self):
#         print('进入D')
#         B.__init__(self)
#         C.__init__(self)
#         print('离开D')
# d=D()

# class A:
#     def println(self):
#         print(1)
# a=A()
# A.println(a)

# class A:
#     a=111
# b=A()
# b.a=10
# print(A.a)

