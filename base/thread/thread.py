'''
线程
模块：
    1、_thread模块 低级模块
    2、threading模块 高级模块，对_thread进行了封装

'''
import threading, time

def run(num):
    print("子线程(%s),args=%d"%(threading.current_thread().name, num))
    # 实现线程的功能
    time.sleep(2)
    print("打印")
    time.sleep(2)

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
    t = threading.Thread(target=run, name="runThread", args=(1,))
    t.start()
    # 等待线程结束
    t.join()

    print("主线程(%s)结束" % (threading.current_thread().name))