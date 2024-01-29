from threading import *
import time

# if we set 1 then it will work as binary semaphore that is mutex
# Mutex internally binary semphore hi hote hai
s = Semaphore(4)

def thread(name):
    s.acquire()
    for i in range(2):
        print(f'{name} is working now. ans i: {i}')
        time.sleep(1)
        print('--------------------------')

    s.release()

if __name__ == '__main__':
    t1 = Thread(target=thread, args=("1 Thread", ))
    t2 = Thread(target=thread, args=("2 Thread", ))
    t3 = Thread(target=thread, args=("3 Thread", ))
    t4 = Thread(target=thread, args=("4 Thread", ))
    t5 = Thread(target=thread, args=("5 Thread", ))
    t6 = Thread(target=thread, args=("6 Thread", ))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
