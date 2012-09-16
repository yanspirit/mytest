import os,sys
from stat import *

def walktree(top,callback):
    
    for f in os.listdir(top):
        pathname = os.path.join(top,f)
        mode = os.stat(pathname).st_mode
        if S_ISDIR(mode):
            walktree(pathname,callback)
        elif S_ISREG(mode):
            callback(pathname)
        else:
            print 'skipping %s' % pathname


def visitfile(file):
    print 'visiting',file


if __name__ == '__main__':
    walktree(sys.argv[1],visitfile)
    