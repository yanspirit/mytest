from struct import *
#print pack('hh1',[1,2,3])

record = 'raymond \x32\x12\x08\x01\x08'
name, serialnum, school, gradelevel = unpack('<10sHHb', record)

print name
#from collections import namedtuple
#Student = namedtuple('Student', ' name serialnum school gradelevel')
#print Student._make(unpack('<10sHHb', record))


