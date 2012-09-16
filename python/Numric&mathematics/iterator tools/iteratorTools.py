from itertools import *
from operator import *
from types import *
import sys
a = []
print chain('abc','def')

a,b,c =  imap(pow,(2,3,4),(5,6,7))
print a,b,c

iterable =  takewhile(lambda x:x<5,[1,4,6,4,1])
f = list(iterable)

print f


def tee(iterable,n=2):
    it = iter(iterable)
    deques = [collections.deque() for i in range(n)]
    def gen(mydeque):
        while True:
            if not mydeque:
                newval = next(it)
                for d in deques:
                    d.append(newval)
            yield mydeque.popleft
    return tuple(gen(d) for d in deques)


b = 'BCA'

g = product('abcd','xy')
g = product(rang(4),3)
g = list(g)
print g