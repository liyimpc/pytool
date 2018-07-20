from base.polymorphic.animal import Animal

# 老鼠类，继承父类的行为和方法
class Mouse(Animal):
    def __init__(self, name):
        super(Mouse, self).__init__(name)