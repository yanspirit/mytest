from functools import wraps

def thisIsliving(fun):
    @wraps(fun)
    def living(*args,**kw):
        return fun(*args,**kw)+ 'living is eating'
    return living

@thisIsliving
def whatIsLiving():
    "what is living"
    return "mygod,what is living,"


print whatIsLiving()
print whatIsLiving.__doc__