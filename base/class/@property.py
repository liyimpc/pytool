'''
@property 方法装饰，可以让你对受限制访问的属性用点语法
'''

class Person(object):
    def __init__(self, age):
        self.__age = age

    # 方法名和私有变量名一致
    @property
    def age(self):
        return self.__age

    # 去掉私有变量下划线.setter
    @age.setter
    def age(self, age):
        if age < 0:
            age = 0
        self.__age = age


per = Person(18)
per.age = 100   # 相当于调用setAge
print(per.age)  # 相当于调用getAge
