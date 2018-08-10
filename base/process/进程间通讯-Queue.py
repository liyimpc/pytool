'''
通过Queue来在进程间传递数据
terminate: 强制结束进程
'''
from multiprocessing import Process, Queue
import os, time

def write(q):
    print("启动写子进程%s"%(os.getpid()))
    for chr in ["A", "B", "C", "D"]:
        # 队列写入数据
        q.put(chr)
        time.sleep(1)
    print("结束写子进程%s" % (os.getpid()))

def read(q):
    print("启动读子进程%s"%(os.getpid()))
    while True:
        # 队列取出数据
        value = q.get(True)
        print("value=", value)
    print("结束读子进程%s" % (os.getpid()))

if __name__ == '__main__':
    # 父进程创建队列，并传递给子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()

    pw.join()
    # 读的子进程是死循环，无法结束，所以只能强行结束子进程
    pr.terminate()

    print("父进程结束")