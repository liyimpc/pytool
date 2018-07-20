from base.polymorphic.animal import Animal

# 猫类，继承父类的行为和方法
class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)