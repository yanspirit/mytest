import sys
import os
import time

#from threading import Thread

try:
    from paramiko import SSHClient
    from paramiko import AutoAddPolicy
    
except ImportError:
    print G+'''You need paramiko module.  
    http://www.lag.net/paramiko/      
    Debian/Ubuntu: sudo apt-get install aptitude  
    sudo aptitude install python-paramiko\n''' 
    sys.exit(1)



docs='''
            [*] This was written for educational purpose and pentest only. Use it at your own risk.  

            [*] Author will be not responsible for any damage!                                                                 

            [*] Toolname        : ssh_bf.py  

            [*] Author          : xfk  

            [*] Version         : v.0.2  

            [*] Example of use  : python ssh_bf.py [-T target] [-P port] [-U userslist] [-W wordlist] [-H help]  

'''

if sys.platform == 'linux' or sys.platform == 'linux':
    clearing = 'clear'
else:
    clearing = 'cls'
os.system(clearing)



R=""


def BruteForce(hostname,port,username,passward):
    ssh=SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    try:
        ssh.connect(hostname)
    except Exception,e:
        status = 'error'
        pass
return status



def makelist(file):
    items=[]
    
    try:
        fd=open(file,'r')
    except IOError:
        print R+'unable to read file  \'%s\'' %file+END
        pass
    
    for line in fd.readlines():
        item = line.replace('\n','').replace('\r','')
        items.append(item)
        
    fd.close()
    return items


def main():
    logo()
    
    
    
        
    


