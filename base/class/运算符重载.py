'''
运算符重载：加法运算对应的函数是__add__,其他运算符都有对应的函数，可以重写
__add__: 加法运算
__str__: 在调用print打印对象时自动调用，是一个描述对象的方法，是给开发者使用的
'''

class Person(object):
    def __init__(self, num):
        self.num = num

    # 运算符重载
    def __add__(self, other):
        return Person(self.num + other.num)

    def __str__(self):
        return "num=" + str(self.num)

per1 = Person(1)
per2 = Person(2)

print(per1 + per2)

print(per1.__add__(per2))