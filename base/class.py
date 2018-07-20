'''
=====class定义=====
object: 基类，超类，所有类的父类。一般没有合适的父类，就写object

=====构造函数=====
__init__: 在使用类创建对象的时候自动调用
注意：如果不显式的写出构造函数，默认会自动添加一个空的构造函数

=====定义方法=====
注意：方法的参数必须以self当第一个参数
self: 代表类的实例，哪个对象调用方法，那么该方法中的self就代表那个对象。self并不是关键字，换成其他的名字也可以
self.__class__: 代表类名

=====析构方法=====
__del__: 释放对象内存时自动调用

=====释放内存=====
del: 手动释放内存

=====打印对象，自动调用=====
__str__(): 在调用print打印对象时自动调用，是一个描述对象的方法，是给开发者使用的
__repr__(): 是在shell下用的，在python解释器里直接敲对象名在回车的时候调用的方法
注意：在没有str时，且有repr, str = repr，所以一般开发直接写__str__即可
优点：当一个对象的属性很多，并且都需要打印，重写__str__，简化了代码

=====私有属性=====
例如: __money
格式: __属性名
如果要让内部的属性不被外部访问，在属性前加两个下划线(__)
在python中，如果在属性前加两个下划算，那么这个属性就变成了私有属性(private)
说明：不能直接访问私有属性，是因为python解释器把__money变成了_Person__money，格式：(_类名__属性名)，不同版本的解释器可能存在解释的变量名不同
注意：内部是可以直接使用的

=====特殊属性=====
例如：__init__
格式：前后两个下划线
说明：有特殊含义

=====当成私有属性=====
例如: _age
格式：_属性名
说明：只有一个下划线，虽然可以直接访问，请视我为私有属性

'''

class Person(object):
    name = "lym"
    age =30
    height = 160
    weight = 90
    def run(self):
        print(self.name)
        print(self.__money) # 私有属性，内部是可以使用的
        p = self.__class__("wo", 181, 1000)
        print(p.name)
        print("run")
    def eat(self, food):
        print("eat " + food)

    # 通过内部的方法修改私有属性
    def setMoney(self, money):
        if money < 0:
            __money = 0
        self.__money = money

    # 通过内部的方法获取私有属性
    def getMoney(self):
        return self.__money

    def __init__(self,name,height,money):
        self.name = name
        self.height = height
        self.__money = money
        print("这里是init", name, height)
        pass

    def __del__(self):
        print("这里是析构函数")

    def __str__(self):
        return "%s-%d-%d-%d" % (self.name, self.age, self.weight, self.height)

p = Person("liyiming", 160, 10000)
print(p)
# print(p.__money) 私有属性，调用直接报错
# print(p._Person__money) 私有属性访问，格式：(_类名__属性名)
p.eat("dami")
p.run()

# 手动释放内存
del p

# 对象释放以后就不能再访问了
#print(p.name)

# 在函数里定义的对象，会在函数结束时自动释放内存，这样可以减少内存空间的浪费
def fun():
    p2 = Person("liyiming", 160, 2000)

fun()