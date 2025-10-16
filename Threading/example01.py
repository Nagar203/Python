from threading import *
import time


# lock = Lock()
cnt =0

def threadA():
    global cnt
    for i in range(10000000):
        cnt +=1

if __name__ == '__main__':
    t1 = Thread(target=threadA)
    t2 = Thread(target=threadA)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(cnt)
