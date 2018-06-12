#!/usr/bin/python3

list1 = [1, 2, "sunck", "good", False]
print(list1)

# 列表组合
list5 = [1,2,3]
list6 = [4,5,6]
list7 = list5 + list6
print(list7)

# 列表的重复
list8 = [1,2,3]
print(list8 * 3)

# 判断元素是否在列表中
list9 = [1,2,3,4,5]
print(3 in list9)

# 列表截取
list10 = [1,2,3,4,5,6,7,8,9]
print(list10[2:6])
print(list10[:5])
print(list10[3:])

# 二维列表
list11 = [[1,2,3], [4,5,6], [7,8,9]]
print(list11[1][1])

#  ======================= 列表方法 ======================= #
# append (列表末尾添加新元素)
list12 = [1,2,3]
print(list12.append(6))
print(list12.append([7,8,9]))   # [1,2,3,[7,8,9]]

# extend (在末尾一次性追加另一个"列表"的多个值)
list13 = [1,2,3]
list13.extend([4,5,6])  # [1,2,3,4,5,6]
print(list13)

# insert (在下标处添加一个元素，不覆盖原数据，原数据向后顺延)
list14 = [2,3,4]
list14.insert(2, 100) # [2, 100, 3, 4]
list14.insert(2, [200, 300])  # [2,[200, 300], 3, 4]
print(list14)

# pop(x=list[-1]) (移除列表中指定下标处的元素，默认移除最后一个元素)
list15 = [2, 3, 4, 5, 6]
list15.pop()
list15.pop(2)
print(list15)

# remove (移除列表中第一个匹配的的值)
list16 = [1,2,3,4,5,6]
list16.remove(4) #[1,2,3,5,6]
print(list16)

# clear (清除列表中所有的数据)
list17 = [1,2,3]
list17.clear()
print(list17)

# index (从列表中找出某个值的第一个匹配的下标)
list18 = [1,2,3,4,5,3,6,7,8,9]
index18 = list18.index(3)
# index(val, begin, end) 圈定范围删除指定的值，如果没有，抛出异常
index19 = list18.index(3, 3, 7)
print(index18, index19) # 2, 5

# len (列表中元素个数)
list19 = [1,2,3,4,5,6]
print(len(list19))

# max (获取列表中最大值)
list20 = [1,2,3,4,5,6]
print(max(list20))

# min (获取列表中最小值)
list21 = [1,2,3,4,5,6]
print(min(list21))

# count (查看元素在列表中出现的次数)
list22 = [1,2,3,4,4,5,6,3,2,3]
print(list22.count(3))

# 倒叙
list23 = [1,2,3,4,5]
print(list23.reverse())

# 排序
list24 = [2,1,4,3,5]
print(list24.sort())

# 拷贝
list25 = [1,2,3,4,5]
# 浅拷贝，内存地址一样
list26 = list25
print(id(list25))
print(id(list26))
# 深拷贝，内存地址不一样
list27 = list25.copy()
print(id(list25))
print(id(list27))

