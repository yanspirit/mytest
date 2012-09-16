#!/usr/local/bin/python


import os

def countfile(test):
    f=open(test)
    num=0
    for x in f:num=num+1
    return num



def count(test):
    if(os.path.isfile(test)):
        return countfile(test)
    return total(test)


def total(test):
    l=os.listdir(test)
    num=0
    for x in l:num=num+count(test+'//'+x)
    return num


print(total('/root/code/MiddleWare1.0'))