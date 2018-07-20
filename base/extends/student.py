from base.extends.person import Person

# 传入父类的类名,就是继承
class Student(Person):
    def __init__(self, name, age, money):
        # 调用父类中的__init__
        super(Student, self).__init__(name, age, money)
