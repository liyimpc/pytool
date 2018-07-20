from types import MethodType
'''
动态添加方法必须先引入MethodType

__slots__: 限制添加属性,元组类型
'''

class Person(object):

    # 限制添加的属性
    __slots__ = ("name", "age", "speak")

    def __init__(self, name):
        # 对象属性
        self.name = name

p = Person("lym")
# 添加属性
p.age = 18
print(p.age)

# 添加方法（切记要先引入MethodType）
def say(self):
    print("my name is " + self.name)

p.speak = MethodType(say, p)
p.speak()

# 限制添加属性 (定义一个特殊的属性[__slots__])
# p.height = 170 # height在限制外，所以动态添加属性后异常： AttributeError: 'Person' object has no attribute 'height'
