'''
sorted 排序,默认升序排序
'''
list1 = [4,7,2,6,3]
list2 = sorted(list1)
print(list1)
print(list2)

# 按绝对值大小排序
list3 = [4, -7, 2, 6, -3]
# key接受函数来实现自定义排序规则
list4 = sorted(list3, key=abs)
print(list3)
print(list4)

# 降序
list5 = [4, 7, 2, 6, 3]
list6 = sorted(list5, reverse=True)
print(list5)
print(list6)

# 按字符串长短来排序
list7 = ['b333', 'a1111111', 'c22', 'd5544', 'f123']
list8 = sorted(list7, key=len)
print(list7)
print(list8)

# 自定义函数
def myLen(str):
    return len(str)
list8 = sorted(list7, key=myLen)
print(list7)
print(list8)