#coding: UTF-8
from threading import Thread
import time

def test(a, b):
    for i in range(a, b):
        print(i)

thread1 = Thread(target=test, args=(0, 20))
thread2 = Thread(target=test, args=(20, 51))

thread1.start()
time.sleep(1)
thread2.start()
thread1.join()
thread2.join()