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
        f(age);
    return inner

m = outer1(say)
m(-10)
