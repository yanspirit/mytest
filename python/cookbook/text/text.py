import sets
'''list comprehension'''
def do_something_with(c):
    print c
    
thestring="hello"
results = [ do_something_with(c) for c in thestring]
results = map(do_something_with,thestring)


print ord('a')
print chr(97)

print ''.join(map(chr,range(97,100)))



'''userString support also'''
def  isStringLike(anobj):
    try: anobj + ''
    except:return False
    else:return True
    
    
print '|','hej'.ljust(20),'|'
print 'ysp'.center(20,'+'),'|'

x='hij    yspp   '
print "|",x.lstrip(),"|"
'''
rstrip   strip
'''
print '|'+x.strip('hij')+'|'

x = 'xyxxyy hejyx  yyx'
print '|'+x.strip('xy')+'|'

    
pieces=['ysp',' is',' clever']
largeString = ''.join(pieces)
print largeString

largeString = '%s%s something %s yet more' % ('ysp', ' is', ' very clever')
print largeString


import operator
largeString = reduce(operator.add, pieces, '')
print largeString





