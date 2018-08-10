'''
线程间内存是共享的
'''
import threading

num =10

def run(n):
    global num
    for i in range(1000000):
        num = num + n
        num = num - n

if __name__ == '__main__':
    # 任何进程默认就会启动一个线程，称为主线程，主线程可以启动新的子线程

    # current_thread: 返回当前线程的实例
    print("主线程(%s)启动"%(threading.current_thread().name))

    '''
    创建子线程
    target: 调用的子线程方法
    name: 传递的子线程名字
    args: 给子线程传递数据
    '''
    t1 = threading.Thread(target=run, name="runThread-1", args=(1,))
    t2 = threading.Thread(target=run, name="runThread-2", args=(2,))
    t1.start()
    t2.start()
    # 等待线程结束
    t1.join()
    t2.join()

    print("主线程(%s)结束, num=%d" % (threading.current_thread().name, num))