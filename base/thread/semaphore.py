'''
semaphore: 信号量
    控制并发线程数量
语法：
with sem
'''
import threading, time

sem = threading.Semaphore(2)

def run():
    with sem:
        for i in range(10):
            print("%s--%d"%(threading.current_thread().name, i))
            time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=run).start()