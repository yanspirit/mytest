# encoding: UTF-8
import threading
import time
 
data = 0
lock = threading.Lock()
 
def func():
    global data
    print '%s acquire lock...' % threading.currentThread().getName()
    
    # ����acquire([timeout])ʱ���߳̽�һֱ������
    # ֱ�������������ֱ��timeout���timeout������ѡ����
    # �����Ƿ�������
    if lock.acquire():
        print '%s get the lock.' % threading.currentThread().getName()
        data += 1
        time.sleep(2)
        print '%s release lock...' % threading.currentThread().getName()
        
        # ����release()���ͷ�����
        lock.release()
 
t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)
t1.start()
t2.start()
t3.start()