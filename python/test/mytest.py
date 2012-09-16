# -*- encoding:utf-8 -*-
import sys
print dir()


print id(sys)
print id(sys.modules['sys'])


import site
print site.getusersitepackages()

def test(a,b,c):
    print a,b,c
    
    
test(c='cc',b='bb',a = 'aa')

def test2(a,b,*args):
    print a,b,args

test2('aa','bb','cc')

def test3(**args):
    print args


test2('dd','bb','ee')

ret = 0
for a in range(1,1001):
    ret += a

print ret

a = 1
b = 2
a,b = b,a
print a,b


hasht = {}
hasht['one'] = '111'
hasht['two'] = '222'

print hasht.get('thread',0)

copy = hasht.copy()
print copy

#print  dir(sys)
#print help(sys)


a = 10

while a < 12:
        a+=1
else:
    print a


print type(33)
print type(30.02012)

print ur'\u0062\n'

print ("hello,what\'s "  
'your name?')

print int('32')
print int(-2.3)
print float(32)
print str(3.141514)

print ord('A')

print locals()
print globals()

print range(1,10,2)
print range(0,10)



a = [1,3,4,5,6]
b = [3,4,6,8,9.12]
print a+b

print [1,2,3]*3

list = ['a','b','c']
list[1:3] = ['d','e']
print list


list = ['a','d','e']
list[1:1] = ['b','c']
print list
del list[1:3]
print list


a= [1,2,3]
b= [1,2,3]
print id(a),id(b)

#��¡
c = a[:]
print c



list = ["hello",10,90,['a','b']]
print list[3][0]


matrix = [[1,2,3],[4,5,6],[8.9,10]]
print matrix[2][0]


import string
song = "the rain in spain"
str = string.split(song)
#print string.split(song,'n')
print string.join(str,'_')

list = []
print isinstance(list,type([1,2]))

print type((1,)) ; print 'a'


i = 10
print \
i  ;print 2


def someFunc():
    pass

someFunc()

print 2**3
print 5//2
print 7%2
print 4>>1

x = 19
if 10<x<20:
    print 'ok'
    
    
print 3&5
print 5|3
print 5^3
print ~5
    
a = 1
b = 1
print a is b


print 'a' not in ['b','c','d']



#actions = [name[3:]for name in wikiaction.__dict__ if name.startswith('do_')]



print chr(254)


print locals()


input('enter one num:')







