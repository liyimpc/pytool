'''
python对协程的支持是通过generator实现的
run()=>data = "" 必须先创建一个存储变量，send传递值的时候用来接收数据
m = run() 创建生成器
m.send() 给函数传递值
'''

def run():
    print(1)
    yield 10
    print(2)
    yield 20
    print(3)
    yield 30

# 协程的最简单风格，控制函数的阶段执行，节约线程或进程的的切换
# 返回值是一个生成器
m = run()
print(next(m))
print(next(m))
print(next(m))
