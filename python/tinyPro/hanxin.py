#!/usr/local/bin/python

def test(people):
    if  people%3==2 and people%5==3 and people%7 == 2:
        return True
    else:
        return False

for i in xrange(1,100):
    if test(i) == True:
        print "least sodiors",i
#    else:
#     print ""