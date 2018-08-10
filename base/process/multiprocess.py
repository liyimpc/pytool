'''
多进程库
multiprocessing库
跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象
'''

from multiprocessing import Process
from time import sleep
import os

def run(str):
    while True:
        print("进程2=%s pid=%d parentpid=%d"%(str, os.getpid(), os.getppid()))
        sleep(1.2)

if __name__ == '__main__':
    print("主进程启动")

    '''
    创建子进程
    target：说明进程执行的任务
    args: 传递参数，如果只有一个参数，需要在参数后面加逗号
    '''
    p = Process(target=run, args=("nice",))
    # 启动进程
    p.start()

    while True:
        print("进程1 pid=%d parentpid=%d"%(os.getpid(), os.getppid()))
        sleep(1)

