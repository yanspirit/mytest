#!/usr/local/bin/python

import psutil
import re
import sys


def processinfo(x):
    p=psutil.get_process_list()
    for r in p:
        aa = str(r)
        f=re.compile(x,re.I)
        if f.search(aa):
            print aa.split('pid=')

processinfo(sys.argv[1])