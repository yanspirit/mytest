import re
import sys
import os

def getFilesize(filename):
    global FILE_SIZE
    fstream = open(filename,'r')
    fstream.seek(0,os.SEEK_END)
    FILE_SIZE = fstream.tell()
    fstream.close()
    
def filterLog(filename,mapping):
    getFilesize(filename)
    fp = open(filename,'r')
    startPos = fp.tell()
    print 'the startPos is %d' %startPos
    
    while startPos < FILE_SIZE:
        line = fp.readline()
        print re.compile(mapping).findall(line)
        re.compile
#        result = re.compile(r"\b^\[.+\]$\b").match(line)
#        if result:
#            print re.compile(mapping).findall(line)
#        if result:
#            print result
        startPos = fp.tell()

if __name__ == '__main__':
    mapping= "r'\\bWebBench.+\\b'"
    print mapping
    filterLog('test.txt',mapping)
#    ['ERROR.+',
    
    
    
    
    
    
    