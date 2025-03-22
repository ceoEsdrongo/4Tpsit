import threading
import time

def print_1(a,b):
    print(a)
    time.sleep(1)
    print(b)
def print_2(a):
    print(a)
def main():
    t1=threading.Thread(target=print_1, args=('CIAO','secondo parametro',))
    t2=threading.Thread(target=print_2, args=('come stai?',))
    t1.start()
    t2.start()
main()
