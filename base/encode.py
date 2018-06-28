'''
编码与解码格式必须一致
二进制文件，如果要写入字符串必须指定编码
字符串默认编码是utf-8
'''

'''
编码
'''

path = '/opt/log/TestWeb.log.2018-04-08.log'
with open(path, "wb") as f:
    str = "my name is god"
    f.write(str.encode("utf-8"))

'''
解码
'''
with open(path, "rb") as f1:
    sb = f1.read()
    print(sb)
    print(type(sb))
    newsb = sb.decode("utf-8")
    print(newsb)
    print(type(newsb))
