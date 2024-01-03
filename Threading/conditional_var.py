from threading import *
import time

done = 1
cond = Condition()

def threadName(name):
    global done
    
    with cond:
        if done == 1:
            done = 2
            print("Waiting on condition variable cond: ",name)
            cond.wait()
            print('Condition met: ', name)

        else:
            for i in range(5):
                print('.')
                time.sleep(1)

            print('Signaling conditional variable cond: ', name)
            cond.notify_all()
            print("Notification done: ", name)



if __name__ == '__main__':
    t1 = Thread(target=threadName, args=('t1',))
    t2 = Thread(target=threadName, args=('t2',))

    t1.start()
    t2.start()
    t1.join()
    t2.join()