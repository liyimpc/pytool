'''
全局变量在多个进程中不能共享
'''

from multiprocessing import Process
from time import sleep

# 全局变量
num =100

def run(str):
    print("子进程启动")
    sleep(3)
    global num
    num +=1
    print("子进程结束, num=%d"%(num))


if __name__ == '__main__':
    print("父进程启动")

    '''
    创建子进程
    target：说明进程执行的任务
    args: 传递参数，如果只有一个参数，需要在参数后面加逗号
    '''
    p = Process(target=run, args=("nice",))
    # 启动进程
    p.start()
    # 让子进程结束后再执行父进程
    p.join()

    print("父进程结束, num=%d"%(num))

