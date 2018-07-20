from base.multipleextends.father import Father
from base.multipleextends.mother import Mother

# 继承多个父类
class Child(Father, Mother):
    def __init__(self, money, faceValue):
        # self传递给父类，给self所代表的对象添加属性和方法
        Father.__init__(self, money)
        Mother.__init__(self, faceValue)

