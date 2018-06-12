#!/usr/bin/python3

'''
while 表达式:
    语句1
else:
    语句2
'''

num = 1
str = "lym is a good man"
while num < len(str):
    print("str[%d] = %s" % (num, str[num]))
    num += 1
else:
    print("very good")

'''
for 变量名 in 集合:
    语句
'''
for i in [1, 2, 3, 4, 5]:
    print(i)

'''
range()函数 
列表生成器，生成数列
'''
a = range(10)
print(a)
for x in range(10):
    print(x)
# range(begin, end, step) 起始，结束，步长
for y in range(2, 20, 2):
    print(y)

'''
enumerate()
同时遍历下标和元素
'''
for index, m in enumerate([1,2,3,4,5,6]):
    print(index, m)