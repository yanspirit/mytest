import operator

print operator.lt(2,4)
print operator.__lt__(2,4)
print operator.truth(0)

a = 1
print id(a)
b = 1
print operator.is_(a, b)
b = 2
print operator.is_(a, b)

a = -1
print id(a)




print operator.index(1)

print operator.inv(8)

print operator.lshift(4, 1)


print operator.or_(2,4)


print operator.pos(30)



print operator.pow(2,8)




