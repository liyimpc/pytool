'''
run()=>data = "" 必须先创建一个存储变量，send传递值的时候用来接收数据
m = run() 创建生成器
m.send() 给函数传递值
m.close() 关闭生成器
'''

def run():
    # 存储变量，始终为空
    data = ""
    r = yield data
    print(1, r, data)
    r = yield data
    print(2, r, data)
    r = yield data
    print(3, r, data)
    r = yield data

# 创建生成器
m = run()

# 启动m
print(m.send(None))
print(m.send("a"))
print(m.send("b"))
print(m.send("c"))
m.close()

'''
详细解析：
m.send(None),执行run的方法内容（data = "" r = yield data）
m.send("a"),接收了返回值，r = a, 所以接下来打印 1，a, 接着执行r = yield data


'''
