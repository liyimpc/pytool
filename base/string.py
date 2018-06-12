#!/usr/bin/python3

# len(str)
# 返回字符串长度
print(len("lym is good man"))

# str.lower()
# 大写转小写
print("LYM is good man".lower())

# str.upper()
# 小写转大写
print("lym is good man".upper())

# str.swapcase()
# 大写转小写，小写转大写
print("LYM is GOod Man".swapcase())

# str.capitalize()
# 整个句子首字母大写，其它小写
print("LYM is GOod Man".capitalize())

# str.title()
# 每个单词的首字符大写，其它小写
print("LYM is GOod Man".title())

# str.center(width[, fillchar])
# [, fillchar]意思是可有可无的参数
# 返回一个指定宽度的居中的字符串,fillchar为填充的字符,默认空格填充
print("LYM is GOod Man".center(40, "*"))

# str.ljust(width[, fillchar])
# 返回一个指定宽度的左对齐字符串,fillchar为填充的字符,默认空格填充
print("LYM is GOod Man".ljust(40, "%"), "*")

# str.rjust(width[, fillchar])
# 返回一个指定宽度的右对齐字符串,fillchar为填充的字符,默认空格填充
print("LYM is GOod Man".rjust(40, "%"), "*")

# str.zfill(width)
# 返回一个width长度的字符串，原字符串右对齐，默认0填充
print("LYM is GOod Man".zfill(40))

# str.count(str[, start][, end])
# 统计指定字符str的个数，在设定的起始位置和结束位置内
print("lym is a very very nice man".count("very", 5, len("lym is a very very nice man")))

# str.find(str[, start][, end])
# 检测指定字符串str是否包含在字符串中，在设定的起始位置和结束位置内,得到的是第一次出现的开始下标,没有返回-1
print("lym is a very very nice man".find("very", 5, len("lym is a very very nice man")))

# str.rfind(str[, start][, end])
# 从左向右检测指定字符串str是否包含在字符串中，在设定的起始位置和结束位置内,得到的是第一次出现的开始下标,没有返回-1
print("lym is a very very nice man".rfind("very", 5, len("lym is a very very nice man")))

# str.index(str, start=0, end=len(str))
# 跟find()一样，只不过str不存在的时候抛出异常
print("lym is a very very nice man".index("very"))

# str.rindex(str, start=0, end=len(str))
# 跟rfind()一样，只不过str不存在的时候抛出异常
print("lym is a very very nice man".rindex("very"))

# str.lstrip()
# 截掉字符串左侧指定的字符,默认为空格,只能是最左侧数据
print("lym is a very very nice man".lstrip("lym"))

# str.rstrip()
# 截掉字符串右侧指定的字符,默认为空格,只能是最右侧数据
print("lym is a very very nice man".rstrip("n"))

# str.strip()
# 截掉字符串左侧或右侧指定的字符,默认为空格,只能是最右侧或最左侧的数据
print("lym is a very very nice man".strip("man"))

# 转换ascii值
print(ord("a"))
# ascii转换为字符
print(chr(65))


