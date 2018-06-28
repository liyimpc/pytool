'''
装饰器

概念：
    是一个闭包，把一个函数当做参数返回，一个替代版的函数返回，本质上就是一个返回函数的函数
'''

# simple decoration
def func1():
    print("lym is a good man")

def outer(f):
    def inner():
        print("***")
        f()
    return inner

inner = outer(func1)
inner()

# difficult deoration
def say(age):
    print("lym is %s years old" % (age))


def outer1(f):

    def inner(age):
        if age < 0:
            age = 0
        f(age)
    return inner

m = outer1(say)
m(-10)

'''
解释：
    say()是被装饰的方法
    outer1()是装饰器，传入的f是say()的加强版本
'''

# 注解(@)装饰器
def outer2(f):

    def inner(age):
        if age < 0:
            age = 0
        f(age)
    return inner

@outer2   # 等同于 say1 = outer2(say1)
def say1(age):
    print("lym is %s years old" % (age))

say1(-10)

# 通用装饰器
def outers(func):
    def inner(*args, **kwargs):
        # 添加修改的功能
        func(*args, **kwargs)

    return inner

@outers
def says(name, age):
    print("my name is %s, I am %d years old" % (name, age)) # %号需要传入元组入参

says("lym", 10)