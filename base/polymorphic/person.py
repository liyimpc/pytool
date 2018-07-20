# 定义一个人类，喂猫和老鼠食物, 抽象出动物的方法
class Person(object):
    def __init__(self):
        pass

    def feedCat(self, cat):
        print("给猫食物")
        cat.eat()

    def feedMouse(self, mouse):
        print("给老鼠食物")
        mouse.eat()

    # 通过父类对象抽象方法
    def feedAnimal(self, animal):
        print("给%s食物" % (animal.name))
        animal.eat()