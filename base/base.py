#!/usr/bin/python3
'''

id(变量): 查看变量的内存值
'''

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

# 变量作用域
'''
变量作用域
    访问权限决定于变量在哪里赋值的
    
作用域：
    局部作用域
    全局作用域
    内建作用域    
    
'''

# 判断引入模块正确性
'''
# 判断引入模块的正确性，确保引入的不是本地同名文件
print(datetime.__file__)
'''

# 自定义模块引入
'''
引入自定义模块，不用加.py后缀
import assert
注意：一个模块只会被引入一次，不管你执行了多少次import。防止模块被多次引入

使用模块中的内容：
格式：模块名.函数名/变量名
'''

# 自定义模块引入部分
'''
from......import语句
作用：从模块导入一个指定的部分到当前命名空间
格式：from module import name1[,name2[,……namen]]

'''

# 自定义模块引入全部
'''
from......import *语句
作用：把一个模块中的所有的内容导入当前命名空间
注意：最好不要过多的使用，命名重复无法感知，导致方法或变量被覆盖
'''

# 如果不同的人编写的模块同名怎么办？
'''
解决：为了解决模块命名的冲突，引入了按目录来组织模块的方法，称为包
特点：引入了包以后，只要顶层的包不与其他人发生冲突，那么模块都不会与别人的发生冲突
注意：目录只有包含一个叫做"__init__.py"的文件才被认作是一个包，主要是为了避免一些滥竽充数的名字，目前这个文件中什么也不用写
'''