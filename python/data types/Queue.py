#Object Queue   
#qsize   empty  full   put 
#put_nowait== put(item,False)   get   get_nowait  
# task_done(对每一个put进去的item都会调用)
#join   all be gotten and processed



#LifoQueue   PriorityQueue   
#exception   Empty   Full
def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()


q = Queue()

for i in range(num_worker_threads):
    t = Thread(target = worker)
    t.daemon = True;
    t.start()



for item in source():
    q.put(item)
    
q.join()



