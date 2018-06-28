'''

try …… except …… else

格式:
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句n
else:
    语句e

作用：用来检测try语句中的错误，而让except语句捕获错误信息并处理

注意：else语句可有可无,如果try语句块没有异常，最终会执行else语句
'''

try:
    #print(3/0)
    #print(num)
    print(3/1)
except ZeroDivisionError as e:
    print("除数为0")
except NameError as e:
    print("没有该变量")
else:
    print("代码没有问题")


# 使用except而不使用任何的错误类型
try:
    print(3/0)
except:
    print("程序出现了异常")

# 使用except包含多个异常
try:
    print(3/0)
except(ZeroDivisionError, NameError):
    print("出现了NameError或ZeroDivisionError")

# 特殊
#1、所有的错误都继承自BaseException
try:
    print(3/0)
except BaseException as e:
    print("异常1")
except ZeroDivisionError as e:
    print("异常2")

#2、跨越多层调用
def func1(num):
    print(1/num)
def func2(num):
    func1(num)
def main():
    func2(0)

try:
    main()
except ZeroDivisionError as e:
    print("捕获异常:%s" % (e))

'''
try……exccept……finally

格式:
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句n
finally:
    语句e

作用：无论语句是否有错误，都将执行finally    
'''

try:
    print(3/0)
except ZeroDivisionError as e:
    print("捕获异常:%s" % (e))
finally:
    print("最终执行")