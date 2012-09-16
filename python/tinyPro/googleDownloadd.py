#!/usr/local/bin/python

import urllib.request,io,os,sys

req = urllib.request.Request("http://www.google.hk.cn")

f = urllib.request.urlopen(req)

s = f.read()

s = s.decode('gbk','ignore')

mdir = sys.path[0]+'/'

file = open(mdir+'admin6.txt','a',1,'gbk')

file.write(s)
file.close()