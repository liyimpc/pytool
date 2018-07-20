'''
对象属性与类属性
说明：对象属性的优先级高于类属性
注意：不能让对象属性与类属性重名，因为对象属性会屏蔽掉类属性。但是删除对象属性之后，又能使用类属性，所以不太好控制。
'''

class Person(object):
    # 类属性
    name = "person"

    def __init__(self, name):
        # 对象属性
        self.name = name

# 类属性
print(Person.name)

# 对象属性
p = Person("tom")
print(p.name)
print(Person.name)

# 动态的给对象添加对象属性, 只针对于当前对象生效，对于类创建的其他对象没有作用
p.age = 18
p1 = Person("jerry")
#print(p1.age) 对象不存在，无效

# 删除对象属性，会在类属性寻找
del p.name
print(p.name)