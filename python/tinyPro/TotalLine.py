import os
#count the line of a single file
def CountLine(path):
    tempfile = open(path)
    res=0
    '''
    iterate lines one by one
    '''
    for lines in tempfile:
        res+=1
    print "%s %d"%(path,res)
    return res

def TotalLine(path):
    total=0
    '''
    this root is just for current path
    '''
    for root,dirs,files in os.walk(path):
        for item in files:
            ext = item.split('.')
            ext=ext[-1]
            if(ext in ["cpp","c","h","java","py","php"]):
                subpath = root+"/"+item
                total += CountLine(subpath)
    return total



print "Input Path"
path = raw_input()
print TotalLine(path)