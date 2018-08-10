'''
barrier: 凑够一定数量才能一起执行
'''
import threading, time

bar = threading.Barrier(4)

def run():
    print("%s--start"%(threading.current_thread().name))
    time.sleep(1)
    bar.wait()
    print("%s--end" % (threading.current_thread().name))

if __name__ == '__main__':
    for i in range(10):
        threading.Thread(target=run).start()