# 动物类，抽象的父类
class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + "吃")