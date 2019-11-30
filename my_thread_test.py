
import threading
import time,random,math

from threading import current_thread, main_thread
 
# idx 循环次数
def printNum(idx, delay ):
    for num in range(idx):
        #打印当前运行的线程名字
        print("{0}\tnum={1}".format(threading.current_thread().getName(), num) )
        # delay = math.ceil(random.random() * 2)
        time.sleep(delay)
 
def is_huozhe(th1, th2):
    while th1.is_alive() or th2.is_alive():
        print(threading.active_count(), threading.current_thread().getName(), th1.is_alive(), th2.is_alive())
        time.sleep(0.05)
    time.sleep(0.05)
    print(threading.current_thread().getName(), th1.is_alive(), th2.is_alive())
    print(threading.active_count(), "zuihou============")
    time.sleep(0.05)
    print(threading.current_thread().getName(), th1.is_alive(), th2.is_alive())
    print(threading.active_count(),"zuihou============")

if __name__ == '__main__':
    step = 9
    th1 = threading.Thread(target=printNum, args=(step,0.1),name="thread1")
    th2 = threading.Thread(target=printNum, args=(step, 0.3), name="thread2",daemon=True)
    th3 = threading.Thread(target=is_huozhe, args=(th1, th2), name="is_huozhe")
    
    #启动2个线程
    # th1.setDaemon(True)
    th1.start()
    th2.start()
    th3.start()
    #等待至线程中止
    # th1.join()
    # th2.join()
    # time.sleep(4)
    # print(threading.active_count(),"++++++++++++++")

    print("{0} 线程结束".format(threading.current_thread().getName()))


​