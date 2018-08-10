'''
timer: 定时执行
'''
import threading, time

def run():
    print("开始执行线程")

if __name__ == '__main__':
    # 延时执行线程
    t = threading.Timer(5, run)
    t.start()

    t.join()
    print("父线程结束")