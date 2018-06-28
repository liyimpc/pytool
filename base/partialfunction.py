'''
偏函数
    通过调用functools.partial方法，把入参固定住或设置默认值，封装成一个新的函数

'''

import functools

print(int("1010", base=2))

# 把一个参数固定住，形成一个新的函数
int3 = functools.partial(int, base = 2)
print(int3("1010"))

# 自定义函数，包装成偏函数
def test(name, age):
    print("my name is %s, now is %d years old" % (name, age))

test1 = functools.partial(test, age = 2)
print(test1("lym"))