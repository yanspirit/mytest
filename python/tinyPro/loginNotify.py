#!/usr/bin/python
#encoding=utf-8
from smtplib import  SMTP
import subprocess
import time

smtp = "smtp.163.com"
user = 'yanspirit'
password = '66709601984'



run_comd = subprocess.Popen('w|grep pts',shell=True,stdout=subprocess.PIPE)
data = run_comd.stdout.read()

mailb = ["hello",data]
mailh = ["From:yanspirit@163.com","To:yansuopeng@163.com","Subject:loginlog"]
mailmsg = "\r\n\r\n".join(["\r\n".join(mailh), "\r\n".join(mailb)])


def send_mail():
    send = SMTP(smtp)
    send.login(user,password)
    result = send.sendmail("yanspirit@163.com", ("yansuopeng@163.com",), mailmsg)
    send.quit()
    
while 1:
    if data == '':
        pass
        time.sleep(20)
    else:
        send_mail()