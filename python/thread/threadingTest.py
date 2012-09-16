import threading

def func():
    print 'func() passed to Thread'
    
    

t = threading.Thread(target=func)
t.start()

