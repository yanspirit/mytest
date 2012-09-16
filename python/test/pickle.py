import pickle
import sys,os
f = open('test.txt','w')

pickle.dump(12.3, f)
pickle.dump('hello',f)

f.close()


f = open('test.txt','r')
x = pickle.load(f)

print x

y = pickle.load(f)
print y