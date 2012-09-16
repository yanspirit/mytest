def factorial(x):
    if x==0:
        return 1
    else:
        return x * factorial(x-1)
    
def  fact(x):
    return x>1 and x*fact(x-1) or 1

f = lambda x: x and x*f(x-1) or 1

print factorial(6)