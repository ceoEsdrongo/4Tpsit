import threading
import time

def print_1(a,b):
    for i in range(10):
        print(i,'Thread 1')
        time.sleep(1)
def print_2(a):
    for i in range(10):
        print(i, 'thread 2')
        time.sleep(1)
def main():
    t1=threading.Thread(target=print_1, args=('CIAO','secondo parametro',))
    t2=threading.Thread(target=print_2, args=('come stai?',))
    t1.start()
    t2.start()
main()
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import threading
import time

def print_1(a,b):
    for i in range(10):
        print(i,'Thread 1')
        time.sleep(1)
def print_2(a):
    for i in range(10):
        print(i, 'thread 2')
        time.sleep(1)
def main():
    t1=threading.Thread(target=print_1, args=('CIAO','secondo parametro',))
    t2=threading.Thread(target=print_2, args=('come stai?',))
    t1.start()
    t1.join()
    t2.start()
main()
----------------------------------------------------------------------------------------------------------------------
import threading
import time

def print_1():
    print('start thread: ', threading.current_thread().name)
    time.sleep(2)
    print('fine thread ', threading.current_thread().name)
def print_2():
    for i in range(10):
        print('start thread: ', threading.current_thread().name)
        print('end thread: ', threading.current_thread().name)

def main():
    t1=threading.Thread(target=print_1, name="THREAD1-UNO")
    t2=threading.Thread(target=print_2, name="THREAD1-UNO")
    t1.start()
    t1.join()
    t2.start()
main()
-----------------------------------------------------------------------------------------------------------------------------------------
import threading
import time

def print_1():
    print('start thread: ', threading.current_thread().name)

def main():
    t1=threading.Thread(target=print_1, name="THREAD1-UNO")
    t1.start()
    print('thread number: ', threading.get_ident())
    print('thread native_id: ', threading.get_native_id())
    print('thread local data: ', threading.local())
    
main()
------------------------------------------------------------------------------------------------------------------------------------------
