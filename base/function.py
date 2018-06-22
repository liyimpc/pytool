'''
定义函数:

格式:

def 函数名(参数列表)
    语句
    return 表达式

'''

# 定义默认参数
# 如果h定义一个默认参数，最后放到参数最后，否则容易报错
def myPrint(str="my name", age=18):
    print(str, age)

myPrint("my name is lym", 17)

# 不定长度参数
# *arr 是一个元组(tuple)
# 加了*号的变量存放所有未命名的变量参数，如果在函数调用时没有指定参数，它就是一个空元组
def func(name, *arr):
    print(name)
    print(type(arr))
    for x in arr:
        print(x)

func("lym", "is", "a", "good", "body")

# 不定长参数
# **arr 是一个字典(dict)
def func3(**arr):
    print(arr)
    print(type(arr))

func3(x=1, y=2, z=3)

'''
匿名函数
    不使用def这样的语句定义函数，使用lambda来创建匿名函数
    
特点：
1、lambda只是一个表达式，函数体比def简单
2、lambda的主体是一个表达式，而不是代码块，仅仅只能在lambda中封装简单的逻辑
3、lambda函数有自己的命名空间，且不能访问自有参数列表之外的或全局命名空间里的参数
4、虽然lambda是一个表达式，且看起来只能写一行，与C和C++的内联函数不同。

格式：
    lambda 参数1，参数2，……，参数n:expression
'''
sum = lambda num1, num2:num1 + num2
print(sum(1,2))


'''
值传递: 传递不可变类型
string, tuple, number是不可变的
'''
def func1(num):
    print(id(num))
    num =10
    print(id(num))

temp = 20
print(id(temp))
func1(temp)
print(temp)

'''
引用传递: 传递可变类型 
list, dict, set是可变的
'''
def func2(list):
    list[0] = 100
l = [1,2,3]
func2(l)
print(l)


a = 10
b = 10
c = b
b = 20
print(id(a))
print(id(b))
print(id(c))
'''
思考：
10在内存中存在【数据常量区】或【静态存储区】  

a = 10 创建一个内存地址0x100
b = 10 根据值寻找内存中是否已经存在对应的内存地址0x100
所以a,b,c使用的是同一个内存地址

如果b = 20,会在常量区创建一个新的内存地址0x200
然后指定b=0x200
'''


