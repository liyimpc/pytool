'''
生产者和消费者
'''

# 生产者
def product(c):
    c.send(None)
    for i in range(5):
        print("生产者产生数据%d"%i)
        r = c.send(str(i))
        print("消费者消费了数据%s"%r)
    c.close()

# 消费者
def consumer():
    data = ""
    while True:
        n = yield data
        if not n:
            return
        print("消费者消费了%s"%n)
        data = "200"

# 创建生成器
c = consumer()

product(c)