import threading


local = threading.local()
local.tname = 'main'


def func():
    local.tname = 'ysp'
    print local.tname


t1 = threading.Thread(target=func)
t1.start()
t1.join()


print local.tname