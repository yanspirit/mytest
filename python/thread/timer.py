import threading

def func():
    print 'hello timer'


timer = threading.Timer(5,func)
timer.start()