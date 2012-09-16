import string
import datetime
print string.ascii_lowercase

print string.digits

print string.letters



#class string.Formatter
#format   vformat
#
#parse(format_string)


d = datetime.datetime(2012,8,15,10,26,30)
print '{:%Y-%m-%d %H:%M:%S}'.format(d)


points = 18.9
total = 100
print 'Correct answers: {:.2%}'.format(points/total)




for align,text in zip('<^>',['left','center','right']):
    print '{0:{fill}{align}16}'.format(text,fill=align,align=align)
    
    

octets = [192,168,0,1]
print '{:02X}{:02X}{:02X}{:02X}'.format(*octets)

width = 5
for num in range(5,12):
    for flag in 'dXob':
        print '{0:{width}{base}}'.format(num,base=flag,width=width),
    print



from string import Template
s = Template('$who likes $what')
print s.substitute(who='tim',what='kung pao')

d = dict(who='tim')
print Template('Give $who $100').safe_substitute(d)

