#!/usr/bin/python3

'''
tuple

本质：是一种有序集合

特点：
1、与列表非常相似
2、一旦初始化就不能修改。元素不能改变，列表可以。
3、使用小括号

思考：
为什么有列表，为何还要创造元组？
元组不可变，安全性较高，能用元组的不要用列表

创建tuple:
元组名=（元组元素1，元组元素2，……，元组元素n）
'''

# 创建空的元组
tuple1 = ()
print(tuple1)

# 创建带有元素的元组
tuple2 = (1,2,3,"good",True)
print(tuple2)

# 定义只有一个元素的元组
tuple3 = (1, )
print(tuple3)
print(type(tuple3))

# 元组元素的访问
# tuple[下标]
tuple4 = (1,2,3,4)
print(tuple4[0])

# 获取最后一个元素
print(tuple4[-1])

# 修改元组
tuple5 = (1,2,3,4,[1,2,3])
#tuple5[0] = 500 报错，元组内的元素不能改变
tuple5[-1][0] = 500 # 列表可以改变

# 删除元组
tuple6 = (1,2,3)
del tuple6

# 元组的操作
t7 = (1,2,3)
t8 = (4,5,6)
t9 = t7 + t8
print(t9)

# 元组重复
t10 = (1,2,3)
print(t10 * 3)

# 判断元素是否在元组中
t11 = (1,2,3,4)
print(4 in t11)

# 元组的截取
# tuple[开始下标:结束下标]
t12 = (1,2,3,4,5,6,7,8,9)
print(t12[3:7])
print(t12[3:])
print(t12[:7])

# 二维元组
t13 = ((1,2,3), (4,5,6), (7,8,9))
print(t13[1][1])

# 元组的方法
t14 = (1,2,3,4,5,6)
print(len(t14)) # len 返回元组元素个数
print(max(t14)) # len 返回元组中最大值
print(min(t14)) # len 返回元组中最小值

# 将列表转换成元组
list = [1,2,3]
t15 = tuple(list)
print(t15)

# 遍历
for i in (1,2,3,4,5):
    print(i)





