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

# str.split(str="", num)
# 截出来的数据放到列表里
str38 = "sunk**is*a**good*man"
print(str38.split("*"))
# num：仅截取num次*
print(str38.split("*", 4))

# splitlines 按照('\r', '\r\n', '\n')分割
# keepends = True 会保留换行符, 默认False
str40 = '''
lym is a good man
lym is a nice man 
lym is a handsome man

'''
print(str40.splitlines())
print(str40.splitlines(True))

# join(seq) 以指定的字符串分隔符，将seq中的所有元组组合成一个字符串
list41 = ['sunk', 'is', 'a', 'good', 'man']
str42 = "&".join(list41)
print(str42)

# max() min(), 比较按照ascii来比较
str43 = "lym is a good man"
print(max(str43))
print("*"+min(str43)+"*")

# replace(oldstr, newstr, count)
# 用newstr替换oldstr,默认是全部替换，如果指定了count,只替换count个
str44 = "lym is a good man"
str45 = str44.replace("good", "nice", 1)
print(str45)

# str.makestrans(oldstr, newstr)
# 创建一个字符串映射表
# translate() 结合映射表一起使用
t46 = str.maketrans("ac", "65")
# 映射规则：a->6 c->5
str47 = "lym is a good man good cca"
str48 = str47.translate(t46)
print(str48)

# startswith(str, start=0, end=len(str))
# 在给定的范围内，是否是以给定的字符串开头，如果没有指定范围，默认整个字符串
str49 = "lym is a good man"
print(str49.startswith("lym", 0, 5))

# endswith(str, start=0, end=len(str))
# 在给定的范围内，是否是以给定的字符串结尾，如果没有指定范围，默认整个字符串
print(str49.endswith("lym", 0, 5))

# encode(encoding="UTF-8", errors="strict")
# 编码
str50 = "lym is a good man 李一鸣"
data52 = str50.encode("utf-8", "ignore")
print(data52)

# decode(encoding="UTF-8", errors="strict")
# 解码   注意：要与编码格式一致
str53 = data52.decode("utf-8", "ignore")
print(str53)

# isalpha()
# 如果字符串中至少有一个字符且所有的字符都是字母,返回True,否则返回False
str54 = "lym is a good man"
print(str54.isalpha())

# isalnum()
# 如果字符串中至少有一个字符且所有的字符都是数字，返回True，否则返回False
str55 = "123"
print(str55.isalnum())

# isupper()
# 如果字符串中至少有一个字符且所有的字符都是大写，返回True，否则返回False
str56 = "LYM"
print(str56.isupper())

# istitle()
# 如果字符串是标题化的,返回True，否则返回False
# 标题化：首字母大写,其余字母小写
print("Lym Is".istitle())

# isdgit()
# 如果字符串只包含数字字符，返回True,否则返回False
print("123".isdigit())

# isnumeric()
# 如果字符串只包含数字，返回True,否则返回False
print("123".isnumeric())

# isdecimal()
# 如果字符串只包含十进制字符，返回True,否则返回False
print("123".isdecimal())

# isspace()
# 如果字符串只包空格，返回True,否则返回False
# \t \n \r
print("\t".isspace())