#!/usr/bin/python3


# Number Python3 支持 int、float、bool、complex（复数）
# 内置的 type() 函数可以用来查询变量所指的对象类型。
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
#结果： <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>


# 此外还可以用 isinstance 来判断
r = isinstance(a, int)
print(r)
# True


# isinstance 和 type 的区别在于
# type() 不会认为子类是一种父类类型。
# isinstance() 会认为子类是一种父类类型。
class A:
    pass

class B(A):
    pass

isinstance(A(), A)  # returns True
type(A()) == A      # returns True
isinstance(B(), A)    # returns True
type(B()) == A        # returns False


# 可以使用del语句删除一些对象引用
# del var1[,var2[,var3[....,varN]]]]
var1 = 1
var2 = 10
del var1, var2


# 数值运算
'''
>>>5 + 4  # 加法
9
>>> 4.3 - 2 # 减法
2.3
>>> 3 * 7  # 乘法
21
>>> 2 / 4  # 除法，得到一个浮点数
0.5
>>> 2 // 4 # 除法，得到一个整数
0
>>> 17 % 3 # 取余 
2
>>> 2 ** 5 # 乘方
32
'''

# 打印格式化
num = 10
str = "lym is a good man"
f = 1.2361
print("num = %d", num)
print("num = %d, str = %s, f = %.3f" % (num, str, f))

# 转义 [\]
print('lym is g \'good\' man')

# type
num1 = 10
print(type(num1))

# eval
print(eval("12+3"))

# None 表示空值
n = None
print(n)

# True, False 布尔类型，注意首字母大写

# 类型转换
int('1') # 字符串转换成整形