import re,sys

def baidu(username):
    return "using parser baidu.and the user name is %s." % username

def qzone(uin):
     return "Using parser Qzone, and the user's QQ is: %s." % uin
 
def group(seq,size):
     def take(seq,n):
         for i in xrange(n):
             yield seq.next()
             
     
     if not hasattr(seq,'next'):
         seq = iter(seq)
     while True:
         x = list(take(seq,size))
         if x:
             yield x
         else:
             break
         

def parser_init(url,mapping):
    for pat,what in group(mapping,2):
        result = re.compile('^'+pat+'$').match(url)
        if result:
            return what,[x for x in result.groups()]
    return None,None


if __name__ == '__main__':
    mapping = ('http://(?:hi|space).baidu.com/([^/]+)(?:/.*)?','baidu',
               'http://(\d+).qzone.qq.com(?:/.*)?','qzone',)
    
    
    (func,args) = parser_init(sys.argv[1],mapping)
    
    
    if func:
        callback = func
        
        if func in globals():
            callback = globals()[func]
            
        if callable(callback):
            print callback(*args)
    else:
        print 'No parser found.';