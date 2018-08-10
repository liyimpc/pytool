'''
自定义进程封装类
'''
from multiprocessing import Process
import os, time

class MyProcess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print("子进程(%s-%s)启动"%(self.name, os.getpid()))
        # 子进程的功能
        time.sleep(3)
        print("子进程(%s-%s)结束" % (self.name, os.getpid()))


if __name__ == '__main__':
    print("父进程启动")
    p = MyProcess("test")
    # 自动调用封装函数的run方法
    p.start()
    p.join()
    print("父进程结束")