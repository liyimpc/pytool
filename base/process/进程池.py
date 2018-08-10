'''
Pool: 进程池
'''
from multiprocessing import Pool
import os, time, random


def run(num):
    print("子进程启动%d,pid=%d"%(num, os.getpid()))
    start = time.time()
    time.sleep(random.choice([1,2,3]))
    end = time.time()
    print("子进程结束%d,pid=%d,耗时%.2f"%(num, os.getpid(), end-start))


if __name__ == '__main__':
    print("启动父进程")

    # 创建进程池
    # Pool默认大小是cpu核心数
    pp = Pool(4)
    for i in range(5):
        # 创建进程，放入进程池统一管理
        pp.apply_async(run, args=(i,))
    # 在调用join之前必须先调用close,调用close之后就不能再继续添加新的进程了
    pp.close()
    # 进程池对象调用join,会等待进程池中所有的子进程结束完毕再去执行父进程
    pp.join()
    print("父进程结束")