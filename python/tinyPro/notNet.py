import os,sys

host_path = os.environ.get('SYSTEMROOT',r'C:\Windows')+ r'\system32\drivers\etc\hosts'

filter_urls = ['www.xiaonei.com','www.renren.com','www.oschina.cn','www.weibo.com']



def CNMode():
    add_filter=''
    f = open(host_path,'r+')
    fread = f.read()
    for f_url in filter_urls:
        if f_url not in fread:
            add_filter += '127.0.0.1  '+ f_url + '\n'
            
    try:
        f.write(add_filter)
        print "change to CN mode successfully"
    except:
        print "open file error"
    finally:
        f.close()



def FreeMode():
    f = open(host_path,'r+')
    unremove = ''
    try:
        for line in f.readlines():
            if line.split()[-1] not in filter_urls:unremove += line
        f.close()
    
        f.open(host_path,'w')
        f.write(unremove)
        print "change to free mode successfully"
    except:
        print "open file error"
    finally:
        f.close()


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].upper() == 'CN':
        CNMode()
    elif len(sys.argv) == 2 and sys.argv[1].upper() == 'FREE':
        FreeMode() 
    else:
        print '''
        para is error!

        such as: python host.py cn ;

            or: python host.py free
        '''
