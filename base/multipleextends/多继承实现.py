from base.multipleextends.child import Child


def main():
    c = Child(300, 100)
    print(c.money, c.faceValue)
    c.play()
    c.eat()
    # 注意：多继承，父类中方法名相同，默认调用的是在括号(Father, Mother)中排前面父类中的方法
    c.func()

if __name__ == '__main__':
    main();
