'''sort a list of object by an attribute'''

'''DSU module'''

import operator
'''得到副本'''
def sort_by_attr(seq,attr):
    return sorted(seq,key=operator.attrgetter(attr))


'''原地排序'''
def sort_by_attr_inplace(lst,attr):
    lst.sort(key=operator.attrgetter(attr))

class  hist(dict):
    def add(self,item,increment=1):
        self[item]=increment+self.get(item,0)
    def counts(self,reverse=False):
        aux=[(self[k],k) for k in self ]
        aux.sort()
        if  reverse:aux.reverse()
        return [k for v,k in  aux]


class hist1(list):
    def __init__(self, n):
        ''' initialize this list to count occurrences of n distinct items '''
        list.__init__(self, n*[0])
    def add(self, item, increment=1):
        ''' add 'increment' to the entry for 'item' '''
        self[item] += increment
    def counts(self, reverse=False):
        ''' return list of indices sorted by corresponding values '''
        aux = [ (v, k) for k, v in enumerate(self) ]
        aux.sort( )
        if reverse: aux.reverse( )
        return [k for v, k in aux]


       '''可以抽象出counts过程'''
   def sorted_keys(container,keys,reverse):
       aux=[(container[k],k]) for k in keys ]
       aux.sort()
       if reverse:aux.reverse()
       return [ k for v,k in aux]
       '''return sorted(keyss,key=container.__getitem__,reverse=reverse)'''
   




def  case_insensitive_sort(string_list):
    auxiliary_list = [(x.lower(),x) for x in string_list]
    auxiliary_list.sort()
    return [x[1] for x in auxiliary_list]
'''return sorted(string_list,key=str.lower)'''




    
