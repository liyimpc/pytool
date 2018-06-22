'''
set：类似dict, 是一组key的集合，不存储value
本质：无序，无重复元素的集合
'''

# 创建
# 创建set需要一个list或tuple或dict作为输入集合
# 如果有重复值，自动去重
s1 = set([1,2,3,4,5,2])
print(s1)

s2 = set((1,2,3,3,2,1))
print(s2)

# 只拿了key
s3 = set({"one":1, "two":2})
print(s3)

# 添加
s4 = set([1,2,3,4,5,2])
s4.add(6)
s4.add((7,8,9)) # 可以添加不可变元素，例如元组。添加list或tuple就会抛异常
print(s4)

# 更新
# 插入整个list,tuple,字符串，插入的类型被打碎插入
s5 = set([1,2,3,4,5,2])
s5.update([7,8])
s5.update((9,10))
s5.update("lym")
print(s5)

# 删除
s6 = set([1,2,3,4,5,2])
s6.remove(3)
print(s6)

# 遍历
for i in s6:
    print(i)

for index, data in enumerate(s6):
    print(index, data)

# 交集
s8 = set([2,3,5])
s9 = set([2,3,4])
a1 = s8 & s9
print(a1)

# 并集
a2 = s8 | s9
print(a2)