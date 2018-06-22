from collections import Iterable
from collections import Iterator
'''
可迭代对象：可以直接作用于for循环的对象
Iterable: 可以用isinstance()去判断一个对象是否是Iterable对象

可以直接作用于for的数据类型一般分两种：
1、集合数据类型，如list,tuple,dict,set,string
2、generator,包括生成器和带yield的generator function
'''

print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print(isinstance("", Iterable))
print(isinstance((x for x in range(10)), Iterable))

'''
迭代器：不但可以作用于for循环，还可以被next()函数不断调用，并返回下一个值，直到最后跑出一个StopIteration错误，表示无法继续返回下一个值
Iterator: 可以用isinstance()去判断一个对象是否是迭代器

返回类型是generator object对象，用next()函数去调用
'''
print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance({}, Iterator))
print(isinstance("", Iterator))
print(isinstance((x for x in range(10)), Iterator)) # 只有这个是迭代器

l = (y for y in range(3))  # <generator object <genexpr> at 0x108fb3fc0>
print(next(l))
print(next(l))
print(next(l))
# print(next(l)) # 超出范围之后，返回StopIteration错误