'''
概述：
使用键值存储，具有极快的查找速度

key的特性：
1、字典的key必须唯一
2、key必须是不可变的对象
3、字符串，整数都是不可变的，可以作为key
4、list是可变的，不能作为key
5、字典是无序的

和list比较：
1、查询和插入速度极快，不会随着key-value的增加而变慢
2、需要占用大量的内存
'''

dict1 = {"tom":60, "lilei":70}

# 元素的访问
# 获取：字典[key]
print(dict1["lilei"])

# 按照此种方式查询，如果key不存在，不会报错，并返回None
ret = dict1.get("sunck")
if ret == None:
    print("没有")
else:
    print("存在")

# 添加
dict1["han"] = 99

# 修改
dict1["lilei"] = 80

# 删除
dict1.pop("tom")
print(dict1)

# 遍历
for key in dict1:
    print(key, dict1[key])

# 遍历返回值
for value in dict1.values():
    print(value)

# 遍历返回元组
for k, v in dict1.items():
    print(k, v)

# 遍历返回索引和key
for i, v2 in enumerate(dict1):
    print(i, v2)
