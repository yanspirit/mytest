#!/usr/local/bin/python

import os

def existdisk():
    curdisks = []
    allDisks = ['C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', \
                 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', \
                 'U:', 'V:', 'W:', 'X:', 'Y:', 'Z:', 'A:', 'B:' ]  


    for disk in allDisks:
        if os.path.exists(disk):
            curdisks.append(disk)
        
    return curdisks



def SearchDirFile(path,src):
    if not os.path.exists(path):
        print "%s path not exists"% path
    for root,dirs,files in os.walk(path, True):
       if -1 != root.find(src):
           print root
       for item in files:
           path = os.path.join(root,item)
           if -1 != path.find(src):
               print path


def SearchFile(path,src):
    if not os.path.exists(path):
        print "%s path not exists" %path
        
        for root,dirs,files in os.walk(path, True):
            for item in files:
                path = os.path.join(root,item)
                
                try:
                    f = open(path,'r')
                    for eachline in f.readlines():
                        if -1!= eachline.find(src):
                            print path
                            f.close()
                            break
                except:
                    pass


def SearchAllDirFile(src):
    curdisks = existdisk()
    for disk in curdisks:
        dis = disk + '\\'
        SearchDirFile(disk,src)
    print "finished search"
    
    
    
    def SearchAllFile(src):
        curdisks = existdisk()
        for disk in curdisks:
            disk = disk + '\\'
            SearchFile(disk,src)
        print "finished search"
        

