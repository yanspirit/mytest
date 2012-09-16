


try:
	set
except  NameError:
	from sets import Set as set


a = set(xrange(1000))
b = set(xrange(500,1500))
union =  a | b
inter = a & b
print union

'''intersection==&'''
phones=(1352,1545)
addresses=(1235,5254)
for name in set(phones)& set(addresses):
	print name,phones[name],addresses[name]


class Bunch(object):
	def __init__(self,**kwds):
		self.__dict__.update(kwds)

point=Bunch(daatum=z,hi=y*y,coord=x)



def throws(t,f,*a,**k)
	try:
		f(*a,**k)
	except t:
		return True
	else:
		return False

data = [float(line) for line in open(file) if not throws(ValueError,float,line)]


	
