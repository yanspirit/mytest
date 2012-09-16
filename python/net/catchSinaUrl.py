import urllib
def cbk(a,b,c):
    per=100.0*a*b/c
    if per > 100:
        per=100
    print '%.2f%%'%per
    
url='http://www.sina.com.cn'
local='d:\\sina.html'
urllib.urlretrieve(url,local,cbk)



'''
urllib.quote(string[,safe)
urllib.unquote(string)
urllib.unqote_plus(string)

'''
